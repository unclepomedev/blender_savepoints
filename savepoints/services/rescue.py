# SPDX-License-Identifier: GPL-3.0-or-later

import os
import shutil
import time
from pathlib import Path

import bpy

from .storage import (
    RESCUE_TEMP_FILENAME, get_history_dir
)


def create_rescue_temp_file(snapshot_path: Path) -> Path:
    """
    Create a temporary copy of the snapshot for rescue operations.

    Args:
        snapshot_path (Path): Path to the source snapshot file.

    Returns:
        Path: Path to the created temporary file.

    Raises:
        OSError: If copying fails.
        TimeoutError: If the temp file cannot be validated within 1 second.
    """
    version_dir = snapshot_path.parent
    temp_blend_path = version_dir / RESCUE_TEMP_FILENAME

    shutil.copy2(str(snapshot_path), str(temp_blend_path))

    if hasattr(os, "sync"):
        try:
            os.sync()
        except OSError:
            pass

    timeout = 5.0
    start_time = time.time()

    is_ready = False

    while (time.time() - start_time) < timeout:
        try:
            if temp_blend_path.stat().st_size > 0:
                is_ready = True
                break
        except OSError:
            pass

        time.sleep(0.05)

    if not is_ready:
        try:
            if temp_blend_path.exists():
                os.remove(temp_blend_path)
        except Exception:
            pass

        raise TimeoutError(f"[SavePoints] Failed to create valid temp file within {timeout}s: {temp_blend_path}")

    print(f"[SavePoints] Created temp file for rescue: {temp_blend_path}")

    return temp_blend_path


def delete_rescue_temp_file(temp_path: Path, delay: float = 5.0, max_retries: int = 5):
    """
    Safely delete the rescue temporary file.
    Uses a timer to handle file locks (common on Windows) and ensure deletion.

    Args:
        temp_path (Path): Path to the temporary file to delete.
        delay (float): Initial delay in seconds before attempting deletion.
        max_retries (int): Number of times to retry if deletion fails.
    """
    target_path = Path(temp_path)

    def _deletion_task():
        nonlocal max_retries
        if not target_path.exists():
            return None  # File already gone, stop timer

        try:
            os.remove(target_path)
            print(f"[SavePoints] Removed temp file for rescue: {target_path}")
            return None  # Success, stop timer
        except (PermissionError, OSError) as e:
            if max_retries > 0:
                max_retries -= 1
                return 1.0  # Retry in 1 second
            else:
                print(f"[SavePoints] Failed to remove temp file after retries: {e}")
                return None  # Stop timer

    # Register the timer
    # Note: Closures create new function objects, so register calls are always unique
    bpy.app.timers.register(_deletion_task, first_interval=delay)


def cleanup_rescue_temp_files() -> int:
    """
    Remove any lingering rescue temporary files from all version directories.

    Returns:
        int: The number of files removed.
    """
    history_dir_str = get_history_dir()
    if not history_dir_str:
        return 0

    history_dir = Path(history_dir_str)
    if not history_dir.exists():
        return 0

    count = 0
    # Iterate over all subdirectories (versions)
    for version_dir in history_dir.iterdir():
        if version_dir.is_dir():
            temp_file = version_dir / RESCUE_TEMP_FILENAME
            if temp_file.exists():
                try:
                    temp_file.unlink()
                    count += 1
                except Exception as e:
                    print(f"[SavePoints] Failed to remove temp file {temp_file}: {e}")

    if count > 0:
        print(f"[SavePoints] Cleaned up {count} rescue temporary file(s).")

    return count


def get_rescue_append_dir(temp_blend_path: Path) -> str:
    """
    Get the directory path for appending objects from the rescue temp file.

    Args:
        temp_blend_path (Path): Path to the temporary blend file.

    Returns:
        str: The directory path string formatted for Blender's append operator (ending with separator).
    """
    virtual_dir = temp_blend_path / "Object"
    return str(virtual_dir) + os.sep
