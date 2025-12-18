# SPDX-License-Identifier: GPL-3.0-or-later

import shutil
import time
from pathlib import Path

from .storage import get_history_dir_for_path


class HistoryDirectoryUnavailableError(Exception):
    """Raised when the history directory cannot be determined."""
    pass


def create_backup(file_path: Path) -> Path:
    """
    Creates a backup of the given file in its history directory.

    Args:
        file_path (Path): The path to the file to back up.

    Returns:
        Path: The path to the created backup file.

    Raises:
        FileNotFoundError: If the source file does not exist.
        HistoryDirectoryUnavailableError: If the history directory cannot be determined.
        OSError: If the copy operation fails.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    history_dir_str = get_history_dir_for_path(str(file_path))
    if not history_dir_str:
        raise HistoryDirectoryUnavailableError("History directory unavailable.")

    history_dir = Path(history_dir_str)
    history_dir.mkdir(parents=True, exist_ok=True)

    timestamp = int(time.time())
    filename = file_path.name
    backup_filename = f"{filename}.{timestamp}.bak"
    backup_path = history_dir / backup_filename

    shutil.copy2(file_path, backup_path)
    
    return backup_path
