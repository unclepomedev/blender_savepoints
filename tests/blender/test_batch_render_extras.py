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
from savepoints.services.batch_render import extract_render_settings
from savepoints.services.post_process import create_vse_timelapse


class TestBatchRenderExtras(SavePointsTestCase):
    def test_settings_extraction_complex_formats(self):
        """
        Scenario:
        Test if complex image settings (EXR, JPEG Quality) are correctly extracted to the dictionary.
        This ensures the Worker receives the correct data without running the actual render.
        """
        print("\nStarting Settings Extraction Test...")

        # --- Step 1: EXR Extraction Test ---
        with self.subTest(step="1. EXR Settings"):
            scene = bpy.context.scene
            img_settings = scene.render.image_settings

            # Setup specific OPEN_EXR settings
            img_settings.file_format = 'OPEN_EXR'
            img_settings.color_depth = '16'
            img_settings.exr_codec = 'ZIP'
            img_settings.color_mode = 'RGBA'

            # Extract
            data = extract_render_settings(bpy.context)

            # Verify
            self.assertEqual(data["image_settings"]["file_format"], 'OPEN_EXR')
            self.assertEqual(data["image_settings"]["exr_codec"], 'ZIP')
            self.assertEqual(data["image_settings"]["color_depth"], '16')
            self.assertEqual(data["image_settings"]["color_mode"], 'RGBA')

        # --- Step 2: JPEG Extraction Test ---
        with self.subTest(step="2. JPEG Settings"):
            scene = bpy.context.scene
            img_settings = scene.render.image_settings

            # Setup JPEG with Quality
            img_settings.file_format = 'JPEG'
            img_settings.quality = 45
            img_settings.color_mode = 'BW'  # Test non-standard color mode for JPEG

            data = extract_render_settings(bpy.context)

            self.assertEqual(data["image_settings"]["file_format"], 'JPEG')
            self.assertEqual(data["image_settings"]["quality"], 45)
            self.assertEqual(data["image_settings"]["color_mode"], 'BW')

        print("Settings Extraction Test: Completed")

    def test_vse_timelapse_creation(self):
        """
        Scenario:
        Test the VSE timelapse creation logic explicitly.
        1. Create dummy image files.
        2. Run create_vse_timelapse.
        3. Verify Scene, FPS, and Strip length.
        """
        print("\nStarting VSE Timelapse Test...")

        # --- Step 1: Setup Logic ---
        with self.subTest(step="1. Setup Logic"):
            # Setup specific FPS to test inheritance
            bpy.context.scene.render.fps = 60
            bpy.context.scene.render.fps_base = 1.001

            temp_dir = tempfile.mkdtemp()

        try:
            # --- Step 2: Create Dummy Files ---
            with self.subTest(step="2. Create Dummy Files"):
                dummy_img = bpy.data.images.new("TempDummy", width=4, height=4, alpha=True)

                original_settings = bpy.context.scene.render.image_settings.file_format
                bpy.context.scene.render.image_settings.file_format = 'PNG'

                file_names = ["render_001.png", "render_002.png", "render_003.png"]
                for fname in file_names:
                    filepath = os.path.join(temp_dir, fname)
                    dummy_img.filepath_raw = filepath
                    dummy_img.save()

                bpy.data.images.remove(dummy_img)
                bpy.context.scene.render.image_settings.file_format = original_settings

            # --- Step 3: Execute Service ---
            with self.subTest(step="3. Execute Service"):
                scene_name = create_vse_timelapse(temp_dir, scene_name_suffix="_TestTL")

                # Verifications
                self.assertIsNotNone(scene_name)
                self.assertIn(scene_name, bpy.data.scenes)

                new_scene = bpy.data.scenes[scene_name]

                # Check FPS Inheritance
                self.assertEqual(new_scene.render.fps, 60)
                self.assertAlmostEqual(new_scene.render.fps_base, 1.001)

                # Check Strip
                self.assertIsNotNone(new_scene.sequence_editor)

                if hasattr(new_scene.sequence_editor, 'strips'):
                    strips = new_scene.sequence_editor.strips
                else:
                    strips = new_scene.sequence_editor.sequences

                self.assertEqual(len(strips), 1)

                strip = strips[0]
                self.assertEqual(strip.type, 'IMAGE')
                self.assertEqual(strip.frame_final_duration, 3)  # Should match file count

        finally:
            shutil.rmtree(temp_dir)

        print("VSE Timelapse Test: Completed")

    def test_partial_failure_resilience(self):
        """
        Scenario:
        Queue 3 versions.
        - V1: Success
        - V2: Failure (Simulated by deleting the snapshot file)
        - V3: Success

        Ensure that V2's failure does not stop V3 from rendering.
        """
        print("\nStarting Partial Failure Resilience Test...")

        # --- Step 1: Create 3 Versions ---
        with self.subTest(step="1. Setup History"):
            bpy.context.scene.render.engine = 'CYCLES'
            bpy.context.scene.cycles.device = 'CPU'

            bpy.context.scene.cycles.samples = 1
            bpy.context.scene.cycles.preview_samples = 1
            bpy.context.scene.cycles.max_bounces = 0
            bpy.context.scene.cycles.diffuse_bounces = 0
            bpy.context.scene.cycles.glossy_bounces = 0
            bpy.context.scene.cycles.transparent_max_bounces = 0
            bpy.context.scene.cycles.transmission_bounces = 0
            bpy.context.scene.cycles.volume_bounces = 0
            bpy.context.scene.cycles.use_denoising = False
            bpy.context.scene.render.resolution_x = 32
            bpy.context.scene.render.resolution_y = 32
            bpy.context.scene.render.resolution_percentage = 100

            if not bpy.context.scene.camera:
                bpy.ops.object.camera_add(location=(0, -10, 5), rotation=(1.1, 0, 0))
                bpy.context.scene.camera = bpy.context.active_object

            # V1
            bpy.ops.mesh.primitive_cube_add()
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="V1_Success")

            # V2 (Will be corrupted)
            bpy.context.active_object.location.x += 2
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="V2_Fail")
            v2_id = bpy.context.scene.savepoints_settings.versions[-1].version_id

            # V3
            bpy.context.active_object.location.x += 2
            bpy.ops.savepoints.commit('EXEC_DEFAULT', note="V3_Success")

            # Save Mainfile
            bpy.ops.wm.save_mainfile()

        # --- Step 2: Sabotage V2 ---
        from savepoints.services.snapshot import find_snapshot_path

        v2_snapshot = find_snapshot_path("v002")
        if v2_snapshot and v2_snapshot.exists():
            os.remove(v2_snapshot)
            print(f"Deleted snapshot for test: {v2_snapshot}")

        # --- Step 3: Execute Batch Render Loop ---
        with self.subTest(step="3. Execute Loop"):
            settings = bpy.context.scene.savepoints_settings
            target_versions = [v for v in settings.versions if v.version_id.startswith('v')]

            # Setup output
            from savepoints.services.batch_render import get_batch_render_output_dir
            output_dir = Path(get_batch_render_output_dir())
            if output_dir.exists():
                shutil.rmtree(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)

            # Setup Worker
            from savepoints.services.batch_render import extract_render_settings, get_worker_script_path

            render_settings = extract_render_settings(bpy.context)
            temp_dir = tempfile.mkdtemp()

            try:
                # Config setup
                settings_path = os.path.join(temp_dir, "render_config.json")
                with open(settings_path, 'w') as f:
                    json.dump(render_settings, f)

                worker_script_path = get_worker_script_path()
                blender_bin = bpy.app.binary_path

                # The Simulation Loop
                for v in target_versions:
                    snapshot_path = find_snapshot_path(v.version_id)

                    # NOTE: In real operator, we skip if file not found BEFORE process start.
                    # But here, we want to simulate a crash or blender failure.
                    # So we pass a non-existent path to Blender to force a failure.
                    cmd_path = str(snapshot_path)

                    cmd = [
                        blender_bin,
                        "-b",
                        "--factory-startup",
                        cmd_path,
                        "-P", worker_script_path,
                        "--",
                        settings_path,
                        str(output_dir),
                        f"{v.version_id}_resilience"
                    ]

                    try:
                        subprocess.run(cmd, check=True, capture_output=True, text=True)
                    except subprocess.CalledProcessError as e:
                        if v2_id in v.version_id:
                            continue

            finally:
                shutil.rmtree(temp_dir)

            # --- Step 4: Verification ---
            # V1 and V3 should exist. V2 should not.
            files = list(output_dir.glob("*.png"))
            file_names = [f.name for f in files]
            print(f"Generated Files: {file_names}")

            self.assertTrue(any("v001" in f for f in file_names), "V1 should succeed")
            self.assertFalse(any("v002" in f for f in file_names), "V2 should fail (no file)")
            self.assertTrue(any("v003" in f for f in file_names), "V3 should succeed (resilience works)")

            # Cleanup
            if output_dir.exists():
                shutil.rmtree(output_dir)

        print("Partial Failure Resilience Test: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
