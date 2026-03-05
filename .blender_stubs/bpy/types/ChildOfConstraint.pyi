# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ChildOfConstraint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Constraint import Constraint
from .Object import Object

class ChildOfConstraint(Constraint):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Constraint name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
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
    def owner_space(self, value: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']):
        ...
    @property
    def target_space(self) -> Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL', 'LOCAL_OWNER_ORIENT']:
        """Space that target is evaluated in"""
        ...
    @target_space.setter
    def target_space(self, value: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL', 'LOCAL_OWNER_ORIENT']):
        ...
    @property
    def space_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object for Custom Space"""
        ...
    @space_object.setter
    def space_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def space_subtarget(self) -> Annotated[str, "is_animatable=False"]:
        """Armature bone, mesh or lattice vertex group, ..."""
        ...
    @space_subtarget.setter
    def space_subtarget(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def mute(self) -> bool:
        """Enable/Disable Constraint"""
        ...
    @mute.setter
    def mute(self, value: bool):
        ...
    @property
    def enabled(self) -> bool:
        """Use the results of this constraint"""
        ...
    @enabled.setter
    def enabled(self, value: bool):
        ...
    @property
    def show_expanded(self) -> bool:
        """Constraint's panel is expanded in UI"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool):
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
    def active(self, value: bool):
        ...
    @property
    def influence(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of influence constraint will have on the final solution"""
        ...
    @influence.setter
    def influence(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
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
    def target(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def subtarget(self) -> Annotated[str, "is_animatable=False"]:
        """Armature bone, mesh or lattice vertex group, ..."""
        ...
    @subtarget.setter
    def subtarget(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def use_location_x(self) -> bool:
        """Use X Location of Parent"""
        ...
    @use_location_x.setter
    def use_location_x(self, value: bool):
        ...
    @property
    def use_location_y(self) -> bool:
        """Use Y Location of Parent"""
        ...
    @use_location_y.setter
    def use_location_y(self, value: bool):
        ...
    @property
    def use_location_z(self) -> bool:
        """Use Z Location of Parent"""
        ...
    @use_location_z.setter
    def use_location_z(self, value: bool):
        ...
    @property
    def use_rotation_x(self) -> bool:
        """Use X Rotation of Parent"""
        ...
    @use_rotation_x.setter
    def use_rotation_x(self, value: bool):
        ...
    @property
    def use_rotation_y(self) -> bool:
        """Use Y Rotation of Parent"""
        ...
    @use_rotation_y.setter
    def use_rotation_y(self, value: bool):
        ...
    @property
    def use_rotation_z(self) -> bool:
        """Use Z Rotation of Parent"""
        ...
    @use_rotation_z.setter
    def use_rotation_z(self, value: bool):
        ...
    @property
    def use_scale_x(self) -> bool:
        """Use X Scale of Parent"""
        ...
    @use_scale_x.setter
    def use_scale_x(self, value: bool):
        ...
    @property
    def use_scale_y(self) -> bool:
        """Use Y Scale of Parent"""
        ...
    @use_scale_y.setter
    def use_scale_y(self, value: bool):
        ...
    @property
    def use_scale_z(self) -> bool:
        """Use Z Scale of Parent"""
        ...
    @use_scale_z.setter
    def use_scale_z(self, value: bool):
        ...
    @property
    def set_inverse_pending(self) -> bool:
        """Set to true to request recalculation of the inverse matrix"""
        ...
    @set_inverse_pending.setter
    def set_inverse_pending(self, value: bool):
        ...
    @property
    def inverse_matrix(self) -> Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Transformation matrix to apply before"""
        ...
    @inverse_matrix.setter
    def inverse_matrix(self, value: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...