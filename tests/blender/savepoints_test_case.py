import unittest
import shutil
import sys
from pathlib import Path
import bpy

# Setup path to find the module
# Assumes this file is in tests/blender/
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
        # Create a unique test directory based on the test class
        # ensuring isolation between test classes if run in parallel (though Blender runs them sequentially per file usually)
        self.test_dir = ROOT / f"test_env_{self.__class__.__name__}"
        
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)
        self.test_dir.mkdir()
        
        # Set up a standard blend file path
        self.blend_path = self.test_dir / "test_project.blend"
        
        # Save the current blend file to this location to initialize the context
        bpy.ops.wm.save_as_mainfile(filepath=str(self.blend_path))
        
        # Register the addon
        # We try to register, but if it's already registered (e.g. from previous test file in same session - unlikely with -P but possible), catch it.
        try:
            savepoints.register()
        except ValueError:
            # "Loaded multiple times" or similar if already registered
            pass
        except RuntimeError:
            # Addon already registered
            pass

    def tearDown(self):
        # Unregister the addon
        try:
            savepoints.unregister()
        except Exception:
            pass
            
        # Cleanup test directory
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir, ignore_errors=True)
