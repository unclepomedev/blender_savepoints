# SPDX-License-Identifier: GPL-3.0-or-later

from pathlib import Path

import bpy

from .snapshot import find_snapshot_path
from .storage import (
    get_history_dir,
    SNAPSHOT_FILENAME,
    LEGACY_SNAPSHOT_FILENAME,
    is_safe_filename
)

_LINKED_DATA_COLLECTIONS = (
    "objects", "collections", "meshes", "materials", "textures", "images",
    "armatures", "actions", "curves", "lights", "cameras",
    "node_groups", "fonts", "cache_files", "movieclips"
)


def get_ghost_collection_name(version_id: str) -> str:
    return f"Ghost_Reference_{version_id}"


def unload_ghost(version_id: str, context: bpy.types.Context) -> None:
    collection_name = get_ghost_collection_name(version_id)
    existing_col = bpy.data.collections.get(collection_name)

    if existing_col:
        _remove_ghost_collection(existing_col, context)

    _purge_ghost_libraries(version_id)
    _cleanup_orphan_libraries()


def _cleanup_orphan_libraries():
    """Removes any libraries that have 0 users to prevent buildup."""
    for lib in list(bpy.data.libraries):
        if lib.users == 0:
            try:
                bpy.data.libraries.remove(lib)
            except Exception:
                pass


def _remove_ghost_collection(collection: bpy.types.Collection, context: bpy.types.Context) -> None:
    # 1. Identify objects to remove
    objects_to_remove = [obj for obj in collection.objects]

    # 2. Unlink collection from scene
    if context.scene.collection.children.get(collection.name):
        context.scene.collection.children.unlink(collection)

    # 3. Remove collection data
    bpy.data.collections.remove(collection)

    # 4. Remove objects
    for obj in objects_to_remove:
        try:
            bpy.data.objects.remove(obj, do_unlink=True)
        except Exception:
            pass


def _purge_ghost_libraries(version_id: str) -> None:
    if not is_safe_filename(version_id):
        print(f"[SavePoints] Security Warning: Invalid version_id detected in purge: {version_id}")
        return

    history_dir_str = get_history_dir()
    if not history_dir_str:
        return

    history_dir = Path(history_dir_str).resolve()

    expected_paths = set()
    for fname in [SNAPSHOT_FILENAME, LEGACY_SNAPSHOT_FILENAME]:
        p = (history_dir / version_id / fname).resolve()
        expected_paths.add(p)

    libs_to_process = []
    for lib in bpy.data.libraries:
        if not lib.filepath:
            continue

        abs_filepath_str = bpy.path.abspath(lib.filepath)

        try:
            lib_path = Path(abs_filepath_str).resolve()

            if lib_path in expected_paths:
                libs_to_process.append(lib)
        except (OSError, ValueError):
            continue

    for lib in libs_to_process:
        for attr in _LINKED_DATA_COLLECTIONS:
            collection = getattr(bpy.data, attr, None)
            if not collection:
                continue

            items = [item for item in collection if getattr(item, "library", None) == lib]
            for item in items:
                try:
                    collection.remove(item, do_unlink=True)
                except Exception:
                    pass

        # Now remove the library itself
        try:
            bpy.data.libraries.remove(lib)
        except Exception:
            pass


def load_ghost(version_id: str, context: bpy.types.Context) -> int:
    collection_name = get_ghost_collection_name(version_id)

    snapshot_path = find_snapshot_path(version_id)

    if not snapshot_path:
        raise FileNotFoundError(f"Snapshot file not found for version: {version_id}")

    objects = _load_objects_from_snapshot(str(snapshot_path))
    return _setup_ghost_collection(collection_name, objects, context)


def _load_objects_from_snapshot(path: str) -> list:
    with bpy.data.libraries.load(path, link=True) as (data_from, data_to):
        data_to.objects = data_from.objects
    return data_to.objects


def _setup_ghost_collection(name: str, objects: list, context: bpy.types.Context) -> int:
    new_col = bpy.data.collections.new(name)
    context.scene.collection.children.link(new_col)

    count = 0
    for obj in objects:
        if obj:
            new_col.objects.link(obj)
            obj.display_type = 'WIRE'
            obj.hide_select = True
            obj.show_in_front = False
            count += 1
    return count


def load_single_object_ghost(version_id: str, object_name: str, context: bpy.types.Context) -> None:
    cleanup_single_object_ghost(object_name, context)

    snapshot_path = find_snapshot_path(version_id)
    if not snapshot_path or not Path(snapshot_path).exists():
        print(f"[SavePoints] Snapshot file missing for version: {version_id}")
        return

    try:
        with bpy.data.libraries.load(str(snapshot_path), link=True) as (data_from, data_to):
            if object_name in data_from.objects:
                data_to.objects = [object_name]
            else:
                return
    except OSError:
        print(f"[SavePoints] Failed to load library: {snapshot_path}")
        return

    obj = data_to.objects[0] if data_to.objects else None
    if not obj:
        return

    col_name = f"Ghost_Single_{object_name}"

    new_col = bpy.data.collections.new(col_name)
    context.scene.collection.children.link(new_col)
    new_col.objects.link(obj)

    obj.display_type = 'WIRE'
    obj.hide_select = True
    obj.show_in_front = True


def cleanup_single_object_ghost(object_name: str, context: bpy.types.Context) -> None:
    col_name = f"Ghost_Single_{object_name}"
    col = bpy.data.collections.get(col_name)

    if col:
        _remove_ghost_collection(col, context)

    _cleanup_orphan_libraries()
