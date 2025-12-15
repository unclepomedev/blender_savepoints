import sys
import unittest
from pathlib import Path

import bpy

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import savepoints.operators


class TestContextAwareNotes(unittest.TestCase):
    def setUp(self):
        # Reset scene
        bpy.ops.wm.read_homefile(use_empty=True)

    def test_get_default_note_object_mode(self):
        # Create Cube
        bpy.ops.mesh.primitive_cube_add(size=2)
        cube = bpy.context.active_object
        cube.name = "MyCube"

        # Ensure Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # Call method directly on class, passing None as self
        note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)

        self.assertEqual(note, "Object: MyCube")

    def test_get_default_note_edit_mode(self):
        # Create Cube
        bpy.ops.mesh.primitive_cube_add()
        cube = bpy.context.active_object
        cube.name = "EditCube"

        # Switch to Edit Mode
        bpy.ops.object.mode_set(mode='EDIT')

        note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)

        self.assertEqual(note, "Edit: EditCube")

    def test_get_default_note_sculpt_mode(self):
        # Create Cube
        bpy.ops.mesh.primitive_cube_add()
        cube = bpy.context.active_object
        cube.name = "SculptCube"

        # Switch to Sculpt Mode
        bpy.ops.object.mode_set(mode='SCULPT')

        note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)

        self.assertEqual(note, "Sculpt: SculptCube")

    def test_get_default_note_no_active_object(self):
        # Deselect/Deactivate all
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = None

        note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)

        self.assertEqual(note, "")


if __name__ == '__main__':
    # Running unittest inside Blender
    # Pass argv=[''] to prevent unittest from parsing Blender's command line args
    unittest.main(argv=[''], exit=False)
