import sys
import unittest
from pathlib import Path

import bpy

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))
from savepoints_test_case import SavePointsTestCase
from savepoints.services.storage import load_manifest


class TestQuickSaveEditNote(SavePointsTestCase):
    def test_quick_save_edit_note(self):
        print("Starting Quick Save & Edit Note Test...")
        # SavePointsTestCase setup provides self.test_dir and self.blend_path (test_project.blend)

        # 1. Setup
        # Create an object to verify context-aware note assignment
        bpy.ops.mesh.primitive_cube_add()
        bpy.context.object.name = "QuickSaveCube"
        obj = bpy.context.object

        # Ensure it is active
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)

        settings = bpy.context.scene.savepoints_settings

        print("\n--- Test 1: Quick Save (Skip Dialog) ---")

        # Enable Quick Save (disable dialog)
        settings.show_save_dialog = False

        # When show_save_dialog is False, the operator should execute immediately (via invoke calling execute)
        # without showing a popup. But since we invoke operators via python script with 'INVOKE_DEFAULT',
        # we can test if it runs without blocking or error.

        # Execute operator

        # Override context to ensure active_object is passed correctly in background mode
        # Using temp_override for Blender 3.2+
        with bpy.context.temp_override(active_object=obj, object=obj, selected_objects=[obj],
                                       selected_editable_objects=[obj]):
            res = bpy.ops.savepoints.commit('INVOKE_DEFAULT')

        if "FINISHED" not in res:
            self.fail(f"Quick Save failed: result={res}")

        # Verify version created
        manifest = load_manifest()
        versions = manifest.get("versions", [])
        if not versions:
            self.fail("Version not created")

        v1 = versions[0]  # Newest
        print(f"Generated Note: '{v1['note']}'")

        # Verify default note generation (Strict check restored after manual fix)
        # The manual fix ensures invoke() sets the note before execution.
        expected_note = "Object: QuickSaveCube"
        if v1['note'] != expected_note:
            self.fail(f"Note mismatch. Expected '{expected_note}', got '{v1['note']}'")

        print("Test 1 Passed.")

        print("\n--- Test 2: Edit Note ---")

        v1_id = v1["id"]
        new_note_text = "Updated Note"

        # Call edit_note operator
        # We pass properties directly and use EXEC_DEFAULT to skip invoke dialog
        res = bpy.ops.savepoints.edit_note('EXEC_DEFAULT', version_id=v1_id, new_note=new_note_text)

        if "FINISHED" not in res:
            self.fail(f"Edit Note failed: result={res}")

        # Verify manifest
        manifest = load_manifest()
        v1_updated = manifest["versions"][0]

        if v1_updated["id"] != v1_id:
            self.fail("Version order changed unexpectedly")

        if v1_updated["note"] != new_note_text:
            self.fail(f"Note update failed. Expected '{new_note_text}', got '{v1_updated['note']}'")

        print("Test 2 Passed.")
        print("\nALL TESTS PASSED")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
