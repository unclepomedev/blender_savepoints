# SPDX-License-Identifier: GPL-3.0-or-later

import os
import shutil
import tempfile
from pathlib import Path

import bpy

from .asset_path import fix_retrieved_assets
from .storage import RETRIEVE_TEMP_FILENAME, get_history_dir_for_path, get_project_path


def create_retrieve_temp_file(snapshot_path: Path) -> Path:
    """
    Create a temporary copy of the snapshot for retrieve operations in the same directory.
    This ensures relative paths (e.g. //../../texture.png) remain valid during append.

    Args:
        snapshot_path (Path): Path to the source snapshot file.

    Returns:
        Path: Path to the created temporary file.
    """
    # Use the pre-defined temp filename to keep relative paths valid
    temp_path = snapshot_path.parent / RETRIEVE_TEMP_FILENAME

    try:
        shutil.copy2(str(snapshot_path), str(temp_path))
    except Exception as e:
        # If copy fails, try to cleanup the empty temp file
        if temp_path.exists():
            try:
                os.remove(temp_path)
            except OSError:
                pass
        raise OSError(f"Failed to copy snapshot to temp file: {e}")

    return temp_path


def delete_retrieve_temp_file(temp_path: Path):
    """
    Delete the retrieve temporary file.

    Args:
        temp_path (Path): Path to the temporary file to delete.
    """
    try:
        if temp_path.exists():
            os.remove(temp_path)
            print(f"[SavePoints] Removed temp file: {temp_path}")
    except Exception as e:
        print(f"[SavePoints] Warning: Failed to remove temp file {temp_path}: {e}")


def get_importable_objects(blend_path: Path) -> list[str]:
    """
    Get a list of object names available in the blend file.

    Args:
        blend_path (Path): Path to the blend file.

    Returns:
        list[str]: List of object names.
    """
    with bpy.data.libraries.load(str(blend_path)) as (data_from, _):
        return sorted(data_from.objects)


def append_objects(blend_path: Path, object_names: list[str]) -> list[bpy.types.Object]:
    """
    Append specified objects from the blend file to the current scene.

    Args:
        blend_path (Path): Path to the blend file.
        object_names (list[str]): List of object names to append.

    Returns:
        list[bpy.types.Object]: List of appended objects.
    """
    if not object_names:
        return []

    # Capture existing assets to identify new ones for path fixing
    def get_current_assets():
        assets = set()
        # Collections to check for dependencies
        collections = [
            bpy.data.images,
            bpy.data.libraries,
            bpy.data.sounds,
            bpy.data.fonts,
            bpy.data.volumes,
            bpy.data.texts,
        ]
        for col in collections:
            for item in col:
                assets.add(item)
        return assets

    existing_assets = get_current_assets()

    appended_objects = []

    try:
        with bpy.data.libraries.load(str(blend_path), link=False) as (data_from, data_to):
            # Filter objects that exist in source
            valid_names = [name for name in object_names if name in data_from.objects]
            data_to.objects = valid_names
    except Exception as e:
        print(f"[SavePoints] Error loading library: {e}")
        return []

    # Link appended objects to the current collection
    collection = bpy.context.view_layer.active_layer_collection.collection

    for obj in data_to.objects:
        if obj:
            if obj.name not in collection.objects:
                try:
                    collection.objects.link(obj)
                except RuntimeError:
                    # Object might be already linked if it's the same file (unlikely for retrieve)
                    pass
            appended_objects.append(obj)

            # Select the appended objects
            obj.select_set(True)

    # Identify and fix paths for new assets
    # Re-fetch all assets and find the difference
    current_assets = get_current_assets()
    new_assets = list(current_assets - existing_assets)

    if new_assets:
        print(f"[SavePoints] Found {len(new_assets)} new assets (dependencies). Fixing paths...")
        fix_retrieved_assets(new_assets)

    return appended_objects


def cleanup_retrieve_temp_files() -> int:
    """
    Clean up legacy retrieve temp files from history directories.
    """
    project_path = get_project_path()
    if not project_path:
        return 0

    history_dir_str = get_history_dir_for_path(project_path)
    if not history_dir_str:
        return 0

    history_dir = Path(history_dir_str)
    if not history_dir.exists():
        return 0

    cleaned_count = 0
    try:
        # Iterate over version directories
        for version_dir in history_dir.iterdir():
            if version_dir.is_dir():
                temp_file = version_dir / RETRIEVE_TEMP_FILENAME
                if temp_file.exists():
                    try:
                        os.remove(temp_file)
                        cleaned_count += 1
                        print(f"[SavePoints] Cleaned up legacy temp file: {temp_file}")
                    except OSError as e:
                        print(f"[SavePoints] Warning: Failed to remove legacy temp file {temp_file}: {e}")
    except Exception as e:
        print(f"[SavePoints] Error during cleanup: {e}")

    return cleaned_count
