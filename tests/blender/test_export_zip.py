import sys
import unittest
import zipfile
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


class TestExportZip(SavePointsTestCase):
    def test_export_zip_scenario(self):
        """
        Scenario:
        1. Create multiple versions (history).
        2. Execute the 'export_project_zip' operator.
        3. Verify the ZIP structure (main file, manifest, snapshots).
        4. Verify that compression is disabled (ZIP_STORED) for performance.
        """
        print("Starting Export Zip Scenario...")

        # Setup paths
        # SavePointsTestCase creates 'test_project.blend', so history is '.test_project_history'
        history_dir_name = ".test_project_history"
        output_zip_path = self.test_dir / "export.zip"

        # --- Step 1: Create History Data ---
        with self.subTest(step="1. Create History"):
            print("Creating versions...")

            # Version 1
            bpy.ops.mesh.primitive_cube_add()
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="V1")

            # Version 2
            bpy.ops.mesh.primitive_uv_sphere_add()
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="V2")

            # Sanity check: History directory should exist on disk now
            history_dir = self.test_dir / history_dir_name
            self.assertTrue(history_dir.exists(), "History directory failed to generate during setup")

        # --- Step 2: Execute Export Operator ---
        with self.subTest(step="2. Execute Export"):
            print("Executing Export Operator...")

            # Pass filepath explicitly for headless execution
            res = bpy.ops.savepoints.export_project_zip('EXEC_DEFAULT', filepath=str(output_zip_path))

            self.assertIn('FINISHED', res, "Export operator failed or did not finish")
            self.assertTrue(output_zip_path.exists(), "Export ZIP file was not created")

        # --- Step 3: Verify Zip Content & Compression ---
        with self.subTest(step="3. Verify Zip Content"):
            print("Verifying Zip structure...")

            with zipfile.ZipFile(output_zip_path, 'r') as zf:
                file_list = zf.namelist()

                # 1. Verify Main Blend File
                self.assertIn("test_project.blend", file_list, "Main blend file missing in zip")

                # 2. Verify Manifest
                expected_manifest = f"{history_dir_name}/manifest.json"
                self.assertIn(expected_manifest, file_list, f"Manifest missing in zip: {expected_manifest}")

                # 3. Verify Snapshot Structure (Loose check for file paths)
                # We check if path contains 'v001/snapshot' etc.
                v1_exists = any(f"v001/snapshot" in f for f in file_list)
                v2_exists = any(f"v002/snapshot" in f for f in file_list)

                self.assertTrue(v1_exists, "Version 1 snapshot missing in zip")
                self.assertTrue(v2_exists, "Version 2 snapshot missing in zip")

                # 4. Verify Compression Type
                # The addon should use ZIP_STORED (no compression) for speed with blend files
                info = zf.getinfo("test_project.blend")
                self.assertEqual(
                    info.compress_type,
                    zipfile.ZIP_STORED,
                    f"Compression type is {info.compress_type}, expected ZIP_STORED (0)"
                )

        print("Export Zip Scenario: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
