import sys
import unittest
from pathlib import Path
from unittest.mock import patch

import bpy

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services import versioning, autosave
from savepoints_test_case import SavePointsTestCase


class TestAutosavePhysicalDeletion(SavePointsTestCase):
    """
    Verify that autosave deletions and explicit physical deletions
    bypass the system trash (recycle bin) and use direct removal.
    """

    def test_delete_version_by_id_physical(self):
        """
        Scenario:
        Verify that delete_version_by_id with use_trash=False actually deletes
        the directory and ensures send2trash is NOT called.
        Mocks get_history_dir to ensure we are targeting the test folder specifically.
        """
        print("Starting Physical Deletion Test...")

        # Setup paths
        history_dir = self.test_dir / ".test_project_history"
        version_id = "v_phys_test"
        version_dir = history_dir / version_id

        # Mock manifest data
        fake_manifest = {
            "versions": [
                {"id": version_id, "is_protected": False}
            ]
        }

        # --- Step 1: Setup Environment ---
        with self.subTest(step="1. Prepare Version Directory"):
            history_dir.mkdir(parents=True, exist_ok=True)
            version_dir.mkdir(exist_ok=True)
            self.assertTrue(version_dir.exists(), "Setup failed: Version dir should exist.")

        # --- Step 2: Execute & Verify ---
        with self.subTest(step="2. Execute Deletion and Verify Mechanics"):
            # Mock get_history_dir to point explicitly to our test history_dir
            # This ensures the function targets the folder we created, regardless of bpy.data.filepath
            with patch("savepoints.services.versioning.load_manifest", return_value=fake_manifest), \
                    patch("savepoints.services.versioning.save_manifest"), \
                    patch("savepoints.services.versioning.get_history_dir", return_value=str(history_dir)), \
                    patch("savepoints.services.versioning.send2trash") as mock_send2trash:
                print(f"Executing delete_version_by_id('{version_id}', use_trash=False)...")

                # Execute
                versioning.delete_version_by_id(version_id, use_trash=False)

                # Verify 1: send2trash was NOT called
                mock_send2trash.assert_not_called()

                # Verify 2: The directory is physically gone
                self.assertFalse(
                    version_dir.exists(),
                    "Physical deletion failed: Directory still exists."
                )

        print("Physical Deletion Test: Completed")

    def test_autosave_uses_physical_deletion(self):
        """
        Scenario:
        Verify that the autosave timer calls the deletion function
        specifically with use_trash=False.
        """
        print("Starting Autosave Wiring Test...")

        context = bpy.context
        scene = context.scene

        # Ensure settings exist
        if not hasattr(scene, "savepoints_settings"):
            self.fail("savepoints_settings not found")

        settings = scene.savepoints_settings

        # --- Step 1: Configure Settings ---
        with self.subTest(step="1. Configure Autosave Settings"):
            settings.use_auto_save = True
            settings.auto_save_interval = 1  # min
            settings.last_autosave_timestamp = "500.0"

        # --- Step 2: Verify Timer Logic ---
        with self.subTest(step="2. Trigger Timer and Verify Calls"):
            # Mock time to control "now"
            with patch("savepoints.services.autosave.delete_version_by_id") as mock_delete, \
                    patch("savepoints.services.autosave.create_snapshot") as mock_create, \
                    patch("savepoints.services.autosave.time.time", return_value=100000.0):
                print("Executing autosave_timer()...")
                autosave.autosave_timer()

                # Verify: create_snapshot was called
                mock_create.assert_called()

                # Verify: delete_version_by_id was called for 'autosave' with use_trash=False
                mock_delete.assert_called_with("autosave", use_trash=False)

        print("Autosave Wiring Test: Completed")


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
