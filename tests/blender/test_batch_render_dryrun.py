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
from savepoints.services.batch_render import extract_render_settings, get_worker_script_content, \
    get_batch_render_output_dir
from savepoints.services.snapshot import find_snapshot_path


class TestBatchRenderDryRun(SavePointsTestCase):
    def test_dry_run_execution(self):
        """
        Test the Dry Run functionality:
        1. Checks if 'dry_run=True' overrides settings correctly (JPEG, low res, samples=1).
        2. Checks if output directory has '_dryrun' suffix.
        3. Executes a subprocess render to verify the worker script respects these settings.
        """
        print("\nStarting Dry Run Execution Test...")

        # --- Step 1: Scene Setup ---
        with self.subTest(step="1. Scene Setup"):
            bpy.context.scene.render.resolution_x = 100
            bpy.context.scene.render.resolution_y = 100
            bpy.context.scene.render.resolution_percentage = 100
            bpy.context.scene.render.image_settings.file_format = 'PNG'  # Start with PNG
            bpy.context.scene.render.engine = 'CYCLES'
            bpy.context.scene.cycles.samples = 128  # High samples initially

            if not bpy.context.scene.camera:
                bpy.ops.object.camera_add()
                bpy.context.scene.camera = bpy.context.active_object
                bpy.context.scene.camera.location = (0, -5, 5)
                bpy.context.scene.camera.rotation_euler = (0.8, 0, 0)

            bpy.ops.mesh.primitive_cube_add()
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="DryRun_Version")

        # --- Step 2: Verify Dry Run Settings Extraction ---
        with self.subTest(step="2. Verify Settings & Path"):
            # Check Directory Name
            output_dir_str = get_batch_render_output_dir(dry_run=True)
            print(f"Dry run output dir: {output_dir_str}")
            self.assertTrue(output_dir_str.endswith("_dryrun"),
                            f"Output directory '{output_dir_str}' should end with '_dryrun'")

            # Check Render Settings Overrides
            settings = extract_render_settings(bpy.context, dry_run=True)
            self.assertEqual(settings["output_format_override"], "JPEG", "Format should be forced to JPEG")
            self.assertEqual(settings["resolution_percentage"], 25, "Resolution should be 25%")
            self.assertEqual(settings["samples"], 1, "Samples should be reduced to 1")
            self.assertEqual(settings.get("jpeg_quality"), 70, "JPEG Quality should be 70")

        # --- Step 3: Execute Render via Subprocess ---
        with self.subTest(step="3. Execute Worker"):
            bpy.ops.wm.save_mainfile()  # Ensure snapshot is saved

            v = bpy.context.scene.savepoints_settings.versions[0]
            snapshot_path = find_snapshot_path(v.version_id)
            self.assertTrue(snapshot_path and snapshot_path.exists(), "Snapshot file must exist")

            temp_dir = tempfile.mkdtemp()
            try:
                # write config
                settings_path = os.path.join(temp_dir, "dry_run_config.json")
                with open(settings_path, 'w') as f:
                    json.dump(settings, f)

                # write worker
                worker_script_path = os.path.join(temp_dir, "worker.py")
                with open(worker_script_path, 'w') as f:
                    f.write(get_worker_script_content())

                render_output_dir = os.path.join(temp_dir, "render_result")
                os.makedirs(render_output_dir, exist_ok=True)

                blender_bin = bpy.app.binary_path
                file_prefix = f"{v.version_id}_dryrun"

                cmd = [
                    blender_bin,
                    "-b",
                    "--factory-startup",
                    str(snapshot_path),
                    "-P", worker_script_path,
                    "--",
                    settings_path,
                    render_output_dir,
                    file_prefix
                ]

                print(f"Running subprocess: {cmd}")
                result = subprocess.run(cmd, capture_output=True, text=True)

                if result.returncode != 0:
                    print("STDOUT:", result.stdout)
                    print("STDERR:", result.stderr)

                self.assertEqual(result.returncode, 0, "Render subprocess failed")

                # Check for JPEG file
                expected_file = os.path.join(render_output_dir, f"{file_prefix}.jpg")
                self.assertTrue(os.path.exists(expected_file), f"Expected output file not found: {expected_file}")

                print(f"Dry run render successful: {expected_file}")

            finally:
                shutil.rmtree(temp_dir)


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
