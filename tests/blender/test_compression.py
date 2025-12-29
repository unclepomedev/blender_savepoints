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

from savepoints import operators
from savepoints_test_case import SavePointsTestCase


class TestCompression(SavePointsTestCase):
    """
    Verify that the compression setting works as expected.
    """

    def is_compressed(self, file_path):
        """Check if file has Gzip or Zstd magic number."""
        with open(file_path, 'rb') as f:
            header = f.read(4)
            # Gzip: 1f 8b
            if header.startswith(b'\x1f\x8b'):
                return True
            # Zstd: 28 b5 2f fd
            if header == b'\x28\xb5\x2f\xfd':
                return True
        return False

    def test_compression_setting(self):
        """
        Scenario:
        1. Enable compression -> Snapshot -> Verify Compression
        2. Disable compression -> Snapshot -> Verify Standard
        """
        print("Starting Compression Test...")

        context = bpy.context
        scene = context.scene

        # Ensure settings exist
        if not hasattr(scene, "savepoints_settings"):
            self.fail("savepoints_settings not found on scene")

        settings = scene.savepoints_settings

        # --- Step 1: Compressed Snapshot ---
        with self.subTest(step="1. Compressed Snapshot"):
            try:
                settings.use_compression = True
            except AttributeError:
                self.fail("Property 'use_compression' not defined in SavePointsSettings")

            version_id_comp = "v_compressed"
            operators.create_snapshot(context, version_id_comp, "Compressed", skip_thumbnail=True)

            history_dir = self.test_dir / ".test_project_history"
            snap_path = history_dir / version_id_comp / "snapshot.blend_snapshot"

            self.assertTrue(snap_path.exists(), "Snapshot file missing")

            self.assertTrue(self.is_compressed(snap_path), "File should be compressed (Gzip/Zstd) but is not")
            print("Verified: File is compressed.")

        # --- Step 2: Uncompressed Snapshot ---
        with self.subTest(step="2. Uncompressed Snapshot"):
            settings.use_compression = False

            version_id_raw = "v_raw"
            operators.create_snapshot(context, version_id_raw, "Raw", skip_thumbnail=True)

            snap_path_raw = history_dir / version_id_raw / "snapshot.blend_snapshot"

            self.assertTrue(snap_path_raw.exists(), "Snapshot file missing")
            self.assertFalse(self.is_compressed(snap_path_raw), "File should NOT be compressed")
            print("Verified: File is NOT compressed.")


if __name__ == '__main__':
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
