# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LimitScaleConstraint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Constraint import Constraint
from .Object import Object

class LimitScaleConstraint(Constraint):

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
    def use_min_x(self) -> bool:
        """Use the minimum X value"""
        ...
    @use_min_x.setter
    def use_min_x(self, value: bool) -> None:
        ...
    @property
    def use_min_y(self) -> bool:
        """Use the minimum Y value"""
        ...
    @use_min_y.setter
    def use_min_y(self, value: bool) -> None:
        ...
    @property
    def use_min_z(self) -> bool:
        """Use the minimum Z value"""
        ...
    @use_min_z.setter
    def use_min_z(self, value: bool) -> None:
        ...
    @property
    def use_max_x(self) -> bool:
        """Use the maximum X value"""
        ...
    @use_max_x.setter
    def use_max_x(self, value: bool) -> None:
        ...
    @property
    def use_max_y(self) -> bool:
        """Use the maximum Y value"""
        ...
    @use_max_y.setter
    def use_max_y(self, value: bool) -> None:
        ...
    @property
    def use_max_z(self) -> bool:
        """Use the maximum Z value"""
        ...
    @use_max_z.setter
    def use_max_z(self, value: bool) -> None:
        ...
    @property
    def min_x(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Lowest X value to allow"""
        ...
    @min_x.setter
    def min_x(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def min_y(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Lowest Y value to allow"""
        ...
    @min_y.setter
    def min_y(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def min_z(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Lowest Z value to allow"""
        ...
    @min_z.setter
    def min_z(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def max_x(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Highest X value to allow"""
        ...
    @max_x.setter
    def max_x(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def max_y(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Highest Y value to allow"""
        ...
    @max_y.setter
    def max_y(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def max_z(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Highest Z value to allow"""
        ...
    @max_z.setter
    def max_z(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_transform_limit(self) -> bool:
        """Transform tools are affected by this constraint as well"""
        ...
    @use_transform_limit.setter
    def use_transform_limit(self, value: bool) -> None:
        ...