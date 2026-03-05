# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.StretchToConstraint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Constraint import Constraint
from .Object import Object

class StretchToConstraint(Constraint):

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
    def head_tail(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Target along length of bone: Head is 0, Tail is 1"""
        ...
    @head_tail.setter
    def head_tail(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_bbone_shape(self) -> bool:
        """Follow shape of B-Bone segments when calculating Head/Tail position"""
        ...
    @use_bbone_shape.setter
    def use_bbone_shape(self, value: bool) -> None:
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
    def volume(self) -> Literal['VOLUME_XZX', 'VOLUME_X', 'VOLUME_Z', 'NO_VOLUME']:
        """Maintain the object's volume as it stretches"""
        ...
    @volume.setter
    def volume(self, value: Literal['VOLUME_XZX', 'VOLUME_X', 'VOLUME_Z', 'NO_VOLUME']) -> None:
        ...
    @property
    def keep_axis(self) -> Literal['PLANE_X', 'PLANE_Z', 'SWING_Y']:
        """The rotation type and axis order to use"""
        ...
    @keep_axis.setter
    def keep_axis(self, value: Literal['PLANE_X', 'PLANE_Z', 'SWING_Y']) -> None:
        ...
    @property
    def rest_length(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=5"]:
        """Length at rest position"""
        ...
    @rest_length.setter
    def rest_length(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=5"]) -> None:
        ...
    @property
    def bulge(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Factor between volume variation and stretching"""
        ...
    @bulge.setter
    def bulge(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_bulge_min(self) -> bool:
        """Use lower limit for volume variation"""
        ...
    @use_bulge_min.setter
    def use_bulge_min(self, value: bool) -> None:
        ...
    @property
    def use_bulge_max(self) -> bool:
        """Use upper limit for volume variation"""
        ...
    @use_bulge_max.setter
    def use_bulge_max(self, value: bool) -> None:
        ...
    @property
    def bulge_min(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Minimum volume stretching factor"""
        ...
    @bulge_min.setter
    def bulge_min(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def bulge_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum volume stretching factor"""
        ...
    @bulge_max.setter
    def bulge_max(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def bulge_smooth(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Strength of volume stretching clamping"""
        ...
    @bulge_smooth.setter
    def bulge_smooth(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...