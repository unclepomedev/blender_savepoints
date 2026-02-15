# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from ._GenericBone import _GenericBone
from .Bone import Bone
from .BoneColor import BoneColor
from .Constraint import Constraint
from .MotionPath import MotionPath
from .Object import Object
from .PoseBoneConstraints import PoseBoneConstraints
class PoseBone(bpy_struct, _GenericBone):
    @property
    def constraints(self) -> Annotated['PoseBoneConstraints', "is_animatable=False"]:
        """Constraints that act on this pose channel"""
        ...
    name: Annotated[str, "is_animatable=False"]
    @property
    def motion_path(self) -> Annotated[Optional['MotionPath'], "is_animatable=False"]:
        """Motion Path for this element"""
        ...
    @property
    def bone(self) -> Annotated['Bone', "is_animatable=False"]:
        """Bone associated with this PoseBone"""
        ...
    @property
    def parent(self) -> Annotated[Optional['PoseBone'], "is_animatable=False"]:
        """Parent of this pose bone"""
        ...
    @property
    def child(self) -> Annotated[Optional['PoseBone'], "is_animatable=False"]:
        """Child of this pose bone"""
        ...
    location: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]
    scale: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    rotation_quaternion: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]
    """Rotation in Quaternions"""
    rotation_axis_angle: Annotated[list[float], "subtype='AXISANGLE'", "step=10.0", "precision=3"]
    """Angle of Rotation for Axis-Angle rotation representation"""
    rotation_euler: Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=100.0", "precision=5"]
    """Rotation in Eulers"""
    rotation_mode: Literal['QUATERNION', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'AXIS_ANGLE']
    """The kind of rotation to apply, values from other rotation modes are not used"""
    bbone_rollin: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2"]
    """Roll offset for the start of the B-Bone, adjusts twist"""
    bbone_rollout: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2"]
    """Roll offset for the end of the B-Bone, adjusts twist"""
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
    bbone_scalein: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]
    """Scale factors for the start of the B-Bone, adjusts thickness (for tapering effects)"""
    bbone_scaleout: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]
    """Scale factors for the end of the B-Bone, adjusts thickness (for tapering effects)"""
    @property
    def bbone_custom_handle_start(self) -> Annotated[Optional['PoseBone'], "is_animatable=False"]:
        """Bone that serves as the start handle for the B-Bone curve"""
        ...
    @property
    def bbone_custom_handle_end(self) -> Annotated[Optional['PoseBone'], "is_animatable=False"]:
        """Bone that serves as the end handle for the B-Bone curve"""
        ...
    @property
    def matrix_channel(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """4×4 matrix of the bone's location/rotation/scale channels (including animation and drivers) and the effect of bone constraints"""
        ...
    matrix_basis: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3", "is_animatable=False"]
    """Alternative access to location/scale/rotation relative to the parent and own rest bone"""
    matrix: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]
    """Final 4×4 matrix after constraints and drivers are applied, in the armature object space"""
    @property
    def head(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Location of head of the channel's bone"""
        ...
    @property
    def tail(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:
        """Location of tail of the channel's bone"""
        ...
    @property
    def length(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Length of the bone"""
        ...
    @property
    def is_in_ik_chain(self) -> bool:
        """Is part of an IK chain"""
        ...
    lock_ik_x: bool
    """Disallow movement around the X axis"""
    lock_ik_y: bool
    """Disallow movement around the Y axis"""
    lock_ik_z: bool
    """Disallow movement around the Z axis"""
    use_ik_limit_x: bool
    """Limit movement around the X axis"""
    use_ik_limit_y: bool
    """Limit movement around the Y axis"""
    use_ik_limit_z: bool
    """Limit movement around the Z axis"""
    use_ik_rotation_control: bool
    """Apply channel rotation as IK constraint"""
    use_ik_linear_control: bool
    """Apply channel size as IK constraint if stretching is enabled"""
    ik_min_x: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Minimum angles for IK Limit"""
    ik_max_x: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Maximum angles for IK Limit"""
    ik_min_y: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Minimum angles for IK Limit"""
    ik_max_y: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Maximum angles for IK Limit"""
    ik_min_z: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Minimum angles for IK Limit"""
    ik_max_z: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Maximum angles for IK Limit"""
    ik_stiffness_x: Annotated[float, "step=10.0", "precision=3"]
    """IK stiffness around the X axis"""
    ik_stiffness_y: Annotated[float, "step=10.0", "precision=3"]
    """IK stiffness around the Y axis"""
    ik_stiffness_z: Annotated[float, "step=10.0", "precision=3"]
    """IK stiffness around the Z axis"""
    ik_stretch: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Allow scaling of the bone for IK"""
    ik_rotation_weight: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Weight of rotation constraint for IK"""
    ik_linear_weight: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Weight of scale constraint for IK"""
    custom_shape: Annotated[Optional['Object'], "is_animatable=False"]
    """Object that defines custom display shape for this bone"""
    custom_shape_scale_xyz: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Adjust the size of the custom shape"""
    custom_shape_translation: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=5"]
    """Adjust the location of the custom shape"""
    custom_shape_rotation_euler: Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=100.0", "precision=5"]
    """Adjust the rotation of the custom shape"""
    use_transform_at_custom_shape: bool
    """The location and orientation of the Custom Shape Transform bone will be used for transform gizmos and for other transform operators in the 3D Viewport. When disabled, the 3D Viewport will still use the actual bone transform for these, even when the custom bone shape transform is overridden."""
    use_transform_around_custom_shape: bool
    """Transform the bone as if it was a child of the Custom Shape Transform bone. This can be useful when combining shape-key and armature deformations."""
    use_custom_shape_bone_size: bool
    """Scale the custom object by the bone length"""
    hide: bool
    """Bone is not visible except for Edit Mode"""
    select: Annotated[bool, "is_animatable=False"]
    """Bone is selected in Pose Mode"""
    custom_shape_transform: Annotated[Optional['PoseBone'], "is_animatable=False"]
    """Bone that defines the display transform of this custom shape"""
    custom_shape_wire_width: Annotated[float, "step=1.0", "precision=1"]
    """Adjust the line thickness of custom shapes"""
    @property
    def color(self) -> Annotated[Optional['BoneColor'], "is_animatable=False"]:
        ...
    lock_location: list[bool]
    """Lock editing of location when transforming"""
    lock_rotation: list[bool]
    """Lock editing of rotation when transforming"""
    lock_rotation_w: bool
    """Lock editing of 'angle' component of four-component rotations when transforming"""
    lock_rotations_4d: bool
    """Lock editing of four component rotations by components (instead of as Eulers)"""
    lock_scale: list[bool]
    """Lock editing of scale when transforming"""
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def evaluate_envelope(self, *args, **kwargs) -> Any: ...
    def bbone_segment_index(self, *args, **kwargs) -> Any: ...
    def bbone_segment_matrix(self, *args, **kwargs) -> Any: ...
    def compute_bbone_handles(self, *args, **kwargs) -> Any: ...