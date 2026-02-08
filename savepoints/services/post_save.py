# SPDX-License-Identifier: GPL-3.0-or-later

import shlex
import subprocess
import sys
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
    except KeyError as ex:
        print(f"[SavePoints] Error: Missing placeholder {ex} in command template.")
        return None


class PostSaveManager:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PostSaveManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if PostSaveManager._initialized:
            return
        self._timer = None
        self.process = None
        PostSaveManager._initialized = True

    @property
    def is_running(self):
        return self.process is not None and self.process.poll() is None

    def start_command(self, command_str, context_dict):
        if self.is_running:
            print("Post-save command already running.")
            return

        formatted_cmd = format_command(command_str, context_dict)
        if formatted_cmd is None:
            self._report_error("Command formatting failed. Check placeholders.")
            return
        print(f"[SavePoints] Starting post-save command: {formatted_cmd}")

        try:
            self.process = subprocess.Popen(
                formatted_cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            bpy.app.timers.register(self._monitor_process)

        except Exception as e:
            self._report_error(f"Failed to start command: {e}")
            self.process = None

    def cancel(self):
        if self.process:
            print("Canceling post-save command...")
            self.process.terminate()
            try:
                self.process.wait(timeout=1)
            except subprocess.TimeoutExpired:
                self.process.kill()

            self.process = None

            for window in bpy.context.window_manager.windows:
                for area in window.screen.areas:
                    area.tag_redraw()

    def poll(self):
        """Check status manually (mainly for tests)"""
        if self.process:
            return self.process.poll() is not None
        return True

    def _monitor_process(self):
        if self.process is None:
            return None  # Stop timer

        ret_code = self.process.poll()
        if ret_code is None:
            return 0.5  # Check again in 0.5 seconds

        # Finished
        stdout, stderr = self.process.communicate()
        if ret_code == 0:
            self._report_success("Post-save command finished successfully.")
        else:
            msg = f"Post-save command failed (Code {ret_code})."
            self._report_error(msg, details=f"STDOUT:\n{stdout}\nSTDERR:\n{stderr}")

        self.process = None

        for window in bpy.context.window_manager.windows:
            for area in window.screen.areas:
                area.tag_redraw()

        return None

    @staticmethod
    def _report_success(message):
        print(message)
        try:
            bpy.ops.savepoints.report_message(message=message, type="INFO")
        except Exception as ex:
            print(f"[SavePoints] report message error: {ex}")

    @staticmethod
    def _report_error(message, details=""):
        print(message)
        if details:
            print(details)
            text_name = "SavePoints_Log.txt"
            text = bpy.data.texts.get(text_name)
            if not text:
                text = bpy.data.texts.new(text_name)

            text.clear()
            text.write(message + "\n\n")
            text.write(details)

        try:
            bpy.ops.savepoints.report_message(message=message, type="ERROR")
        except Exception as ex:
            print(f"[SavePoints] report message error: {ex}")


def trigger_post_save_if_enabled(context, version_id: str, note: str):
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

    PostSaveManager().start_command(prefs.post_save_command, ctx_dict)
