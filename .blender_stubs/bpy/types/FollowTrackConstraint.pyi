# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FollowTrackConstraint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Constraint import Constraint
from .MovieClip import MovieClip
from .Object import Object

class FollowTrackConstraint(Constraint):

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
    def clip(self) -> Annotated[Optional['MovieClip'], "is_animatable=False"]:
        """Movie Clip to get tracking data from"""
        ...
    @clip.setter
    def clip(self, value: Annotated[Optional['MovieClip'], "is_animatable=False"]) -> None:
        ...
    @property
    def track(self) -> Annotated[str, "is_animatable=False"]:
        """Movie tracking track to follow"""
        ...
    @track.setter
    def track(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def use_active_clip(self) -> bool:
        """Use active clip defined in scene"""
        ...
    @use_active_clip.setter
    def use_active_clip(self, value: bool) -> None:
        ...
    @property
    def use_3d_position(self) -> bool:
        """Use 3D position of track to parent to"""
        ...
    @use_3d_position.setter
    def use_3d_position(self, value: bool) -> None:
        ...
    @property
    def object(self) -> Annotated[str, "is_animatable=False"]:
        """Movie tracking object to follow (if empty, camera object is used)"""
        ...
    @object.setter
    def object(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def camera(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Camera to which motion is parented (if empty active scene camera is used)"""
        ...
    @camera.setter
    def camera(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def depth_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object used to define depth in camera space by projecting onto surface of this object"""
        ...
    @depth_object.setter
    def depth_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def frame_method(self) -> Literal['STRETCH', 'FIT', 'CROP']:
        """How the footage fits in the camera frame"""
        ...
    @frame_method.setter
    def frame_method(self, value: Literal['STRETCH', 'FIT', 'CROP']) -> None:
        ...
    @property
    def use_undistorted_position(self) -> bool:
        """Parent to undistorted position of 2D track"""
        ...
    @use_undistorted_position.setter
    def use_undistorted_position(self, value: bool) -> None:
        ...