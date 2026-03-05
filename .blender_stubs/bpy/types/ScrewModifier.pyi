# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ScrewModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .Object import Object

class ScrewModifier(Modifier):

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
        """Object to define the screw axis"""
        ...
    @object.setter
    def object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def steps(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of steps in the revolution"""
        ...
    @steps.setter
    def steps(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def render_steps(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of steps in the revolution"""
        ...
    @render_steps.setter
    def render_steps(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def iterations(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of times to apply the screw operation"""
        ...
    @iterations.setter
    def iterations(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def axis(self) -> Literal['X', 'Y', 'Z']:
        """Screw axis"""
        ...
    @axis.setter
    def axis(self, value: Literal['X', 'Y', 'Z']):
        ...
    @property
    def angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=-1"]:
        """Angle of revolution"""
        ...
    @angle.setter
    def angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=-1"]):
        ...
    @property
    def screw_offset(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Offset the revolution along its axis"""
        ...
    @screw_offset.setter
    def screw_offset(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def merge_threshold(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=4"]:
        """Limit below which to merge vertices"""
        ...
    @merge_threshold.setter
    def merge_threshold(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=4"]):
        ...
    @property
    def use_normal_flip(self) -> bool:
        """Flip normals of lathed faces"""
        ...
    @use_normal_flip.setter
    def use_normal_flip(self, value: bool):
        ...
    @property
    def use_normal_calculate(self) -> bool:
        """Calculate the order of edges (needed for meshes, but not curves)"""
        ...
    @use_normal_calculate.setter
    def use_normal_calculate(self, value: bool):
        ...
    @property
    def use_object_screw_offset(self) -> bool:
        """Use the distance between the objects to make a screw"""
        ...
    @use_object_screw_offset.setter
    def use_object_screw_offset(self, value: bool):
        ...
    @property
    def use_merge_vertices(self) -> bool:
        """Merge adjacent vertices (screw offset must be zero)"""
        ...
    @use_merge_vertices.setter
    def use_merge_vertices(self, value: bool):
        ...
    @property
    def use_smooth_shade(self) -> bool:
        """Output faces with smooth shading rather than flat shaded"""
        ...
    @use_smooth_shade.setter
    def use_smooth_shade(self, value: bool):
        ...
    @property
    def use_stretch_u(self) -> bool:
        """Stretch the U coordinates between 0 and 1 when UVs are present"""
        ...
    @use_stretch_u.setter
    def use_stretch_u(self, value: bool):
        ...
    @property
    def use_stretch_v(self) -> bool:
        """Stretch the V coordinates between 0 and 1 when UVs are present"""
        ...
    @use_stretch_v.setter
    def use_stretch_v(self, value: bool):
        ...