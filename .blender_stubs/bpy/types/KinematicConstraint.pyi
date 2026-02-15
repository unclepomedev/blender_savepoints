# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.KinematicConstraint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Constraint import Constraint
from .Object import Object

class KinematicConstraint(Constraint):

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
    target: Annotated[Optional['Object'], "is_animatable=False"]
    """Target object"""
    subtarget: Annotated[str, "is_animatable=False"]
    """Armature bone, mesh or lattice vertex group, ..."""
    iterations: Annotated[int, "step=1"]
    """Maximum number of solving iterations"""
    pole_target: Annotated[Optional['Object'], "is_animatable=False"]
    """Object for pole rotation"""
    pole_subtarget: Annotated[str, "is_animatable=False"]

    pole_angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=4"]
    """Pole rotation offset"""
    weight: Annotated[float, "step=10.0", "precision=3"]
    """For Tree-IK: Weight of position control for this target"""
    orient_weight: Annotated[float, "step=10.0", "precision=3"]
    """For Tree-IK: Weight of orientation control for this target"""
    chain_count: Annotated[int, "step=1", "is_animatable=False"]
    """How many bones are included in the IK effect - 0 uses all bones"""
    use_tail: bool
    """Include bone's tail as last element in chain"""
    reference_axis: Literal['BONE', 'TARGET']
    """Constraint axis Lock options relative to Bone or Target reference"""
    use_location: bool
    """Chain follows position of target"""
    lock_location_x: bool
    """Constraint position along X axis"""
    lock_location_y: bool
    """Constraint position along Y axis"""
    lock_location_z: bool
    """Constraint position along Z axis"""
    use_rotation: bool
    """Chain follows rotation of target"""
    lock_rotation_x: bool
    """Constraint rotation along X axis"""
    lock_rotation_y: bool
    """Constraint rotation along Y axis"""
    lock_rotation_z: bool
    """Constraint rotation along Z axis"""
    use_stretch: bool
    """Enable IK Stretching"""
    ik_type: Literal['COPY_POSE', 'DISTANCE']

    limit_mode: Literal['LIMITDIST_INSIDE', 'LIMITDIST_OUTSIDE', 'LIMITDIST_ONSURFACE']
    """Distances in relation to sphere of influence to allow"""
    distance: Annotated[float, "step=10.0", "precision=3"]
    """Radius of limiting sphere"""