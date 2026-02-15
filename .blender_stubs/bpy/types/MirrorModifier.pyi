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
from .Object import Object
class MirrorModifier(Modifier):
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
    use_axis: list[bool]
    """Enable axis mirror"""
    use_bisect_axis: list[bool]
    """Cuts the mesh across the mirror plane"""
    use_bisect_flip_axis: list[bool]
    """Flips the direction of the slice"""
    use_clip: bool
    """Prevent vertices from going through the mirror during transform"""
    use_mirror_vertex_groups: bool
    """Mirror vertex groups (e.g. .R->.L)"""
    use_mirror_merge: bool
    """Merge vertices within the merge threshold"""
    use_mirror_u: bool
    """Mirror the U texture coordinate around the flip offset point"""
    use_mirror_v: bool
    """Mirror the V texture coordinate around the flip offset point"""
    use_mirror_udim: bool
    """Mirror the texture coordinate around each tile center"""
    mirror_offset_u: Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]
    """Amount to offset mirrored UVs flipping point from the 0.5 on the U axis"""
    mirror_offset_v: Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]
    """Amount to offset mirrored UVs flipping point from the 0.5 point on the V axis"""
    offset_u: Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]
    """Mirrored UV offset on the U axis"""
    offset_v: Annotated[float, "subtype='FACTOR'", "step=2.0", "precision=4"]
    """Mirrored UV offset on the V axis"""
    merge_threshold: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=6"]
    """Distance within which mirrored vertices are merged"""
    bisect_threshold: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=6"]
    """Distance from the bisect plane within which vertices are removed"""
    mirror_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Object to use as mirror"""