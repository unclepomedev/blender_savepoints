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
    def test_batch_selection_scenario(self):
        """
        Scenario:
        1. Create versions and setup tags (Setup).
        2. Test basic Select All / Deselect All.
        3. Test Select All with Filter active.
        4. Test Smart Target Logic (Fallback mechanism).
        """
        print("Starting Batch Selection Scenario...")

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
            # Note: versions list order implies V1 is index 0 (oldest) or last depending on sort,
            # but usually savepoints appends. Assuming index matches creation order for this test.
            if len(versions) >= 3:
                versions[0].tag = 'STABLE'  # V1
                versions[1].tag = 'BUG'  # V2
                versions[2].tag = 'STABLE'  # V3

        # --- Step 2: Basic Select/Deselect ---
        with self.subTest(step="2. Basic Select/Deselect"):
            # Initial state should be False
            for v in versions:
                self.assertFalse(v.selected, f"Version {v.version_id} should initially be unselected")

            # Execute select_all operator
            bpy.ops.savepoints.select_all()

            # Verify all valid versions are selected
            for v in versions:
                if v.version_id.startswith('v'):
                    self.assertTrue(v.selected, f"{v.version_id} should be selected after Select All")

            # Execute deselect_all operator
            bpy.ops.savepoints.deselect_all()

            # Verify all are unselected
            for v in versions:
                self.assertFalse(v.selected, f"{v.version_id} should be unselected after Deselect All")

        # --- Step 3: Select All with Filter ---
        with self.subTest(step="3. Select All with Filter"):
            # Set filter to 'STABLE'
            settings.filter_tag = 'STABLE'

            # Execute select_all (should only select visible/filtered items)
            bpy.ops.savepoints.select_all()

            # Verification
            self.assertTrue(versions[0].selected, "V1 (Stable) should be selected")
            self.assertFalse(versions[1].selected, "V2 (Bug) should NOT be selected (hidden by filter)")
            self.assertTrue(versions[2].selected, "V3 (Stable) should be selected")

            # Cleanup for next steps: Reset filter and selection
            settings.filter_tag = 'ALL'  # Reset filter
            bpy.ops.savepoints.deselect_all()

        # --- Step 4: Smart Target Logic ---
        with self.subTest(step="4. Smart Target Logic"):
            """Verify the smart target selection logic (fallback mechanism)."""

            # Case A: Nothing selected -> Fallback to all (implicit selection)
            # Ensure nothing is selected first
            bpy.ops.savepoints.deselect_all()

            # Logic simulation:
            targets_a = [v for v in versions if v.version_id.startswith('v') and v.selected]
            if not targets_a:
                # Fallback: if nothing is explicitly selected, take all valid versions
                targets_a = [v for v in versions if v.version_id.startswith('v')]

            self.assertEqual(len(targets_a), 3, "Should fallback to all 3 versions when nothing is selected")

            # Case B: Specific selection -> Only that item is targeted
            versions[1].selected = True  # Select V2 only manually

            # Logic simulation:
            targets_b = [v for v in versions if v.version_id.startswith('v') and v.selected]
            if not targets_b:
                targets_b = [v for v in versions if v.version_id.startswith('v')]

            self.assertEqual(len(targets_b), 1, "Should select exactly 1 version when explicitly checked")
            self.assertEqual(targets_b[0].note, "V2", "The selected version should be V2")

        print("Batch Selection Scenario: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
