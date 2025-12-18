import sys
import unittest
from pathlib import Path

import bpy

# Add project root to path so we can import the addon modules
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints import operators
from savepoints_test_case import SavePointsTestCase


class TestAutosaveSkipThumb(SavePointsTestCase):
    def test_autosave_skip_thumb(self):
        """
        E2E Scenario Test:
        Validates the workflow of creating snapshots with different thumbnail settings
        sequentially. Uses subTests to ensure failure in one step doesn't block the others.
        """
        print("Starting Autosave/Thumbnail Workflow Scenario...")

        context = bpy.context
        if not hasattr(context.scene, "savepoints_settings"):
            self.fail("savepoints_settings not found on scene")

        history_dir = self.test_dir / ".test_project_history"

        # --- Step 1: Explicit Thumbnail Skipping ---
        with self.subTest(step="1. Explicit Skip Thumbnail"):
            print("Step 1: Testing create_snapshot(skip_thumbnail=True)...")
            version_id_no_thumb = "v_no_thumb"

            operators.create_snapshot(context, version_id_no_thumb, "No Thumb", skip_thumbnail=True)

            # Verification: Snapshot exists, but thumbnail does not.
            v_dir = history_dir / version_id_no_thumb
            self.assertTrue(v_dir.exists(), f"Version dir {v_dir} missing")
            self.assertTrue((v_dir / "snapshot.blend_snapshot").exists(), "Snapshot file missing")
            self.assertFalse((v_dir / "thumbnail.png").exists(), "Thumbnail exists but should have been skipped")

        # --- Step 2: Default Behavior (Attempt Thumbnail) ---
        with self.subTest(step="2. Default Behavior (Attempt Thumbnail)"):
            print("Step 2: Testing create_snapshot(skip_thumbnail=False)...")

            # Simulate some work to change the state for the scenario
            bpy.ops.mesh.primitive_cube_add()

            version_id_with_thumb = "v_with_thumb"

            # Note: In background/headless mode, thumbnail generation may fail or be skipped internally.
            # We wrap this in try-except to ensure the test fails gracefully if the operator crashes.
            try:
                operators.create_snapshot(context, version_id_with_thumb, "With Thumb", skip_thumbnail=False)
            except Exception as e:
                self.fail(f"Snapshot creation failed during thumbnail generation step: {e}")

            v_dir = history_dir / version_id_with_thumb
            self.assertTrue(v_dir.exists(), "Version dir missing for Step 2")
            self.assertTrue((v_dir / "snapshot.blend_snapshot").exists(), "Snapshot file missing for Step 2")

            # Note: We do not strictly assert 'thumbnail.png' exists here because
            # it might not be generated in a headless environment.

        # --- Step 3: Autosave Simulation ---
        with self.subTest(step="3. Autosave Simulation"):
            print("Step 3: Testing Autosave logic simulation...")

            # Simulate autosave call (which forces skip_thumbnail=True)
            # This validates that the 'autosave' reserved ID is handled correctly.
            operators.create_snapshot(context, "autosave", "Auto Save", skip_thumbnail=True)

            autosave_dir = history_dir / "autosave"
            self.assertTrue(autosave_dir.exists(), "Autosave dir not created")
            self.assertFalse((autosave_dir / "thumbnail.png").exists(), "Autosave SHOULD NOT have thumbnail")

        print("Autosave/Thumbnail Workflow Scenario: Completed")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
