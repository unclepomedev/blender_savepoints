# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ParticleInstanceModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .Object import Object
from .ParticleSystem import ParticleSystem

class ParticleInstanceModifier(Modifier):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Modifier name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Literal['GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY', 'DATA_TRANSFER', 'MESH_CACHE', 'MESH_SEQUENCE_CACHE', 'NORMAL_EDIT', 'WEIGHTED_NORMAL', 'UV_PROJECT', 'UV_WARP', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_PROXIMITY', 'GREASE_PENCIL_COLOR', 'GREASE_PENCIL_TINT', 'GREASE_PENCIL_OPACITY', 'GREASE_PENCIL_VERTEX_WEIGHT_ANGLE', 'GREASE_PENCIL_TIME', 'GREASE_PENCIL_TEXTURE', 'ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 'EDGE_SPLIT', 'NODES', 'MASK', 'MIRROR', 'MESH_TO_VOLUME', 'MULTIRES', 'REMESH', 'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'VOLUME_TO_MESH', 'WELD', 'WIREFRAME', 'GREASE_PENCIL_ARRAY', 'GREASE_PENCIL_BUILD', 'GREASE_PENCIL_LENGTH', 'LINEART', 'GREASE_PENCIL_MIRROR', 'GREASE_PENCIL_MULTIPLY', 'GREASE_PENCIL_SIMPLIFY', 'GREASE_PENCIL_SUBDIV', 'GREASE_PENCIL_ENVELOPE', 'GREASE_PENCIL_OUTLINE', 'ARMATURE', 'CAST', 'CURVE', 'DISPLACE', 'HOOK', 'LAPLACIANDEFORM', 'LATTICE', 'MESH_DEFORM', 'SHRINKWRAP', 'SIMPLE_DEFORM', 'SMOOTH', 'CORRECTIVE_SMOOTH', 'LAPLACIANSMOOTH', 'SURFACE_DEFORM', 'WARP', 'WAVE', 'VOLUME_DISPLACE', 'GREASE_PENCIL_HOOK', 'GREASE_PENCIL_NOISE', 'GREASE_PENCIL_OFFSET', 'GREASE_PENCIL_SMOOTH', 'GREASE_PENCIL_THICKNESS', 'GREASE_PENCIL_LATTICE', 'GREASE_PENCIL_DASH', 'GREASE_PENCIL_ARMATURE', 'GREASE_PENCIL_SHRINKWRAP', 'CLOTH', 'COLLISION', 'DYNAMIC_PAINT', 'EXPLODE', 'FLUID', 'OCEAN', 'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM', 'SOFT_BODY', 'SURFACE']:

        ...
    @property
    def show_viewport(self) -> bool:
        """Display modifier in viewport"""
        ...
    @show_viewport.setter
    def show_viewport(self, value: bool):
        ...
    @property
    def show_render(self) -> bool:
        """Use modifier during render"""
        ...
    @show_render.setter
    def show_render(self, value: bool):
        ...
    @property
    def show_in_editmode(self) -> bool:
        """Display modifier in Edit mode"""
        ...
    @show_in_editmode.setter
    def show_in_editmode(self, value: bool):
        ...
    @property
    def show_on_cage(self) -> bool:
        """Adjust edit cage to modifier result"""
        ...
    @show_on_cage.setter
    def show_on_cage(self, value: bool):
        ...
    @property
    def show_expanded(self) -> bool:
        """Set modifier expanded in the user interface"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool):
        ...
    @property
    def is_active(self) -> Annotated[bool, "is_animatable=False"]:
        """The active modifier in the list"""
        ...
    @is_active.setter
    def is_active(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pin_to_last(self) -> Annotated[bool, "is_animatable=False"]:
        """Keep the modifier at the end of the list"""
        ...
    @use_pin_to_last.setter
    def use_pin_to_last(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def is_override_data(self) -> bool:
        """In a local override object, whether this modifier comes from the linked reference object, or is local to the override"""
        ...
    @property
    def use_apply_on_spline(self) -> bool:
        """Apply this and all preceding deformation modifiers on splines' points rather than on filled curve/surface"""
        ...
    @use_apply_on_spline.setter
    def use_apply_on_spline(self, value: bool):
        ...
    @property
    def execution_time(self) -> Annotated[float, "subtype='TIME_ABSOLUTE'", "unit='TIME_ABSOLUTE'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Time in seconds that the modifier took to evaluate. This is only set on evaluated objects. If multiple modifiers run in parallel, execution time is not a reliable metric."""
        ...
    @property
    def persistent_uid(self) -> Annotated[int, "step=1"]:
        """Uniquely identifies the modifier within the modifier stack that it is part of"""
        ...
    @property
    def object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object that has the particle system"""
        ...
    @object.setter
    def object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def particle_system_index(self) -> Annotated[int, "step=1"]:

        ...
    @particle_system_index.setter
    def particle_system_index(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def particle_system(self) -> Annotated[Optional['ParticleSystem'], "is_animatable=False"]:

        ...
    @particle_system.setter
    def particle_system(self, value: Annotated[Optional['ParticleSystem'], "is_animatable=False"]):
        ...
    @property
    def axis(self) -> Literal['X', 'Y', 'Z']:
        """Pole axis for rotation"""
        ...
    @axis.setter
    def axis(self, value: Literal['X', 'Y', 'Z']):
        ...
    @property
    def space(self) -> Literal['LOCAL', 'WORLD']:
        """Space to use for copying mesh data"""
        ...
    @space.setter
    def space(self, value: Literal['LOCAL', 'WORLD']):
        ...
    @property
    def use_normal(self) -> bool:
        """Create instances from normal particles"""
        ...
    @use_normal.setter
    def use_normal(self, value: bool):
        ...
    @property
    def use_children(self) -> bool:
        """Create instances from child particles"""
        ...
    @use_children.setter
    def use_children(self, value: bool):
        ...
    @property
    def use_path(self) -> bool:
        """Create instances along particle paths"""
        ...
    @use_path.setter
    def use_path(self, value: bool):
        ...
    @property
    def show_unborn(self) -> bool:
        """Show instances when particles are unborn"""
        ...
    @show_unborn.setter
    def show_unborn(self, value: bool):
        ...
    @property
    def show_alive(self) -> bool:
        """Show instances when particles are alive"""
        ...
    @show_alive.setter
    def show_alive(self, value: bool):
        ...
    @property
    def show_dead(self) -> bool:
        """Show instances when particles are dead"""
        ...
    @show_dead.setter
    def show_dead(self, value: bool):
        ...
    @property
    def use_preserve_shape(self) -> bool:
        """Don't stretch the object"""
        ...
    @use_preserve_shape.setter
    def use_preserve_shape(self, value: bool):
        ...
    @property
    def use_size(self) -> bool:
        """Use particle size to scale the instances"""
        ...
    @use_size.setter
    def use_size(self, value: bool):
        ...
    @property
    def position(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Position along path"""
        ...
    @position.setter
    def position(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def random_position(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Randomize position along path"""
        ...
    @random_position.setter
    def random_position(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def rotation(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Rotation around path"""
        ...
    @rotation.setter
    def rotation(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def random_rotation(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Randomize rotation around path"""
        ...
    @random_rotation.setter
    def random_rotation(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def particle_amount(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of particles to use for instancing"""
        ...
    @particle_amount.setter
    def particle_amount(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def particle_offset(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Relative offset of particles to use for instancing, to avoid overlap of multiple instances"""
        ...
    @particle_offset.setter
    def particle_offset(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def index_layer_name(self) -> Annotated[str, "is_animatable=False"]:
        """Custom data layer name for the index"""
        ...
    @index_layer_name.setter
    def index_layer_name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def value_layer_name(self) -> Annotated[str, "is_animatable=False"]:
        """Custom data layer name for the randomized value"""
        ...
    @value_layer_name.setter
    def value_layer_name(self, value: Annotated[str, "is_animatable=False"]):
        ...