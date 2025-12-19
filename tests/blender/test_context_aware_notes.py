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

from savepoints.services.versioning import generate_default_note
from savepoints_test_case import SavePointsTestCase


class TestContextAwareNotes(SavePointsTestCase):

    def _create_dummy_object(self, obj_type, name):
        """Helper to create and activate an object for testing."""
        # Ensure we are in object mode before adding new objects
        if bpy.context.object and bpy.context.object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.select_all(action='DESELECT')

        if obj_type == 'MESH':
            bpy.ops.mesh.primitive_cube_add()
        elif obj_type == 'ARMATURE':
            bpy.ops.object.armature_add()
        else:
            self.fail(f"Unknown object type: {obj_type}")

        obj = bpy.context.active_object
        obj.name = name
        return obj

    def test_mesh_modes(self):
        """Test default notes for various Mesh modes using subTest."""
        print("Testing Mesh Modes...")

        # Define test cases: (Mode, Object Name, Expected Note)
        # Note: TEXTURE_PAINT works on Meshes
        cases = [
            ('OBJECT', "MyCube", "Object: MyCube"),
            ('EDIT', "EditMesh", "Edit Mesh: EditMesh"),
            ('SCULPT', "SculptMesh", "Sculpt: SculptMesh"),
            ('VERTEX_PAINT', "VPMesh", "Vertex Paint: VPMesh"),
            ('WEIGHT_PAINT', "WPMesh", "Weight Paint: WPMesh"),
            ('TEXTURE_PAINT', "TPMesh", "Texture Paint: TPMesh"),
        ]

        for mode, name, expected in cases:
            with self.subTest(mode=mode):
                self._create_dummy_object('MESH', name)

                # Switch mode
                try:
                    bpy.ops.object.mode_set(mode=mode)
                except RuntimeError as e:
                    # If headless execution fails for specific paint modes, fail explicitly
                    # or use self.skipTest("...") if it's a known limitation.
                    self.fail(f"Failed to enter {mode}: {e}")

                # Verify
                note = generate_default_note(bpy.context)
                self.assertEqual(note, expected)

    def test_armature_modes(self):
        """Test default notes for Armature modes."""
        print("Testing Armature Modes...")

        cases = [
            ('EDIT', "EditArmature", "Edit Armature: EditArmature"),
            ('POSE', "PoseArmature", "Pose: PoseArmature"),
        ]

        for mode, name, expected in cases:
            with self.subTest(mode=mode):
                self._create_dummy_object('ARMATURE', name)

                bpy.ops.object.mode_set(mode=mode)

                note = generate_default_note(bpy.context)
                self.assertEqual(note, expected)

    def test_particle_edit_mode(self):
        """Test Particle Edit mode (Requires specific setup)."""
        print("Testing Particle Edit Mode...")

        obj = self._create_dummy_object('MESH', "PartMesh")

        # Setup: Need a particle system to enter Particle Edit
        obj.modifiers.new(name="Particles", type='PARTICLE_SYSTEM')

        try:
            bpy.ops.object.mode_set(mode='PARTICLE_EDIT')
        except RuntimeError as e:
            self.fail(f"Failed to enter PARTICLE_EDIT: {e}")

        note = generate_default_note(bpy.context)
        self.assertEqual(note, "Particle Edit: PartMesh")

    def test_no_active_object(self):
        """Test behavior when no object is active."""
        print("Testing No Active Object...")

        if bpy.context.object and bpy.context.object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = None

        note = generate_default_note(bpy.context)
        self.assertEqual(note, "No Active Object")


if __name__ == '__main__':
    import sys

    result = unittest.main(argv=['first-arg-is-ignored'], exit=False).result
    if not result.wasSuccessful():
        print("\n❌ Tests Failed!")
        sys.exit(1)
