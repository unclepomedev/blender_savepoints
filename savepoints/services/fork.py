import bpy

def make_all_local_and_clear_assets():
    """
    Make all linked data local AND clear their asset status.
    Returns:
        tuple: (has_changed, cleared_count)
    """
    has_changed = False
    cleared_count = 0

    try:
        if bpy.data.libraries:
            try:
                bpy.ops.wm.make_local(type='ALL')
                has_changed = True
            except (RuntimeError, AttributeError):
                data_collections = [
                    bpy.data.objects, bpy.data.meshes, bpy.data.materials,
                    bpy.data.node_groups, bpy.data.textures, bpy.data.images,
                    bpy.data.actions, bpy.data.collections
                ]

                found_linked = False
                for collection in data_collections:
                    for data_block in collection:
                        if data_block.library:
                            data_block.make_local()
                            found_linked = True

                if found_linked:
                    has_changed = True

    except Exception as e:
        print(f"SavePoints: Error during localization: {e}")

    check_collections = [
        bpy.data.objects,
        bpy.data.materials,
        bpy.data.node_groups,
        bpy.data.collections,
        bpy.data.actions,
        bpy.data.worlds
    ]

    for collection in check_collections:
        for data_block in collection:
            if data_block.asset_data:
                data_block.asset_clear()
                cleared_count += 1
                has_changed = True
                print(f"SavePoints: Cleared asset mark from {data_block.name}")

    return has_changed, cleared_count
