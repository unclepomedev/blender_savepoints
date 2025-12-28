# SPDX-License-Identifier: GPL-3.0-or-later

import os
import subprocess
from typing import Any

from .snapshot import find_snapshot_path


class BatchRenderExecutor:
    """
    Manages the execution of batch render tasks.
    Handles process creation, monitoring, and queue management.
    """

    def __init__(self, tasks: list[Any], temp_dir: str, output_dir: str, settings_path: str, worker_script_path: str,
                 blender_bin: str):
        self.task_queue = list(tasks)
        self.total_tasks = len(tasks)
        self.current_task_idx = 0

        self.temp_dir = temp_dir
        self.output_dir = output_dir
        self.settings_path = settings_path
        self.worker_script_path = worker_script_path
        self.blender_bin = blender_bin

        self.current_process: subprocess.Popen | None = None
        self.current_version_id: str | None = None
        self.current_log_path: str | None = None
        self.current_log_handle = None

        self.is_cancelled = False
        self.finished = False
        self.startup_flags = ["-b", "--factory-startup"]

    def update(self) -> dict[str, Any]:
        """
        Called periodically to check process status and start next task.
        """
        if self.is_cancelled:
            return {'status': 'CANCELLED'}

        # 1. Check existing process
        if self.current_process:
            return_code = self.current_process.poll()

            if return_code is not None:
                # --- Task Finished (Success or Failure) ---
                log_path = self.current_log_path
                version_id = self.current_version_id

                self._cleanup_current_log()
                self.current_process = None
                self.current_task_idx += 1

                return {
                    'status': 'TASK_FINISHED',
                    'version_id': version_id,
                    'return_code': return_code,
                    'log_path': log_path,
                    'progress': (self.current_task_idx, self.total_tasks)
                }
            else:
                # --- Still Running ---
                return {
                    'status': 'RUNNING',
                    'version_id': self.current_version_id,
                    'progress': (self.current_task_idx, self.total_tasks)
                }

        # 2. No process running, try to start next
        if self.finished or not self.task_queue:
            self.finished = True
            return {'status': 'FINISHED'}

        # Get next task
        version = self.task_queue.pop(0)
        self.current_version_id = version.version_id

        snapshot_path = find_snapshot_path(version.version_id)
        if not snapshot_path or not snapshot_path.exists():
            self.current_task_idx += 1
            return {
                'status': 'SKIPPED',
                'version_id': self.current_version_id,
                'progress': (self.current_task_idx, self.total_tasks)
            }

        if self._launch_process(snapshot_path):
            return {
                'status': 'RUNNING',
                'version_id': self.current_version_id,
                'progress': (self.current_task_idx, self.total_tasks)
            }
        else:
            error_log = self.current_log_path
            failed_id = self.current_version_id

            self.current_task_idx += 1
            self._cleanup_current_log()
            self.current_process = None

            return {
                'status': 'TASK_FINISHED',
                'version_id': failed_id,
                'return_code': -1,
                'log_path': error_log,
                'progress': (self.current_task_idx, self.total_tasks)
            }

    def _launch_process(self, snapshot_path) -> bool:
        """
        Starts the subprocess. Returns True if successful, False otherwise.
        """
        log_filename = f"render_log_{self.current_version_id}.txt"
        self.current_log_path = os.path.join(self.temp_dir, log_filename)

        try:
            self.current_log_handle = open(self.current_log_path, 'w', encoding='utf-8')
        except OSError as e:
            print(f"[SavePoints] Failed to create log file: {e}")
            return False

        cmd = [
            self.blender_bin,
            *self.startup_flags,
            str(snapshot_path),
            "-P", self.worker_script_path,
            "--",
            self.settings_path,
            self.output_dir,
            f"{self.current_version_id}_render"
        ]

        try:
            self.current_process = subprocess.Popen(
                cmd,
                stdout=self.current_log_handle,
                stderr=self.current_log_handle
            )
            print(f"[SavePoints] Rendering {self.current_version_id} (PID: {self.current_process.pid})")
            return True

        except Exception as e:
            error_msg = f"[SavePoints] Critical Error: Process start failed.\n{e}\nCommand: {cmd}"
            print(error_msg)
            if self.current_log_handle:
                try:
                    self.current_log_handle.write(error_msg)
                except:
                    pass
            return False

    def cancel(self):
        """Cancels the current process and clears queue."""
        self.is_cancelled = True
        self.task_queue.clear()

        if self.current_process:
            print(f"[SavePoints] Killing process PID: {self.current_process.pid}")
            try:
                self.current_process.kill()
                self.current_process.wait(timeout=1)
            except Exception as e:
                print(f"Error killing process: {e}")
            self.current_process = None

        self._cleanup_current_log()

    def _cleanup_current_log(self):
        if self.current_log_handle:
            try:
                self.current_log_handle.close()
            except Exception:
                pass
            self.current_log_handle = None
