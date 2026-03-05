# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.StripModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Mask import Mask
from .Strip import Strip

class StripModifier(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Literal['BRIGHT_CONTRAST', 'COLOR_BALANCE', 'COMPOSITOR', 'CURVES', 'HUE_CORRECT', 'MASK', 'TONEMAP', 'WHITE_BALANCE', 'SOUND_EQUALIZER']:

        ...
    @property
    def mute(self) -> bool:
        """Mute this modifier"""
        ...
    @mute.setter
    def mute(self, value: bool):
        ...
    @property
    def enable(self) -> bool:
        """Enable this modifier"""
        ...
    @enable.setter
    def enable(self, value: bool):
        ...
    @property
    def show_expanded(self) -> bool:
        """Mute expanded settings for the modifier"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool):
        ...
    @property
    def input_mask_type(self) -> Literal['STRIP', 'ID']:
        """Type of input data used for mask"""
        ...
    @input_mask_type.setter
    def input_mask_type(self, value: Literal['STRIP', 'ID']):
        ...
    @property
    def mask_time(self) -> Literal['RELATIVE', 'ABSOLUTE']:
        """Time to use for the Mask animation"""
        ...
    @mask_time.setter
    def mask_time(self, value: Literal['RELATIVE', 'ABSOLUTE']):
        ...
    @property
    def input_mask_strip(self) -> Annotated[Optional['Strip'], "is_animatable=False"]:
        """Strip used as mask input for the modifier"""
        ...
    @input_mask_strip.setter
    def input_mask_strip(self, value: Annotated[Optional['Strip'], "is_animatable=False"]):
        ...
    @property
    def input_mask_id(self) -> Annotated[Optional['Mask'], "is_animatable=False"]:
        """Mask ID used as mask input for the modifier"""
        ...
    @input_mask_id.setter
    def input_mask_id(self, value: Annotated[Optional['Mask'], "is_animatable=False"]):
        ...
    @property
    def is_active(self) -> Annotated[bool, "is_animatable=False"]:
        """This modifier is active"""
        ...
    @is_active.setter
    def is_active(self, value: Annotated[bool, "is_animatable=False"]):
        ...