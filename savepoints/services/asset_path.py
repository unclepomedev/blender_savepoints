# SPDX-License-Identifier: GPL-3.0-or-later

from typing import Any, Generator

import bpy

from .storage import (
    HISTORY_SUFFIX, SNAPSHOT_EXT
)


def _get_collections_to_remap():
    return [
        getattr(bpy.data, "images", []),
        getattr(bpy.data, "libraries", []),
        getattr(bpy.data, "sounds", []),
        getattr(bpy.data, "fonts", []),
        getattr(bpy.data, "volumes", []),
        getattr(bpy.data, "texts", []),
    ]


def _get_all_sequences():
    scene = getattr(bpy.context, "scene", None)
    if not scene or not getattr(scene, "sequence_editor", None):
        return []

    # Support for Blender < 4.4 (sequences_all) and >= 4.4 (strips_all)
    sequences = getattr(scene.sequence_editor, "sequences_all", None)
    if sequences is None:
        sequences = getattr(scene.sequence_editor, "strips_all", [])
    return sequences


def _iter_asset_attributes() -> Generator[tuple[Any, str], None, None]:
    # Collections to iterate over
    for collection in _get_collections_to_remap():
        for item in collection:
            if hasattr(item, "filepath"):
                yield item, "filepath"

    # VSE Support
    for seq in _get_all_sequences():
        if hasattr(seq, "filepath"):
            yield seq, "filepath"
        if hasattr(seq, "directory"):
            yield seq, "directory"


def _transform_path_to_history(path: str) -> str | None:
    # Normalize slashes to handle Windows paths (e.g. //..\..\)
    path_normalized = path.replace("\\", "/")
    # Check for relative path (starts with //) and avoid double remapping
    if path_normalized.startswith("//") and not path_normalized.startswith("//../../"):
        return "//../../" + path_normalized[2:]
    return None


def _transform_path_from_history(path: str) -> str | None:
    # Normalize slashes
    path_normalized = path.replace("\\", "/")
    # Check for //../../
    if path_normalized.startswith("//../../"):
        # Remove ../../ (keep //)
        # //../../path -> //path
        return "//" + path_normalized[8:]
    return None


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

    for item, attr in _iter_asset_attributes():
        current_path = getattr(item, attr)
        new_path = _transform_path_to_history(current_path)

        if new_path:
            setattr(item, attr, new_path)

            # Try reloading if supported (mostly for images/libraries)
            if hasattr(item, "reload"):
                try:
                    item.reload()
                except RuntimeError:
                    # Some libraries/images might fail to reload if the file is missing
                    pass


def unmap_snapshot_paths() -> bool:
    """
    Dynamically revert relative paths (remove //../../ prefix) for objects/assets.
    This is used when restoring assets to the project root (e.g. Retrieve or Fork fixup).

    Returns:
        bool: True if any path was modified, False otherwise.
    """
    changed = False

    for item, attr in _iter_asset_attributes():
        current_path = getattr(item, attr)
        new_path = _transform_path_from_history(current_path)

        if new_path:
            setattr(item, attr, new_path)
            changed = True

    return changed


def fix_retrieved_assets(assets) -> int:
    """
    Fix relative paths for a specific list of assets.
    Used by Retrieve Objects to fix paths of newly imported assets.
    
    Args:
        assets: Iterable of Blender ID blocks (Images, Libraries, etc.)

    Returns:
        int: Number of assets fixed.
    """
    count = 0
    for item in assets:
        # Check standard filepath
        if hasattr(item, "filepath"):
            current_path = item.filepath
            new_path = _transform_path_from_history(current_path)
            if new_path:
                item.filepath = new_path
                count += 1

        # Check directory (mostly for VSE but could be others)
        if hasattr(item, "directory"):
            current_path = item.directory
            new_path = _transform_path_from_history(current_path)
            if new_path:
                item.directory = new_path
                count += 1

    if count > 0:
        print(f"[SavePoints] Fixed relative paths for {count} retrieved assets.")
    return count
