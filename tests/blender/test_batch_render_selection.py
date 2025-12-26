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


class TestBatchSelection(SavePointsTestCase):
    def test_batch_selection_ui_operators(self):
        """
        Scenario:
        1. Create versions and setup tags (Setup).
        2. Test 'Select All' and 'Deselect All' operators.
        3. Test 'Select All' behavior when a Filter is active.
        """
        print("Starting Batch Selection UI Operators Test...")

        settings = bpy.context.scene.savepoints_settings
        versions = settings.versions

        # --- Step 1: Data Setup ---
        with self.subTest(step="1. Data Setup"):
            # Prepare 3 versions
            bpy.ops.mesh.primitive_cube_add()
            bpy.ops.savepoints.commit(note="V1")
            bpy.ops.savepoints.commit(note="V2")
            bpy.ops.savepoints.commit(note="V3")

            # Assign tags: V1: STABLE, V2: BUG, V3: STABLE
            if len(versions) >= 3:
                versions[0].tag = 'STABLE'  # V1
                versions[1].tag = 'BUG'  # V2
                versions[2].tag = 'STABLE'  # V3

        # --- Step 2: Basic Select/Deselect ---
        with self.subTest(step="2. Basic Select/Deselect"):
            # Initial state should be False
            for v in versions:
                self.assertFalse(v.selected, f"Version {v.version_id} should initially be unselected")

            # Execute select_all operator (Simulate UI button click)
            bpy.ops.savepoints.select_all()

            # Verify flags are updated
            for v in versions:
                if v.version_id.startswith('v'):
                    self.assertTrue(v.selected, f"{v.version_id} should be selected after Select All")

            # Execute deselect_all operator
            bpy.ops.savepoints.deselect_all()

            # Verify flags are cleared
            for v in versions:
                self.assertFalse(v.selected, f"{v.version_id} should be unselected after Deselect All")

        # --- Step 3: Select All with Filter ---
        with self.subTest(step="3. Select All with Filter"):
            # Set filter to 'STABLE'
            settings.filter_tag = 'STABLE'

            # Execute select_all (Operator should respect the filter)
            bpy.ops.savepoints.select_all()

            # Verification
            self.assertTrue(versions[0].selected, "V1 (Stable) should be selected")
            self.assertFalse(versions[1].selected, "V2 (Bug) should NOT be selected (hidden by filter)")
            self.assertTrue(versions[2].selected, "V3 (Stable) should be selected")

            # Cleanup: Reset filter and selection
            settings.filter_tag = 'ALL'
            bpy.ops.savepoints.deselect_all()

        print("Batch Selection UI Operators Test: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
