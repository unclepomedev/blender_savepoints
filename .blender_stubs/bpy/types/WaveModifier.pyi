# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.WaveModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .Object import Object
from .Texture import Texture

class WaveModifier(Modifier):

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
    def use_x(self) -> bool:
        """X axis motion"""
        ...
    @use_x.setter
    def use_x(self, value: bool):
        ...
    @property
    def use_y(self) -> bool:
        """Y axis motion"""
        ...
    @use_y.setter
    def use_y(self, value: bool):
        ...
    @property
    def use_cyclic(self) -> bool:
        """Cyclic wave effect"""
        ...
    @use_cyclic.setter
    def use_cyclic(self, value: bool):
        ...
    @property
    def use_normal(self) -> bool:
        """Displace along normals"""
        ...
    @use_normal.setter
    def use_normal(self, value: bool):
        ...
    @property
    def use_normal_x(self) -> bool:
        """Enable displacement along the X normal"""
        ...
    @use_normal_x.setter
    def use_normal_x(self, value: bool):
        ...
    @property
    def use_normal_y(self) -> bool:
        """Enable displacement along the Y normal"""
        ...
    @use_normal_y.setter
    def use_normal_y(self, value: bool):
        ...
    @property
    def use_normal_z(self) -> bool:
        """Enable displacement along the Z normal"""
        ...
    @use_normal_z.setter
    def use_normal_z(self, value: bool):
        ...
    @property
    def time_offset(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Either the starting frame (for positive speed) or ending frame (for negative speed)"""
        ...
    @time_offset.setter
    def time_offset(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]):
        ...
    @property
    def lifetime(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Lifetime of the wave in frames, zero means infinite"""
        ...
    @lifetime.setter
    def lifetime(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]):
        ...
    @property
    def damping_time(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Number of frames in which the wave damps out after it dies"""
        ...
    @damping_time.setter
    def damping_time(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]):
        ...
    @property
    def falloff_radius(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=100.0", "precision=2"]:
        """Distance after which it fades out"""
        ...
    @falloff_radius.setter
    def falloff_radius(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=100.0", "precision=2"]):
        ...
    @property
    def start_position_x(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=100.0", "precision=2"]:
        """X coordinate of the start position"""
        ...
    @start_position_x.setter
    def start_position_x(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=100.0", "precision=2"]):
        ...
    @property
    def start_position_y(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=100.0", "precision=2"]:
        """Y coordinate of the start position"""
        ...
    @start_position_y.setter
    def start_position_y(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=100.0", "precision=2"]):
        ...
    @property
    def start_position_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object which defines the wave center"""
        ...
    @start_position_object.setter
    def start_position_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group name for modulating the wave"""
        ...
    @vertex_group.setter
    def vertex_group(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def invert_vertex_group(self) -> bool:
        """Invert vertex group influence"""
        ...
    @invert_vertex_group.setter
    def invert_vertex_group(self, value: bool):
        ...
    @property
    def speed(self) -> Annotated[float, "step=10.0", "precision=2"]:
        """Speed of the wave, towards the starting point when negative"""
        ...
    @speed.setter
    def speed(self, value: Annotated[float, "step=10.0", "precision=2"]):
        ...
    @property
    def height(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]:
        """Height of the wave"""
        ...
    @height.setter
    def height(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]):
        ...
    @property
    def width(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]:
        """Distance between the waves"""
        ...
    @width.setter
    def width(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]):
        ...
    @property
    def narrowness(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]:
        """Distance between the top and the base of a wave, the higher the value, the more narrow the wave"""
        ...
    @narrowness.setter
    def narrowness(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]):
        ...
    @property
    def texture(self) -> Annotated[Optional['Texture'], "is_animatable=False"]:

        ...
    @texture.setter
    def texture(self, value: Annotated[Optional['Texture'], "is_animatable=False"]):
        ...
    @property
    def texture_coords(self) -> Literal['LOCAL', 'GLOBAL', 'OBJECT', 'UV']:

        ...
    @texture_coords.setter
    def texture_coords(self, value: Literal['LOCAL', 'GLOBAL', 'OBJECT', 'UV']):
        ...
    @property
    def uv_layer(self) -> Annotated[str, "is_animatable=False"]:
        """UV map name"""
        ...
    @uv_layer.setter
    def uv_layer(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def texture_coords_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to set the texture coordinates"""
        ...
    @texture_coords_object.setter
    def texture_coords_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def texture_coords_bone(self) -> Annotated[str, "is_animatable=False"]:
        """Bone to set the texture coordinates"""
        ...
    @texture_coords_bone.setter
    def texture_coords_bone(self, value: Annotated[str, "is_animatable=False"]):
        ...