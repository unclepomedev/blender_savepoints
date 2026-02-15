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

    name: Annotated[str, "is_animatable=False"]
    """Constraint name"""
    @property
    def type(self) -> Literal['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'ARMATURE', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'GEOMETRY_ATTRIBUTE', 'PIVOT', 'SHRINKWRAP']:

        ...
    @property
    def is_override_data(self) -> bool:
        """In a local override object, whether this constraint comes from the linked reference object, or is local to the override"""
        ...
    owner_space: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL']
    """Space that owner is evaluated in"""
    target_space: Literal['WORLD', 'CUSTOM', 'POSE', 'LOCAL_WITH_PARENT', 'LOCAL', 'LOCAL_OWNER_ORIENT']
    """Space that target is evaluated in"""
    space_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Object for Custom Space"""
    space_subtarget: Annotated[str, "is_animatable=False"]
    """Armature bone, mesh or lattice vertex group, ..."""
    mute: bool
    """Enable/Disable Constraint"""
    enabled: bool
    """Use the results of this constraint"""
    show_expanded: bool
    """Constraint's panel is expanded in UI"""
    @property
    def is_valid(self) -> bool:
        """Constraint has valid settings and can be evaluated"""
        ...
    active: bool
    """Constraint is the one being edited"""
    influence: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of influence constraint will have on the final solution"""
    @property
    def error_location(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of residual error in Blender space unit for constraints that work on position"""
        ...
    @property
    def error_rotation(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of residual error in radians for constraints that work on orientation"""
        ...
    clip: Annotated[Optional['MovieClip'], "is_animatable=False"]
    """Movie Clip to get tracking data from"""
    track: Annotated[str, "is_animatable=False"]
    """Movie tracking track to follow"""
    use_active_clip: bool
    """Use active clip defined in scene"""
    use_3d_position: bool
    """Use 3D position of track to parent to"""
    object: Annotated[str, "is_animatable=False"]
    """Movie tracking object to follow (if empty, camera object is used)"""
    camera: Annotated[Optional['Object'], "is_animatable=False"]
    """Camera to which motion is parented (if empty active scene camera is used)"""
    depth_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Object used to define depth in camera space by projecting onto surface of this object"""
    frame_method: Literal['STRETCH', 'FIT', 'CROP']
    """How the footage fits in the camera frame"""
    use_undistorted_position: bool
    """Parent to undistorted position of 2D track"""