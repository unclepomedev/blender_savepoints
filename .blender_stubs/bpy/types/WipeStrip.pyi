# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .EffectStrip import EffectStrip
from .Strip import Strip
from .StripCrop import StripCrop
from .StripModifier import StripModifier
from .StripProxy import StripProxy
from .StripTransform import StripTransform
class WipeStrip(EffectStrip):
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
    use_deinterlace: bool
    alpha_mode: str
    use_flip_x: bool
    use_flip_y: bool
    use_float: bool
    use_reverse_frames: bool
    color_multiply: float
    multiply_alpha: bool
    color_saturation: float
    strobe: float
    transform: 'StripTransform'
    crop: 'StripCrop'
    use_proxy: bool
    proxy: 'StripProxy'
    input_count: int
    input_1: 'Strip'
    input_2: 'Strip'
    blur_width: float
    angle: float
    direction: str
    transition_type: str
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def strip_elem_from_frame(self, *args, **kwargs) -> Any: ...
    def swap(self, *args, **kwargs) -> Any: ...
    def move_to_meta(self, *args, **kwargs) -> Any: ...
    def parent_meta(self, *args, **kwargs) -> Any: ...
    def invalidate_cache(self, *args, **kwargs) -> Any: ...
    def split(self, *args, **kwargs) -> Any: ...