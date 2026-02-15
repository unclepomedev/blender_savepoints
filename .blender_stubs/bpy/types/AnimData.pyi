# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Action import Action
from .ActionSlot import ActionSlot
from .AnimDataDrivers import AnimDataDrivers
from .FCurve import FCurve
from .NlaTrack import NlaTrack
from .NlaTracks import NlaTracks
class AnimData(bpy_struct):
    @property
    def nla_tracks(self) -> Annotated['NlaTracks', "is_animatable=False"]:
        """NLA Tracks (i.e. Animation Layers)"""
        ...
    action: Annotated[Optional['Action'], "is_animatable=False"]
    """Active Action for this data-block"""
    action_extrapolation: Literal['NOTHING', 'HOLD', 'HOLD_FORWARD']
    """Action to take for gaps past the Active Action's range (when evaluating with NLA)"""
    action_blend_type: Literal['REPLACE', 'COMBINE', 'ADD', 'SUBTRACT', 'MULTIPLY']
    """Method used for combining Active Action's result with result of NLA stack"""
    action_influence: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount the Active Action contributes to the result of the NLA stack"""
    action_tweak_storage: Annotated[Optional['Action'], "is_animatable=False"]
    """Storage to temporarily hold the main action while in tweak mode"""
    action_slot_handle_tweak_storage: Annotated[int, "step=1"]
    """Storage to temporarily hold the main action slot while in tweak mode"""
    @property
    def drivers(self) -> Annotated['AnimDataDrivers', "is_animatable=False"]:
        """The Drivers/Expressions for this data-block"""
        ...
    use_nla: bool
    """NLA stack is evaluated when evaluating this block"""
    use_tweak_mode: bool
    """Whether to enable or disable tweak mode in NLA"""
    use_pin: bool
    action_slot_handle: Annotated[int, "step=1"]
    """A number that identifies which sub-set of the Action is considered to be for this data-block"""
    last_slot_identifier: Annotated[str, "is_animatable=False"]
    """The identifier of the most recently assigned action slot. The slot identifies which sub-set of the Action is considered to be for this data-block, and its identifier is used to find the right slot when assigning an Action."""
    action_slot: Annotated[Optional['ActionSlot'], "is_animatable=False"]
    """The slot identifies which sub-set of the Action is considered to be for this data-block, and its name is used to find the right slot when assigning an Action"""
    @property
    def action_suitable_slots(self) -> Annotated[bpy_prop_collection['ActionSlot'], "is_animatable=False"]:
        """The list of slots in this animation data-block"""
        ...
    def nla_tweak_strip_time_to_scene(self, *args, **kwargs) -> Any: ...
    def fix_paths_rename_all(self, *args, **kwargs) -> Any: ...