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
from savepoints.services.retrieve import (
    create_retrieve_temp_file,
    get_importable_objects,
    append_objects,
    delete_retrieve_temp_file
)


class TestRetrieveObjects(SavePointsTestCase):

    def setUp(self):
        super().setUp()
        self.history_dir = self.test_dir / ".test_project_history"

    def test_retrieve_service_workflow(self):
        """
        Scenario:
        1. Create a snapshot with a specific object.
        2. Delete the object from current scene.
        3. Use retrieve service functions to bring it back.
        4. Verify success and cleanup.
        """
        print("Starting Retrieve Service Workflow Test...")

        version_id = "v001"
        obj_name = "RetrieveMe_Service"

        # --- 1. Setup Snapshot ---
        # Create object
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.name = obj_name

        # Create version directory
        version_dir = self.history_dir / version_id
        version_dir.mkdir(parents=True, exist_ok=True)

        # Save snapshot
        snapshot_path = version_dir / "snapshot.blend_snapshot"
        bpy.ops.wm.save_as_mainfile(filepath=str(snapshot_path), copy=True)
        print(f"Created snapshot: {snapshot_path}")

        # Delete object
        bpy.data.objects.remove(obj)
        self.assertNotIn(obj_name, bpy.data.objects)

        # --- 2. Create Temp File ---
        temp_path = create_retrieve_temp_file(snapshot_path)
        print(f"Created temp file: {temp_path}")

        try:
            self.assertTrue(temp_path.exists())
            self.assertTrue(str(temp_path).endswith(".blend"))

            # --- 3. Get Importable Objects ---
            objects = get_importable_objects(temp_path)
            print(f"Importable objects: {objects}")
            self.assertIn(obj_name, objects)

            # --- 4. Append Object ---
            appended = append_objects(temp_path, [obj_name])
            print(f"Appended objects: {appended}")

            self.assertEqual(len(appended), 1)
            self.assertEqual(appended[0].name, obj_name)
            self.assertIn(obj_name, bpy.data.objects)

        finally:
            # --- 5. Cleanup ---
            delete_retrieve_temp_file(temp_path)
            self.assertFalse(temp_path.exists())

        print("Retrieve Service Workflow Test: Completed")


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
