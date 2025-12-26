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

from savepoints.services.batch_render import extract_render_settings, get_worker_script_content, get_batch_render_output_dir
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

            # Use the actual service to determine output path
            output_dir_str = get_batch_render_output_dir()
            output_dir = Path(output_dir_str)
            
            if output_dir.exists():
                shutil.rmtree(output_dir)
            
            # Helper creates the full path, but we need to ensure it exists for the test logic (worker expects it to exist? No, worker assumes it can write to it. Operator creates it.)
            # The operator creates the directory. So we should create it here too.
            output_dir.mkdir(parents=True, exist_ok=True)

            render_settings = extract_render_settings(bpy.context)
            temp_dir = tempfile.mkdtemp()

            try:
                settings_path = os.path.join(temp_dir, "render_config.json")
                with open(settings_path, 'w') as f:
                    json.dump(render_settings, f)

                worker_script_path = os.path.join(temp_dir, "worker.py")
                with open(worker_script_path, 'w') as f:
                    f.write(get_worker_script_content())

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

        print("Batch Render Scenario: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
