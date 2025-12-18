# SPDX-License-Identifier: GPL-3.0-or-later

import datetime
import shutil
from pathlib import Path
from typing import Any

from .storage import (
    to_posix_path, is_safe_filename,
    get_history_dir,
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


def generate_default_note(context) -> str:
    """Generate a default note based on the current context (active object, mode)."""
    try:
        obj = context.active_object
        if not obj:
            return ""

        mode = obj.mode

        if mode == 'EDIT':
            friendly_mode = f"Edit {obj.type.title()}"
        else:
            mode_map = {
                'OBJECT': 'Object',
                'POSE': 'Pose',
                'SCULPT': 'Sculpt',
                'VERTEX_PAINT': 'Vertex Paint',
                'WEIGHT_PAINT': 'Weight Paint',
                'TEXTURE_PAINT': 'Texture Paint',
                'PARTICLE_EDIT': 'Particle Edit',
            }
            friendly_mode = mode_map.get(mode, mode.replace('_', ' ').title())

        return f"{friendly_mode}: {obj.name}"
    except Exception:
        return ""
