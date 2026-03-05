# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GreasePencilSmoothModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .CurveMapping import CurveMapping
from .Material import Material

class GreasePencilSmoothModifier(Modifier):

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
    def tree_node_filter(self) -> Annotated[str, "is_animatable=False"]:
        """Layer name"""
        ...
    @tree_node_filter.setter
    def tree_node_filter(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def use_layer_pass_filter(self) -> bool:
        """Use layer pass filter"""
        ...
    @use_layer_pass_filter.setter
    def use_layer_pass_filter(self, value: bool):
        ...
    @property
    def layer_pass_filter(self) -> Annotated[int, "step=1"]:
        """Layer pass filter"""
        ...
    @layer_pass_filter.setter
    def layer_pass_filter(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def invert_layer_filter(self) -> bool:
        """Invert layer filter"""
        ...
    @invert_layer_filter.setter
    def invert_layer_filter(self, value: bool):
        ...
    @property
    def invert_layer_pass_filter(self) -> bool:
        """Invert layer pass filter"""
        ...
    @invert_layer_pass_filter.setter
    def invert_layer_pass_filter(self, value: bool):
        ...
    @property
    def use_layer_group_filter(self) -> bool:
        """Filter by layer group name"""
        ...
    @use_layer_group_filter.setter
    def use_layer_group_filter(self, value: bool):
        ...
    @property
    def material_filter(self) -> Annotated[Optional['Material'], "is_animatable=False"]:
        """Material used for filtering"""
        ...
    @material_filter.setter
    def material_filter(self, value: Annotated[Optional['Material'], "is_animatable=False"]):
        ...
    @property
    def use_material_pass_filter(self) -> bool:
        """Use material pass filter"""
        ...
    @use_material_pass_filter.setter
    def use_material_pass_filter(self, value: bool):
        ...
    @property
    def material_pass_filter(self) -> Annotated[int, "step=1"]:
        """Material pass"""
        ...
    @material_pass_filter.setter
    def material_pass_filter(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def invert_material_filter(self) -> bool:
        """Invert material filter"""
        ...
    @invert_material_filter.setter
    def invert_material_filter(self, value: bool):
        ...
    @property
    def invert_material_pass_filter(self) -> bool:
        """Invert material pass filter"""
        ...
    @invert_material_pass_filter.setter
    def invert_material_pass_filter(self, value: bool):
        ...
    @property
    def vertex_group_name(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group name for modulating the deform"""
        ...
    @vertex_group_name.setter
    def vertex_group_name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def invert_vertex_group(self) -> bool:
        """Invert vertex group weights"""
        ...
    @invert_vertex_group.setter
    def invert_vertex_group(self, value: bool):
        ...
    @property
    def use_custom_curve(self) -> bool:
        """Use a custom curve to define a factor along the strokes"""
        ...
    @use_custom_curve.setter
    def use_custom_curve(self, value: bool):
        ...
    @property
    def custom_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Custom curve to apply effect"""
        ...
    @property
    def open_influence_panel(self) -> bool:

        ...
    @open_influence_panel.setter
    def open_influence_panel(self, value: bool):
        ...
    @property
    def factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of smooth to apply"""
        ...
    @factor.setter
    def factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_edit_position(self) -> bool:
        """The modifier affects the position of the point"""
        ...
    @use_edit_position.setter
    def use_edit_position(self, value: bool):
        ...
    @property
    def use_edit_strength(self) -> bool:
        """The modifier affects the color strength of the point"""
        ...
    @use_edit_strength.setter
    def use_edit_strength(self, value: bool):
        ...
    @property
    def use_edit_thickness(self) -> bool:
        """The modifier affects the thickness of the point"""
        ...
    @use_edit_thickness.setter
    def use_edit_thickness(self, value: bool):
        ...
    @property
    def use_edit_uv(self) -> bool:
        """The modifier affects the UV rotation factor of the point"""
        ...
    @use_edit_uv.setter
    def use_edit_uv(self, value: bool):
        ...
    @property
    def step(self) -> Annotated[int, "step=1"]:
        """Number of times to apply smooth (high numbers can reduce fps)"""
        ...
    @step.setter
    def step(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def use_keep_shape(self) -> bool:
        """Smooth the details, but keep the overall shape"""
        ...
    @use_keep_shape.setter
    def use_keep_shape(self, value: bool):
        ...
    @property
    def use_smooth_ends(self) -> bool:
        """Smooth ends of strokes"""
        ...
    @use_smooth_ends.setter
    def use_smooth_ends(self, value: bool):
        ...