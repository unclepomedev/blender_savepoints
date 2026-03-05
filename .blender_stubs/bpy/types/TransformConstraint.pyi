# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.TransformConstraint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Constraint import Constraint
from .Object import Object

class TransformConstraint(Constraint):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Constraint name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def type(self) -> Literal['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'ARMATURE', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'GEOMETRY_ATTRIBUTE', 'PIVOT', 'SHRINKWRAP']:

        ...
    @property
    def is_override_data(self) -> bool:
        """In a local override object, whether this constraint comes from the linked reference object, or is local to the override"""
        ...
    @property
    def owner_space(self) -> Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']:
        """Space that owner is evaluated in"""
        ...
    @owner_space.setter
    def owner_space(self, value: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']) -> None:
        ...
    @property
    def target_space(self) -> Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL', 'LOCAL_OWNER_ORIENT']:
        """Space that target is evaluated in"""
        ...
    @target_space.setter
    def target_space(self, value: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL', 'LOCAL_OWNER_ORIENT']) -> None:
        ...
    @property
    def space_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object for Custom Space"""
        ...
    @space_object.setter
    def space_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def space_subtarget(self) -> Annotated[str, "is_animatable=False"]:
        """Armature bone, mesh or lattice vertex group, ..."""
        ...
    @space_subtarget.setter
    def space_subtarget(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def mute(self) -> bool:
        """Enable/Disable Constraint"""
        ...
    @mute.setter
    def mute(self, value: bool) -> None:
        ...
    @property
    def enabled(self) -> bool:
        """Use the results of this constraint"""
        ...
    @enabled.setter
    def enabled(self, value: bool) -> None:
        ...
    @property
    def show_expanded(self) -> bool:
        """Constraint's panel is expanded in UI"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool) -> None:
        ...
    @property
    def is_valid(self) -> bool:
        """Constraint has valid settings and can be evaluated"""
        ...
    @property
    def active(self) -> bool:
        """Constraint is the one being edited"""
        ...
    @active.setter
    def active(self, value: bool) -> None:
        ...
    @property
    def influence(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of influence constraint will have on the final solution"""
        ...
    @influence.setter
    def influence(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def error_location(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of residual error in Blender space unit for constraints that work on position"""
        ...
    @property
    def error_rotation(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of residual error in radians for constraints that work on orientation"""
        ...
    @property
    def target(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Target object"""
        ...
    @target.setter
    def target(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def subtarget(self) -> Annotated[str, "is_animatable=False"]:
        """Armature bone, mesh or lattice vertex group, ..."""
        ...
    @subtarget.setter
    def subtarget(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def map_from(self) -> Literal['LOCATION', 'ROTATION', 'SCALE']:
        """The transformation type to use from the target"""
        ...
    @map_from.setter
    def map_from(self, value: Literal['LOCATION', 'ROTATION', 'SCALE']) -> None:
        ...
    @property
    def map_to(self) -> Literal['LOCATION', 'ROTATION', 'SCALE']:
        """The transformation type to affect on the constrained object"""
        ...
    @map_to.setter
    def map_to(self, value: Literal['LOCATION', 'ROTATION', 'SCALE']) -> None:
        ...
    @property
    def map_to_x_from(self) -> Literal['X', 'Y', 'Z']:
        """The source axis constrained object's X axis uses"""
        ...
    @map_to_x_from.setter
    def map_to_x_from(self, value: Literal['X', 'Y', 'Z']) -> None:
        ...
    @property
    def map_to_y_from(self) -> Literal['X', 'Y', 'Z']:
        """The source axis constrained object's Y axis uses"""
        ...
    @map_to_y_from.setter
    def map_to_y_from(self, value: Literal['X', 'Y', 'Z']) -> None:
        ...
    @property
    def map_to_z_from(self) -> Literal['X', 'Y', 'Z']:
        """The source axis constrained object's Z axis uses"""
        ...
    @map_to_z_from.setter
    def map_to_z_from(self, value: Literal['X', 'Y', 'Z']) -> None:
        ...
    @property
    def use_motion_extrapolate(self) -> bool:
        """Extrapolate ranges"""
        ...
    @use_motion_extrapolate.setter
    def use_motion_extrapolate(self, value: bool) -> None:
        ...
    @property
    def from_rotation_mode(self) -> Literal['AUTO', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'QUATERNION', 'SWING_TWIST_X', 'SWING_TWIST_Y', 'SWING_TWIST_Z']:
        """Specify the type of rotation channels to use"""
        ...
    @from_rotation_mode.setter
    def from_rotation_mode(self, value: Literal['AUTO', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'QUATERNION', 'SWING_TWIST_X', 'SWING_TWIST_Y', 'SWING_TWIST_Z']) -> None:
        ...
    @property
    def to_euler_order(self) -> Literal['AUTO', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']:
        """Explicitly specify the output euler rotation order"""
        ...
    @to_euler_order.setter
    def to_euler_order(self, value: Literal['AUTO', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']) -> None:
        ...
    @property
    def from_min_x(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Bottom range of X axis source motion"""
        ...
    @from_min_x.setter
    def from_min_x(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_min_y(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Bottom range of Y axis source motion"""
        ...
    @from_min_y.setter
    def from_min_y(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_min_z(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Bottom range of Z axis source motion"""
        ...
    @from_min_z.setter
    def from_min_z(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_max_x(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Top range of X axis source motion"""
        ...
    @from_max_x.setter
    def from_max_x(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_max_y(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Top range of Y axis source motion"""
        ...
    @from_max_y.setter
    def from_max_y(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_max_z(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Top range of Z axis source motion"""
        ...
    @from_max_z.setter
    def from_max_z(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_min_x(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Bottom range of X axis destination motion"""
        ...
    @to_min_x.setter
    def to_min_x(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_min_y(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Bottom range of Y axis destination motion"""
        ...
    @to_min_y.setter
    def to_min_y(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_min_z(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Bottom range of Z axis destination motion"""
        ...
    @to_min_z.setter
    def to_min_z(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_max_x(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Top range of X axis destination motion"""
        ...
    @to_max_x.setter
    def to_max_x(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_max_y(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Top range of Y axis destination motion"""
        ...
    @to_max_y.setter
    def to_max_y(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_max_z(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Top range of Z axis destination motion"""
        ...
    @to_max_z.setter
    def to_max_z(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def mix_mode(self) -> Literal['REPLACE', 'ADD']:
        """Specify how to combine the new location with original"""
        ...
    @mix_mode.setter
    def mix_mode(self, value: Literal['REPLACE', 'ADD']) -> None:
        ...
    @property
    def from_min_x_rot(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Bottom range of X axis source motion"""
        ...
    @from_min_x_rot.setter
    def from_min_x_rot(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_min_y_rot(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Bottom range of Y axis source motion"""
        ...
    @from_min_y_rot.setter
    def from_min_y_rot(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_min_z_rot(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Bottom range of Z axis source motion"""
        ...
    @from_min_z_rot.setter
    def from_min_z_rot(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_max_x_rot(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Top range of X axis source motion"""
        ...
    @from_max_x_rot.setter
    def from_max_x_rot(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_max_y_rot(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Top range of Y axis source motion"""
        ...
    @from_max_y_rot.setter
    def from_max_y_rot(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_max_z_rot(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Top range of Z axis source motion"""
        ...
    @from_max_z_rot.setter
    def from_max_z_rot(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_min_x_rot(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Bottom range of X axis destination motion"""
        ...
    @to_min_x_rot.setter
    def to_min_x_rot(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_min_y_rot(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Bottom range of Y axis destination motion"""
        ...
    @to_min_y_rot.setter
    def to_min_y_rot(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_min_z_rot(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Bottom range of Z axis destination motion"""
        ...
    @to_min_z_rot.setter
    def to_min_z_rot(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_max_x_rot(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Top range of X axis destination motion"""
        ...
    @to_max_x_rot.setter
    def to_max_x_rot(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_max_y_rot(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Top range of Y axis destination motion"""
        ...
    @to_max_y_rot.setter
    def to_max_y_rot(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_max_z_rot(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Top range of Z axis destination motion"""
        ...
    @to_max_z_rot.setter
    def to_max_z_rot(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def mix_mode_rot(self) -> Literal['REPLACE', 'ADD', 'BEFORE', 'AFTER']:
        """Specify how to combine the new rotation with original"""
        ...
    @mix_mode_rot.setter
    def mix_mode_rot(self, value: Literal['REPLACE', 'ADD', 'BEFORE', 'AFTER']) -> None:
        ...
    @property
    def from_min_x_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Bottom range of X axis source motion"""
        ...
    @from_min_x_scale.setter
    def from_min_x_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_min_y_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Bottom range of Y axis source motion"""
        ...
    @from_min_y_scale.setter
    def from_min_y_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_min_z_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Bottom range of Z axis source motion"""
        ...
    @from_min_z_scale.setter
    def from_min_z_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_max_x_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Top range of X axis source motion"""
        ...
    @from_max_x_scale.setter
    def from_max_x_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_max_y_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Top range of Y axis source motion"""
        ...
    @from_max_y_scale.setter
    def from_max_y_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def from_max_z_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Top range of Z axis source motion"""
        ...
    @from_max_z_scale.setter
    def from_max_z_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_min_x_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Bottom range of X axis destination motion"""
        ...
    @to_min_x_scale.setter
    def to_min_x_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_min_y_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Bottom range of Y axis destination motion"""
        ...
    @to_min_y_scale.setter
    def to_min_y_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_min_z_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Bottom range of Z axis destination motion"""
        ...
    @to_min_z_scale.setter
    def to_min_z_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_max_x_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Top range of X axis destination motion"""
        ...
    @to_max_x_scale.setter
    def to_max_x_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_max_y_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Top range of Y axis destination motion"""
        ...
    @to_max_y_scale.setter
    def to_max_y_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def to_max_z_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Top range of Z axis destination motion"""
        ...
    @to_max_z_scale.setter
    def to_max_z_scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def mix_mode_scale(self) -> Literal['REPLACE', 'MULTIPLY']:
        """Specify how to combine the new scale with original"""
        ...
    @mix_mode_scale.setter
    def mix_mode_scale(self, value: Literal['REPLACE', 'MULTIPLY']) -> None:
        ...