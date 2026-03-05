# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.WarpModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .CurveMapping import CurveMapping
from .Object import Object
from .Texture import Texture

class WarpModifier(Modifier):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Modifier name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def type(self) -> Literal['GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY', 'DATA_TRANSFER', 'MESH_CACHE', 'MESH_SEQUENCE_CACHE', 'NORMAL_EDIT', 'WEIGHTED_NORMAL', 'UV_PROJECT', 'UV_WARP', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_PROXIMITY', 'GREASE_PENCIL_COLOR', 'GREASE_PENCIL_TINT', 'GREASE_PENCIL_OPACITY', 'GREASE_PENCIL_VERTEX_WEIGHT_ANGLE', 'GREASE_PENCIL_TIME', 'GREASE_PENCIL_TEXTURE', 'ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 'EDGE_SPLIT', 'NODES', 'MASK', 'MIRROR', 'MESH_TO_VOLUME', 'MULTIRES', 'REMESH', 'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'VOLUME_TO_MESH', 'WELD', 'WIREFRAME', 'GREASE_PENCIL_ARRAY', 'GREASE_PENCIL_BUILD', 'GREASE_PENCIL_LENGTH', 'LINEART', 'GREASE_PENCIL_MIRROR', 'GREASE_PENCIL_MULTIPLY', 'GREASE_PENCIL_SIMPLIFY', 'GREASE_PENCIL_SUBDIV', 'GREASE_PENCIL_ENVELOPE', 'GREASE_PENCIL_OUTLINE', 'ARMATURE', 'CAST', 'CURVE', 'DISPLACE', 'HOOK', 'LAPLACIANDEFORM', 'LATTICE', 'MESH_DEFORM', 'SHRINKWRAP', 'SIMPLE_DEFORM', 'SMOOTH', 'CORRECTIVE_SMOOTH', 'LAPLACIANSMOOTH', 'SURFACE_DEFORM', 'WARP', 'WAVE', 'VOLUME_DISPLACE', 'GREASE_PENCIL_HOOK', 'GREASE_PENCIL_NOISE', 'GREASE_PENCIL_OFFSET', 'GREASE_PENCIL_SMOOTH', 'GREASE_PENCIL_THICKNESS', 'GREASE_PENCIL_LATTICE', 'GREASE_PENCIL_DASH', 'GREASE_PENCIL_ARMATURE', 'GREASE_PENCIL_SHRINKWRAP', 'CLOTH', 'COLLISION', 'DYNAMIC_PAINT', 'EXPLODE', 'FLUID', 'OCEAN', 'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM', 'SOFT_BODY', 'SURFACE']:

        ...
    @property
    def show_viewport(self) -> bool:
        """Display modifier in viewport"""
        ...
    @show_viewport.setter
    def show_viewport(self, value: bool) -> None:
        ...
    @property
    def show_render(self) -> bool:
        """Use modifier during render"""
        ...
    @show_render.setter
    def show_render(self, value: bool) -> None:
        ...
    @property
    def show_in_editmode(self) -> bool:
        """Display modifier in Edit mode"""
        ...
    @show_in_editmode.setter
    def show_in_editmode(self, value: bool) -> None:
        ...
    @property
    def show_on_cage(self) -> bool:
        """Adjust edit cage to modifier result"""
        ...
    @show_on_cage.setter
    def show_on_cage(self, value: bool) -> None:
        ...
    @property
    def show_expanded(self) -> bool:
        """Set modifier expanded in the user interface"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool) -> None:
        ...
    @property
    def is_active(self) -> Annotated[bool, "is_animatable=False"]:
        """The active modifier in the list"""
        ...
    @is_active.setter
    def is_active(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_pin_to_last(self) -> Annotated[bool, "is_animatable=False"]:
        """Keep the modifier at the end of the list"""
        ...
    @use_pin_to_last.setter
    def use_pin_to_last(self, value: Annotated[bool, "is_animatable=False"]) -> None:
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
    def use_apply_on_spline(self, value: bool) -> None:
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
    def object_from(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to transform from"""
        ...
    @object_from.setter
    def object_from(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def bone_from(self) -> Annotated[str, "is_animatable=False"]:
        """Bone to transform from"""
        ...
    @bone_from.setter
    def bone_from(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def object_to(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to transform to"""
        ...
    @object_to.setter
    def object_to(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def bone_to(self) -> Annotated[str, "is_animatable=False"]:
        """Bone defining offset"""
        ...
    @bone_to.setter
    def bone_to(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def strength(self) -> Annotated[float, "step=10.0", "precision=2"]:

        ...
    @strength.setter
    def strength(self, value: Annotated[float, "step=10.0", "precision=2"]) -> None:
        ...
    @property
    def falloff_type(self) -> Literal['NONE', 'CURVE', 'SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT']:

        ...
    @falloff_type.setter
    def falloff_type(self, value: Literal['NONE', 'CURVE', 'SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT']) -> None:
        ...
    @property
    def falloff_radius(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Radius to apply"""
        ...
    @falloff_radius.setter
    def falloff_radius(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def falloff_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Custom falloff curve"""
        ...
    @property
    def use_volume_preserve(self) -> bool:
        """Preserve volume when rotations are used"""
        ...
    @use_volume_preserve.setter
    def use_volume_preserve(self, value: bool) -> None:
        ...
    @property
    def vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group name for modulating the deform"""
        ...
    @vertex_group.setter
    def vertex_group(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def invert_vertex_group(self) -> bool:
        """Invert vertex group influence"""
        ...
    @invert_vertex_group.setter
    def invert_vertex_group(self, value: bool) -> None:
        ...
    @property
    def texture(self) -> Annotated[Optional['Texture'], "is_animatable=False"]:

        ...
    @texture.setter
    def texture(self, value: Annotated[Optional['Texture'], "is_animatable=False"]) -> None:
        ...
    @property
    def texture_coords(self) -> Literal['LOCAL', 'GLOBAL', 'OBJECT', 'UV']:

        ...
    @texture_coords.setter
    def texture_coords(self, value: Literal['LOCAL', 'GLOBAL', 'OBJECT', 'UV']) -> None:
        ...
    @property
    def uv_layer(self) -> Annotated[str, "is_animatable=False"]:
        """UV map name"""
        ...
    @uv_layer.setter
    def uv_layer(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def texture_coords_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to set the texture coordinates"""
        ...
    @texture_coords_object.setter
    def texture_coords_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def texture_coords_bone(self) -> Annotated[str, "is_animatable=False"]:
        """Bone to set the texture coordinates"""
        ...
    @texture_coords_bone.setter
    def texture_coords_bone(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...