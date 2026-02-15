# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.VertexWeightProximityModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .CurveMapping import CurveMapping
from .Object import Object
from .Texture import Texture

class VertexWeightProximityModifier(Modifier):

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
    vertex_group: Annotated[str, "is_animatable=False"]
    """Vertex group name"""
    proximity_mode: Literal['OBJECT', 'GEOMETRY']
    """Which distances to target object to use"""
    proximity_geometry: set[str]
    """Use the shortest computed distance to target object's geometry as weight"""
    target: Annotated[Optional['Object'], "is_animatable=False"]
    """Object to calculate vertices distances from"""
    min_dist: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=-1"]
    """Distance mapping to weight 0.0"""
    max_dist: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=-1"]
    """Distance mapping to weight 1.0"""
    falloff_type: Literal['LINEAR', 'CURVE', 'SHARP', 'SMOOTH', 'ROOT', 'ICON_SPHERECURVE', 'RANDOM', 'STEP']
    """How weights are mapped to their new values"""
    invert_falloff: bool
    """Invert the resulting falloff weight"""
    normalize: bool
    """Normalize the resulting weights (otherwise they are only clamped within 0.0 to 1.0 range)"""
    @property
    def map_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Custom mapping curve"""
        ...
    mask_constant: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=-1"]
    """Global influence of current modifications on vgroup"""
    mask_vertex_group: Annotated[str, "is_animatable=False"]
    """Masking vertex group name"""
    invert_mask_vertex_group: bool
    """Invert vertex group mask influence"""
    mask_texture: Annotated[Optional['Texture'], "is_animatable=False"]
    """Masking texture"""
    mask_tex_use_channel: Literal['INT', 'RED', 'GREEN', 'BLUE', 'HUE', 'SAT', 'VAL', 'ALPHA']
    """Which texture channel to use for masking"""
    mask_tex_mapping: Literal['LOCAL', 'GLOBAL', 'OBJECT', 'UV']
    """Which texture coordinates to use for mapping"""
    mask_tex_uv_layer: Annotated[str, "is_animatable=False"]
    """UV map name"""
    mask_tex_map_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Which object to take texture coordinates from"""
    mask_tex_map_bone: Annotated[str, "is_animatable=False"]
    """Which bone to take texture coordinates from"""