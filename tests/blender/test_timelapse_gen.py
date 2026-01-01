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


class TestTimelapseGen(SavePointsTestCase):
    def setUp(self):
        super().setUp()
        self.temp_dir = tempfile.mkdtemp(prefix="sp_test_timelapse_")
        self.input_dir = os.path.join(self.temp_dir, "input_images")
        os.makedirs(self.input_dir, exist_ok=True)
        self._create_dummy_frames(self.input_dir, count=5)
        self.worker_script = os.path.join(PROJECT_ROOT, "savepoints", "workers", "timelapse_worker.py")

    def tearDown(self):
        try:
            shutil.rmtree(self.temp_dir)
        except Exception as e:
            print(f"Warning: Failed to clean up temp dir: {e}")
        super().tearDown()

    def _create_dummy_frames(self, directory, count=5):
        print(f"Creating dummy frames in: {directory}")
        for i in range(count):
            # Create a simple image (64x64)
            img = bpy.data.images.new(f"v{i:03d}_render", width=64, height=64)
            # Make it colored (R=1.0) just to have data
            img.generated_color = (1.0, 0.0, 0.0, 1.0)

            file_path = os.path.join(directory, f"v{i:03d}_render.png")
            img.filepath_raw = file_path
            img.file_format = 'PNG'
            img.save()
            bpy.data.images.remove(img)

    def test_timelapse_worker_basic(self):
        """Test basic timelapse generation without burn-in."""
        print("\n=== Test: Basic Timelapse ===")
        output_file = os.path.join(self.temp_dir, "output_basic.mp4")

        cmd = [
            bpy.app.binary_path,
            "-b",
            "--factory-startup",
            "-P", self.worker_script,
            "--",
            self.input_dir,
            output_file,
            "24"
        ]

        self._run_worker(cmd)
        self._assert_file_exists(output_file)

    def test_timelapse_worker_basic_duration(self):
        """Test basic timelapse generation duration check."""
        print("\n=== Test: Basic Timelapse Duration ===")
        output_file = os.path.join(self.temp_dir, "output_basic_duration.mp4")

        cmd = [
            bpy.app.binary_path,
            "-b",
            "--factory-startup",
            "-P", self.worker_script,
            "--",
            self.input_dir,
            output_file,
            "24"
        ]

        stdout = self._run_worker(cmd)
        self.assertIn("Timelapse Duration: 30 frames", stdout)
        self._assert_file_exists(output_file)

    def test_timelapse_worker_burnin(self):
        """Test timelapse generation WITH burn-in."""
        print("\n=== Test: Burn-in Timelapse ===")
        output_file = os.path.join(self.temp_dir, "output_burnin.mp4")

        # Args: input, output, fps, burn_in(1), pos('TL')
        cmd = [
            bpy.app.binary_path,
            "-b",
            "--factory-startup",
            "-P", self.worker_script,
            "--",
            self.input_dir,
            output_file,
            "24",
            "1",  # Burn-in True
            "TL"  # Top Left
        ]

        stdout = self._run_worker(cmd)
        self.assertIn("Burn-in: True (TL)", stdout)
        self.assertIn("Adding Burn-in text", stdout)
        self.assertNotIn("Warning: Failed to add text strip", stdout)
        self._assert_file_exists(output_file)

    def _run_worker(self, cmd):
        print(f"Running worker command: {' '.join(cmd)}")
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print("--- Worker STDOUT ---")
            print(result.stdout)
            print("---------------------")
            return result.stdout
        except subprocess.CalledProcessError as e:
            print("--- Worker FAILED ---")
            print(f"Return Code: {e.returncode}")
            print("STDOUT:", e.stdout)
            print("STDERR:", e.stderr)
            self.fail("Worker process failed. See output above.")

    def _assert_file_exists(self, filepath):
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            print(f"Success: File created at {filepath} ({file_size} bytes)")
            self.assertGreater(file_size, 0, "File is empty")
        else:
            self.fail(f"File was not created at {filepath}")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
