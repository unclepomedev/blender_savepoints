# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.AnimData.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Action import Action
from .ActionSlot import ActionSlot
from .AnimDataDrivers import AnimDataDrivers
from .FCurve import FCurve
from .NlaTrack import NlaTrack
from .NlaTracks import NlaTracks
from .bpy_prop_collection import bpy_prop_collection

class AnimData(bpy_struct):

    @property
    def nla_tracks(self) -> Annotated['NlaTracks', "is_animatable=False"]:
        """NLA Tracks (i.e. Animation Layers)"""
        ...
    @property
    def action(self) -> Annotated[Optional['Action'], "is_animatable=False"]:
        """Active Action for this data-block"""
        ...
    @action.setter
    def action(self, value: Annotated[Optional['Action'], "is_animatable=False"]) -> None:
        ...
    @property
    def action_extrapolation(self) -> Literal['NOTHING', 'HOLD', 'HOLD_FORWARD']:
        """Action to take for gaps past the Active Action's range (when evaluating with NLA)"""
        ...
    @action_extrapolation.setter
    def action_extrapolation(self, value: Literal['NOTHING', 'HOLD', 'HOLD_FORWARD']) -> None:
        ...
    @property
    def action_blend_type(self) -> Literal['REPLACE', 'COMBINE', 'ADD', 'SUBTRACT', 'MULTIPLY']:
        """Method used for combining Active Action's result with result of NLA stack"""
        ...
    @action_blend_type.setter
    def action_blend_type(self, value: Literal['REPLACE', 'COMBINE', 'ADD', 'SUBTRACT', 'MULTIPLY']) -> None:
        ...
    @property
    def action_influence(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount the Active Action contributes to the result of the NLA stack"""
        ...
    @action_influence.setter
    def action_influence(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def action_tweak_storage(self) -> Annotated[Optional['Action'], "is_animatable=False"]:
        """Storage to temporarily hold the main action while in tweak mode"""
        ...
    @action_tweak_storage.setter
    def action_tweak_storage(self, value: Annotated[Optional['Action'], "is_animatable=False"]) -> None:
        ...
    @property
    def action_slot_handle_tweak_storage(self) -> Annotated[int, "step=1"]:
        """Storage to temporarily hold the main action slot while in tweak mode"""
        ...
    @action_slot_handle_tweak_storage.setter
    def action_slot_handle_tweak_storage(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def drivers(self) -> Annotated['AnimDataDrivers', "is_animatable=False"]:
        """The Drivers/Expressions for this data-block"""
        ...
    @property
    def use_nla(self) -> bool:
        """NLA stack is evaluated when evaluating this block"""
        ...
    @use_nla.setter
    def use_nla(self, value: bool) -> None:
        ...
    @property
    def use_tweak_mode(self) -> bool:
        """Whether to enable or disable tweak mode in NLA"""
        ...
    @use_tweak_mode.setter
    def use_tweak_mode(self, value: bool) -> None:
        ...
    @property
    def use_pin(self) -> bool:

        ...
    @use_pin.setter
    def use_pin(self, value: bool) -> None:
        ...
    @property
    def action_slot_handle(self) -> Annotated[int, "step=1"]:
        """A number that identifies which sub-set of the Action is considered to be for this data-block"""
        ...
    @action_slot_handle.setter
    def action_slot_handle(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def last_slot_identifier(self) -> Annotated[str, "is_animatable=False"]:
        """The identifier of the most recently assigned action slot. The slot identifies which sub-set of the Action is considered to be for this data-block, and its identifier is used to find the right slot when assigning an Action."""
        ...
    @last_slot_identifier.setter
    def last_slot_identifier(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def action_slot(self) -> Annotated[Optional['ActionSlot'], "is_animatable=False"]:
        """The slot identifies which sub-set of the Action is considered to be for this data-block, and its name is used to find the right slot when assigning an Action"""
        ...
    @action_slot.setter
    def action_slot(self, value: Annotated[Optional['ActionSlot'], "is_animatable=False"]) -> None:
        ...
    @property
    def action_suitable_slots(self) -> Annotated[bpy_prop_collection['ActionSlot'], "is_animatable=False"]:
        """The list of slots in this animation data-block"""
        ...
    def nla_tweak_strip_time_to_scene(self, *args, **kwargs) -> Any: ...
    def fix_paths_rename_all(self, *args, **kwargs) -> Any: ...