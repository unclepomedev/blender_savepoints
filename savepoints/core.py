# SPDX-License-Identifier: GPL-3.0-or-later

import datetime
import json
import shutil
from pathlib import Path
from typing import Any

import bpy

HISTORY_SUFFIX = "_history"
SNAPSHOT_EXT = ".blend_snapshot"
MANIFEST_NAME = "manifest.json"


def to_posix_path(path: str | None) -> str:
    """Convert a path to POSIX style (forward slashes)."""
    if not path:
        return ""
    return Path(path).as_posix()


def from_posix_path(path: str | None) -> str:
    """Convert a POSIX path to the current OS separator."""
    if not path:
        return ""
    return str(Path(path))


def get_project_path() -> str:
    """Return the current Blender project filepath."""
    return bpy.data.filepath


def get_history_dir_for_path(blend_path: str | None) -> str | None:
    """
    Get the history directory path for a given blend file.
    
    Args:
        blend_path: The path to the .blend file.
        
    Returns:
        The path to the history directory, or None if blend_path is empty.
    """
    if not blend_path:
        return None
    filename = os.path.basename(blend_path)
    name_without_ext = os.path.splitext(filename)[0]
    return os.path.join(os.path.dirname(blend_path), f".{name_without_ext}_history")


def get_parent_path_from_snapshot(blend_path: str | None) -> str | None:
    """
    Determine the parent .blend file path if the current file is a snapshot.
    Structure: [ProjectDir]/.{filename}_history/{version_id}/snapshot.blend_snapshot
    Parent:    [ProjectDir]/{filename}.blend
    
    Args:
        blend_path: The path of the current snapshot file.
        
    Returns:
        The path to the parent project file, or None if not in a snapshot.
    """
    if not blend_path:
        return None

    abspath = os.path.abspath(blend_path)

    # .../vXXX/snapshot.blend_snapshot -> dirname -> .../vXXX
    version_dir = os.path.dirname(abspath)

    # .../vXXX -> dirname -> .../.{filename}_history
    history_dir = os.path.dirname(version_dir)

    history_dirname = os.path.basename(history_dir)

    if history_dirname.startswith(".") and history_dirname.endswith("_history"):
        # Extract filename: .my_project_history -> my_project
        name_without_ext = history_dirname[1:-8]

        # Parent dir: .../ProjectDir
        project_dir = os.path.dirname(history_dir)

        # Reconstruct parent path. We assume .blend extension.
        parent_path = os.path.join(project_dir, f"{name_without_ext}.blend")
        return parent_path

    return None


def get_history_dir() -> str | None:
    """
    Get the history directory for the current project.
    
    Returns:
        The history directory path, or None.
    """
    return get_history_dir_for_path(get_project_path())


def get_manifest_path() -> str | None:
    """
    Get the full path to the manifest.json file.
    
    Returns:
        Path to manifest.json, or None if history dir cannot be determined.
    """
    history_dir = get_history_dir()
    if history_dir:
        return os.path.join(history_dir, "manifest.json")
    return None


def load_manifest() -> dict[str, Any]:
    """
    Load the manifest file.
    
    Returns:
        A dictionary containing manifest data. Returns a default structure if loading fails.
    """
    path = get_manifest_path()
    if path and os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading manifest: {e}")
    return {"parent_file": get_project_path(), "versions": []}


def save_manifest(data: dict[str, Any]) -> None:
    """
    Save data to the manifest file.
    
    Args:
        data: The dictionary data to save.
    """
    path = get_manifest_path()
    if path:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


def format_file_size(size_in_bytes: float | int) -> str:
    """
    Format bytes into human-readable string.
    
    Args:
        size_in_bytes: Size in bytes.
        
    Returns:
        Formatted string (e.g. "1.5 MB").
    """
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


def get_next_version_id(versions: list[dict[str, Any]]) -> str:
    """
    Determine the next version ID string (e.g., v005).
    
    Args:
        versions: List of version dictionaries.
        
    Returns:
        Next version ID string.
    """
    max_id = 0
    for v in versions:
        vid = v.get("id", "")
        num = _extract_version_number(vid)
        if num > max_id:
            max_id = num
    new_id_num = max_id + 1
    return f"v{new_id_num:03d}"


def _extract_version_number(vid: str) -> int:
    if vid.startswith("v"):
        try:
            return int(vid[1:])
        except ValueError:
            pass
    return -1


def capture_thumbnail(context: bpy.types.Context, thumb_path: str) -> None:
    """
    Capture the current viewport as a thumbnail.
    
    Args:
        context: Blender context.
        thumb_path: Path where the thumbnail should be saved.
    """
    render = context.scene.render
    old_filepath = render.filepath

    try:
        render.filepath = thumb_path
        # OpenGL render of viewport
        if context.window_manager.windows:
            bpy.ops.render.opengl(write_still=True)

            # Resize thumbnail to save space
            if os.path.exists(thumb_path):
                try:
                    img = bpy.data.images.load(thumb_path)
                    width, height = img.size
                    max_dim = 360  # Max dimension in pixels

                    if width > max_dim or height > max_dim:
                        scale_factor = min(max_dim / width, max_dim / height)
                        new_width = int(width * scale_factor)
                        new_height = int(height * scale_factor)

                        new_width = max(1, new_width)
                        new_height = max(1, new_height)

                        img.scale(new_width, new_height)
                        img.save()

                    bpy.data.images.remove(img)
                except Exception as resize_e:
                    print(f"Failed to resize thumbnail: {resize_e}")
        else:
            pass
    except Exception as e:
        print(f"Thumbnail generation failed: {e}")
    finally:
        render.filepath = old_filepath


def add_version_to_manifest(
        manifest: dict[str, Any],
        version_id: str,
        note: str,
        thumb_rel: str,
        blend_rel: str,
        object_count: int = 0,
        file_size: int = 0
) -> None:
    """
    Add a new version entry to the manifest and save it.
    
    Args:
        manifest: The current manifest data.
        version_id: The new version ID.
        note: Commit note.
        thumb_rel: Relative path to thumbnail.
        blend_rel: Relative path to blend file.
        object_count: Number of objects.
        file_size: Size of the blend file in bytes.
    """
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_version = {
        "id": version_id,
        "timestamp": now_str,
        "note": note,
        "thumbnail": to_posix_path(thumb_rel),
        "blend": to_posix_path(blend_rel),
        "object_count": object_count,
        "file_size": file_size
    }
    versions = manifest.get("versions", [])
    versions.append(new_version)
    manifest["versions"] = versions
    save_manifest(manifest)


def delete_version_by_id(version_id: str) -> None:
    """
    Delete a version from the manifest and file system.
    
    Args:
        version_id: The ID of the version to delete.
    """
    manifest = load_manifest()
    versions = manifest.get("versions", [])

    target_v = None
    for v in versions:
        if v.get("id") == version_id:
            target_v = v
            break

    if target_v:
        history_dir = get_history_dir()
        if target_v.get('blend'):
            blend_rel = from_posix_path(target_v['blend'])
            v_folder = os.path.dirname(os.path.join(history_dir, blend_rel)) if history_dir else None
            # Security check: ensure we are deleting inside history dir
            if history_dir and v_folder and os.path.abspath(history_dir) in os.path.abspath(v_folder):
                shutil.rmtree(v_folder, ignore_errors=True)

        versions.remove(target_v)
        manifest["versions"] = versions
        save_manifest(manifest)
