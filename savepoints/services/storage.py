# SPDX-License-Identifier: GPL-3.0-or-later

import ctypes
import shutil
import sys
from pathlib import Path

import bpy

HISTORY_SUFFIX = "_history"
SNAPSHOT_EXT = ".blend_snapshot"
SNAPSHOT_FILENAME = "snapshot.blend_snapshot"
LEGACY_SNAPSHOT_FILENAME = "snapshot.blend"
THUMBNAIL_FILENAME = "thumbnail.png"
RETRIEVE_TEMP_FILENAME = "snapshot_retrieve_temp.blend"
MANIFEST_NAME = "manifest.json"
SCHEMA_VERSION = 1


def to_posix_path(path: str | None) -> str:
    """
    Return the given filesystem path using POSIX-style forward slashes.
    
    If `path` is falsy (`None` or empty), returns an empty string.
    
    Returns:
        str: The path with forward slashes, or an empty string if input was falsy.
    """
    if not path:
        return ""
    return Path(path).as_posix()


def from_posix_path(path: str | None) -> str:
    """Convert a POSIX path to the current OS separator."""
    if not path:
        return ""
    return str(Path(path.replace("\\", "/")))


def is_safe_filename(name: str) -> bool:
    """Check if the filename is safe (no path traversal)."""
    if not name:
        return False
    # Explicitly check for traversal attempts
    if ".." in name or "/" in name or "\\" in name:
        return False
    return True


def ensure_directory(path: Path) -> None:
    """
    Ensure the directory exists.
    On Windows, if the directory name starts with '.', apply the hidden attribute.
    """
    path.mkdir(parents=True, exist_ok=True)

    if sys.platform == 'win32' and path.name.startswith('.'):
        try:
            # FILE_ATTRIBUTE_HIDDEN = 0x02
            path_str = str(path)
            # Get existing attributes
            attrs = ctypes.windll.kernel32.GetFileAttributesW(path_str)
            if attrs != -1:  # -1 indicates error
                # Preserve existing attributes and add hidden
                ctypes.windll.kernel32.SetFileAttributesW(path_str, attrs | 0x02)
        except Exception as e:
            print(f"Warning: Failed to hide directory {path}: {e}")


def get_project_path() -> str:
    """Return the current Blender project filepath."""
    return bpy.data.filepath


def get_history_dir_for_path(blend_path: str | None) -> str | None:
    """Get the history directory path for a given blend file."""
    if not blend_path:
        return None

    path = Path(blend_path)
    # parent / .{stem}_history
    history_dir = path.parent / f".{path.stem}{HISTORY_SUFFIX}"
    return str(history_dir)


def get_parent_path_from_snapshot(blend_path: str | None) -> str | None:
    """
    Determine the parent .blend file path if the current file is a snapshot.
    Structure: .../ProjectDir/.{filename}_history/{version_id}/snapshot.blend_snapshot
    """
    if not blend_path:
        return None

    try:
        path = Path(blend_path).resolve()

        # .../vXXX/snapshot.blend_snapshot -> parent -> vXXX
        version_dir = path.parent
        # .../vXXX -> parent -> .{filename}_history
        history_dir = version_dir.parent

        history_dirname = history_dir.name

        if history_dirname.startswith(".") and history_dirname.endswith(HISTORY_SUFFIX):
            # Extract filename: .my_project_history -> my_project
            name_without_ext = history_dirname[1:-len(HISTORY_SUFFIX)]

            # Parent dir: .../ProjectDir
            project_dir = history_dir.parent
            parent_path = project_dir / f"{name_without_ext}.blend"

            return str(parent_path)

    except Exception:
        return None

    return None


def get_history_dir() -> str | None:
    """Get the history directory for the current project."""
    return get_history_dir_for_path(get_project_path())


def get_manifest_path() -> str | None:
    """Get the full path to the manifest.json file."""
    history_dir = get_history_dir()
    if history_dir:
        return str(Path(history_dir) / MANIFEST_NAME)
    return None


def get_fork_target_path(snapshot_path: Path) -> Path:
    """
    Calculate the target path for a forked version based on the snapshot path.
    
    Args:
        snapshot_path (Path): Path to the snapshot file.
        
    Returns:
        Path: The calculated target path for the fork.
        
    Raises:
        FileNotFoundError: If the project root cannot be determined.
    """
    # source_path is .../history_dir/version_id/snapshot.blend
    # parent is .../history_dir/version_id
    # grandparent is .../history_dir
    # great-grandparent is project root
    version_dir = snapshot_path.parent
    version_id = version_dir.name

    history_dir = version_dir.parent
    history_dirname = history_dir.name

    project_root = history_dir.parent

    if not project_root.exists():
        raise FileNotFoundError(f"Project root not found: {project_root}")

    # Calculate filename
    stem = "project"
    if history_dirname.startswith(".") and history_dirname.endswith("_history"):
        # Extract original stem
        stem = history_dirname[1:-8]  # remove '.' and '_history'

    filename = f"{stem}_{version_id}.blend"
    target_path = project_root / filename

    if not target_path.exists():
        return target_path

    # Handle collision with sequential numbering
    counter = 1
    while True:
        filename = f"{stem}_{version_id}_{counter:03d}.blend"
        target_path = project_root / filename
        if not target_path.exists():
            return target_path
        counter += 1


def format_file_size(size_in_bytes: float | int) -> str:
    """Format bytes into human-readable string."""
    try:
        size = float(size_in_bytes)
    except (ValueError, TypeError):
        return "0 B"

    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            if unit == 'B':
                return f"{int(size)} {unit}"
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"


def get_free_disk_space(path: str) -> int:
    """
    Return the free disk space in bytes for the given path.
    """
    try:
        if not path:
            return 0
        usage = shutil.disk_usage(path)
        return usage.free
    except Exception:
        return 0
