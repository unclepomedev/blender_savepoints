# SPDX-License-Identifier: GPL-3.0-or-later

import json
import uuid
from pathlib import Path
from typing import Any

import bpy

HISTORY_SUFFIX = "_history"
SNAPSHOT_EXT = ".blend_snapshot"
SNAPSHOT_FILENAME = "snapshot.blend_snapshot"
LEGACY_SNAPSHOT_FILENAME = "snapshot.blend_snapshot"
THUMBNAIL_FILENAME = "thumbnail.png"
RESCUE_TEMP_FILENAME = "snapshot_rescue_temp.blend"
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


def load_manifest(create_if_missing: bool = True) -> dict[str, Any]:
    """
    Load and return the savepoints manifest for the current project.
    
    Reads manifest.json from the project's history directory, validates that the file contains a JSON object, and backfills missing fields: `schema_version`, `project_uuid`, `parent_file`, and `versions` (ensuring `versions` is a list). If any backfilled fields are added the manifest is persisted. If the manifest file is missing or cannot be read/parsed, a default manifest with `parent_file`, empty `versions`, `schema_version`, and a new `project_uuid` is returned. Errors encountered while loading are printed.

    Args:
        create_if_missing (bool): If True, creates the default manifest on disk if it is missing.
    
    Returns:
        manifest (dict): Manifest object containing at least the keys:
            - `parent_file` (str): path to the parent .blend file
            - `versions` (list): list of version entries
            - `schema_version` (str): manifest schema version
            - `project_uuid` (str): stable UUID for the project
    """
    path_str = get_manifest_path()
    if path_str:
        path = Path(path_str)
        if path.exists():
            try:
                with path.open('r', encoding='utf-8') as f:
                    data = json.load(f)

                    if not isinstance(data, dict):
                        raise ValueError("Manifest JSON must be an object")

                    # Backfill for older manifests
                    mutated = False
                    if "schema_version" not in data:
                        data["schema_version"] = SCHEMA_VERSION
                        mutated = True
                    if "project_uuid" not in data:
                        data["project_uuid"] = str(uuid.uuid4())
                        mutated = True
                    if "parent_file" not in data:
                        data["parent_file"] = get_project_path()
                        mutated = True
                    if not isinstance(data.get("versions", []), list):
                        data["versions"] = []
                        mutated = True

                    # Optional: persist backfilled fields so UUID stabilizes after first load
                    if mutated:
                        save_manifest(data)

                    return data
            except Exception as e:
                print(f"Error loading manifest: {e}")
    default_manifest = {
        "parent_file": get_project_path(),
        "versions": [],
        "schema_version": SCHEMA_VERSION,
        "project_uuid": str(uuid.uuid4()),
    }
    if create_if_missing:
        save_manifest(default_manifest)
    return default_manifest


def save_manifest(data: dict[str, Any]) -> None:
    """
    Write the given manifest dictionary to the project's manifest.json inside the history directory.
    
    Parameters:
        data (dict[str, Any]): Manifest data to persist. Will be serialized as pretty-printed JSON with UTF-8 encoding.
    
    Notes:
        - Creates parent directories for the manifest file if they do not exist.
        - Errors encountered while writing are caught and printed; the function does not raise.
    """
    path_str = get_manifest_path()
    if path_str:
        path = Path(path_str)
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open('w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving manifest: {e}")


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
