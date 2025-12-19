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

from savepoints_test_case import SavePointsTestCase


class TestCommitSelectionPersistenceExtended(SavePointsTestCase):

    def test_context_persistence_variants_scenario(self):
        """
        Scenario:
        1. Pose Mode: Verify persistence when saving an Armature in Pose Mode.
        2. Sculpt Mode: Verify persistence when saving a Mesh in Sculpt Mode.
        3. No Selection: Verify persistence (and no errors) when nothing is selected.
        """
        print("Starting Context Persistence Variants Scenario...")

        # --- Step 1: Pose Mode Persistence ---
        with self.subTest(step="1. Pose Mode Persistence"):
            print("Testing Pose Mode...")

            # Setup
            bpy.ops.object.armature_add()
            armature = bpy.context.active_object
            armature.name = "TestArmature"

            # Enter Pose Mode
            bpy.ops.object.mode_set(mode='POSE')
            self.assertEqual(bpy.context.object.mode, 'POSE')

            # Commit
            res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Pose Mode Test")
            self.assertIn('FINISHED', res, "Commit failed in Pose Mode")

            # Verify
            # Re-fetch object to avoid stale reference
            current_obj = bpy.context.active_object
            self.assertIsNotNone(current_obj)
            self.assertEqual(current_obj.name, "TestArmature")
            self.assertEqual(current_obj.mode, 'POSE', "Failed to return to Pose Mode after commit")

            # CLEANUP: Return to Object Mode for next step
            bpy.ops.object.mode_set(mode='OBJECT')

        # --- Step 2: Sculpt Mode Persistence ---
        with self.subTest(step="2. Sculpt Mode Persistence"):
            print("Testing Sculpt Mode...")

            # Setup
            bpy.ops.mesh.primitive_uv_sphere_add()
            mesh = bpy.context.active_object
            mesh.name = "SculptMesh"

            # Enter Sculpt Mode
            bpy.ops.object.mode_set(mode='SCULPT')
            self.assertEqual(bpy.context.object.mode, 'SCULPT')

            # Commit
            res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Sculpt Mode Test")
            self.assertIn('FINISHED', res, "Commit failed in Sculpt Mode")

            # Verify
            current_obj = bpy.context.active_object
            self.assertIsNotNone(current_obj)
            self.assertEqual(current_obj.name, "SculptMesh")
            self.assertEqual(current_obj.mode, 'SCULPT', "Failed to return to Sculpt Mode after commit")

            # CLEANUP: Return to Object Mode for next step
            bpy.ops.object.mode_set(mode='OBJECT')

        # --- Step 3: No Selection Persistence ---
        with self.subTest(step="3. No Selection Persistence"):
            print("Testing No Selection...")

            # Setup: Deselect everything
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.view_layer.objects.active = None

            # Verify precondition
            self.assertIsNone(bpy.context.active_object)
            self.assertEqual(len(bpy.context.selected_objects), 0)

            # Commit
            # Ensures the addon handles "None" active object gracefully without crashing
            res = bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Empty Selection Test")
            self.assertIn('FINISHED', res, "Commit failed with no selection")

            # Verify
            self.assertIsNone(bpy.context.active_object, "Active object appeared from nowhere")
            self.assertEqual(len(bpy.context.selected_objects), 0, "Objects got selected unexpectedly")

        print("Context Persistence Variants Scenario: Completed")


if __name__ == "__main__":
    import sys

    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
