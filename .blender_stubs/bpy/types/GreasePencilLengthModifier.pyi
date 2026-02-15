# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .Modifier import Modifier
from .Material import Material
class GreasePencilLengthModifier(Modifier):
    name: Annotated[str, "is_animatable=False"]
    """Modifier name"""
    @property
    def type(self) -> Literal['GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY', 'DATA_TRANSFER', 'MESH_CACHE', 'MESH_SEQUENCE_CACHE', 'NORMAL_EDIT', 'WEIGHTED_NORMAL', 'UV_PROJECT', 'UV_WARP', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_PROXIMITY', 'GREASE_PENCIL_COLOR', 'GREASE_PENCIL_TINT', 'GREASE_PENCIL_OPACITY', 'GREASE_PENCIL_VERTEX_WEIGHT_ANGLE', 'GREASE_PENCIL_TIME', 'GREASE_PENCIL_TEXTURE', 'ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 'EDGE_SPLIT', 'NODES', 'MASK', 'MIRROR', 'MESH_TO_VOLUME', 'MULTIRES', 'REMESH', 'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'VOLUME_TO_MESH', 'WELD', 'WIREFRAME', 'GREASE_PENCIL_ARRAY', 'GREASE_PENCIL_BUILD', 'GREASE_PENCIL_LENGTH', 'LINEART', 'GREASE_PENCIL_MIRROR', 'GREASE_PENCIL_MULTIPLY', 'GREASE_PENCIL_SIMPLIFY', 'GREASE_PENCIL_SUBDIV', 'GREASE_PENCIL_ENVELOPE', 'GREASE_PENCIL_OUTLINE', 'ARMATURE', 'CAST', 'CURVE', 'DISPLACE', 'HOOK', 'LAPLACIANDEFORM', 'LATTICE', 'MESH_DEFORM', 'SHRINKWRAP', 'SIMPLE_DEFORM', 'SMOOTH', 'CORRECTIVE_SMOOTH', 'LAPLACIANSMOOTH', 'SURFACE_DEFORM', 'WARP', 'WAVE', 'VOLUME_DISPLACE', 'GREASE_PENCIL_HOOK', 'GREASE_PENCIL_NOISE', 'GREASE_PENCIL_OFFSET', 'GREASE_PENCIL_SMOOTH', 'GREASE_PENCIL_THICKNESS', 'GREASE_PENCIL_LATTICE', 'GREASE_PENCIL_DASH', 'GREASE_PENCIL_ARMATURE', 'GREASE_PENCIL_SHRINKWRAP', 'CLOTH', 'COLLISION', 'DYNAMIC_PAINT', 'EXPLODE', 'FLUID', 'OCEAN', 'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM', 'SOFT_BODY', 'SURFACE']:
        ...
    show_viewport: bool
    """Display modifier in viewport"""
    show_render: bool
    """Use modifier during render"""
    show_in_editmode: bool
    """Display modifier in Edit mode"""
    show_on_cage: bool
    """Adjust edit cage to modifier result"""
    show_expanded: bool
    """Set modifier expanded in the user interface"""
    is_active: Annotated[bool, "is_animatable=False"]
    """The active modifier in the list"""
    use_pin_to_last: Annotated[bool, "is_animatable=False"]
    """Keep the modifier at the end of the list"""
    @property
    def is_override_data(self) -> bool:
        """In a local override object, whether this modifier comes from the linked reference object, or is local to the override"""
        ...
    use_apply_on_spline: bool
    """Apply this and all preceding deformation modifiers on splines' points rather than on filled curve/surface"""
    @property
    def execution_time(self) -> Annotated[float, "subtype='TIME_ABSOLUTE'", "unit='TIME_ABSOLUTE'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Time in seconds that the modifier took to evaluate. This is only set on evaluated objects. If multiple modifiers run in parallel, execution time is not a reliable metric."""
        ...
    @property
    def persistent_uid(self) -> Annotated[int, "step=1"]:
        """Uniquely identifies the modifier within the modifier stack that it is part of"""
        ...
    tree_node_filter: Annotated[str, "is_animatable=False"]
    """Layer name"""
    use_layer_pass_filter: bool
    """Use layer pass filter"""
    layer_pass_filter: Annotated[int, "step=1"]
    """Layer pass filter"""
    invert_layer_filter: bool
    """Invert layer filter"""
    invert_layer_pass_filter: bool
    """Invert layer pass filter"""
    use_layer_group_filter: bool
    """Filter by layer group name"""
    material_filter: Annotated[Optional['Material'], "is_animatable=False"]
    """Material used for filtering"""
    use_material_pass_filter: bool
    """Use material pass filter"""
    material_pass_filter: Annotated[int, "step=1"]
    """Material pass"""
    invert_material_filter: bool
    """Invert material filter"""
    invert_material_pass_filter: bool
    """Invert material pass filter"""
    open_random_panel: bool
    open_curvature_panel: bool
    open_influence_panel: bool
    start_factor: Annotated[float, "step=0.10000000149011612", "precision=2"]
    """Added length to the start of each stroke relative to its length"""
    end_factor: Annotated[float, "step=0.10000000149011612", "precision=2"]
    """Added length to the end of each stroke relative to its length"""
    start_length: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]
    """Absolute added length to the start of each stroke"""
    end_length: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]
    """Absolute added length to the end of each stroke"""
    random_start_factor: Annotated[float, "step=0.10000000149011612", "precision=1"]
    """Size of random length added to the start of each stroke"""
    random_end_factor: Annotated[float, "step=0.10000000149011612", "precision=1"]
    """Size of random length added to the end of each stroke"""
    random_offset: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Smoothly offset each stroke's random value"""
    use_random: bool
    """Use random values over time"""
    seed: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Random seed"""
    step: Annotated[int, "step=1"]
    """Number of frames between randomization steps"""
    overshoot_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Defines what portion of the stroke is used for the calculation of the extension"""
    mode: Literal['RELATIVE', 'ABSOLUTE']
    """Mode to define length"""
    use_curvature: bool
    """Follow the curvature of the stroke"""
    invert_curvature: bool
    """Invert the curvature of the stroke's extension"""
    point_density: Annotated[float, "step=1.0", "precision=1"]
    """Multiplied by Start/End for the total added point count"""
    segment_influence: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]
    """Factor to determine how much the length of the individual segments should influence the final computed curvature. Higher factors makes small segments influence the overall curvature less."""
    max_angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=1"]
    """Ignore points on the stroke that deviate from their neighbors by more than this angle when determining the extrapolation shape"""