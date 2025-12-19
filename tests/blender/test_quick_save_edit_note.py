import sys
import unittest
from pathlib import Path

import bpy

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.storage import load_manifest
from savepoints_test_case import SavePointsTestCase


class TestQuickSaveEditNote(SavePointsTestCase):

    def test_quick_save_and_edit_scenario(self):
        """
        Scenario:
        1. Quick Save: Execute commit with 'show_save_dialog=False'.
           Verify it runs without blocking (FINISHED) and generates a context-aware note.
        2. Edit Note: Modify the note of the existing version.
           Verify the change is persisted to the manifest.
        """
        print("Starting Quick Save & Edit Note Scenario...")

        # Variables to persist across subtests
        version_id = None
        target_obj_name = "QuickSaveCube"
        initial_expected_note = f"Object: {target_obj_name}"
        updated_note_text = "Updated Note by Test"

        # --- Step 1: Setup & Quick Save ---
        with self.subTest(step="1. Quick Save (Skip Dialog)"):
            print("Executing Quick Save...")

            # Setup Object
            bpy.ops.mesh.primitive_cube_add()
            obj = bpy.context.active_object
            obj.name = target_obj_name

            # Configure Settings: Disable Dialog for Quick Save behavior
            bpy.context.scene.savepoints_settings.show_save_dialog = False

            # Execute Commit using INVOKE_DEFAULT.
            # We use INVOKE because the logic to "Skip Dialog" resides in the invoke() method.
            # We use temp_override to ensure 'generate_default_note' sees the correct active object.
            with bpy.context.temp_override(
                    active_object=obj,
                    object=obj,
                    selected_objects=[obj],
                    selected_editable_objects=[obj]
            ):
                res = bpy.ops.savepoints.commit('INVOKE_DEFAULT')

            self.assertIn('FINISHED', res, "Quick Save failed (likely stuck in modal or error)")

        # --- Step 2: Verify Created Version ---
        with self.subTest(step="2. Verify Auto Note"):
            print("Verifying auto-generated note...")

            manifest = load_manifest()
            versions = manifest.get("versions", [])

            self.assertEqual(len(versions), 1, "Expected exactly 1 version to be created")

            v1 = versions[0]
            self.assertEqual(v1['note'], initial_expected_note,
                             f"Note mismatch. Expected '{initial_expected_note}', got '{v1['note']}'")

            # Store ID for next step
            version_id = v1['id']

        # --- Step 3: Edit Note ---
        with self.subTest(step="3. Edit Note"):
            print(f"Editing note for {version_id}...")

            # Execute Edit Note using EXEC_DEFAULT (Direct execution, no UI needed)
            res = bpy.ops.savepoints.edit_note(
                'EXEC_DEFAULT',
                version_id=version_id,
                new_note=updated_note_text
            )

            self.assertIn('FINISHED', res, "Edit Note operator failed")

        # --- Step 4: Verify Update ---
        with self.subTest(step="4. Verify Note Update"):
            print("Verifying persistence of updated note...")

            # Reload manifest to check disk state
            manifest = load_manifest()
            v1_updated = manifest["versions"][0]

            # Verify integrity
            self.assertEqual(v1_updated["id"], version_id, "Version ID mismatch (Order changed?)")
            self.assertEqual(v1_updated["note"], updated_note_text,
                             f"Note update failed. Expected '{updated_note_text}', got '{v1_updated['note']}'")

        print("Quick Save & Edit Note Scenario: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
