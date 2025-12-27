import os
import shutil
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


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
