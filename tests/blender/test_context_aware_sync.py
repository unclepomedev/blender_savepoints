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
from savepoints.services.batch_render import extract_render_settings
# Assuming these functions are in workers/scene_utils.py based on previous context
from savepoints.workers.scene_utils import setup_camera, setup_view_settings


class TestContextAwareSync(SavePointsTestCase):
    def setUp(self):
        super().setUp()
        self.scene = bpy.context.scene

    def test_camera_lens_sync(self):
        """
        Scenario:
        Verify that camera lens data (Focal Length, Shift, Clipping, Sensor Fit)
        is correctly extracted and reapplied to a new camera.
        """
        print("\nStarting Camera Lens Sync Test...")

        # --- Step 1: Setup Source Camera ---
        cam_data_src = bpy.data.cameras.new("SourceCam")
        cam_obj_src = bpy.data.objects.new("SourceCam", cam_data_src)
        self.scene.collection.objects.link(cam_obj_src)
        self.scene.camera = cam_obj_src

        # Set non-default values
        cam_data_src.lens = 85.0
        cam_data_src.shift_x = 0.2
        cam_data_src.shift_y = -0.1
        cam_data_src.clip_start = 0.5
        cam_data_src.clip_end = 500.0
        cam_data_src.sensor_fit = 'VERTICAL'

        # --- Step 2: Extract Settings ---
        settings = extract_render_settings(bpy.context)

        extracted_data = settings.get("camera_data")
        self.assertIsNotNone(extracted_data, "camera_data should be present in settings")
        self.assertEqual(extracted_data["lens"], 85.0)
        self.assertEqual(extracted_data["sensor_fit"], 'VERTICAL')

        # --- Step 3: Apply to Target (Simulate Worker) ---
        # Clear the current camera to force setup_camera to create/assign a new one
        self.scene.camera = None
        setup_camera(self.scene, settings)

        # --- Step 4: Verification ---
        new_cam = self.scene.camera
        self.assertIsNotNone(new_cam, "A camera should be assigned to the scene")

        cd = new_cam.data
        self.assertAlmostEqual(cd.lens, 85.0)
        self.assertAlmostEqual(cd.shift_x, 0.2)
        self.assertAlmostEqual(cd.shift_y, -0.1)
        self.assertAlmostEqual(cd.clip_start, 0.5)
        self.assertEqual(cd.sensor_fit, 'VERTICAL')

        print("Camera Lens Sync Test: Completed")

    def test_orthographic_sync(self):
        """
        Scenario:
        Verify that Orthographic projection settings (Type, Scale) are synced.
        """
        print("\nStarting Orthographic Sync Test...")

        # --- Step 1: Setup Source (Ortho) ---
        cam_data = bpy.data.cameras.new("OrthoCam")
        cam_obj = bpy.data.objects.new("OrthoCam", cam_data)
        self.scene.collection.objects.link(cam_obj)
        self.scene.camera = cam_obj

        cam_data.type = 'ORTHO'
        cam_data.ortho_scale = 12.5

        # --- Step 2: Extract & Apply ---
        settings = extract_render_settings(bpy.context)

        # Clear camera
        self.scene.camera = None
        setup_camera(self.scene, settings)

        # --- Step 3: Verification ---
        new_cam = self.scene.camera
        self.assertEqual(new_cam.data.type, 'ORTHO')
        self.assertAlmostEqual(new_cam.data.ortho_scale, 12.5)

        print("Orthographic Sync Test: Completed")

    def test_color_management_sync(self):
        """
        Scenario:
        Verify that Color Management settings (View Transform, Look, Exposure, Gamma)
        are correctly synced.
        """
        print("\nStarting Color Management Sync Test...")

        # --- Step 1: Setup Source Settings ---
        vs = self.scene.view_settings

        try:
            vs.view_transform = 'AgX'
            target_look = 'AgX - High Contrast'
        except TypeError:
            vs.view_transform = 'Standard'
            target_look = 'High Contrast'

        try:
            vs.look = target_look
        except TypeError:
            print(f"Warning: Look '{target_look}' not found. Using 'None'.")
            vs.look = 'None'
            target_look = 'None'

        vs.exposure = 1.5
        vs.gamma = 2.2

        # --- Step 2: Extract ---
        settings = extract_render_settings(bpy.context)

        vs_data = settings.get("view_settings")
        self.assertIsNotNone(vs_data)
        self.assertEqual(vs_data["look"], target_look)
        self.assertAlmostEqual(vs_data["exposure"], 1.5)

        # --- Step 3: Reset & Apply ---
        # Reset settings to default to ensure values are actually applied
        vs.look = 'None'
        vs.exposure = 0.0
        vs.gamma = 1.0

        setup_view_settings(self.scene, settings)

        # --- Step 4: Verification ---
        self.assertEqual(vs.look, target_look)
        self.assertAlmostEqual(vs.exposure, 1.5)
        self.assertAlmostEqual(vs.gamma, 2.2)

        print("Color Management Sync Test: Completed")

    def test_missing_data_resilience(self):
        """
        Scenario:
        Ensure the setup functions do not crash if the JSON data is incomplete
        (e.g., data from older versions of the addon).
        """
        print("\nStarting Resilience Test...")

        # Simulate empty/legacy settings
        empty_settings = {
            "camera_matrix_world": [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
            # "camera_data" is missing
            "view_settings": {}
        }

        try:
            setup_camera(self.scene, empty_settings)
            setup_view_settings(self.scene, empty_settings)
        except Exception as e:
            self.fail(f"Setup functions crashed on missing data: {e}")

        # Check if defaults are applied (Default lens is usually 50mm)
        if self.scene.camera:
            self.assertEqual(self.scene.camera.data.lens, 50.0)

        print("Resilience Test: Completed")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
