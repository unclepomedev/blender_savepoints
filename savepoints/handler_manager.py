import bpy
from .services.asset_path import unmap_snapshot_paths
from .services.rescue import delete_rescue_temp_file

class RescuePostLoadHandler:
    """
    Handler to fix asset paths and cleanup temporary files after rescue operation.
    """
    def __init__(self, temp_blend_path, initial_obj_count):
        self.temp_blend_path = temp_blend_path
        self.initial_obj_count = initial_obj_count

    def __call__(self, scene, _):
        # Check if append actually happened (objects added or paths fixed)
        current_obj_count = len(bpy.data.objects)
        paths_fixed = False
        try:
            paths_fixed = unmap_snapshot_paths()
        except Exception as e:
            print(f"[SavePoints] Error fixing paths after rescue: {e}")

        # If objects were added OR paths were modified, we assume the user is done with the file
        has_changes = (current_obj_count != self.initial_obj_count) or paths_fixed

        if has_changes:
            self.unregister()
            # Cleanup temp file
            delete_rescue_temp_file(self.temp_blend_path)

    def register(self):
        bpy.app.handlers.depsgraph_update_post.append(self)

    def unregister(self):
        if self in bpy.app.handlers.depsgraph_update_post:
            bpy.app.handlers.depsgraph_update_post.remove(self)
