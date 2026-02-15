# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SubtractStrip.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .EffectStrip import EffectStrip
from .Strip import Strip
from .StripCrop import StripCrop
from .StripModifier import StripModifier
from .StripModifiers import StripModifiers
from .StripProxy import StripProxy
from .StripTransform import StripTransform
from .bpy_prop_collection import bpy_prop_collection

class SubtractStrip(EffectStrip):

    name: Annotated[str, "is_animatable=False"]

    @property
    def type(self) -> Literal['IMAGE', 'META', 'SCENE', 'MOVIE', 'MOVIECLIP', 'MASK', 'SOUND', 'CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'WIPE', 'GLOW', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX']:

        ...
    select: bool

    select_left_handle: bool

    select_right_handle: bool

    mute: bool
    """Disable strip so that it cannot be viewed in the output"""
    lock: Annotated[bool, "is_animatable=False"]
    """Lock strip so that it cannot be transformed"""
    frame_final_duration: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """The length of the contents of this strip after the handles are applied"""
    @property
    def frame_duration(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """The length of the contents of this strip before the handles are applied"""
        ...
    frame_start: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=100.0", "precision=0", "is_animatable=False"]
    """X position where the strip begins"""
    frame_final_start: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """Start frame displayed in the sequence editor after offsets are applied, setting this is equivalent to moving the handle, not the actual start frame"""
    frame_final_end: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """End frame displayed in the sequence editor after offsets are applied"""
    frame_offset_start: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=100.0", "precision=0"]

    frame_offset_end: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=100.0", "precision=0"]

    channel: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Y position of the sequence strip"""
    use_linear_modifiers: bool
    """Calculate modifiers in linear space instead of sequencer's space"""
    blend_type: Literal['REPLACE', 'CROSS', 'DARKEN', 'MULTIPLY', 'BURN', 'LINEAR_BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'HARD_LIGHT', 'VIVID_LIGHT', 'LINEAR_LIGHT', 'PIN_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'HUE', 'SATURATION', 'COLOR', 'VALUE', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS']
    """Method for controlling how the strip combines with other strips"""
    blend_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Percentage of how much the strip's colors affect other strips"""
    effect_fader: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]
    """Custom fade value"""
    use_default_fade: bool
    """Fade effect using the built-in default (usually makes the transition as long as the effect strip)"""
    color_tag: Literal['NONE', 'COLOR_01', 'COLOR_02', 'COLOR_03', 'COLOR_04', 'COLOR_05', 'COLOR_06', 'COLOR_07', 'COLOR_08', 'COLOR_09']
    """Color tag for a strip"""
    @property
    def modifiers(self) -> Annotated['StripModifiers', "is_animatable=False"]:
        """Modifiers affecting this strip"""
        ...
    show_retiming_keys: bool
    """Show retiming keys, so they can be moved"""
    use_deinterlace: bool
    """Remove fields from video movies"""
    alpha_mode: Literal['STRAIGHT', 'PREMUL']
    """Representation of alpha information in the RGBA pixels"""
    use_flip_x: bool
    """Flip on the X axis"""
    use_flip_y: bool
    """Flip on the Y axis"""
    use_float: bool
    """Convert input to float data"""
    use_reverse_frames: bool
    """Reverse frame order"""
    color_multiply: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]

    multiply_alpha: bool
    """Multiply alpha along with color channels"""
    color_saturation: Annotated[float, "subtype='UNSIGNED'", "step=3.0", "precision=3"]
    """Adjust the intensity of the input's color"""
    strobe: Annotated[float, "step=10.0", "precision=3"]
    """Only display every nth frame"""
    @property
    def transform(self) -> Annotated[Optional['StripTransform'], "is_animatable=False"]:

        ...
    @property
    def crop(self) -> Annotated[Optional['StripCrop'], "is_animatable=False"]:

        ...
    use_proxy: bool
    """Use a preview proxy and/or time-code index for this strip"""
    @property
    def proxy(self) -> Annotated[Optional['StripProxy'], "is_animatable=False"]:

        ...
    @property
    def input_count(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:

        ...
    input_1: Annotated['Strip', "is_animatable=False"]
    """First input for the effect strip"""
    input_2: Annotated['Strip', "is_animatable=False"]
    """Second input for the effect strip"""
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def strip_elem_from_frame(self, *args, **kwargs) -> Any: ...
    def swap(self, *args, **kwargs) -> Any: ...
    def move_to_meta(self, *args, **kwargs) -> Any: ...
    def parent_meta(self, *args, **kwargs) -> Any: ...
    def invalidate_cache(self, *args, **kwargs) -> Any: ...
    def split(self, *args, **kwargs) -> Any: ...