# SPDX-License-Identifier: GPL-3.0-or-later

import datetime
import json
import shutil
import uuid
from pathlib import Path
from typing import Any

import bpy

HISTORY_SUFFIX = "_history"
SNAPSHOT_EXT = ".blend_snapshot"
MANIFEST_NAME = "manifest.json"
SCHEMA_VERSION = 1
DAILY_BACKUP_DAYS = 14


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
    """
    Load and return the savepoints manifest for the current project.
    
    Reads manifest.json from the project's history directory, validates that the file contains a JSON object, and backfills missing fields: `schema_version`, `project_uuid`, `parent_file`, and `versions` (ensuring `versions` is a list). If any backfilled fields are added the manifest is persisted. If the manifest file is missing or cannot be read/parsed, a default manifest with `parent_file`, empty `versions`, `schema_version`, and a new `project_uuid` is returned. Errors encountered while loading are printed.
    
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
        thumb_rel_path: str,
        blend_rel_path: str,
        object_count: int = 0,
        file_size: int = 0,
        is_protected: bool = False
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


def prune_versions(max_keep: int, keep_daily_backups: bool = False) -> int:
    """
    Prune old versions to keep 'max_keep' manual versions.
    If 'keep_daily_backups' is True, keeps one version per day for the last 14 days.
    Returns number of deleted versions.
    """
    if max_keep <= 0:
        return 0

    manifest = load_manifest()
    versions = manifest.get("versions", [])

    # Filter only manual versions (exclude autosave)
    # List is ordered Newest -> Oldest
    manual_versions = [v for v in versions if v.get("id") != "autosave"]

    if not keep_daily_backups and len(manual_versions) <= max_keep:
        return 0

    # Identify Daily Keep Candidates
    daily_keep_ids = set()
    if keep_daily_backups:
        now = datetime.datetime.now()
        cutoff_date = now - datetime.timedelta(days=DAILY_BACKUP_DAYS)

        # Group by Date
        # Since list is Newest -> Oldest, the first version we encounter for a given date is the latest one.
        seen_dates = set()

        for v in manual_versions:
            ts_str = v.get("timestamp", "")
            try:
                dt = datetime.datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
                if dt < cutoff_date:
                    continue

                date_key = dt.date()
                if date_key not in seen_dates:
                    daily_keep_ids.add(v.get("id"))
                    seen_dates.add(date_key)
            except (ValueError, TypeError):
                continue

    ids_to_delete = []

    # Iterate all versions to determine fate
    # We keep index < max_keep (Recent)
    for i, v in enumerate(manual_versions):
        vid = v.get("id")

        is_recent = i < max_keep
        is_locked = v.get("is_protected", False)
        is_daily = vid in daily_keep_ids

        if is_recent or is_locked or is_daily:
            continue
        else:
            ids_to_delete.append(vid)

    for vid in ids_to_delete:
        delete_version_by_id(vid)

    return len(ids_to_delete)


def delete_version_by_id(version_id: str) -> None:
    """Delete a version from disk and manifest."""
    manifest = load_manifest()
    versions = manifest.get("versions", [])

    version_to_remove = None
    for v in versions:
        if v.get("id") == version_id:
            version_to_remove = v
            break

    if version_to_remove:
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
