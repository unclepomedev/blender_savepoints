import json
import os
import shutil
import subprocess
import sys
import tempfile
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
from savepoints.services.snapshot import find_snapshot_path
from savepoints.services.export import create_glb_export_executor


class TestExportGLB(SavePointsTestCase):
    def test_export_glb_scenario(self):
        print("Starting Export GLB Scenario...")

        # --- Step 1: Create History ---
        with self.subTest(step="1. Create History"):
            # V1: Cube
            bpy.ops.mesh.primitive_cube_add(size=2)
            cube = bpy.context.active_object
            cube.name = "MyCube"
            bpy.ops.savepoints.commit("EXEC_DEFAULT", note="V1_Cube")

            # V2: Sphere
            bpy.ops.mesh.primitive_uv_sphere_add(radius=1)
            sphere = bpy.context.active_object
            sphere.name = "MySphere"
            # V2 has MyCube (from V1) and MySphere
            bpy.ops.savepoints.commit("EXEC_DEFAULT", note="V2_Sphere")

        # --- Step 2: Execute Export GLB Logic ---
        with self.subTest(step="2. Execute Export Logic"):
            bpy.ops.wm.save_mainfile()

            settings = bpy.context.scene.savepoints_settings

            # Find V1
            v1 = next(v for v in settings.versions if v.note == "V1_Cube")

            output_dir = Path(tempfile.mkdtemp())
            self.addCleanup(lambda d=output_dir: shutil.rmtree(d, ignore_errors=True))

            # --- Verify Service Configuration ---
            # Verify that the service picks up the blend filename
            executor = create_glb_export_executor(v1, ["MyCube"], str(output_dir))
            expected_filename = Path(bpy.data.filepath).stem
            self.assertEqual(
                executor.filename_override,
                expected_filename,
                "Service did not use Blender filename as override",
            )

            # Verify Custom Filename Template
            custom_template = "MyAsset_{version}"
            executor_custom = create_glb_export_executor(
                v1, ["MyCube"], str(output_dir), filename_template=custom_template
            )
            expected_custom_filename = bpy.path.clean_name(f"MyAsset_{v1.version_id}")
            self.assertEqual(
                executor_custom.filename_override,
                expected_custom_filename,
                "Service did not use custom filename template correctly",
            )

            # Cleanup executor temp
            if executor.temp_dir and os.path.exists(executor.temp_dir):
                shutil.rmtree(executor.temp_dir)
            if executor_custom.temp_dir and os.path.exists(executor_custom.temp_dir):
                shutil.rmtree(executor_custom.temp_dir)

            # --- Verify Worker Execution with Custom Name ---
            # We simulate what the executor would pass (the custom name)
            custom_name = "MyGameAsset"

            # Prepare settings: select "MyCube"
            export_settings = {"target_objects": ["MyCube"]}

            settings_path = output_dir / "export_settings.json"
            with open(settings_path, "w") as f:
                json.dump(export_settings, f)

            worker_script_path = (
                PROJECT_ROOT / "savepoints" / "workers" / "export_worker.py"
            )
            blender_bin = bpy.app.binary_path

            snapshot_path = find_snapshot_path(v1.version_id)

            # Run worker
            cmd = [
                blender_bin,
                "-b",
                "--factory-startup",
                str(snapshot_path),
                "-P",
                str(worker_script_path),
                "--",
                str(settings_path),
                str(output_dir),
                custom_name,  # Passing the custom name here
            ]

            print(f"Running command: {cmd}")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)

            self.assertEqual(result.returncode, 0, "Worker process failed")

            # Check output
            expected_output = output_dir / f"{custom_name}.glb"
            self.assertTrue(
                expected_output.exists(), "GLB file was not created with custom name"
            )

            # Test missing object warning
            export_settings_missing = {"target_objects": ["NonExistentObject"]}
            settings_path_missing = output_dir / "export_settings_missing.json"
            with open(settings_path_missing, "w") as f:
                json.dump(export_settings_missing, f)

            cmd_missing = [
                blender_bin,
                "-b",
                "--factory-startup",
                str(snapshot_path),
                "-P",
                str(worker_script_path),
                "--",
                str(settings_path_missing),
                str(output_dir),
                f"{v1.version_id}_missing",
            ]

            result_missing = subprocess.run(
                cmd_missing, capture_output=True, text=True, timeout=30
            )
            # Expect failure because worker exits with 1 if no objects found
            self.assertNotEqual(
                result_missing.returncode, 0, "Worker should fail when no objects found"
            )
            self.assertIn("No matching objects found", result_missing.stdout)


if __name__ == "__main__":
    result = unittest.main(argv=["first-arg-is-ignored"], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
