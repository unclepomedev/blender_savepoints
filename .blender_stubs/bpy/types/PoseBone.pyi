# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PoseBone.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from ._GenericBone import _GenericBone
from .Bone import Bone
from .BoneColor import BoneColor
from .Constraint import Constraint
from .MotionPath import MotionPath
from .Object import Object
from .PoseBoneConstraints import PoseBoneConstraints
from .bpy_prop_collection import bpy_prop_collection

class PoseBone(bpy_struct, _GenericBone):

    @property
    def constraints(self) -> Annotated['PoseBoneConstraints', "is_animatable=False"]:
        """Constraints that act on this pose channel"""
        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
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
    @property
    def location(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]:

        ...
    @location.setter
    def location(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def scale(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:

        ...
    @scale.setter
    def scale(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def rotation_quaternion(self) -> Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]:
        """Rotation in Quaternions"""
        ...
    @rotation_quaternion.setter
    def rotation_quaternion(self, value: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def rotation_axis_angle(self) -> Annotated[list[float], "subtype='AXISANGLE'", "step=10.0", "precision=3"]:
        """Angle of Rotation for Axis-Angle rotation representation"""
        ...
    @rotation_axis_angle.setter
    def rotation_axis_angle(self, value: Annotated[list[float], "subtype='AXISANGLE'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def rotation_euler(self) -> Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=100.0", "precision=5"]:
        """Rotation in Eulers"""
        ...
    @rotation_euler.setter
    def rotation_euler(self, value: Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=100.0", "precision=5"]) -> None:
        ...
    @property
    def rotation_mode(self) -> Literal['QUATERNION', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'AXIS_ANGLE']:
        """The kind of rotation to apply, values from other rotation modes are not used"""
        ...
    @rotation_mode.setter
    def rotation_mode(self, value: Literal['QUATERNION', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'AXIS_ANGLE']) -> None:
        ...
    @property
    def bbone_rollin(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2"]:
        """Roll offset for the start of the B-Bone, adjusts twist"""
        ...
    @bbone_rollin.setter
    def bbone_rollin(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2"]) -> None:
        ...
    @property
    def bbone_rollout(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2"]:
        """Roll offset for the end of the B-Bone, adjusts twist"""
        ...
    @bbone_rollout.setter
    def bbone_rollout(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=2"]) -> None:
        ...
    @property
    def bbone_curveinx(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """X-axis handle offset for start of the B-Bone's curve, adjusts curvature"""
        ...
    @bbone_curveinx.setter
    def bbone_curveinx(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def bbone_curveinz(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """Z-axis handle offset for start of the B-Bone's curve, adjusts curvature"""
        ...
    @bbone_curveinz.setter
    def bbone_curveinz(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def bbone_curveoutx(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """X-axis handle offset for end of the B-Bone's curve, adjusts curvature"""
        ...
    @bbone_curveoutx.setter
    def bbone_curveoutx(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def bbone_curveoutz(self) -> Annotated[float, "step=1.0", "precision=5"]:
        """Z-axis handle offset for end of the B-Bone's curve, adjusts curvature"""
        ...
    @bbone_curveoutz.setter
    def bbone_curveoutz(self, value: Annotated[float, "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def bbone_easein(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Length of first Bézier Handle (for B-Bones only)"""
        ...
    @bbone_easein.setter
    def bbone_easein(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def bbone_easeout(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Length of second Bézier Handle (for B-Bones only)"""
        ...
    @bbone_easeout.setter
    def bbone_easeout(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def bbone_scalein(self) -> Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]:
        """Scale factors for the start of the B-Bone, adjusts thickness (for tapering effects)"""
        ...
    @bbone_scalein.setter
    def bbone_scalein(self, value: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def bbone_scaleout(self) -> Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]:
        """Scale factors for the end of the B-Bone, adjusts thickness (for tapering effects)"""
        ...
    @bbone_scaleout.setter
    def bbone_scaleout(self, value: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]) -> None:
        ...
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
    @property
    def matrix_basis(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Alternative access to location/scale/rotation relative to the parent and own rest bone"""
        ...
    @matrix_basis.setter
    def matrix_basis(self, value: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def matrix(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]:
        """Final 4×4 matrix after constraints and drivers are applied, in the armature object space"""
        ...
    @matrix.setter
    def matrix(self, value: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]) -> None:
        ...
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
    @property
    def lock_ik_x(self) -> bool:
        """Disallow movement around the X axis"""
        ...
    @lock_ik_x.setter
    def lock_ik_x(self, value: bool) -> None:
        ...
    @property
    def lock_ik_y(self) -> bool:
        """Disallow movement around the Y axis"""
        ...
    @lock_ik_y.setter
    def lock_ik_y(self, value: bool) -> None:
        ...
    @property
    def lock_ik_z(self) -> bool:
        """Disallow movement around the Z axis"""
        ...
    @lock_ik_z.setter
    def lock_ik_z(self, value: bool) -> None:
        ...
    @property
    def use_ik_limit_x(self) -> bool:
        """Limit movement around the X axis"""
        ...
    @use_ik_limit_x.setter
    def use_ik_limit_x(self, value: bool) -> None:
        ...
    @property
    def use_ik_limit_y(self) -> bool:
        """Limit movement around the Y axis"""
        ...
    @use_ik_limit_y.setter
    def use_ik_limit_y(self, value: bool) -> None:
        ...
    @property
    def use_ik_limit_z(self) -> bool:
        """Limit movement around the Z axis"""
        ...
    @use_ik_limit_z.setter
    def use_ik_limit_z(self, value: bool) -> None:
        ...
    @property
    def use_ik_rotation_control(self) -> bool:
        """Apply channel rotation as IK constraint"""
        ...
    @use_ik_rotation_control.setter
    def use_ik_rotation_control(self, value: bool) -> None:
        ...
    @property
    def use_ik_linear_control(self) -> bool:
        """Apply channel size as IK constraint if stretching is enabled"""
        ...
    @use_ik_linear_control.setter
    def use_ik_linear_control(self, value: bool) -> None:
        ...
    @property
    def ik_min_x(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Minimum angles for IK Limit"""
        ...
    @ik_min_x.setter
    def ik_min_x(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def ik_max_x(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Maximum angles for IK Limit"""
        ...
    @ik_max_x.setter
    def ik_max_x(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def ik_min_y(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Minimum angles for IK Limit"""
        ...
    @ik_min_y.setter
    def ik_min_y(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def ik_max_y(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Maximum angles for IK Limit"""
        ...
    @ik_max_y.setter
    def ik_max_y(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def ik_min_z(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Minimum angles for IK Limit"""
        ...
    @ik_min_z.setter
    def ik_min_z(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def ik_max_z(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Maximum angles for IK Limit"""
        ...
    @ik_max_z.setter
    def ik_max_z(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def ik_stiffness_x(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """IK stiffness around the X axis"""
        ...
    @ik_stiffness_x.setter
    def ik_stiffness_x(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def ik_stiffness_y(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """IK stiffness around the Y axis"""
        ...
    @ik_stiffness_y.setter
    def ik_stiffness_y(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def ik_stiffness_z(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """IK stiffness around the Z axis"""
        ...
    @ik_stiffness_z.setter
    def ik_stiffness_z(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def ik_stretch(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Allow scaling of the bone for IK"""
        ...
    @ik_stretch.setter
    def ik_stretch(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def ik_rotation_weight(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Weight of rotation constraint for IK"""
        ...
    @ik_rotation_weight.setter
    def ik_rotation_weight(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def ik_linear_weight(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Weight of scale constraint for IK"""
        ...
    @ik_linear_weight.setter
    def ik_linear_weight(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def custom_shape(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object that defines custom display shape for this bone"""
        ...
    @custom_shape.setter
    def custom_shape(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def custom_shape_scale_xyz(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Adjust the size of the custom shape"""
        ...
    @custom_shape_scale_xyz.setter
    def custom_shape_scale_xyz(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def custom_shape_translation(self) -> Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=5"]:
        """Adjust the location of the custom shape"""
        ...
    @custom_shape_translation.setter
    def custom_shape_translation(self, value: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=5"]) -> None:
        ...
    @property
    def custom_shape_rotation_euler(self) -> Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=100.0", "precision=5"]:
        """Adjust the rotation of the custom shape"""
        ...
    @custom_shape_rotation_euler.setter
    def custom_shape_rotation_euler(self, value: Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=100.0", "precision=5"]) -> None:
        ...
    @property
    def use_transform_at_custom_shape(self) -> bool:
        """The location and orientation of the Custom Shape Transform bone will be used for transform gizmos and for other transform operators in the 3D Viewport. When disabled, the 3D Viewport will still use the actual bone transform for these, even when the custom bone shape transform is overridden."""
        ...
    @use_transform_at_custom_shape.setter
    def use_transform_at_custom_shape(self, value: bool) -> None:
        ...
    @property
    def use_transform_around_custom_shape(self) -> bool:
        """Transform the bone as if it was a child of the Custom Shape Transform bone. This can be useful when combining shape-key and armature deformations."""
        ...
    @use_transform_around_custom_shape.setter
    def use_transform_around_custom_shape(self, value: bool) -> None:
        ...
    @property
    def use_custom_shape_bone_size(self) -> bool:
        """Scale the custom object by the bone length"""
        ...
    @use_custom_shape_bone_size.setter
    def use_custom_shape_bone_size(self, value: bool) -> None:
        ...
    @property
    def hide(self) -> bool:
        """Bone is not visible except for Edit Mode"""
        ...
    @hide.setter
    def hide(self, value: bool) -> None:
        ...
    @property
    def select(self) -> Annotated[bool, "is_animatable=False"]:
        """Bone is selected in Pose Mode"""
        ...
    @select.setter
    def select(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def custom_shape_transform(self) -> Annotated[Optional['PoseBone'], "is_animatable=False"]:
        """Bone that defines the display transform of this custom shape"""
        ...
    @custom_shape_transform.setter
    def custom_shape_transform(self, value: Annotated[Optional['PoseBone'], "is_animatable=False"]) -> None:
        ...
    @property
    def custom_shape_wire_width(self) -> Annotated[float, "step=1.0", "precision=1"]:
        """Adjust the line thickness of custom shapes"""
        ...
    @custom_shape_wire_width.setter
    def custom_shape_wire_width(self, value: Annotated[float, "step=1.0", "precision=1"]) -> None:
        ...
    @property
    def color(self) -> Annotated[Optional['BoneColor'], "is_animatable=False"]:

        ...
    @property
    def lock_location(self) -> list[bool]:
        """Lock editing of location when transforming"""
        ...
    @lock_location.setter
    def lock_location(self, value: list[bool]) -> None:
        ...
    @property
    def lock_rotation(self) -> list[bool]:
        """Lock editing of rotation when transforming"""
        ...
    @lock_rotation.setter
    def lock_rotation(self, value: list[bool]) -> None:
        ...
    @property
    def lock_rotation_w(self) -> bool:
        """Lock editing of 'angle' component of four-component rotations when transforming"""
        ...
    @lock_rotation_w.setter
    def lock_rotation_w(self, value: bool) -> None:
        ...
    @property
    def lock_rotations_4d(self) -> bool:
        """Lock editing of four component rotations by components (instead of as Eulers)"""
        ...
    @lock_rotations_4d.setter
    def lock_rotations_4d(self, value: bool) -> None:
        ...
    @property
    def lock_scale(self) -> list[bool]:
        """Lock editing of scale when transforming"""
        ...
    @lock_scale.setter
    def lock_scale(self, value: list[bool]) -> None:
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def evaluate_envelope(self, *args, **kwargs) -> Any: ...
    def bbone_segment_index(self, *args, **kwargs) -> Any: ...
    def bbone_segment_matrix(self, *args, **kwargs) -> Any: ...
    def compute_bbone_handles(self, *args, **kwargs) -> Any: ...