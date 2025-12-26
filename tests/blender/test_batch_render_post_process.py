import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import bpy

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints_test_case import SavePointsTestCase
from savepoints.services.post_process import (
    create_vse_timelapse,
    open_folder_platform_independent,
    send_os_notification
)


class TestBatchRenderPostProcess(SavePointsTestCase):

    def test_vse_timelapse_generation(self):
        """
        Test if VSE scene is correctly created from a folder of images.
        """
        print("\nTesting VSE Timelapse Generation...")

        # 1. Setup Dummy Images with VALID PNG HEADER
        # Blender logs error if file format is unknown.
        # Minimal 1x1 Transparent PNG signature
        valid_png_data = (
            b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89'
            b'\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
        )

        temp_dir = tempfile.mkdtemp()
        try:
            for i in range(1, 4):  # 3 frames
                fname = f"v{i:03d}.png"
                with open(os.path.join(temp_dir, fname), 'wb') as f:
                    f.write(valid_png_data)

            # 2. Execute
            scene_name = create_vse_timelapse(temp_dir, scene_name_suffix="_TestTL")

            # 3. Verify Scene
            self.assertIsNotNone(scene_name)
            self.assertIn("_TestTL", scene_name)
            self.assertIn(scene_name, bpy.data.scenes)

            new_scene = bpy.data.scenes[scene_name]

            # 4. Verify VSE Data
            self.assertIsNotNone(new_scene.sequence_editor)

            # API Compatibility Check
            strips = getattr(new_scene.sequence_editor, 'strips', None)
            if strips is None:
                strips = getattr(new_scene.sequence_editor, 'sequences', None)

            self.assertEqual(len(strips), 1, "Should have exactly 1 strip")

            strip = strips[0]
            # Even with dummy png, Blender might read it differently,
            # but we check if logic set the duration based on file count
            self.assertEqual(strip.frame_final_duration, 3, "Strip duration should match file count")
            self.assertEqual(new_scene.frame_end, 3, "Scene end frame should match file count")

            print(f"  [OK] VSE Scene '{scene_name}' created with 3 frames.")

        finally:
            shutil.rmtree(temp_dir)

    def test_folder_open_mock(self):
        """
        Test folder opening logic using Mock.
        Fix: Patch 'bpy.ops.wm' instead of 'path_open' directly to handle dynamic API.
        """
        print("\nTesting Folder Open (Mocked)...")

        # Patching 'bpy.ops.wm' ensures we intercept the call even if path_open is dynamically resolved
        with patch('bpy.ops.wm') as mock_wm:
            temp_dir = tempfile.mkdtemp()
            try:
                # Execute
                result = open_folder_platform_independent(temp_dir)

                # Verify
                self.assertTrue(result)
                # Check if path_open was called on the mock object
                mock_wm.path_open.assert_called_once_with(filepath=temp_dir)
                print("  [OK] bpy.ops.wm.path_open was called correctly.")

            finally:
                shutil.rmtree(temp_dir)

    def test_os_notification_mock(self):
        """
        Test OS notification logic for different platforms.
        Fix: Mock 'subprocess' module entirely to inject Windows constants on macOS/Linux.
        """
        print("\nTesting OS Notification (Mocked)...")

        title = "Test Title"
        message = "Test Message"

        # --- Subtest 1: macOS ---
        with self.subTest("macOS Notification"):
            # Patch subprocess in the target module
            with patch('sys.platform', 'darwin'), \
                    patch('savepoints.services.post_process.subprocess') as mock_subprocess:
                send_os_notification(title, message)

                self.assertTrue(mock_subprocess.run.called)
                args, _ = mock_subprocess.run.call_args
                command_list = args[0]
                self.assertEqual(command_list[0], "osascript")
                print("  [OK] macOS logic verified.")

        # --- Subtest 2: Windows ---
        with self.subTest("Windows Notification"):
            # Patch subprocess AND inject CREATE_NO_WINDOW constant which is missing on macOS
            with patch('sys.platform', 'win32'), \
                    patch('savepoints.services.post_process.subprocess') as mock_subprocess:
                # Inject the Windows-only constant into the mock
                mock_subprocess.CREATE_NO_WINDOW = 0x08000000

                send_os_notification(title, message)

                self.assertTrue(mock_subprocess.run.called)
                args, kw = mock_subprocess.run.call_args
                command_list = args[0]
                self.assertEqual(command_list[0], "powershell")

                # Verify creationflags was passed using our mocked constant
                self.assertEqual(kw.get('creationflags'), 0x08000000)
                print("  [OK] Windows logic verified.")

        # --- Subtest 3: Linux ---
        with self.subTest("Linux Notification"):
            with patch('sys.platform', 'linux'), \
                    patch('savepoints.services.post_process.subprocess') as mock_subprocess:
                send_os_notification(title, message)

                self.assertTrue(mock_subprocess.run.called)
                args, _ = mock_subprocess.run.call_args
                command_list = args[0]
                self.assertEqual(command_list[0], "notify-send")
                print("  [OK] Linux logic verified.")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
