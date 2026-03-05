# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SubsurfModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier

class SubsurfModifier(Modifier):

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
    def uv_smooth(self) -> Literal['NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL']:
        """Controls how smoothing is applied to UVs"""
        ...
    @uv_smooth.setter
    def uv_smooth(self, value: Literal['NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL']) -> None:
        ...
    @property
    def quality(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Accuracy of vertex positions, lower value is faster but less precise"""
        ...
    @quality.setter
    def quality(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def boundary_smooth(self) -> Literal['PRESERVE_CORNERS', 'ALL']:
        """Controls how open boundaries are smoothed"""
        ...
    @boundary_smooth.setter
    def boundary_smooth(self, value: Literal['PRESERVE_CORNERS', 'ALL']) -> None:
        ...
    @property
    def subdivision_type(self) -> Literal['CATMULL_CLARK', 'SIMPLE']:
        """Select type of subdivision algorithm"""
        ...
    @subdivision_type.setter
    def subdivision_type(self, value: Literal['CATMULL_CLARK', 'SIMPLE']) -> None:
        ...
    @property
    def levels(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of subdivisions to perform in the 3D viewport"""
        ...
    @levels.setter
    def levels(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def render_levels(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of subdivisions to perform when rendering"""
        ...
    @render_levels.setter
    def render_levels(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def show_only_control_edges(self) -> bool:
        """Skip displaying interior subdivided edges"""
        ...
    @show_only_control_edges.setter
    def show_only_control_edges(self, value: bool) -> None:
        ...
    @property
    def use_creases(self) -> bool:
        """Use mesh crease information to sharpen edges or corners"""
        ...
    @use_creases.setter
    def use_creases(self, value: bool) -> None:
        ...
    @property
    def use_custom_normals(self) -> bool:
        """Interpolates existing custom normals to resulting mesh"""
        ...
    @use_custom_normals.setter
    def use_custom_normals(self, value: bool) -> None:
        ...
    @property
    def use_limit_surface(self) -> bool:
        """Place vertices at the surface that would be produced with infinite levels of subdivision (smoothest possible shape)"""
        ...
    @use_limit_surface.setter
    def use_limit_surface(self, value: bool) -> None:
        ...
    @property
    def use_adaptive_subdivision(self) -> bool:
        """Adaptively subdivide mesh based on camera distance"""
        ...
    @use_adaptive_subdivision.setter
    def use_adaptive_subdivision(self, value: bool) -> None:
        ...
    @property
    def adaptive_space(self) -> Literal['PIXEL', 'OBJECT']:
        """How to adaptively subdivide the mesh"""
        ...
    @adaptive_space.setter
    def adaptive_space(self, value: Literal['PIXEL', 'OBJECT']) -> None:
        ...
    @property
    def adaptive_pixel_size(self) -> Annotated[float, "subtype='PIXEL'", "step=10.0", "precision=3"]:
        """Target polygon pixel size for adaptive subdivision"""
        ...
    @adaptive_pixel_size.setter
    def adaptive_pixel_size(self, value: Annotated[float, "subtype='PIXEL'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def adaptive_object_edge_length(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Target object space edge length for adaptive subdivision"""
        ...
    @adaptive_object_edge_length.setter
    def adaptive_object_edge_length(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def open_adaptive_subdivision_panel(self) -> bool:

        ...
    @open_adaptive_subdivision_panel.setter
    def open_adaptive_subdivision_panel(self, value: bool) -> None:
        ...
    @property
    def open_advanced_panel(self) -> bool:

        ...
    @open_advanced_panel.setter
    def open_advanced_panel(self, value: bool) -> None:
        ...