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
    def mix_mode(self) -> Literal['REPLACE', 'BEFORE_FULL', 'BEFORE', 'BEFORE_SPLIT', 'AFTER_FULL', 'AFTER', 'AFTER_SPLIT']:
        """Specify how existing transformations and the action channels are combined"""
        ...
    @mix_mode.setter
    def mix_mode(self, value: Literal['REPLACE', 'BEFORE_FULL', 'BEFORE', 'BEFORE_SPLIT', 'AFTER_FULL', 'AFTER', 'AFTER_SPLIT']):
        ...
    @property
    def transform_channel(self) -> Literal['LOCATION_X', 'LOCATION_Y', 'LOCATION_Z', 'ROTATION_X', 'ROTATION_Y', 'ROTATION_Z', 'SCALE_X', 'SCALE_Y', 'SCALE_Z']:
        """Transformation channel from the target that is used to key the Action"""
        ...
    @transform_channel.setter
    def transform_channel(self, value: Literal['LOCATION_X', 'LOCATION_Y', 'LOCATION_Z', 'ROTATION_X', 'ROTATION_Y', 'ROTATION_Z', 'SCALE_X', 'SCALE_Y', 'SCALE_Z']):
        ...
    @property
    def action(self) -> Annotated[Optional['Action'], "is_animatable=False"]:
        """The constraining action"""
        ...
    @action.setter
    def action(self, value: Annotated[Optional['Action'], "is_animatable=False"]):
        ...
    @property
    def action_slot_handle(self) -> Annotated[int, "step=1"]:
        """A number that identifies which sub-set of the Action is considered to be for this Action Constraint"""
        ...
    @action_slot_handle.setter
    def action_slot_handle(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def last_slot_identifier(self) -> Annotated[str, "is_animatable=False"]:
        """The identifier of the most recently assigned action slot. The slot identifies which sub-set of the Action is considered to be for this constraint, and its identifier is used to find the right slot when assigning an Action."""
        ...
    @last_slot_identifier.setter
    def last_slot_identifier(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def action_slot(self) -> Annotated[Optional['ActionSlot'], "is_animatable=False"]:
        """The slot identifies which sub-set of the Action is considered to be for this strip, and its name is used to find the right slot when assigning another Action"""
        ...
    @action_slot.setter
    def action_slot(self, value: Annotated[Optional['ActionSlot'], "is_animatable=False"]):
        ...
    @property
    def action_suitable_slots(self) -> Annotated[bpy_prop_collection['ActionSlot'], "is_animatable=False"]:
        """The list of action slots suitable for this NLA strip"""
        ...
    @property
    def use_bone_object_action(self) -> bool:
        """Bones only: apply the object's transformation channels of the action to the constrained bone, instead of bone's channels"""
        ...
    @use_bone_object_action.setter
    def use_bone_object_action(self, value: bool):
        ...
    @property
    def frame_start(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """First frame of the Action to use"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]):
        ...
    @property
    def frame_end(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """Last frame of the Action to use"""
        ...
    @frame_end.setter
    def frame_end(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]):
        ...
    @property
    def max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum value for target channel range"""
        ...
    @max.setter
    def max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def min(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Minimum value for target channel range"""
        ...
    @min.setter
    def min(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def eval_time(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Interpolates between Action Start and End frames"""
        ...
    @eval_time.setter
    def eval_time(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_eval_time(self) -> bool:
        """Interpolate between Action Start and End frames, with the Evaluation Time slider instead of the Target object/bone"""
        ...
    @use_eval_time.setter
    def use_eval_time(self, value: bool):
        ...