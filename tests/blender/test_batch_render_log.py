import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints_test_case import SavePointsTestCase
from savepoints.services.batch_render import create_error_log_text_block


class TestBatchRenderLog(SavePointsTestCase):

    def test_log_import_logic(self):
        """
        Test if a text file on disk is correctly imported into Blender's Text Editor.
        """
        print("\nTesting Log Import Logic...")

        # 1. Prepare a dummy log file
        temp_dir = tempfile.mkdtemp()
        log_path = os.path.join(temp_dir, "test_render_log.txt")
        dummy_content = "Error: Out of Memory\nDetails: Texture too large."
        version_id = "v999_Test"

        try:
            with open(log_path, 'w', encoding='utf-8') as f:
                f.write(dummy_content)

            # 2. Execute the function
            text_block = create_error_log_text_block(version_id, log_path)

            # 3. Verify
            self.assertIsNotNone(text_block)
            self.assertEqual(text_block.name, f"Log_{version_id}")

            # Check content (Blender TextBlock lines are stored as a collection)
            # Combine lines back to string for checking
            full_text = "\n".join([line.body for line in text_block.lines])

            self.assertIn(dummy_content, full_text)
            self.assertIn("# SavePoints Batch Render Log", full_text)  # Header check

            print(f"Log imported successfully to: {text_block.name}")

        finally:
            shutil.rmtree(temp_dir)

    def test_subprocess_failure_capture(self):
        """
        Test if we can catch a subprocess failure and capture its stderr to a file.
        (Simulates the Worker failing)
        """
        print("\nTesting Subprocess Failure Capture...")

        temp_dir = tempfile.mkdtemp()
        log_path = os.path.join(temp_dir, "failure_log.txt")

        # A script that definitely fails and prints to stderr
        failing_script = "import sys; sys.stderr.write('CRITICAL WORKER FAILURE'); sys.exit(1)"

        try:
            # Prepare log handle
            with open(log_path, 'w', encoding='utf-8') as log_handle:

                # Execute Python command that fails
                cmd = [sys.executable, "-c", failing_script]

                process = subprocess.Popen(
                    cmd,
                    stdout=log_handle,
                    stderr=log_handle
                )
                exit_code = process.wait()

            # 1. Verify Exit Code is Error (not 0)
            self.assertNotEqual(exit_code, 0, "Process should have failed")

            # 2. Verify Log Content
            with open(log_path, 'r', encoding='utf-8') as f:
                content = f.read()

            print(f"Captured Log Content: {content.strip()}")
            self.assertIn("CRITICAL WORKER FAILURE", content)

        finally:
            shutil.rmtree(temp_dir)


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
