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
class SequencerTonemapModifierData(StripModifier):
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
    tonemap_type: Literal['RD_PHOTORECEPTOR', 'RH_SIMPLE']
    """Tone mapping algorithm"""
    key: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """The value the average luminance is mapped to"""
    offset: Annotated[float, "step=10.0", "precision=3"]
    """Normally always 1, but can be used as an extra control to alter the brightness curve"""
    gamma: Annotated[float, "step=10.0", "precision=3"]
    """If not used, set to 1"""
    intensity: Annotated[float, "step=10.0", "precision=3"]
    """If less than zero, darkens image; otherwise, makes it brighter"""
    contrast: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Set to 0 to use estimate from input image"""
    adaptation: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """If 0, global; if 1, based on pixel intensity"""
    correction: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """If 0, same for all channels; if 1, each independent"""
    open_mask_input_panel: bool