# SPDX-License-Identifier: GPL-3.0-or-later

from pathlib import Path

import bpy

from .manifest import (
    load_manifest,
)
from .selection import preserve_selection
from .storage import (
    get_history_dir,
    is_safe_filename,
    SNAPSHOT_FILENAME,
    LEGACY_SNAPSHOT_FILENAME,
    THUMBNAIL_FILENAME
)
from .thumbnail import capture_thumbnail
from .versioning import add_version_to_manifest
from ..ui_utils import sync_history_to_props


def create_snapshot(context, version_id, note, skip_thumbnail=False):
    """Helper to create a snapshot."""
    if not is_safe_filename(version_id):
        print(f"Error: Invalid version ID '{version_id}'.")
        return

    history_dir_str = get_history_dir()
    if not history_dir_str:
        return

    history_dir = Path(history_dir_str)

    # Wrap the operation to ensure selection/mode is restored
    # (Important if capture_thumbnail changes modes or selection)
    with preserve_selection():
        manifest = load_manifest()

        folder_name = version_id
        version_dir = history_dir / folder_name
        version_dir.mkdir(parents=True, exist_ok=True)

        obj_count = len(bpy.data.objects)

        # Thumbnail
        thumb_filename = THUMBNAIL_FILENAME
        thumb_path = version_dir / thumb_filename
        if not skip_thumbnail:
            capture_thumbnail(context, str(thumb_path))

        # Save Snapshot
        snapshot_path = version_dir / SNAPSHOT_FILENAME
        bpy.ops.wm.save_as_mainfile(copy=True, filepath=str(snapshot_path))

        # Capture file size
        file_size = 0
        if snapshot_path.exists():
            file_size = snapshot_path.stat().st_size

        # Update Manifest
        add_version_to_manifest(
            manifest,
            version_id,
            note,
            str(Path(folder_name) / thumb_filename),
            str(Path(folder_name) / SNAPSHOT_FILENAME),
            object_count=obj_count,
            file_size=file_size
        )

        # Update UI
        sync_history_to_props(context)


def find_snapshot_path(version_id: str) -> Path | None:
    """Find the snapshot file path for a given version ID."""
    if not is_safe_filename(version_id):
        return None

    history_dir_str = get_history_dir()
    if not history_dir_str:
        return None

    history_dir = Path(history_dir_str)
    version_dir = history_dir / version_id

    # Check primary filename
    snapshot_path = version_dir / SNAPSHOT_FILENAME
    if snapshot_path.exists():
        return snapshot_path

    # Check legacy filename
    legacy_path = version_dir / LEGACY_SNAPSHOT_FILENAME
    if legacy_path.exists():
        return legacy_path

    return None
