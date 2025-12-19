# SPDX-License-Identifier: GPL-3.0-or-later

from typing import Any

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
        getattr(bpy.data, "cache_files", []),  # This does not exist in Mac, Blender5.0.
        getattr(bpy.data, "movieclips", []),  # This does not exist in Mac, Blender5.0.
        getattr(bpy.data, "volumes", []),
        getattr(bpy.data, "texts", []),
    ]


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
    collections_to_remap = _get_collections_to_remap()

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
    collections_to_remap = _get_collections_to_remap()

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
