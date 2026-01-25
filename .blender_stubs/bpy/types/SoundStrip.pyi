# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Strip import Strip
from .RetimingKey import RetimingKey
from .Sound import Sound
from .StripModifier import StripModifier
class SoundStrip(Strip):
    name: str
    type: str
    select: bool
    select_left_handle: bool
    select_right_handle: bool
    mute: bool
    lock: bool
    frame_final_duration: int
    frame_duration: int
    frame_start: float
    frame_final_start: int
    frame_final_end: int
    frame_offset_start: float
    frame_offset_end: float
    channel: int
    use_linear_modifiers: bool
    blend_type: str
    blend_alpha: float
    effect_fader: float
    use_default_fade: bool
    color_tag: str
    modifiers: bpy_prop_collection['StripModifier']
    show_retiming_keys: bool
    sound: 'Sound'
    volume: float
    pan: float
    sound_offset: float
    show_waveform: bool
    pitch_correction: bool
    retiming_keys: bpy_prop_collection['RetimingKey']
    animation_offset_start: int
    animation_offset_end: int
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def strip_elem_from_frame(self, *args, **kwargs) -> Any: ...
    def swap(self, *args, **kwargs) -> Any: ...
    def move_to_meta(self, *args, **kwargs) -> Any: ...
    def parent_meta(self, *args, **kwargs) -> Any: ...
    def invalidate_cache(self, *args, **kwargs) -> Any: ...
    def split(self, *args, **kwargs) -> Any: ...