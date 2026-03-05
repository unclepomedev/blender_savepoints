# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.VertexWeightMixModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .Object import Object
from .Texture import Texture

class VertexWeightMixModifier(Modifier):

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
    def vertex_group_a(self) -> Annotated[str, "is_animatable=False"]:
        """First vertex group name"""
        ...
    @vertex_group_a.setter
    def vertex_group_a(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def vertex_group_b(self) -> Annotated[str, "is_animatable=False"]:
        """Second vertex group name"""
        ...
    @vertex_group_b.setter
    def vertex_group_b(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def invert_vertex_group_a(self) -> bool:
        """Invert the influence of vertex group A"""
        ...
    @invert_vertex_group_a.setter
    def invert_vertex_group_a(self, value: bool) -> None:
        ...
    @property
    def invert_vertex_group_b(self) -> bool:
        """Invert the influence of vertex group B"""
        ...
    @invert_vertex_group_b.setter
    def invert_vertex_group_b(self, value: bool) -> None:
        ...
    @property
    def default_weight_a(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=-1"]:
        """Default weight a vertex will have if it is not in the first A vgroup"""
        ...
    @default_weight_a.setter
    def default_weight_a(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=-1"]) -> None:
        ...
    @property
    def default_weight_b(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=-1"]:
        """Default weight a vertex will have if it is not in the second B vgroup"""
        ...
    @default_weight_b.setter
    def default_weight_b(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=-1"]) -> None:
        ...
    @property
    def mix_mode(self) -> Literal['SET', 'ADD', 'SUB', 'MUL', 'DIV', 'DIF', 'AVG', 'MIN', 'MAX']:
        """How weights from vgroup B affect weights of vgroup A"""
        ...
    @mix_mode.setter
    def mix_mode(self, value: Literal['SET', 'ADD', 'SUB', 'MUL', 'DIV', 'DIF', 'AVG', 'MIN', 'MAX']) -> None:
        ...
    @property
    def mix_set(self) -> Literal['ALL', 'A', 'B', 'OR', 'AND']:
        """Which vertices should be affected"""
        ...
    @mix_set.setter
    def mix_set(self, value: Literal['ALL', 'A', 'B', 'OR', 'AND']) -> None:
        ...
    @property
    def normalize(self) -> bool:
        """Normalize the resulting weights (otherwise they are only clamped within 0.0 to 1.0 range)"""
        ...
    @normalize.setter
    def normalize(self, value: bool) -> None:
        ...
    @property
    def mask_constant(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=-1"]:
        """Global influence of current modifications on vgroup"""
        ...
    @mask_constant.setter
    def mask_constant(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=-1"]) -> None:
        ...
    @property
    def mask_vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Masking vertex group name"""
        ...
    @mask_vertex_group.setter
    def mask_vertex_group(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def invert_mask_vertex_group(self) -> bool:
        """Invert vertex group mask influence"""
        ...
    @invert_mask_vertex_group.setter
    def invert_mask_vertex_group(self, value: bool) -> None:
        ...
    @property
    def mask_texture(self) -> Annotated[Optional['Texture'], "is_animatable=False"]:
        """Masking texture"""
        ...
    @mask_texture.setter
    def mask_texture(self, value: Annotated[Optional['Texture'], "is_animatable=False"]) -> None:
        ...
    @property
    def mask_tex_use_channel(self) -> Literal['INT', 'RED', 'GREEN', 'BLUE', 'HUE', 'SAT', 'VAL', 'ALPHA']:
        """Which texture channel to use for masking"""
        ...
    @mask_tex_use_channel.setter
    def mask_tex_use_channel(self, value: Literal['INT', 'RED', 'GREEN', 'BLUE', 'HUE', 'SAT', 'VAL', 'ALPHA']) -> None:
        ...
    @property
    def mask_tex_mapping(self) -> Literal['LOCAL', 'GLOBAL', 'OBJECT', 'UV']:
        """Which texture coordinates to use for mapping"""
        ...
    @mask_tex_mapping.setter
    def mask_tex_mapping(self, value: Literal['LOCAL', 'GLOBAL', 'OBJECT', 'UV']) -> None:
        ...
    @property
    def mask_tex_uv_layer(self) -> Annotated[str, "is_animatable=False"]:
        """UV map name"""
        ...
    @mask_tex_uv_layer.setter
    def mask_tex_uv_layer(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def mask_tex_map_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Which object to take texture coordinates from"""
        ...
    @mask_tex_map_object.setter
    def mask_tex_map_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def mask_tex_map_bone(self) -> Annotated[str, "is_animatable=False"]:
        """Which bone to take texture coordinates from"""
        ...
    @mask_tex_map_bone.setter
    def mask_tex_map_bone(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...