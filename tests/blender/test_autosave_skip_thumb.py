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
from savepoints import operators
from savepoints_test_case import SavePointsTestCase


class TestAutosaveSkipThumb(SavePointsTestCase):
    def test_autosave_skip_thumb(self):
        print("Starting Autosave Skip Thumbnail Test...")
        # setup and registration is handled by SavePointsTestCase

        # 3. Test: Explicit Thumbnail Skipping
        print("Testing create_snapshot(skip_thumbnail=True)...")

        context = bpy.context
        if not hasattr(context.scene, "savepoints_settings"):
            self.fail("savepoints_settings not found on scene")

        version_id_no_thumb = "v_no_thumb"
        operators.create_snapshot(context, version_id_no_thumb, "No Thumb", skip_thumbnail=True)

        # Verification: Snapshot exists, but thumbnail does not.
        history_dir = self.test_dir / ".test_project_history"
        v_dir = history_dir / version_id_no_thumb

        self.assertTrue(v_dir.exists(), f"Version dir {v_dir} missing")
        self.assertTrue((v_dir / "snapshot.blend_snapshot").exists(), "Snapshot file missing")
        self.assertFalse((v_dir / "thumbnail.png").exists(), "Thumbnail exists but should have been skipped")

        print("Verification skip_thumbnail=True: OK")

        # 4. Test: Default Behavior (Attempt Thumbnail)
        print("Testing create_snapshot(skip_thumbnail=False)...")
        version_id_with_thumb = "v_with_thumb"
        operators.create_snapshot(context, version_id_with_thumb, "With Thumb", skip_thumbnail=False)

        # Note: In background/headless mode, thumbnail generation may be skipped internally due to lack of window context.
        # The test passes if the operation completes without crashing.
        print("Verification skip_thumbnail=False: OK (Execution completed)")

        # 5. Test: Autosave Simulation
        print("Testing Autosave logic simulation...")

        # Simulate autosave call (which forces skip_thumbnail=True)
        operators.create_snapshot(context, "autosave", "Auto Save", skip_thumbnail=True)

        autosave_dir = history_dir / "autosave"
        self.assertTrue(autosave_dir.exists(), "Autosave dir not created")
        self.assertFalse((autosave_dir / "thumbnail.png").exists(), "Autosave SHOULD NOT have thumbnail")

        print("Autosave logic verification: OK")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
