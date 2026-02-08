import sys
import time
import unittest
from pathlib import Path

# --- Standard boilerplate to add project root to path ---
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.post_save import PostSaveManager, format_command
from tests.blender.savepoints_test_case import SavePointsTestCase


class TestPostSave(SavePointsTestCase):
    def setUp(self):
        super().setUp()
        self.manager = PostSaveManager()
        if self.manager.process:
            try:
                self.manager.process.kill()
            except:
                pass
        self.manager.process = None
        self.manager._timer = None

    def test_placeholder_formatting(self):
        cases = [
            {
                "msg": "Normal path (no spaces)",
                "cmd": "echo {filepath}",
                "ctx": {"filepath": "/tmp/test.blend"},
                "expect_win": "/tmp/test.blend",
                "expect_posix": "/tmp/test.blend",
            },
            {
                "msg": "Path with spaces (Needs quoting)",
                "cmd": "cp {src} {dst}",
                "ctx": {
                    "src": "C:/My Documents/file.blend",
                    "dst": "D:/Backup/file.blend",
                },
                "expect_win": '"C:/My Documents/file.blend"',
                "expect_posix": "'C:/My Documents/file.blend'",
            },
            {
                "msg": "Missing Placeholder (Should return None)",
                "cmd": "echo {non_existent_key}",
                "ctx": {"existing": "value"},
                "expect_result": None,
            },
            {
                "msg": "Dangerous characters (Injection prevention)",
                "cmd": "echo {note}",
                "ctx": {"note": "Test & rm -rf /"},
                "should_be_quoted": True,
            },
        ]

        for case in cases:
            with self.subTest(msg=case["msg"]):
                result = format_command(case["cmd"], case["ctx"])

                if "expect_result" in case and case["expect_result"] is None:
                    self.assertIsNone(result, f"Failed: {case['msg']}")
                    continue

                self.assertIsNotNone(result, f"Unexpected None: {case['msg']}")

                if sys.platform == "win32":
                    if "expect_win" in case:
                        self.assertIn(case["expect_win"], result)
                else:
                    if "expect_posix" in case:
                        self.assertIn(case["expect_posix"], result)

                if case.get("should_be_quoted"):
                    if sys.platform == "win32":
                        self.assertTrue(
                            '"' in result, "Should be double-quoted on Windows"
                        )
                    else:
                        self.assertTrue(
                            "'" in result, "Should be single-quoted on POSIX"
                        )

    def test_execution(self):
        test_file = self.test_dir / "test_marker.txt"

        python_exe = sys.executable
        cmd = f"\"{python_exe}\" -c \"open(r'{test_file}', 'w').close()\""

        self.manager.start_command(cmd, {})

        # Wait for completion
        timeout = 5
        start = time.time()

        process_finished = False
        while time.time() - start < timeout:
            if self.manager.process and self.manager.process.poll() is not None:
                process_finished = True
                break
            time.sleep(0.1)

        self.assertTrue(process_finished, "Process timed out")

        self.manager._monitor_process()
        self.assertTrue(test_file.exists(), "Marker file was not created")
        self.assertIsNone(self.manager.process)


if __name__ == "__main__":
    result = unittest.main(argv=["first-arg-is-ignored"], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
