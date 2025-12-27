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


class TestBatchRenderFormat(SavePointsTestCase):
    def test_batch_render_format_overrides(self):
        """
        Scenario:
        1. Setup scene with a specific format (BMP).
        2. Create a version.
        3. Test SCENE mode (should produce BMP).
        4. Test PNG mode (should produce PNG).
        """
        print("Starting Batch Render Format Test...")

        # --- Step 1: Scene Setup ---
        with self.subTest(step="1. Scene Setup"):
            bpy.context.scene.render.resolution_x = 32
            bpy.context.scene.render.resolution_y = 32
            bpy.context.scene.render.resolution_percentage = 100

            # Set unconventional format for verification
            bpy.context.scene.render.image_settings.file_format = 'BMP'

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
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="V1")

            # We need to save the mainfile so the snapshot is valid
            bpy.ops.wm.save_mainfile()

        # --- Step 3: Test SCENE mode (BMP) ---
        with self.subTest(step="3. Test SCENE mode"):
            self._run_render_test(override_format='SCENE', expected_ext='.bmp')

        # --- Step 4: Test PNG mode ---
        with self.subTest(step="4. Test PNG mode"):
            self._run_render_test(override_format='PNG', expected_ext='.png')

        # --- Step 5: Test JPEG mode ---
        with self.subTest(step="5. Test JPEG mode"):
            self._run_render_test(override_format='JPEG', expected_ext='.jpg')

        print("Batch Render Format Test: Completed")

    def _run_render_test(self, override_format, expected_ext):
        print(f"Testing override: {override_format}, expecting {expected_ext}")

        settings = bpy.context.scene.savepoints_settings

        # Inject the override into settings
        settings.batch_output_format = override_format

        output_dir_str = get_batch_render_output_dir()
        output_dir = Path(output_dir_str)
        if output_dir.exists():
            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Extract settings
        render_settings = extract_render_settings(bpy.context)

        temp_dir = tempfile.mkdtemp()
        try:
            settings_path = os.path.join(temp_dir, "render_config.json")
            with open(settings_path, 'w') as f:
                json.dump(render_settings, f)

            worker_script_path = get_worker_script_path()

            blender_bin = bpy.app.binary_path

            # Find snapshot
            versions = [v for v in settings.versions if v.version_id.startswith('v')]
            v = versions[0]
            snapshot_path = find_snapshot_path(v.version_id)
            self.assertIsNotNone(snapshot_path, f"Snapshot not found for version {v.version_id}")

            cmd = [
                blender_bin,
                "-b",
                "--factory-startup",
                str(snapshot_path),
                "-P", worker_script_path,
                "--",
                settings_path,
                str(output_dir),
                f"{v.version_id}_render_{override_format}"
            ]

            subprocess.run(cmd, check=True, capture_output=True)

        finally:
            shutil.rmtree(temp_dir)

        # Verification
        files = list(output_dir.glob(f"*{expected_ext}"))
        print(f"Files found: {[f.name for f in files]}")
        self.assertTrue(len(files) > 0, f"No files with extension {expected_ext} found for {override_format}")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
