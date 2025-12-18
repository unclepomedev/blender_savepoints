import bpy
from pathlib import Path
from .storage import get_history_dir

def get_ghost_collection_name(version_id: str) -> str:
    return f"Ghost_Reference_{version_id}"

def unload_ghost(version_id: str, context: bpy.types.Context) -> None:
    collection_name = get_ghost_collection_name(version_id)
    existing_col = bpy.data.collections.get(collection_name)

    if not existing_col:
        return

    # 1. Identify objects to remove
    objects_to_remove = [obj for obj in existing_col.objects]

    # 2. Unlink collection from scene
    if context.scene.collection.children.get(collection_name):
        context.scene.collection.children.unlink(existing_col)

    # 3. Remove collection data
    bpy.data.collections.remove(existing_col)

    # 4. Remove objects
    for obj in objects_to_remove:
        try:
            bpy.data.objects.remove(obj, do_unlink=True)
        except Exception:
            pass

    # 5. Cleanup unused libraries
    history_dir_str = get_history_dir()
    if history_dir_str:
        # Look for libraries that seem to be from this snapshot
        libs_to_process = []
        for lib in bpy.data.libraries:
            path_norm = lib.filepath.replace("\\", "/")
            if (f"/{version_id}/snapshot.blend_snapshot" in path_norm or
                    f"/{version_id}/snapshot.blend" in path_norm):
                libs_to_process.append(lib)

        # Collections to check for linked data
        data_collections = [
            bpy.data.objects, bpy.data.meshes, bpy.data.materials,
            bpy.data.textures, bpy.data.images, bpy.data.armatures,
            bpy.data.actions, bpy.data.curves, bpy.data.lights,
            bpy.data.cameras, bpy.data.node_groups, bpy.data.fonts,
            bpy.data.cache_files, bpy.data.movieclips
        ]

        for lib in libs_to_process:
            # Force remove all data blocks linked from this library
            for col in data_collections:
                items = [item for item in col if getattr(item, "library", None) == lib]
                for item in items:
                    try:
                        col.remove(item, do_unlink=True)
                    except Exception:
                        pass

            # Now remove the library itself
            try:
                bpy.data.libraries.remove(lib)
            except Exception:
                pass

def load_ghost(version_id: str, context: bpy.types.Context) -> int:
    collection_name = get_ghost_collection_name(version_id)
    history_dir_str = get_history_dir()
    if not history_dir_str:
        raise FileNotFoundError("History directory not found")

    version_dir = Path(history_dir_str) / version_id
    snapshot_path = version_dir / "snapshot.blend_snapshot"

    if not snapshot_path.exists():
        # Check for legacy snapshot file (.blend)
        legacy_snapshot_path = version_dir / "snapshot.blend"
        if legacy_snapshot_path.exists():
            snapshot_path = legacy_snapshot_path
        else:
            raise FileNotFoundError(f"Snapshot file not found: {snapshot_path}")

    # Load Objects
    with bpy.data.libraries.load(str(snapshot_path), link=True) as (data_from, data_to):
        # Link all objects
        data_to.objects = data_from.objects

    # Create Collection
    new_col = bpy.data.collections.new(collection_name)
    context.scene.collection.children.link(new_col)

    # Link objects and setup viz
    count = 0
    for obj in data_to.objects:
        if obj:
            new_col.objects.link(obj)
            obj.display_type = 'WIRE'
            obj.hide_select = True
            obj.show_in_front = False
            count += 1
            
    return count
