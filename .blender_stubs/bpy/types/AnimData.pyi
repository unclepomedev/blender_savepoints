# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Action import Action
from .ActionSlot import ActionSlot
from .FCurve import FCurve
from .NlaTrack import NlaTrack
class AnimData(bpy_struct):
    nla_tracks: bpy_prop_collection['NlaTrack']
    action: 'Action'
    action_extrapolation: str
    action_blend_type: str
    action_influence: float
    action_tweak_storage: 'Action'
    action_slot_handle_tweak_storage: int
    drivers: bpy_prop_collection['FCurve']
    use_nla: bool
    use_tweak_mode: bool
    use_pin: bool
    action_slot_handle: int
    last_slot_identifier: str
    action_slot: 'ActionSlot'
    action_suitable_slots: bpy_prop_collection['ActionSlot']
    def nla_tweak_strip_time_to_scene(self, *args, **kwargs) -> Any: ...
    def fix_paths_rename_all(self, *args, **kwargs) -> Any: ...