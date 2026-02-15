# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Bone.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from ._GenericBone import _GenericBone
from .BoneCollection import BoneCollection
from .BoneCollectionMemberships import BoneCollectionMemberships
from .BoneColor import BoneColor
from .bpy_prop_collection import bpy_prop_collection

class Bone(bpy_struct, _GenericBone):

    @property
    def parent(self) -> Annotated[Optional['Bone'], "is_animatable=False"]:
        """Parent bone (in same Armature)"""
        ...
    @property
    def children(self) -> Annotated[bpy_prop_collection['Bone'], "is_animatable=False"]:
        """Bones which are children of this bone"""
        ...
    @property
    def collections(self) -> Annotated['BoneCollectionMemberships', "is_animatable=False"]:
        """Bone Collections that contain this bone"""
        ...
    name: Annotated[str, "is_animatable=False"]

    @property
    def color(self) -> Annotated[Optional['BoneColor'], "is_animatable=False"]:

        ...
    display_type: Literal['ARMATURE_DEFINED', 'OCTAHEDRAL', 'STICK', 'BBONE', 'ENVELOPE', 'WIRE']

    @property
    def use_connect(self) -> bool:
        """When bone has a parent, bone's head is stuck to the parent's tail"""
        ...
    use_inherit_rotation: bool
    """Bone inherits rotation or scale from parent bone"""
    use_envelope_multiply: bool
    """When deforming bone, multiply effects of Vertex Group weights with Envelope influence"""
    use_deform: bool
    """Enable Bone to deform geometry"""
    inherit_scale: Literal['FULL', 'FIX_SHEAR', 'ALIGNED', 'AVERAGE', 'NONE', 'NONE_LEGACY']
    """Specifies how the bone inherits scaling from the parent bone"""
    use_local_location: bool
    """Bone location is set in local space"""
    use_relative_parent: bool
    """Object children will use relative transform, like deform"""
    show_wire: bool
    """Bone is always displayed in wireframe regardless of viewport shading mode (useful for non-obstructive custom bone shapes)"""
    use_cyclic_offset: bool
    """When bone does not have a parent, it receives cyclic offset effects (Deprecated)"""
    hide_select: bool
    """Bone is able to be selected"""
    envelope_distance: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Bone deformation distance (for Envelope deform only)"""
    envelope_weight: Annotated[float, "step=10.0", "precision=3"]
    """Bone deformation weight (for Envelope deform only)"""
    head_radius: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]
    """Radius of head of bone (for Envelope deform only)"""
    tail_radius: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3"]
    """Radius of tail of bone (for Envelope deform only)"""
    bbone_segments: Annotated[int, "step=1"]
    """Number of subdivisions of bone (for B-Bones only)"""
    bbone_mapping_mode: Annotated[Literal['STRAIGHT', 'CURVED'], "is_animatable=False"]
    """Selects how the vertices are mapped to B-Bone segments based on their position"""
    bbone_x: Annotated[float, "step=1.0", "precision=5"]
    """B-Bone X size"""
    bbone_z: Annotated[float, "step=1.0", "precision=5"]
    """B-Bone Z size"""
    bbone_handle_type_start: Annotated[Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'TANGENT'], "is_animatable=False"]
    """Selects how the start handle of the B-Bone is computed"""
    bbone_custom_handle_start: Annotated[Optional['Bone'], "is_animatable=False"]
    """Bone that serves as the start handle for the B-Bone curve"""
    bbone_handle_use_scale_start: list[bool]
    """Multiply B-Bone Scale In channels by the local scale values of the start handle. This is done after the Scale Easing option and isn't affected by it."""
    bbone_handle_use_ease_start: bool
    """Multiply the B-Bone Ease In channel by the local Y scale value of the start handle. This is done after the Scale Easing option and isn't affected by it."""
    bbone_handle_type_end: Annotated[Literal['AUTO', 'ABSOLUTE', 'RELATIVE', 'TANGENT'], "is_animatable=False"]
    """Selects how the end handle of the B-Bone is computed"""
    bbone_custom_handle_end: Annotated[Optional['Bone'], "is_animatable=False"]
    """Bone that serves as the end handle for the B-Bone curve"""
    bbone_handle_use_scale_end: list[bool]
    """Multiply B-Bone Scale Out channels by the local scale values of the end handle. This is done after the Scale Easing option and isn't affected by it."""
    bbone_handle_use_ease_end: bool
    """Multiply the B-Bone Ease Out channel by the local Y scale value of the end handle. This is done after the Scale Easing option and isn't affected by it."""
    bbone_rollin: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2"]
    """Roll offset for the start of the B-Bone, adjusts twist"""
    bbone_rollout: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2"]
    """Roll offset for the end of the B-Bone, adjusts twist"""
    use_endroll_as_inroll: Annotated[bool, "is_animatable=False"]
    """Add Roll Out of the Start Handle bone to the Roll In value"""
    bbone_curveinx: Annotated[float, "step=1.0", "precision=5"]
    """X-axis handle offset for start of the B-Bone's curve, adjusts curvature"""
    bbone_curveinz: Annotated[float, "step=1.0", "precision=5"]
    """Z-axis handle offset for start of the B-Bone's curve, adjusts curvature"""
    bbone_curveoutx: Annotated[float, "step=1.0", "precision=5"]
    """X-axis handle offset for end of the B-Bone's curve, adjusts curvature"""
    bbone_curveoutz: Annotated[float, "step=1.0", "precision=5"]
    """Z-axis handle offset for end of the B-Bone's curve, adjusts curvature"""
    bbone_easein: Annotated[float, "step=1.0", "precision=3"]
    """Length of first Bézier Handle (for B-Bones only)"""
    bbone_easeout: Annotated[float, "step=1.0", "precision=3"]
    """Length of second Bézier Handle (for B-Bones only)"""
    use_scale_easing: bool
    """Multiply the final easing values by the Scale In/Out Y factors"""
    bbone_scalein: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]
    """Scale factors for the start of the B-Bone, adjusts thickness (for tapering effects)"""
    bbone_scaleout: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]
    """Scale factors for the end of the B-Bone, adjusts thickness (for tapering effects)"""
    hide: bool
    """Bone is not visible when it is in Edit Mode"""
    @property
    def matrix(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """3×3 bone matrix"""
        ...
    @property
    def matrix_local(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """4×4 bone matrix relative to armature"""
        ...
    @property
    def tail(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Location of tail end of the bone relative to its parent"""
        ...
    @property
    def tail_local(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Location of tail end of the bone relative to armature"""
        ...
    @property
    def head(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Location of head end of the bone relative to its parent"""
        ...
    @property
    def head_local(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Location of head end of the bone relative to armature"""
        ...
    @property
    def length(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Length of the bone"""
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def evaluate_envelope(self, *args, **kwargs) -> Any: ...
    def convert_local_to_pose(self, *args, **kwargs) -> Any: ...
    def MatrixFromAxisRoll(self, *args, **kwargs) -> Any: ...
    def AxisRollFromMatrix(self, *args, **kwargs) -> Any: ...