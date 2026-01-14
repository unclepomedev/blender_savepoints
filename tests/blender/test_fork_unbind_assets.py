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

from savepoints_test_case import SavePointsTestCase


class TestForkUnbindAssets(SavePointsTestCase):

    def setUp(self):
        super().setUp()
        self.lib_path = self.test_dir / "lib.blend"

        # Setup library content
        bpy.ops.wm.read_factory_settings()
        bpy.ops.mesh.primitive_monkey_add()
        monkey = bpy.context.object
        monkey.name = "LibMonkey"

        monkey.asset_mark()

        # Add a material
        mat = bpy.data.materials.new(name="LibMaterial")
        monkey.data.materials.append(mat)
        mat.asset_mark()

        bpy.ops.wm.save_as_mainfile(filepath=str(self.lib_path))

        bpy.ops.wm.read_factory_settings()
        bpy.ops.wm.save_as_mainfile(filepath=str(self.blend_path))

    def test_fork_with_unbind_assets(self):
        """
        Scenario: Fork with unbind_linked_assets=True.
        Verify objects/materials become local AND asset marks are cleared.
        """
        with bpy.data.libraries.load(str(self.lib_path), link=True) as (data_from, data_to):
            data_to.objects = ["LibMonkey"]

        monkey_obj = data_to.objects[0]
        bpy.context.scene.collection.objects.link(monkey_obj)

        self.assertTrue(monkey_obj.library, "Setup Error: Object should be linked initially")

        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Linked Version")
        bpy.context.scene.savepoints_settings.active_version_index = 0
        bpy.ops.savepoints.checkout()

        bpy.ops.savepoints.fork_version('EXEC_DEFAULT', unbind_linked_assets=True)

        forked_monkey = bpy.data.objects.get("LibMonkey")
        self.assertIsNotNone(forked_monkey)
        self.assertIsNone(forked_monkey.library, "Object should be local after fork")

        forked_mat = forked_monkey.active_material
        self.assertIsNotNone(forked_mat)
        self.assertIsNone(forked_mat.library, "Material should be local after fork")

        self.assertIsNone(forked_monkey.asset_data, "Monkey asset mark should be cleared")
        self.assertIsNone(forked_mat.asset_data, "Material asset mark should be cleared")

    def test_fork_without_unbind_assets(self):
        """
        Scenario: Fork with unbind_linked_assets=False.
        Verify objects remain linked.
        """
        with bpy.data.libraries.load(str(self.lib_path), link=True) as (data_from, data_to):
            data_to.objects = ["LibMonkey"]

        monkey_obj = data_to.objects[0]
        bpy.context.scene.collection.objects.link(monkey_obj)

        bpy.ops.savepoints.commit('EXEC_DEFAULT', note="Linked Version")
        bpy.context.scene.savepoints_settings.active_version_index = 0
        bpy.ops.savepoints.checkout()

        bpy.ops.savepoints.fork_version('EXEC_DEFAULT', unbind_linked_assets=False)

        forked_monkey = bpy.data.objects.get("LibMonkey")
        self.assertIsNotNone(forked_monkey)
        self.assertIsNotNone(forked_monkey.library, "Object should still be linked")

        forked_mat = forked_monkey.active_material
        self.assertIsNotNone(forked_mat.library, "Material should still be linked")


if __name__ == "__main__":
    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
