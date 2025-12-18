import sys
import unittest
import zipfile
from pathlib import Path

import bpy

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))
from savepoints_test_case import SavePointsTestCase


class TestExportZip(SavePointsTestCase):
    def test_export_zip(self):
        print("Starting Export Zip Test...")
        # SavePointsTestCase setup provides self.test_dir and self.blend_path (test_project.blend)

        # 3. Create some history (Version 1)
        print("Creating history...")
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="V1")

        # 4. Create Version 2
        bpy.ops.mesh.primitive_uv_sphere_add()
        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="V2")

        history_dir = self.test_dir / ".test_project_history"
        if not history_dir.exists():
            self.fail("History dir setup failed")

        # 5. Export ZIP
        print("Testing Export Zip...")
        output_zip_path = self.test_dir / "export.zip"

        # Pass filepath explicitly for headless execution
        res = bpy.ops.savepoints.export_project_zip('EXEC_DEFAULT', filepath=str(output_zip_path))

        if "FINISHED" not in res:
            self.fail(f"Export zip failed with result: {res}")

        if not output_zip_path.exists():
            self.fail("Zip file was not created")

        # 6. Verify Zip Content
        print("Verifying Zip content...")
        with zipfile.ZipFile(output_zip_path, 'r') as zf:
            file_list = zf.namelist()
            print("Files in zip:", file_list)

            # Check main blend file
            if "test_project.blend" not in file_list:
                self.fail("Main blend file missing in zip")

            # Check history structure
            # Should have .test_project_history/manifest.json
            expected_manifest = ".test_project_history/manifest.json"
            if expected_manifest not in file_list:
                self.fail(f"Manifest missing in zip: {expected_manifest}")

            # Check versions
            # .test_project_history/v001/snapshot.blend_snapshot
            if not any("v001/snapshot.blend_snapshot" in f for f in file_list):
                self.fail("Version 1 snapshot missing in zip")
            if not any("v002/snapshot.blend_snapshot" in f for f in file_list):
                self.fail("Version 2 snapshot missing in zip")

            # Check compression
            info = zf.getinfo("test_project.blend")
            if info.compress_type != zipfile.ZIP_STORED:
                print(f"Warning: Compression type is {info.compress_type}, expected STORED (0)")
                self.fail(f"Compression is not ZIP_STORED. Got: {info.compress_type}")

        print("Export Zip Verification: OK")
        print("ALL TESTS PASSED")


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
