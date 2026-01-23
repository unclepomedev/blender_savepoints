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
from .FModifier import FModifier
class NlaStrip(bpy_struct):
    name: str
    type: str
    extrapolation: str
    blend_type: str
    frame_start: float
    frame_end: float
    frame_start_raw: float
    frame_end_raw: float
    frame_start_ui: float
    frame_end_ui: float
    blend_in: float
    blend_out: float
    use_auto_blend: bool
    action: 'Action'
    action_slot_handle: int
    last_slot_identifier: str
    action_slot: 'ActionSlot'
    action_suitable_slots: bpy_prop_collection['ActionSlot']
    action_frame_start: float
    action_frame_end: float
    repeat: float
    scale: float
    fcurves: bpy_prop_collection['FCurve']
    modifiers: bpy_prop_collection['FModifier']
    strips: bpy_prop_collection['NlaStrip']
    influence: float
    strip_time: float
    use_animated_influence: bool
    use_animated_time: bool
    use_animated_time_cyclic: bool
    active: bool
    select: bool
    mute: bool
    use_reverse: bool
    use_sync_length: bool