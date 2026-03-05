# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ArrayModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .Object import Object

class ArrayModifier(Modifier):

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
    def fit_type(self) -> Literal['FIXED_COUNT', 'FIT_LENGTH', 'FIT_CURVE']:
        """Array length calculation method"""
        ...
    @fit_type.setter
    def fit_type(self, value: Literal['FIXED_COUNT', 'FIT_LENGTH', 'FIT_CURVE']) -> None:
        ...
    @property
    def count(self) -> Annotated[int, "step=1"]:
        """Number of duplicates to make"""
        ...
    @count.setter
    def count(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def fit_length(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]:
        """Length to fit array within"""
        ...
    @fit_length.setter
    def fit_length(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]) -> None:
        ...
    @property
    def curve(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Curve object to fit array length to"""
        ...
    @curve.setter
    def curve(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_constant_offset(self) -> bool:
        """Add a constant offset"""
        ...
    @use_constant_offset.setter
    def use_constant_offset(self, value: bool) -> None:
        ...
    @property
    def constant_offset_displace(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Value for the distance between arrayed items"""
        ...
    @constant_offset_displace.setter
    def constant_offset_displace(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def use_relative_offset(self) -> bool:
        """Add an offset relative to the object's bounding box"""
        ...
    @use_relative_offset.setter
    def use_relative_offset(self, value: bool) -> None:
        ...
    @property
    def relative_offset_displace(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """The size of the geometry will determine the distance between arrayed items"""
        ...
    @relative_offset_displace.setter
    def relative_offset_displace(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_merge_vertices(self) -> bool:
        """Merge vertices in adjacent duplicates"""
        ...
    @use_merge_vertices.setter
    def use_merge_vertices(self, value: bool) -> None:
        ...
    @property
    def use_merge_vertices_cap(self) -> bool:
        """Merge vertices in first and last duplicates"""
        ...
    @use_merge_vertices_cap.setter
    def use_merge_vertices_cap(self, value: bool) -> None:
        ...
    @property
    def merge_threshold(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=4"]:
        """Limit below which to merge vertices"""
        ...
    @merge_threshold.setter
    def merge_threshold(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=4"]) -> None:
        ...
    @property
    def use_object_offset(self) -> bool:
        """Add another object's transformation to the total offset"""
        ...
    @use_object_offset.setter
    def use_object_offset(self, value: bool) -> None:
        ...
    @property
    def offset_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Use the location and rotation of another object to determine the distance and rotational change between arrayed items"""
        ...
    @offset_object.setter
    def offset_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def start_cap(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Mesh object to use as a start cap"""
        ...
    @start_cap.setter
    def start_cap(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def end_cap(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Mesh object to use as an end cap"""
        ...
    @end_cap.setter
    def end_cap(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def offset_u(self) -> Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]:
        """Amount to offset array UVs on the U axis"""
        ...
    @offset_u.setter
    def offset_u(self, value: Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]) -> None:
        ...
    @property
    def offset_v(self) -> Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]:
        """Amount to offset array UVs on the V axis"""
        ...
    @offset_v.setter
    def offset_v(self, value: Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]) -> None:
        ...