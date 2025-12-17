# SPDX-License-Identifier: GPL-3.0-or-later

import json
import shutil
from pathlib import Path

from .services.storage import (
    RESCUE_TEMP_FILENAME, MANIFEST_NAME,
    to_posix_path, get_history_dir_for_path, get_history_dir
)


def link_history(source_dir: str | Path, blend_filepath: str) -> str:
    """
    Link (move) an existing history folder to be the history for the current blend file.

    Args:
        source_dir: Path to the source directory.
        blend_filepath: Path to the current .blend file.

    Returns:
        The path of the newly linked history directory.

    Raises:
        ValueError: If validation fails (missing manifest, target exists, etc.)
        OSError: If file operations fail.
    """
    source_path = Path(source_dir)
    manifest_file = source_path / MANIFEST_NAME

    if not manifest_file.exists():
        raise ValueError(f"Invalid folder: {MANIFEST_NAME} not found in {source_path.name}")

    # Validate manifest content
    try:
        with manifest_file.open('r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("Manifest root must be a dictionary")
            if "versions" not in data:
                raise ValueError("Manifest missing 'versions' key")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid manifest file (JSON parse error): {e}")
    except Exception as e:
        raise ValueError(f"Invalid manifest file: {e}")

    if not blend_filepath:
        raise ValueError("Save the current file first.")

    target_history = get_history_dir_for_path(blend_filepath)
    if not target_history:
        raise ValueError("Could not determine history path.")

    target_path = Path(target_history)

    if target_path.exists():
        raise ValueError("History folder already exists for this file.")

    shutil.move(str(source_path), str(target_path))

    # Update manifest with new parent file
    try:
        manifest_path = target_path / MANIFEST_NAME
        if manifest_path.exists():
            with manifest_path.open('r', encoding='utf-8') as f:
                manifest_data = json.load(f)

            manifest_data["parent_file"] = to_posix_path(blend_filepath)

            with manifest_path.open('w', encoding='utf-8') as f:
                json.dump(manifest_data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Warning: Failed to update parent_file in linked manifest: {e}")

    return str(target_path)


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
