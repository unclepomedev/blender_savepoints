# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SolidifyModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier

class SolidifyModifier(Modifier):

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
    def solidify_mode(self) -> Literal['EXTRUDE', 'NON_MANIFOLD']:
        """Selects the used algorithm"""
        ...
    @solidify_mode.setter
    def solidify_mode(self, value: Literal['EXTRUDE', 'NON_MANIFOLD']) -> None:
        ...
    @property
    def thickness(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=4"]:
        """Thickness of the shell"""
        ...
    @thickness.setter
    def thickness(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=4"]) -> None:
        ...
    @property
    def thickness_clamp(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=4"]:
        """Offset clamp based on geometry scale"""
        ...
    @thickness_clamp.setter
    def thickness_clamp(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=4"]) -> None:
        ...
    @property
    def use_thickness_angle_clamp(self) -> bool:
        """Clamp thickness based on angles"""
        ...
    @use_thickness_angle_clamp.setter
    def use_thickness_angle_clamp(self, value: bool) -> None:
        ...
    @property
    def thickness_vertex_group(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]:
        """Thickness factor to use for zero vertex group influence"""
        ...
    @thickness_vertex_group.setter
    def thickness_vertex_group(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def offset(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=4"]:
        """Offset the thickness from the center"""
        ...
    @offset.setter
    def offset(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=4"]) -> None:
        ...
    @property
    def edge_crease_inner(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]:
        """Assign a crease to inner edges"""
        ...
    @edge_crease_inner.setter
    def edge_crease_inner(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def edge_crease_outer(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]:
        """Assign a crease to outer edges"""
        ...
    @edge_crease_outer.setter
    def edge_crease_outer(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def edge_crease_rim(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]:
        """Assign a crease to the edges making up the rim"""
        ...
    @edge_crease_rim.setter
    def edge_crease_rim(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def material_offset(self) -> Annotated[int, "step=1"]:
        """Offset material index of generated faces"""
        ...
    @material_offset.setter
    def material_offset(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def material_offset_rim(self) -> Annotated[int, "step=1"]:
        """Offset material index of generated rim faces"""
        ...
    @material_offset_rim.setter
    def material_offset_rim(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group name"""
        ...
    @vertex_group.setter
    def vertex_group(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def shell_vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group that the generated shell geometry will be weighted to"""
        ...
    @shell_vertex_group.setter
    def shell_vertex_group(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def rim_vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group that the generated rim geometry will be weighted to"""
        ...
    @rim_vertex_group.setter
    def rim_vertex_group(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def use_rim(self) -> bool:
        """Create edge loops between the inner and outer surfaces on face edges (slow, disable when not needed)"""
        ...
    @use_rim.setter
    def use_rim(self, value: bool) -> None:
        ...
    @property
    def use_even_offset(self) -> bool:
        """Maintain thickness by adjusting for sharp corners (slow, disable when not needed)"""
        ...
    @use_even_offset.setter
    def use_even_offset(self, value: bool) -> None:
        ...
    @property
    def use_quality_normals(self) -> bool:
        """Calculate normals which result in more even thickness (slow, disable when not needed)"""
        ...
    @use_quality_normals.setter
    def use_quality_normals(self, value: bool) -> None:
        ...
    @property
    def invert_vertex_group(self) -> bool:
        """Invert the vertex group influence"""
        ...
    @invert_vertex_group.setter
    def invert_vertex_group(self, value: bool) -> None:
        ...
    @property
    def use_flat_faces(self) -> bool:
        """Make faces use the minimal vertex weight assigned to their vertices (ensures new faces remain parallel to their original ones, slow, disable when not needed)"""
        ...
    @use_flat_faces.setter
    def use_flat_faces(self, value: bool) -> None:
        ...
    @property
    def use_flip_normals(self) -> bool:
        """Invert the face direction"""
        ...
    @use_flip_normals.setter
    def use_flip_normals(self, value: bool) -> None:
        ...
    @property
    def use_rim_only(self) -> bool:
        """Only add the rim to the original data"""
        ...
    @use_rim_only.setter
    def use_rim_only(self, value: bool) -> None:
        ...
    @property
    def nonmanifold_thickness_mode(self) -> Literal['FIXED', 'EVEN', 'CONSTRAINTS']:
        """Selects the used thickness algorithm"""
        ...
    @nonmanifold_thickness_mode.setter
    def nonmanifold_thickness_mode(self, value: Literal['FIXED', 'EVEN', 'CONSTRAINTS']) -> None:
        ...
    @property
    def nonmanifold_boundary_mode(self) -> Literal['NONE', 'ROUND', 'FLAT']:
        """Selects the boundary adjustment algorithm"""
        ...
    @nonmanifold_boundary_mode.setter
    def nonmanifold_boundary_mode(self, value: Literal['NONE', 'ROUND', 'FLAT']) -> None:
        ...
    @property
    def nonmanifold_merge_threshold(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=4"]:
        """Distance within which degenerated geometry is merged"""
        ...
    @nonmanifold_merge_threshold.setter
    def nonmanifold_merge_threshold(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=4"]) -> None:
        ...
    @property
    def bevel_convex(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Edge bevel weight to be added to outside edges"""
        ...
    @bevel_convex.setter
    def bevel_convex(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...