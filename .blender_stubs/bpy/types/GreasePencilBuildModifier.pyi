# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GreasePencilBuildModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .Material import Material
from .Object import Object

class GreasePencilBuildModifier(Modifier):

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
    def tree_node_filter(self) -> Annotated[str, "is_animatable=False"]:
        """Layer name"""
        ...
    @tree_node_filter.setter
    def tree_node_filter(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def use_layer_pass_filter(self) -> bool:
        """Use layer pass filter"""
        ...
    @use_layer_pass_filter.setter
    def use_layer_pass_filter(self, value: bool) -> None:
        ...
    @property
    def layer_pass_filter(self) -> Annotated[int, "step=1"]:
        """Layer pass filter"""
        ...
    @layer_pass_filter.setter
    def layer_pass_filter(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def invert_layer_filter(self) -> bool:
        """Invert layer filter"""
        ...
    @invert_layer_filter.setter
    def invert_layer_filter(self, value: bool) -> None:
        ...
    @property
    def invert_layer_pass_filter(self) -> bool:
        """Invert layer pass filter"""
        ...
    @invert_layer_pass_filter.setter
    def invert_layer_pass_filter(self, value: bool) -> None:
        ...
    @property
    def use_layer_group_filter(self) -> bool:
        """Filter by layer group name"""
        ...
    @use_layer_group_filter.setter
    def use_layer_group_filter(self, value: bool) -> None:
        ...
    @property
    def material_filter(self) -> Annotated[Optional['Material'], "is_animatable=False"]:
        """Material used for filtering"""
        ...
    @material_filter.setter
    def material_filter(self, value: Annotated[Optional['Material'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_material_pass_filter(self) -> bool:
        """Use material pass filter"""
        ...
    @use_material_pass_filter.setter
    def use_material_pass_filter(self, value: bool) -> None:
        ...
    @property
    def material_pass_filter(self) -> Annotated[int, "step=1"]:
        """Material pass"""
        ...
    @material_pass_filter.setter
    def material_pass_filter(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def invert_material_filter(self) -> bool:
        """Invert material filter"""
        ...
    @invert_material_filter.setter
    def invert_material_filter(self, value: bool) -> None:
        ...
    @property
    def invert_material_pass_filter(self) -> bool:
        """Invert material pass filter"""
        ...
    @invert_material_pass_filter.setter
    def invert_material_pass_filter(self, value: bool) -> None:
        ...
    @property
    def open_influence_panel(self) -> bool:

        ...
    @open_influence_panel.setter
    def open_influence_panel(self, value: bool) -> None:
        ...
    @property
    def open_frame_range_panel(self) -> bool:

        ...
    @open_frame_range_panel.setter
    def open_frame_range_panel(self, value: bool) -> None:
        ...
    @property
    def open_fading_panel(self) -> bool:

        ...
    @open_fading_panel.setter
    def open_fading_panel(self, value: bool) -> None:
        ...
    @property
    def mode(self) -> Literal['SEQUENTIAL', 'CONCURRENT', 'ADDITIVE']:
        """How strokes are being built"""
        ...
    @mode.setter
    def mode(self, value: Literal['SEQUENTIAL', 'CONCURRENT', 'ADDITIVE']) -> None:
        ...
    @property
    def transition(self) -> Literal['GROW', 'SHRINK', 'FADE']:
        """How are strokes animated (i.e. are they appearing or disappearing)"""
        ...
    @transition.setter
    def transition(self, value: Literal['GROW', 'SHRINK', 'FADE']) -> None:
        ...
    @property
    def start_delay(self) -> Annotated[float, "step=1.0", "precision=-1"]:
        """Number of frames after each GP keyframe before the modifier has any effect"""
        ...
    @start_delay.setter
    def start_delay(self, value: Annotated[float, "step=1.0", "precision=-1"]) -> None:
        ...
    @property
    def length(self) -> Annotated[float, "step=1.0", "precision=-1"]:
        """Maximum number of frames that the build effect can run for (unless another GP keyframe occurs before this time has elapsed)"""
        ...
    @length.setter
    def length(self, value: Annotated[float, "step=1.0", "precision=-1"]) -> None:
        ...
    @property
    def concurrent_time_alignment(self) -> Literal['START', 'END']:
        """How should strokes start to appear/disappear"""
        ...
    @concurrent_time_alignment.setter
    def concurrent_time_alignment(self, value: Literal['START', 'END']) -> None:
        ...
    @property
    def time_mode(self) -> Literal['DRAWSPEED', 'FRAMES', 'PERCENTAGE']:
        """Use drawing speed, a number of frames, or a manual factor to build strokes"""
        ...
    @time_mode.setter
    def time_mode(self, value: Literal['DRAWSPEED', 'FRAMES', 'PERCENTAGE']) -> None:
        ...
    @property
    def speed_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=-1"]:
        """Multiply recorded drawing speed by a factor"""
        ...
    @speed_factor.setter
    def speed_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=-1"]) -> None:
        ...
    @property
    def speed_maxgap(self) -> Annotated[float, "step=0.009999999776482582", "precision=-1"]:
        """The maximum gap between strokes in seconds"""
        ...
    @speed_maxgap.setter
    def speed_maxgap(self, value: Annotated[float, "step=0.009999999776482582", "precision=-1"]) -> None:
        ...
    @property
    def use_restrict_frame_range(self) -> bool:
        """Only modify strokes during the specified frame range"""
        ...
    @use_restrict_frame_range.setter
    def use_restrict_frame_range(self, value: bool) -> None:
        ...
    @property
    def use_percentage(self) -> bool:
        """Use a percentage factor to determine the visible points"""
        ...
    @use_percentage.setter
    def use_percentage(self, value: bool) -> None:
        ...
    @property
    def percentage_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Defines how much of the stroke is visible"""
        ...
    @percentage_factor.setter
    def percentage_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def frame_start(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Start Frame (when Restrict Frame Range is enabled)"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def frame_end(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """End Frame (when Restrict Frame Range is enabled)"""
        ...
    @frame_end.setter
    def frame_end(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_fading(self) -> bool:
        """Fade out strokes instead of directly cutting off"""
        ...
    @use_fading.setter
    def use_fading(self, value: bool) -> None:
        ...
    @property
    def fade_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Defines how much of the stroke is fading in/out"""
        ...
    @fade_factor.setter
    def fade_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def target_vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Output Vertex group"""
        ...
    @target_vertex_group.setter
    def target_vertex_group(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def fade_opacity_strength(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How much strength fading applies on top of stroke opacity"""
        ...
    @fade_opacity_strength.setter
    def fade_opacity_strength(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def fade_thickness_strength(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """How much strength fading applies on top of stroke thickness"""
        ...
    @fade_thickness_strength.setter
    def fade_thickness_strength(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object used as build starting position"""
        ...
    @object.setter
    def object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...