# SPDX-License-Identifier: GPL-3.0-or-later

import shlex
import subprocess
import sys
import tempfile
from pathlib import Path

import bpy
from .storage import get_history_dir


def format_command(command_template, context_dict):
    """
    Replace placeholders in command_template with values from context_dict.
    Values are quoted/escaped to handle spaces safely.
    """

    def quote(s):
        s = str(s)
        if sys.platform == "win32":
            if not s:
                return '""'
            s = s.replace('"', '\\"')
            if any(c in s for c in " &^|<>"):
                return f'"{s}"'
            return s
        else:
            return shlex.quote(s)

    safe_ctx = {k: quote(v) for k, v in context_dict.items()}

    try:
        return command_template.format(**safe_ctx)
    except (KeyError, ValueError, IndexError) as ex:
        print(f"[SavePoints] Error: Invalid command template: {ex}")
        return None


class PostSaveManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PostSaveManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._timer = None
        self.process = None
        self._stdout_file = None
        self._stderr_file = None
        self._on_success = None
        self._on_error = None
        self._initialized = True

    @property
    def is_running(self):
        return self.process is not None and self.process.poll() is None

    def start_command(self, command_str, context_dict, on_success=None, on_error=None):
        """
        Args:
            command_str (str): The command to execute.
            context_dict (dict): Context variables for formatting.
            on_success (callable): Function(msg) to call on success.
            on_error (callable): Function(msg, details) to call on error.
        """
        if self.is_running:
            print("Post-save command already running.")
            return

        self._on_success = on_success
        self._on_error = on_error

        formatted_cmd = format_command(command_str, context_dict)
        if formatted_cmd is None:
            if self._on_error:
                self._on_error("Command formatting failed. Check placeholders.", "")
            return
        print(f"[SavePoints] Starting post-save command: {formatted_cmd}")

        try:
            self._stdout_file = tempfile.TemporaryFile(mode="w+", encoding="utf-8")
            self._stderr_file = tempfile.TemporaryFile(mode="w+", encoding="utf-8")

            self.process = subprocess.Popen(
                formatted_cmd,
                shell=True,
                stdout=self._stdout_file,
                stderr=self._stderr_file,
                text=True,
            )

            bpy.app.timers.register(self._monitor_process)

        except Exception as e:
            msg = f"Failed to start command: {e}"
            print(msg)
            if self._on_error:
                self._on_error(msg, str(e))
            self._cleanup()

    def cancel(self):
        if self.process:
            print("Canceling post-save command...")
            self.process.terminate()
            try:
                self.process.wait(timeout=1)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait()
                print("[SavePoints] Process killed.")

            self._cleanup()

            for window in bpy.context.window_manager.windows:
                for area in window.screen.areas:
                    area.tag_redraw()

    def poll(self):
        """Check status manually (mainly for tests)"""
        if self.process:
            return self.process.poll() is not None
        return True

    def _cleanup(self):
        """Clean up process and file handles"""
        self.process = None

        if self._stdout_file:
            try:
                self._stdout_file.close()
            except Exception as ex:
                print(f"[SavePoints] Error closing stdout file: {ex}")
                pass
            self._stdout_file = None

        if self._stderr_file:
            try:
                self._stderr_file.close()
            except Exception as ex:
                print(f"[SavePoints] Error closing stderr file: {ex}")
                pass
            self._stderr_file = None

    def _monitor_process(self):
        if self.process is None:
            return None  # Stop timer

        ret_code = self.process.poll()
        if ret_code is None:
            return 0.5  # Check again in 0.5 seconds

        # Finished - read outputs from temp files
        stdout = ""
        stderr = ""
        try:
            if self._stdout_file:
                self._stdout_file.seek(0)
                stdout = self._stdout_file.read()
            if self._stderr_file:
                self._stderr_file.seek(0)
                stderr = self._stderr_file.read()
        except Exception as e:
            stderr += f"\n[Error reading output logs: {e}]"

        self._cleanup()

        for window in bpy.context.window_manager.windows:
            for area in window.screen.areas:
                area.tag_redraw()

        if ret_code == 0:
            msg = "Post-save command finished successfully."
            print(msg)
            if self._on_success:
                self._on_success(msg)
        else:
            msg = f"Post-save command failed (Code {ret_code})."
            print(msg)
            details = f"STDOUT:\n{stdout}\nSTDERR:\n{stderr}"
            if self._on_error:
                self._on_error(msg, details)

        return None


def trigger_post_save_if_enabled(
    context, version_id: str, note: str, on_success=None, on_error=None
):
    """
    Trigger the post-save command logic.
    Callbacks are injected to handle UI feedback (to avoid bpy.ops here).
    """
    addon_prefs = None
    current_package = __package__
    if current_package and ".services" in current_package:
        parent_package = current_package.split(".services")[0]
        addon = context.preferences.addons.get(parent_package)
        if addon and addon.preferences:
            addon_prefs = addon

    if not addon_prefs:
        for key, addon in context.preferences.addons.items():
            if key.endswith("savepoints") and addon.preferences:
                addon_prefs = addon
                break

    if not addon_prefs:
        print("[SavePoints] Error: Could not find active addon preferences.")
        return

    prefs = addon_prefs.preferences
    if not (prefs.enable_post_save and prefs.post_save_command):
        return

    history_dir = get_history_dir()
    if not history_dir:
        return

    blend_filepath = Path(bpy.data.filepath)
    version_dir = Path(history_dir) / version_id

    ctx_dict = {
        "filepath": str(blend_filepath),
        "filename": blend_filepath.name,
        "stem": blend_filepath.stem,
        "version": version_id,
        "history_dir": str(history_dir),
        "version_dir": str(version_dir),
        "note": note,
    }

    PostSaveManager().start_command(
        prefs.post_save_command, ctx_dict, on_success=on_success, on_error=on_error
    )
