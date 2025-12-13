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


def load_manifest() -> dict[str, Any]:
    """Load the manifest file."""
    path_str = get_manifest_path()
    if path_str:
        path = Path(path_str)
        if path.exists():
            try:
                with path.open('r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading manifest: {e}")
    return {"parent_file": get_project_path(), "versions": []}


def save_manifest(data: dict[str, Any]) -> None:
    """Save data to the manifest file."""
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


def _resize_image_file(image_path: str, max_dim: int = 360) -> None:
    """Resize the image file to save space."""
    if not Path(image_path).exists():
        return

    try:
        img = bpy.data.images.load(image_path)
        width, height = img.size

        if width > max_dim or height > max_dim:
            scale_factor = min(max_dim / width, max_dim / height)
            new_width = max(1, int(width * scale_factor))
            new_height = max(1, int(height * scale_factor))

            img.scale(new_width, new_height)
            img.save()

        bpy.data.images.remove(img)
    except Exception as e:
        print(f"Failed to resize thumbnail: {e}")


def capture_thumbnail(context: bpy.types.Context, filepath: str) -> None:
    """
    Capture a clean viewport render as a thumbnail.
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    # Background mode check
    if not context.window_manager.windows:
        return

    render = context.scene.render
    # Store old settings
    old_filepath = render.filepath

    try:
        # Use simple string for Blender API
        render.filepath = str(path)

        # OpenGL Render (Clean Viewport)
        bpy.ops.render.opengl(write_still=True)

        # Resize logic (To save disk space)
        _resize_image_file(str(path))

    except Exception as e:
        print(f"Thumbnail generation failed: {e}")
    finally:
        # Restore settings
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
