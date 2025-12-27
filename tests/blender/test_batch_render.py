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

from savepoints.services.batch_render import extract_render_settings, get_worker_script_path, \
    get_batch_render_output_dir
from savepoints.services.snapshot import find_snapshot_path


class TestBatchRender(SavePointsTestCase):
    def test_batch_render_scenario(self):
        """
        Scenario:
        1. Setup a simple scene.
        2. Create versions.
        3. [UPDATED] Use Service functions to manually execute render logic synchronously.
        """
        print("Starting Batch Render Scenario...")

        # --- Step 1: Scene Setup ---
        with self.subTest(step="1. Scene Setup"):
            bpy.context.scene.render.resolution_x = 32
            bpy.context.scene.render.resolution_y = 32
            bpy.context.scene.render.resolution_percentage = 100
            bpy.context.scene.render.image_settings.file_format = 'PNG'

            bpy.context.scene.render.engine = 'CYCLES'
            bpy.context.scene.cycles.device = 'CPU'
            bpy.context.scene.cycles.samples = 1

            if not bpy.context.scene.camera:
                bpy.ops.object.camera_add()
                bpy.context.scene.camera = bpy.context.active_object

            bpy.context.scene.camera.location = (0, -10, 5)
            bpy.context.scene.camera.rotation_euler = (1.1, 0, 0)

        # --- Step 2: Create History ---
        with self.subTest(step="2. Create History"):
            bpy.ops.mesh.primitive_cube_add()
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="V1_Cube")

            bpy.ops.mesh.primitive_uv_sphere_add()
            bpy.context.active_object.location.x = 2
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="V2_Sphere")

        # --- Step 3: Execute Batch Render (Direct Logic Test) ---
        with self.subTest(step="3. Execute Batch Render Logic"):
            bpy.ops.wm.save_mainfile()

            settings = bpy.context.scene.savepoints_settings
            target_versions = [v for v in settings.versions if v.version_id.startswith('v')]

            output_dir_str = get_batch_render_output_dir()
            output_dir = Path(output_dir_str)

            if output_dir.exists():
                shutil.rmtree(output_dir)

            output_dir.mkdir(parents=True, exist_ok=True)

            render_settings = extract_render_settings(bpy.context)
            temp_dir = tempfile.mkdtemp()

            try:
                settings_path = os.path.join(temp_dir, "render_config.json")
                with open(settings_path, 'w') as f:
                    json.dump(render_settings, f)

                worker_script_path = get_worker_script_path()

                blender_bin = bpy.app.binary_path

                for v in target_versions:
                    snapshot_path = find_snapshot_path(v.version_id)
                    if not snapshot_path or not snapshot_path.exists():
                        continue

                    cmd = [
                        blender_bin,
                        "-b",
                        "--factory-startup",
                        str(snapshot_path),
                        "-P", worker_script_path,
                        "--",
                        settings_path,
                        str(output_dir),
                        f"{v.version_id}_render"
                    ]

                    subprocess.run(cmd, check=True, capture_output=True)

            finally:
                shutil.rmtree(temp_dir)

            files = list(output_dir.glob("*.png"))
            print(f"Found rendered files in {output_dir}: {[f.name for f in files]}")

            for v in target_versions:
                matched = any(f"{v.version_id}_render" in f.name for f in files)
                self.assertTrue(matched, f"Render output for {v.version_id} missing")

            if output_dir.exists():
                shutil.rmtree(output_dir)

        print("Batch Render Scenario: Completed")

    def test_batch_render_fallback_scenario(self):
        """
        Scenario for Camera Fallback:
        1. Create a version WITH a camera.
        2. Delete the camera and create a version WITHOUT a camera.
        3. Add a new camera to the current scene (Source of Truth).
        4. Execute batch render.
        5. Verify that the version without a camera was rendered using the fallback logic.
        """
        print("\nStarting Batch Render Fallback Scenario...")

        # --- Step 1: Scene Setup (Low Res for Speed) ---
        with self.subTest(step="1. Setup"):
            bpy.context.scene.render.resolution_x = 32
            bpy.context.scene.render.resolution_y = 32
            bpy.context.scene.render.resolution_percentage = 100
            bpy.context.scene.render.engine = 'CYCLES'
            bpy.context.scene.cycles.device = 'CPU'
            bpy.context.scene.cycles.samples = 1

        # --- Step 2: Create History with and without Camera ---
        with self.subTest(step="2. Create Mixed History"):
            # v001: Normal (Has Camera)
            if not bpy.context.scene.camera:
                bpy.ops.object.camera_add()
                bpy.context.scene.camera = bpy.context.active_object

            bpy.ops.mesh.primitive_cube_add()
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Has_Camera")

            # v002: Abnormal (No Camera)
            # Delete the camera to simulate a state where it was removed
            bpy.ops.object.select_all(action='DESELECT')
            for obj in bpy.context.scene.objects:
                if obj.type == 'CAMERA':
                    obj.select_set(True)
            bpy.ops.object.delete()

            bpy.ops.mesh.primitive_uv_sphere_add()
            bpy.context.active_object.location.x = 2
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="No_Camera_Missing")

            # --- CRITICAL STEP ---
            # Restore a camera in the CURRENT scene.
            # The batch render relies on the "current active camera" to define the view.
            bpy.ops.object.camera_add()
            cam = bpy.context.active_object
            cam.name = "New_Master_Camera"
            bpy.context.scene.camera = cam
            cam.location = (0, -15, 5)
            cam.rotation_euler = (1.3, 0, 0)

            # Save main file to ensure paths are correct
            bpy.ops.wm.save_mainfile()

        # --- Step 3: Execute Batch Render ---
        with self.subTest(step="3. Execute Render"):
            settings = bpy.context.scene.savepoints_settings
            # Filter specifically for the "No_Camera" version to test fallback
            target_versions = [v for v in settings.versions if "No_Camera" in v.note]

            self.assertTrue(len(target_versions) > 0, "Failed to find the test version")

            output_dir_str = get_batch_render_output_dir()
            output_dir = Path(output_dir_str)
            if output_dir.exists():
                shutil.rmtree(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)

            # Extract settings (This will capture the "New_Master_Camera" matrix)
            render_settings = extract_render_settings(bpy.context)

            temp_dir = tempfile.mkdtemp()
            try:
                settings_path = os.path.join(temp_dir, "render_config.json")
                with open(settings_path, 'w') as f:
                    json.dump(render_settings, f)

                worker_script_path = get_worker_script_path()

                blender_bin = bpy.app.binary_path

                for v in target_versions:
                    snapshot_path = find_snapshot_path(v.version_id)

                    cmd = [
                        blender_bin,
                        "-b",
                        "--factory-startup",
                        str(snapshot_path),
                        "-P", worker_script_path,
                        "--",
                        settings_path,
                        str(output_dir),
                        f"{v.version_id}_fallback_test"
                    ]

                    # Run process. If fallback logic is missing, this should fail (exit code 1)
                    # or produce no output.
                    try:
                        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
                    except subprocess.CalledProcessError as e:
                        print(f"\n[Worker Stdout]:\n{e.stdout}")
                        print(f"\n[Worker Stderr]:\n{e.stderr}")
                        self.fail(f"Render failed for {v.version_id}. Fallback logic might be missing.")

            finally:
                shutil.rmtree(temp_dir)

            # Verify Output
            files = list(output_dir.glob("*.png"))  # Assuming PNG default
            print(f"Found files: {[f.name for f in files]}")

            self.assertTrue(len(files) > 0, "No image generated. Fallback camera creation likely failed.")

            if output_dir.exists():
                shutil.rmtree(output_dir)

        print("Batch Render Fallback Scenario: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
