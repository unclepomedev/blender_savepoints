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
from .CurveProfile import CurveProfile
class BevelModifier(Modifier):
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
    width: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=4"]
    """Bevel amount"""
    width_pct: Annotated[float, "subtype='PERCENTAGE'", "step=5.0", "precision=2"]
    """Bevel amount for percentage method"""
    segments: Annotated[int, "step=1"]
    """Number of segments for round edges/verts"""
    affect: Literal['VERTICES', 'EDGES']
    """Affect edges or vertices"""
    limit_method: Literal['NONE', 'ANGLE', 'WEIGHT', 'VGROUP']
    edge_weight: Annotated[str, "is_animatable=False"]
    """Attribute name for edge weight"""
    vertex_weight: Annotated[str, "is_animatable=False"]
    """Attribute name for vertex weight"""
    angle_limit: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=4"]
    """Angle above which to bevel edges"""
    vertex_group: Annotated[str, "is_animatable=False"]
    """Vertex group name"""
    invert_vertex_group: bool
    """Invert vertex group influence"""
    use_clamp_overlap: bool
    """Clamp the width to avoid overlap"""
    offset_type: Literal['OFFSET', 'WIDTH', 'DEPTH', 'PERCENT', 'ABSOLUTE']
    """What distance Width measures"""
    profile_type: Literal['SUPERELLIPSE', 'CUSTOM']
    """The type of shape used to rebuild a beveled section"""
    profile: Annotated[float, "subtype='FACTOR'", "step=0.05000000074505806", "precision=2"]
    """The profile shape (0.5 = round)"""
    material: Annotated[int, "step=1"]
    """Material index of generated faces, -1 for automatic"""
    loop_slide: bool
    """Prefer sliding along edges to having even widths"""
    mark_seam: bool
    """Mark Seams along beveled edges"""
    mark_sharp: bool
    """Mark beveled edges as sharp"""
    harden_normals: bool
    """Match normals of new faces to adjacent faces"""
    face_strength_mode: Literal['FSTR_NONE', 'FSTR_NEW', 'FSTR_AFFECTED', 'FSTR_ALL']
    """Whether to set face strength, and which faces to set it on"""
    miter_outer: Literal['MITER_SHARP', 'MITER_PATCH', 'MITER_ARC']
    """Pattern to use for outside of miters"""
    miter_inner: Literal['MITER_SHARP', 'MITER_ARC']
    """Pattern to use for inside of miters"""
    spread: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=4"]
    """Spread distance for inner miter arcs"""
    @property
    def custom_profile(self) -> Annotated[Optional['CurveProfile'], "is_animatable=False"]:
        """The path for the custom profile"""
        ...
    vmesh_method: Literal['ADJ', 'CUTOFF']
    """The method to use to create the mesh at intersections"""