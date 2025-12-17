import shutil
import sys
import traceback
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints  # noqa: E402
from savepoints import core
from savepoints.services.storage import load_manifest

def setup_test_env():
    test_dir = ROOT / "test_quick_save_run"
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    return test_dir


def cleanup_test_env(test_dir):
    if test_dir.exists():
        shutil.rmtree(test_dir)


def main():
    print("Starting Quick Save & Edit Note Test...")
    test_dir = setup_test_env()
    blend_file_path = test_dir / "test_quick_save.blend"

    try:
        # 1. Setup
        # Create an object to verify context-aware note assignment
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.object.name = "QuickSaveCube"
        obj = bpy.context.object

        bpy.ops.wm.save_as_mainfile(filepath=str(blend_file_path))

        # Restore selection/active just in case save cleared it
        if obj.name in bpy.data.objects:
             # Need to get the object from the new file context if save_as_mainfile reloaded it?
             # No, save_as_mainfile keeps the current session alive but might reset some state.
             pass
        
        # Ensure it is active
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)

        savepoints.register()

        settings = bpy.context.scene.savepoints_settings

        print("\n--- Test 1: Quick Save (Skip Dialog) ---")

        # Enable Quick Save (disable dialog)
        settings.show_save_dialog = False

        # When show_save_dialog is False, the operator should execute immediately (via invoke calling execute)
        # without showing a popup. But since we invoke operators via python script with 'INVOKE_DEFAULT',
        # we can test if it runs without blocking or error.
        # Actually, if we call with 'INVOKE_DEFAULT' and it opens a dialog, the script usually blocks or fails
        # in background mode.
        # However, to be sure, we can check the result.

        # Note: If show_save_dialog logic works, invoke() calls execute() directly and returns FINISHED.
        # If it didn't work, it would call invoke_props_dialog which returns RUNNING_MODAL (and might fail in bg).

        # Execute operator
        
        # Override context to ensure active_object is passed correctly in background mode
        # Using temp_override for Blender 3.2+
        with bpy.context.temp_override(active_object=obj, object=obj, selected_objects=[obj], selected_editable_objects=[obj]):
            res = bpy.ops.savepoints.commit('INVOKE_DEFAULT')

        if "FINISHED" not in res:
            raise RuntimeError(f"Quick Save failed: result={res}")

        # Verify version created
        manifest = load_manifest()
        versions = manifest.get("versions", [])
        if not versions:
            raise RuntimeError("Version not created")

        v1 = versions[0]  # Newest
        print(f"Generated Note: '{v1['note']}'")

        # Verify default note generation (Strict check restored after manual fix)
        # The manual fix ensures invoke() sets the note before execution.
        expected_note = "Object: QuickSaveCube"
        if v1['note'] != expected_note:
            raise RuntimeError(f"Note mismatch. Expected '{expected_note}', got '{v1['note']}'")

        print("Test 1 Passed.")

        print("\n--- Test 2: Edit Note ---")

        v1_id = v1["id"]
        new_note_text = "Updated Note"

        # Call edit_note operator
        # We pass properties directly and use EXEC_DEFAULT to skip invoke dialog
        res = bpy.ops.savepoints.edit_note('EXEC_DEFAULT', version_id=v1_id, new_note=new_note_text)

        if "FINISHED" not in res:
            raise RuntimeError(f"Edit Note failed: result={res}")

        # Verify manifest
        manifest = load_manifest()
        v1_updated = manifest["versions"][0]

        if v1_updated["id"] != v1_id:
            raise RuntimeError("Version order changed unexpectedly")

        if v1_updated["note"] != new_note_text:
            raise RuntimeError(f"Note update failed. Expected '{new_note_text}', got '{v1_updated['note']}'")

        print("Test 2 Passed.")

        print("\nALL TESTS PASSED")

    except Exception:
        traceback.print_exc()
        sys.exit(1)
    finally:
        try:
            savepoints.unregister()
        except Exception:
            pass
        cleanup_test_env(test_dir)


if __name__ == "__main__":
    main()
