# SPDX-License-Identifier: GPL-3.0-or-later

import datetime
import json
import shutil
from pathlib import Path
from typing import Any

import bpy

from .services.storage import (
    HISTORY_SUFFIX, SNAPSHOT_EXT, RESCUE_TEMP_FILENAME, MANIFEST_NAME,
    to_posix_path, is_safe_filename,
    get_history_dir_for_path, get_history_dir,
    load_manifest, save_manifest
)


def get_next_version_id(versions: list[dict]) -> str:
    """Generate the next version ID (e.g. "v001")."""
    max_id = 0
    for v in versions:
        vid = v.get("id", "")
        if vid.startswith("v") and vid[1:].isdigit():
            try:
                num = int(vid[1:])
                if num > max_id:
                    max_id = num
            except ValueError:
                pass
    return f"v{max_id + 1:03d}"


def add_version_to_manifest(
        manifest: dict[str, Any],
        version_id: str,
        note: str,
        thumb_rel_path: str,
        blend_rel_path: str,
        object_count: int = 0,
        file_size: int = 0,
        is_protected: bool = False,
        tag: str = "NONE"
) -> None:
    """Add a new version entry to the manifest."""
    versions = manifest.get("versions", [])

    new_version = {
        "id": version_id,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "note": note,
        "thumbnail": to_posix_path(thumb_rel_path),
        "blend": to_posix_path(blend_rel_path),
        "object_count": object_count,
        "file_size": file_size,
        "is_protected": is_protected,
        "tag": tag,
    }
    versions.insert(0, new_version)
    manifest["versions"] = versions
    save_manifest(manifest)


def set_version_protection(version_id: str, is_protected: bool) -> None:
    """Set the protection status of a version."""
    manifest = load_manifest()
    changed = False
    for v in manifest.get("versions", []):
        if v.get("id") == version_id:
            v["is_protected"] = is_protected
            changed = True
            break
    if changed:
        save_manifest(manifest)


def update_version_note(version_id: str, new_note: str) -> None:
    """Update the note for a specific version."""
    manifest = load_manifest()
    changed = False
    for v in manifest.get("versions", []):
        if v.get("id") == version_id:
            v["note"] = new_note
            changed = True
            break
    if changed:
        save_manifest(manifest)


def update_version_tag(version_id: str, new_tag: str) -> None:
    """Update the tag for a specific version."""
    manifest = load_manifest()
    changed = False
    for v in manifest.get("versions", []):
        if v.get("id") == version_id:
            v["tag"] = new_tag
            changed = True
            break
    if changed:
        save_manifest(manifest)


def prune_versions(max_keep: int) -> int:
    """
    Prune old versions to keep 'max_keep' unlocked manual versions.
    Locked versions are ignored (kept automatically and don't count towards the limit).
    Returns number of deleted versions.
    """
    if max_keep <= 0:
        return 0

    manifest = load_manifest()
    versions = manifest.get("versions", [])

    # Filter only manual versions (exclude autosave)
    # List is ordered Newest -> Oldest
    manual_versions = [v for v in versions if v.get("id") != "autosave"]

    ids_to_delete = []
    unlocked_count = 0

    for v in manual_versions:
        vid = v.get("id")
        is_locked = v.get("is_protected", False)

        if is_locked:
            # Locked versions are always kept and don't consume the quota
            continue

        # Unlocked version
        if unlocked_count < max_keep:
            # Keep it
            unlocked_count += 1
        else:
            # Quota exceeded, delete
            ids_to_delete.append(vid)

    for vid in ids_to_delete:
        delete_version_by_id(vid)

    return len(ids_to_delete)


def delete_version_by_id(version_id: str) -> None:
    """Delete a version from disk and manifest."""
    # Validate version_id to prevent path traversal
    if not is_safe_filename(version_id):
        print(f"Error: Invalid version ID '{version_id}'. Path traversal detected.")
        return

    manifest = load_manifest()
    versions = manifest.get("versions", [])

    version_to_remove = None
    for v in versions:
        if v.get("id") == version_id:
            version_to_remove = v
            break

    if version_to_remove:
        # Check protection
        if version_to_remove.get("is_protected", False):
            print(f"Skipping deletion of protected version: {version_id}")
            return

        versions.remove(version_to_remove)
        manifest["versions"] = versions
        save_manifest(manifest)

        # Remove directory
        history_dir_str = get_history_dir()
        if history_dir_str:
            version_dir = Path(history_dir_str) / version_id
            if version_dir.exists():
                try:
                    shutil.rmtree(version_dir)
                except Exception as e:
                    print(f"Failed to remove directory {version_dir}: {e}")


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


def remap_snapshot_paths(dummy: Any) -> None:
    """
    Dynamically fix relative paths when opening a snapshot from the history folder.
    This works in-memory and does not save changes to disk.

    Args:
        dummy: Argument required by the load_post handler (unused).
    """
    if not bpy.data.filepath:
        return

    filepath = bpy.data.filepath
    # Proceed ONLY if the file extension is .blend_snapshot AND path contains _history
    if not filepath.endswith(SNAPSHOT_EXT) or HISTORY_SUFFIX not in filepath:
        return

    print(f"[SavePoints] Detected snapshot load: {filepath}. Remapping relative paths...")

    # Collections to iterate over
    collections_to_remap = [
        getattr(bpy.data, "images", []),
        getattr(bpy.data, "libraries", []),
        getattr(bpy.data, "sounds", []),
        getattr(bpy.data, "fonts", []),
        getattr(bpy.data, "cache_files", []),
        getattr(bpy.data, "movieclips", []),
        getattr(bpy.data, "volumes", []),
        getattr(bpy.data, "texts", []),
    ]

    for collection in collections_to_remap:
        for item in collection:
            if hasattr(item, "filepath"):
                path = item.filepath
                # Check for relative path (starts with //) and avoid double remapping
                # Normalize slashes to handle Windows paths (e.g. //..\..\)
                path_normalized = path.replace("\\", "/")
                if path_normalized.startswith("//") and not path_normalized.startswith("//../../"):
                    new_path = "//../../" + path[2:]
                    item.filepath = new_path

                    if hasattr(item, "reload"):
                        try:
                            item.reload()
                        except RuntimeError:
                            # Some libraries/images might fail to reload if the file is missing
                            pass

    # VSE Support
    scene = getattr(bpy.context, "scene", None)
    if scene and getattr(scene, "sequence_editor", None):
        # Support for Blender < 4.4 (sequences_all) and >= 4.4 (strips_all)
        sequences = getattr(scene.sequence_editor, "sequences_all", None)
        if sequences is None:
            sequences = getattr(scene.sequence_editor, "strips_all", [])

        for seq in sequences:
            # Check for filepath or directory property
            if hasattr(seq, "filepath"):
                path = seq.filepath
                path_normalized = path.replace("\\", "/")
                if path_normalized.startswith("//") and not path_normalized.startswith("//../../"):
                    seq.filepath = "//../../" + path[2:]

            if hasattr(seq, "directory"):
                path = seq.directory
                path_normalized = path.replace("\\", "/")
                if path_normalized.startswith("//") and not path_normalized.startswith("//../../"):
                    seq.directory = "//../../" + path[2:]


def unmap_snapshot_paths() -> bool:
    """
    Dynamically revert relative paths (remove //../../ prefix) for objects/assets.
    This is used when restoring assets to the project root (e.g. Rescue or Fork fixup).

    Returns:
        bool: True if any path was modified, False otherwise.
    """
    changed = False
    # Collections to iterate over
    collections_to_remap = [
        getattr(bpy.data, "images", []),
        getattr(bpy.data, "libraries", []),
        getattr(bpy.data, "sounds", []),
        getattr(bpy.data, "fonts", []),
        getattr(bpy.data, "cache_files", []),
        getattr(bpy.data, "movieclips", []),
        getattr(bpy.data, "volumes", []),
        getattr(bpy.data, "texts", []),
    ]

    for collection in collections_to_remap:
        for item in collection:
            if hasattr(item, "filepath"):
                path = item.filepath
                # Normalize slashes
                path_normalized = path.replace("\\", "/")
                # Check for //../../
                if path_normalized.startswith("//../../"):
                    # Remove ../../ (keep //)
                    # //../../path -> //path
                    new_path = "//" + path_normalized[8:]
                    item.filepath = new_path
                    changed = True

    # VSE Support
    scene = getattr(bpy.context, "scene", None)
    if scene and getattr(scene, "sequence_editor", None):
        sequences = getattr(scene.sequence_editor, "sequences_all", None)
        if sequences is None:
            sequences = getattr(scene.sequence_editor, "strips_all", [])

        for seq in sequences:
            if hasattr(seq, "filepath"):
                path = seq.filepath
                path_normalized = path.replace("\\", "/")
                if path_normalized.startswith("//../../"):
                    seq.filepath = "//" + path_normalized[8:]
                    changed = True

            if hasattr(seq, "directory"):
                path = seq.directory
                path_normalized = path.replace("\\", "/")
                if path_normalized.startswith("//../../"):
                    seq.directory = "//" + path_normalized[8:]
                    changed = True

    return changed


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
