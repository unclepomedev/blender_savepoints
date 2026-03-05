# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MeshCacheModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier

class MeshCacheModifier(Modifier):

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
    def cache_format(self) -> Literal['MDD', 'PC2']:

        ...
    @cache_format.setter
    def cache_format(self, value: Literal['MDD', 'PC2']):
        ...
    @property
    def interpolation(self) -> Literal['NONE', 'LINEAR']:

        ...
    @interpolation.setter
    def interpolation(self, value: Literal['NONE', 'LINEAR']):
        ...
    @property
    def time_mode(self) -> Literal['FRAME', 'TIME', 'FACTOR']:
        """Method to control playback time"""
        ...
    @time_mode.setter
    def time_mode(self, value: Literal['FRAME', 'TIME', 'FACTOR']):
        ...
    @property
    def play_mode(self) -> Literal['SCENE', 'CUSTOM']:

        ...
    @play_mode.setter
    def play_mode(self, value: Literal['SCENE', 'CUSTOM']):
        ...
    @property
    def deform_mode(self) -> Literal['OVERWRITE', 'INTEGRATE']:

        ...
    @deform_mode.setter
    def deform_mode(self, value: Literal['OVERWRITE', 'INTEGRATE']):
        ...
    @property
    def filepath(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Path to external displacements file"""
        ...
    @filepath.setter
    def filepath(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]):
        ...
    @property
    def factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Influence of the deformation"""
        ...
    @factor.setter
    def factor(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the Vertex Group which determines the influence of the modifier per point"""
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
    def forward_axis(self) -> Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z']:

        ...
    @forward_axis.setter
    def forward_axis(self, value: Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z']):
        ...
    @property
    def up_axis(self) -> Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z']:

        ...
    @up_axis.setter
    def up_axis(self, value: Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z']):
        ...
    @property
    def flip_axis(self) -> list[bool]:

        ...
    @flip_axis.setter
    def flip_axis(self, value: list[bool]):
        ...
    @property
    def frame_start(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Add this to the start frame"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]):
        ...
    @property
    def frame_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Evaluation time in seconds"""
        ...
    @frame_scale.setter
    def frame_scale(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def eval_frame(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """The frame to evaluate (starting at 0)"""
        ...
    @eval_frame.setter
    def eval_frame(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def eval_time(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Evaluation time in seconds"""
        ...
    @eval_time.setter
    def eval_time(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def eval_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Evaluation time in seconds"""
        ...
    @eval_factor.setter
    def eval_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...