# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SolidifyModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier

class SolidifyModifier(Modifier):

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
    solidify_mode: Literal['EXTRUDE', 'NON_MANIFOLD']
    """Selects the used algorithm"""
    thickness: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=4"]
    """Thickness of the shell"""
    thickness_clamp: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=4"]
    """Offset clamp based on geometry scale"""
    use_thickness_angle_clamp: bool
    """Clamp thickness based on angles"""
    thickness_vertex_group: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]
    """Thickness factor to use for zero vertex group influence"""
    offset: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=4"]
    """Offset the thickness from the center"""
    edge_crease_inner: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]
    """Assign a crease to inner edges"""
    edge_crease_outer: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]
    """Assign a crease to outer edges"""
    edge_crease_rim: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]
    """Assign a crease to the edges making up the rim"""
    material_offset: Annotated[int, "step=1"]
    """Offset material index of generated faces"""
    material_offset_rim: Annotated[int, "step=1"]
    """Offset material index of generated rim faces"""
    vertex_group: Annotated[str, "is_animatable=False"]
    """Vertex group name"""
    shell_vertex_group: Annotated[str, "is_animatable=False"]
    """Vertex group that the generated shell geometry will be weighted to"""
    rim_vertex_group: Annotated[str, "is_animatable=False"]
    """Vertex group that the generated rim geometry will be weighted to"""
    use_rim: bool
    """Create edge loops between the inner and outer surfaces on face edges (slow, disable when not needed)"""
    use_even_offset: bool
    """Maintain thickness by adjusting for sharp corners (slow, disable when not needed)"""
    use_quality_normals: bool
    """Calculate normals which result in more even thickness (slow, disable when not needed)"""
    invert_vertex_group: bool
    """Invert the vertex group influence"""
    use_flat_faces: bool
    """Make faces use the minimal vertex weight assigned to their vertices (ensures new faces remain parallel to their original ones, slow, disable when not needed)"""
    use_flip_normals: bool
    """Invert the face direction"""
    use_rim_only: bool
    """Only add the rim to the original data"""
    nonmanifold_thickness_mode: Literal['FIXED', 'EVEN', 'CONSTRAINTS']
    """Selects the used thickness algorithm"""
    nonmanifold_boundary_mode: Literal['NONE', 'ROUND', 'FLAT']
    """Selects the boundary adjustment algorithm"""
    nonmanifold_merge_threshold: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=4"]
    """Distance within which degenerated geometry is merged"""
    bevel_convex: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Edge bevel weight to be added to outside edges"""