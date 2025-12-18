import shutil
import sys
import unittest
from pathlib import Path

import bpy

# Setup path to find the module
# Assumes this file is in tests/blender/ (Adjust parent count as needed)
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

import savepoints


class SavePointsTestCase(unittest.TestCase):
    """
    Base class for Blender SavePoints tests.
    Handles setup and teardown of a temporary test environment.
    """

    def setUp(self):
        # 1. Clean the current Blender session properly
        # Make sure we start with a clean slate (no objects, no custom props)
        bpy.ops.wm.read_homefile(use_empty=True)

        # 2. Create a unique test directory for EACH TEST METHOD
        # Using _testMethodName allows debugging individual test artifacts if they fail
        self.test_dir = ROOT / "test_temp" / f"{self.__class__.__name__}_{self._testMethodName}"

        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
        self.test_dir.mkdir(parents=True)

        # 3. Set up a standard blend file path
        self.blend_path = self.test_dir / "test_project.blend"

        # 4. Save the clean blend file to initialize the context
        bpy.ops.wm.save_as_mainfile(filepath=str(self.blend_path))

        # 5. Register the addon
        try:
            savepoints.register()
        except (ValueError, RuntimeError):
            # Already registered
            pass

    def tearDown(self):
        # 1. Unregister the addon
        try:
            savepoints.unregister()
        except Exception:
            pass

        # 2. CRITICAL: Release file lock for Windows
        # Switch to a new empty file so Blender releases 'test_project.blend'
        bpy.ops.wm.read_homefile(use_empty=True)

        # 3. Cleanup test directory
        if self.test_dir.exists():
            try:
                shutil.rmtree(self.test_dir)
            except PermissionError:
                # Retry or ignore if OS is slow to release lock
                print(f"Warning: Could not delete {self.test_dir}")
