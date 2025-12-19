import sys
import unittest
from pathlib import Path
import bpy

# --- Standard boilerplate to add project root to path ---
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints.services.storage import is_safe_filename
from savepoints.services.versioning import delete_version_by_id
from savepoints.services.snapshot import find_snapshot_path, create_snapshot
from savepoints_test_case import SavePointsTestCase


class TestPathTraversal(SavePointsTestCase):
    """
    Test cases regarding security (path traversal).
    Verifies that inputs containing invalid paths (e.g., '../') are blocked or handled appropriately.
    """

    def test_is_safe_filename_logic(self):
        """Verify that is_safe_filename correctly identifies safe and unsafe strings."""

        # Define test cases as tuples: (input_filename, expected_result, failure_message)
        test_cases = [
            # Safe cases
            ("v001", True, "Standard version ID"),
            ("autosave", True, "Standard autosave name"),
            ("my-version_1.0", True, "Symbols allowed in filenames"),

            # Unsafe cases
            ("..", False, "Parent directory traversal"),
            ("../v001", False, "Traversal with filename"),
            ("v001/v002", False, "Slash separator"),
            (r"v001\v002", False, "Backslash separator"),
            ("/etc/passwd", False, "Absolute path"),
            ("", False, "Empty string"),
        ]

        for filename, expected, msg in test_cases:
            with self.subTest(filename=filename):
                self.assertEqual(is_safe_filename(filename), expected, msg)

    def test_find_snapshot_path_traversal(self):
        """Verify that find_snapshot_path returns None when receiving an unsafe ID."""

        # Prepare attack target: place a file outside history to simulate traversal
        traversal_dir = self.test_dir / "traversal_target"
        traversal_dir.mkdir(exist_ok=True)
        (traversal_dir / "snapshot.blend_snapshot").touch()

        # Attack patterns
        unsafe_ids = [
            "../",
            "../traversal_target",
            "/absolute/path"
        ]

        for unsafe_id in unsafe_ids:
            with self.subTest(unsafe_id=unsafe_id):
                # Expect None (or check for specific Exception if your implementation raises one)
                path = find_snapshot_path(unsafe_id)
                self.assertIsNone(
                    path,
                    f"Unsafe ID '{unsafe_id}' should return None, but got: {path}"
                )

    def test_delete_version_traversal(self):
        """Verify that delete_version_by_id does not delete files outside the history directory."""

        # Create a "victim" directory/file that should NOT be deleted
        victim_dir = self.test_dir / "victim_dir"
        victim_dir.mkdir(exist_ok=True)
        victim_file = victim_dir / "important.txt"
        victim_file.touch()

        unsafe_id = "../victim_dir"

        # Execute deletion
        # Depending on implementation, this might raise an error or simply do nothing.
        # We allow execution to proceed to verify the side effects (file existence).
        try:
            delete_version_by_id(unsafe_id)
        except Exception:
            # We ignore exceptions here as we are interested in whether the file persists
            pass

        # Verify: The victim file must still exist
        self.assertTrue(victim_dir.exists(), "Target directory was deleted via traversal!")
        self.assertTrue(victim_file.exists(), "Target file was deleted via traversal!")

    def test_create_snapshot_traversal(self):
        """Verify that create_snapshot does not create directories outside the history directory."""

        unsafe_id = "../outside_version"
        target_outside_dir = self.test_dir / "outside_version"

        # Execute creation
        # NOTE: If the implementation guards with is_safe_filename, this might raise a ValueError
        # or simply do nothing. We catch exceptions to check the file system state.
        try:
            create_snapshot(bpy.context, unsafe_id, "Bad Note", skip_thumbnail=True)
        except Exception:
            # Allow exceptions caused by security checks
            pass

        # Verify: The directory outside history must NOT be created
        self.assertFalse(
            target_outside_dir.exists(),
            "create_snapshot created a directory outside history via traversal!"
        )


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
