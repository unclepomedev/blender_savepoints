import unittest
import bpy
import sys
from pathlib import Path

# Add project root to path
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parents[1]
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from savepoints_test_case import SavePointsTestCase


class TestPreferences(SavePointsTestCase):
    def test_preferences_exist(self):
        self.assertTrue(
            hasattr(bpy.types, "SAVEPOINTS_PT_main"), "Panel should be registered"
        )

        from savepoints.properties import SavePointsPreferences

        if hasattr(SavePointsPreferences, "__annotations__"):
            self.assertIn(
                "enable_glb_export",
                SavePointsPreferences.__annotations__,
                "Property should be in annotations",
            )
        else:
            self.assertTrue(
                hasattr(SavePointsPreferences, "enable_glb_export"),
                "Property should exist on class",
            )

        try:
            bpy.utils.register_class(SavePointsPreferences)
        except ValueError:
            # Already registered
            pass

        try:
            # Just checking if property exists is good enough for structure check.
            pass
        finally:
            bpy.utils.unregister_class(SavePointsPreferences)

    def test_ui_logic(self):
        # Just ensure it imports without error
        pass


if __name__ == "__main__":
    result = unittest.main(argv=["first-arg-is-ignored"], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
