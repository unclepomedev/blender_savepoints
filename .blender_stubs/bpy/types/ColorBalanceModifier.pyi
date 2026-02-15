# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .StripModifier import StripModifier
from .Mask import Mask
from .Strip import Strip
from .StripColorBalanceData import StripColorBalanceData
class ColorBalanceModifier(StripModifier):
    name: Annotated[str, "is_animatable=False"]
    @property
    def type(self) -> Literal['BRIGHT_CONTRAST', 'COLOR_BALANCE', 'COMPOSITOR', 'CURVES', 'HUE_CORRECT', 'MASK', 'TONEMAP', 'WHITE_BALANCE', 'SOUND_EQUALIZER']:
        ...
    mute: bool
    """Mute this modifier"""
    enable: bool
    """Enable this modifier"""
    show_expanded: bool
    """Mute expanded settings for the modifier"""
    input_mask_type: Literal['STRIP', 'ID']
    """Type of input data used for mask"""
    mask_time: Literal['RELATIVE', 'ABSOLUTE']
    """Time to use for the Mask animation"""
    input_mask_strip: Annotated[Optional['Strip'], "is_animatable=False"]
    """Strip used as mask input for the modifier"""
    input_mask_id: Annotated[Optional['Mask'], "is_animatable=False"]
    """Mask ID used as mask input for the modifier"""
    is_active: Annotated[bool, "is_animatable=False"]
    """This modifier is active"""
    @property
    def color_balance(self) -> Annotated[Optional['StripColorBalanceData'], "is_animatable=False"]:
        ...
    color_multiply: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    """Multiply the intensity of each pixel"""
    open_mask_input_panel: bool