# SPDX-License-Identifier: GPL-3.0-or-later

from pathlib import Path

from .storage import (
    RESCUE_TEMP_FILENAME, get_history_dir
)


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
