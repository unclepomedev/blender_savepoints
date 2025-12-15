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
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.name = "MyCube"
        bpy.ops.object.mode_set(mode='OBJECT')

        note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)
        self.assertEqual(note, "Object: MyCube")

    def test_get_default_note_edit_mode_mesh(self):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.name = "EditMesh"
        bpy.ops.object.mode_set(mode='EDIT')

        note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)
        # Expected: "Edit {obj.type.title()}: {obj.name}"
        self.assertEqual(note, "Edit Mesh: EditMesh")

    def test_get_default_note_edit_mode_armature(self):
        bpy.ops.object.armature_add()
        obj = bpy.context.active_object
        obj.name = "EditArmature"
        bpy.ops.object.mode_set(mode='EDIT')

        note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)
        self.assertEqual(note, "Edit Armature: EditArmature")

    def test_get_default_note_pose_mode(self):
        bpy.ops.object.armature_add()
        obj = bpy.context.active_object
        obj.name = "PoseArmature"
        bpy.ops.object.mode_set(mode='POSE')

        note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)
        self.assertEqual(note, "Pose: PoseArmature")

    def test_get_default_note_sculpt_mode(self):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.name = "SculptMesh"
        bpy.ops.object.mode_set(mode='SCULPT')

        note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)
        self.assertEqual(note, "Sculpt: SculptMesh")

    def test_get_default_note_vertex_paint(self):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.name = "VPMesh"
        bpy.ops.object.mode_set(mode='VERTEX_PAINT')

        note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)
        self.assertEqual(note, "Vertex Paint: VPMesh")

    def test_get_default_note_weight_paint(self):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.name = "WPMesh"
        bpy.ops.object.mode_set(mode='WEIGHT_PAINT')

        note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)
        self.assertEqual(note, "Weight Paint: WPMesh")

    def test_get_default_note_texture_paint(self):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.name = "TPMesh"
        # Texture paint works on meshes
        try:
            bpy.ops.object.mode_set(mode='TEXTURE_PAINT')
            if bpy.context.active_object.mode == 'TEXTURE_PAINT':
                note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)
                self.assertEqual(note, "Texture Paint: TPMesh")
        except RuntimeError:
            pass

    def test_get_default_note_particle_edit(self):
        bpy.ops.mesh.primitive_cube_add()
        obj = bpy.context.active_object
        obj.name = "PartMesh"
        # Need a particle system to enter Particle Edit
        obj.modifiers.new(name="Particles", type='PARTICLE_SYSTEM')

        try:
            bpy.ops.object.mode_set(mode='PARTICLE_EDIT')
            if bpy.context.active_object.mode == 'PARTICLE_EDIT':
                note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)
                self.assertEqual(note, "Particle Edit: PartMesh")
        except RuntimeError:
            pass

    def test_get_default_note_no_active_object(self):
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = None

        note = savepoints.operators.SAVEPOINTS_OT_commit._get_default_note(None, bpy.context)
        self.assertEqual(note, "")


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
