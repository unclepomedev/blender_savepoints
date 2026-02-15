# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ActionConstraint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Constraint import Constraint
from .Action import Action
from .ActionSlot import ActionSlot
from .Object import Object
from .bpy_prop_collection import bpy_prop_collection

class ActionConstraint(Constraint):

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
    mix_mode: Literal['REPLACE', 'BEFORE_FULL', 'BEFORE', 'BEFORE_SPLIT', 'AFTER_FULL', 'AFTER', 'AFTER_SPLIT']
    """Specify how existing transformations and the action channels are combined"""
    transform_channel: Literal['LOCATION_X', 'LOCATION_Y', 'LOCATION_Z', 'ROTATION_X', 'ROTATION_Y', 'ROTATION_Z', 'SCALE_X', 'SCALE_Y', 'SCALE_Z']
    """Transformation channel from the target that is used to key the Action"""
    action: Annotated[Optional['Action'], "is_animatable=False"]
    """The constraining action"""
    action_slot_handle: Annotated[int, "step=1"]
    """A number that identifies which sub-set of the Action is considered to be for this Action Constraint"""
    last_slot_identifier: Annotated[str, "is_animatable=False"]
    """The identifier of the most recently assigned action slot. The slot identifies which sub-set of the Action is considered to be for this constraint, and its identifier is used to find the right slot when assigning an Action."""
    action_slot: Annotated[Optional['ActionSlot'], "is_animatable=False"]
    """The slot identifies which sub-set of the Action is considered to be for this strip, and its name is used to find the right slot when assigning another Action"""
    @property
    def action_suitable_slots(self) -> Annotated[bpy_prop_collection['ActionSlot'], "is_animatable=False"]:
        """The list of action slots suitable for this NLA strip"""
        ...
    use_bone_object_action: bool
    """Bones only: apply the object's transformation channels of the action to the constrained bone, instead of bone's channels"""
    frame_start: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """First frame of the Action to use"""
    frame_end: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """Last frame of the Action to use"""
    max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum value for target channel range"""
    min: Annotated[float, "step=10.0", "precision=3"]
    """Minimum value for target channel range"""
    eval_time: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Interpolates between Action Start and End frames"""
    use_eval_time: bool
    """Interpolate between Action Start and End frames, with the Evaluation Time slider instead of the Target object/bone"""