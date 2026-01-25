# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Constraint import Constraint
from .Action import Action
from .ActionSlot import ActionSlot
from .Object import Object
class ActionConstraint(Constraint):
    name: str
    type: str
    is_override_data: bool
    owner_space: str
    target_space: str
    space_object: 'Object'
    space_subtarget: str
    mute: bool
    enabled: bool
    show_expanded: bool
    is_valid: bool
    active: bool
    influence: float
    error_location: float
    error_rotation: float
    target: 'Object'
    subtarget: str
    mix_mode: str
    transform_channel: str
    action: 'Action'
    action_slot_handle: int
    last_slot_identifier: str
    action_slot: 'ActionSlot'
    action_suitable_slots: bpy_prop_collection['ActionSlot']
    use_bone_object_action: bool
    frame_start: int
    frame_end: int
    max: float
    min: float
    eval_time: float
    use_eval_time: bool