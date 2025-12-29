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
    def test_timelapse_worker(self):
        """
        Test the standalone timelapse generation worker script.
        """
        print("\n=== Starting Timelapse Worker Test ===")

        # 1. Setup Input Directory with Dummy Images
        temp_dir = tempfile.mkdtemp(prefix="sp_test_timelapse_")
        input_dir = os.path.join(temp_dir, "input_images")
        os.makedirs(input_dir, exist_ok=True)
        print(f"Creating dummy frames in: {input_dir}")

        width, height = 64, 64
        for i in range(5):
            img_name = f"frame_{i:03d}"
            img = bpy.data.images.new(img_name, width=width, height=height, alpha=True)

            r_val = (i / 5.0)
            pixels = [r_val, 0.0, 1.0 - r_val, 1.0] * (width * height)
            img.pixels = pixels

            file_path = os.path.join(input_dir, f"{img_name}.png")
            img.filepath_raw = file_path
            img.file_format = 'PNG'
            img.save()
            bpy.data.images.remove(img)

        # 2. Define Output Path
        output_file = os.path.join(temp_dir, "output.mp4")

        # 3. Locate Worker Script
        worker_script = os.path.join(PROJECT_ROOT, "savepoints", "workers", "timelapse_worker.py")
        self.assertTrue(os.path.exists(worker_script), f"Worker script not found: {worker_script}")

        # 4. Run Worker
        blender_bin = bpy.app.binary_path
        cmd = [
            blender_bin,
            "-b",
            "--factory-startup",
            "-P", worker_script,
            "--",
            input_dir,
            output_file,
            "24"
        ]

        print(f"Running worker command: {' '.join(cmd)}")

        startupinfo = None
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        try:
            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True,
                startupinfo=startupinfo
            )
        except subprocess.CalledProcessError as e:
            print("--- Worker FAILED ---")
            print(f"Return Code: {e.returncode}")
            print("STDOUT:", e.stdout)
            print("STDERR:", e.stderr)
            self.fail("Worker process failed. See output above.")

        # 5. Assert Output Exists
        if os.path.exists(output_file):
            print(f"Success: MP4 created at {output_file}")
            file_size = os.path.getsize(output_file)
            print(f"File Size: {file_size} bytes")

            self.assertGreater(file_size, 1024, "MP4 file is suspiciously small or empty")
        else:
            self.fail(f"MP4 output file was not created at {output_file}")

        # Cleanup
        try:
            shutil.rmtree(temp_dir)
        except:
            pass
        print("=== Test Finished Successfully ===\n")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
