# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.DecimateModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier

class DecimateModifier(Modifier):

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
    def decimate_type(self) -> Literal['COLLAPSE', 'UNSUBDIV', 'DISSOLVE']:

        ...
    @decimate_type.setter
    def decimate_type(self, value: Literal['COLLAPSE', 'UNSUBDIV', 'DISSOLVE']) -> None:
        ...
    @property
    def ratio(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=4"]:
        """Ratio of triangles to reduce to (collapse only)"""
        ...
    @ratio.setter
    def ratio(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=4"]) -> None:
        ...
    @property
    def iterations(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of times reduce the geometry (unsubdivide only)"""
        ...
    @iterations.setter
    def iterations(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def angle_limit(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=4"]:
        """Only dissolve angles below this (planar only)"""
        ...
    @angle_limit.setter
    def angle_limit(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=4"]) -> None:
        ...
    @property
    def vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group name (collapse only)"""
        ...
    @vertex_group.setter
    def vertex_group(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def invert_vertex_group(self) -> bool:
        """Invert vertex group influence (collapse only)"""
        ...
    @invert_vertex_group.setter
    def invert_vertex_group(self, value: bool) -> None:
        ...
    @property
    def use_collapse_triangulate(self) -> bool:
        """Keep triangulated faces resulting from decimation (collapse only)"""
        ...
    @use_collapse_triangulate.setter
    def use_collapse_triangulate(self, value: bool) -> None:
        ...
    @property
    def use_symmetry(self) -> bool:
        """Maintain symmetry on an axis"""
        ...
    @use_symmetry.setter
    def use_symmetry(self, value: bool) -> None:
        ...
    @property
    def symmetry_axis(self) -> Literal['X', 'Y', 'Z']:
        """Axis of symmetry"""
        ...
    @symmetry_axis.setter
    def symmetry_axis(self, value: Literal['X', 'Y', 'Z']) -> None:
        ...
    @property
    def vertex_group_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=4"]:
        """Vertex group strength"""
        ...
    @vertex_group_factor.setter
    def vertex_group_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=4"]) -> None:
        ...
    @property
    def use_dissolve_boundaries(self) -> bool:
        """Dissolve all vertices in between face boundaries (planar only)"""
        ...
    @use_dissolve_boundaries.setter
    def use_dissolve_boundaries(self, value: bool) -> None:
        ...
    @property
    def delimit(self) -> set[str]:
        """Limit merging geometry"""
        ...
    @delimit.setter
    def delimit(self, value: set[str]) -> None:
        ...
    @property
    def face_count(self) -> Annotated[int, "step=1"]:
        """The current number of faces in the decimated mesh"""
        ...