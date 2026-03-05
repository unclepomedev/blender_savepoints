# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SequencerTonemapModifierData.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .StripModifier import StripModifier
from .Mask import Mask
from .Strip import Strip

class SequencerTonemapModifierData(StripModifier):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def type(self) -> Literal['BRIGHT_CONTRAST', 'COLOR_BALANCE', 'COMPOSITOR', 'CURVES', 'HUE_CORRECT', 'MASK', 'TONEMAP', 'WHITE_BALANCE', 'SOUND_EQUALIZER']:

        ...
    @property
    def mute(self) -> bool:
        """Mute this modifier"""
        ...
    @mute.setter
    def mute(self, value: bool) -> None:
        ...
    @property
    def enable(self) -> bool:
        """Enable this modifier"""
        ...
    @enable.setter
    def enable(self, value: bool) -> None:
        ...
    @property
    def show_expanded(self) -> bool:
        """Mute expanded settings for the modifier"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool) -> None:
        ...
    @property
    def input_mask_type(self) -> Literal['STRIP', 'ID']:
        """Type of input data used for mask"""
        ...
    @input_mask_type.setter
    def input_mask_type(self, value: Literal['STRIP', 'ID']) -> None:
        ...
    @property
    def mask_time(self) -> Literal['RELATIVE', 'ABSOLUTE']:
        """Time to use for the Mask animation"""
        ...
    @mask_time.setter
    def mask_time(self, value: Literal['RELATIVE', 'ABSOLUTE']) -> None:
        ...
    @property
    def input_mask_strip(self) -> Annotated[Optional['Strip'], "is_animatable=False"]:
        """Strip used as mask input for the modifier"""
        ...
    @input_mask_strip.setter
    def input_mask_strip(self, value: Annotated[Optional['Strip'], "is_animatable=False"]) -> None:
        ...
    @property
    def input_mask_id(self) -> Annotated[Optional['Mask'], "is_animatable=False"]:
        """Mask ID used as mask input for the modifier"""
        ...
    @input_mask_id.setter
    def input_mask_id(self, value: Annotated[Optional['Mask'], "is_animatable=False"]) -> None:
        ...
    @property
    def is_active(self) -> Annotated[bool, "is_animatable=False"]:
        """This modifier is active"""
        ...
    @is_active.setter
    def is_active(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def tonemap_type(self) -> Literal['RD_PHOTORECEPTOR', 'RH_SIMPLE']:
        """Tone mapping algorithm"""
        ...
    @tonemap_type.setter
    def tonemap_type(self, value: Literal['RD_PHOTORECEPTOR', 'RH_SIMPLE']) -> None:
        ...
    @property
    def key(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """The value the average luminance is mapped to"""
        ...
    @key.setter
    def key(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def offset(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Normally always 1, but can be used as an extra control to alter the brightness curve"""
        ...
    @offset.setter
    def offset(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def gamma(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """If not used, set to 1"""
        ...
    @gamma.setter
    def gamma(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def intensity(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """If less than zero, darkens image; otherwise, makes it brighter"""
        ...
    @intensity.setter
    def intensity(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def contrast(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Set to 0 to use estimate from input image"""
        ...
    @contrast.setter
    def contrast(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def adaptation(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """If 0, global; if 1, based on pixel intensity"""
        ...
    @adaptation.setter
    def adaptation(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def correction(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """If 0, same for all channels; if 1, each independent"""
        ...
    @correction.setter
    def correction(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def open_mask_input_panel(self) -> bool:

        ...
    @open_mask_input_panel.setter
    def open_mask_input_panel(self, value: bool) -> None:
        ...