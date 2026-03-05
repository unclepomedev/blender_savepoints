# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SoundStrip.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Strip import Strip
from .RetimingKey import RetimingKey
from .RetimingKeys import RetimingKeys
from .Sound import Sound
from .StripModifier import StripModifier
from .StripModifiers import StripModifiers
from .bpy_prop_collection import bpy_prop_collection

class SoundStrip(Strip):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Literal['IMAGE', 'META', 'SCENE', 'MOVIE', 'MOVIECLIP', 'MASK', 'SOUND', 'CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'WIPE', 'GLOW', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX']:

        ...
    @property
    def select(self) -> bool:

        ...
    @select.setter
    def select(self, value: bool):
        ...
    @property
    def select_left_handle(self) -> bool:

        ...
    @select_left_handle.setter
    def select_left_handle(self, value: bool):
        ...
    @property
    def select_right_handle(self) -> bool:

        ...
    @select_right_handle.setter
    def select_right_handle(self, value: bool):
        ...
    @property
    def mute(self) -> bool:
        """Disable strip so that it cannot be viewed in the output"""
        ...
    @mute.setter
    def mute(self, value: bool):
        ...
    @property
    def lock(self) -> Annotated[bool, "is_animatable=False"]:
        """Lock strip so that it cannot be transformed"""
        ...
    @lock.setter
    def lock(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def frame_final_duration(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """The length of the contents of this strip after the handles are applied"""
        ...
    @frame_final_duration.setter
    def frame_final_duration(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]):
        ...
    @property
    def frame_duration(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """The length of the contents of this strip before the handles are applied"""
        ...
    @property
    def frame_start(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=100.0", "precision=0", "is_animatable=False"]:
        """X position where the strip begins"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=100.0", "precision=0", "is_animatable=False"]):
        ...
    @property
    def frame_final_start(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """Start frame displayed in the sequence editor after offsets are applied, setting this is equivalent to moving the handle, not the actual start frame"""
        ...
    @frame_final_start.setter
    def frame_final_start(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]):
        ...
    @property
    def frame_final_end(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """End frame displayed in the sequence editor after offsets are applied"""
        ...
    @frame_final_end.setter
    def frame_final_end(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]):
        ...
    @property
    def frame_offset_start(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=100.0", "precision=0"]:

        ...
    @frame_offset_start.setter
    def frame_offset_start(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=100.0", "precision=0"]):
        ...
    @property
    def frame_offset_end(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=100.0", "precision=0"]:

        ...
    @frame_offset_end.setter
    def frame_offset_end(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=100.0", "precision=0"]):
        ...
    @property
    def channel(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Y position of the sequence strip"""
        ...
    @channel.setter
    def channel(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def use_linear_modifiers(self) -> bool:
        """Calculate modifiers in linear space instead of sequencer's space"""
        ...
    @use_linear_modifiers.setter
    def use_linear_modifiers(self, value: bool):
        ...
    @property
    def blend_type(self) -> Literal['REPLACE', 'CROSS', 'DARKEN', 'MULTIPLY', 'BURN', 'LINEAR_BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'HARD_LIGHT', 'VIVID_LIGHT', 'LINEAR_LIGHT', 'PIN_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'HUE', 'SATURATION', 'COLOR', 'VALUE', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS']:
        """Method for controlling how the strip combines with other strips"""
        ...
    @blend_type.setter
    def blend_type(self, value: Literal['REPLACE', 'CROSS', 'DARKEN', 'MULTIPLY', 'BURN', 'LINEAR_BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'HARD_LIGHT', 'VIVID_LIGHT', 'LINEAR_LIGHT', 'PIN_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'HUE', 'SATURATION', 'COLOR', 'VALUE', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS']):
        ...
    @property
    def blend_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Percentage of how much the strip's colors affect other strips"""
        ...
    @blend_alpha.setter
    def blend_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def effect_fader(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]:
        """Custom fade value"""
        ...
    @effect_fader.setter
    def effect_fader(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3"]):
        ...
    @property
    def use_default_fade(self) -> bool:
        """Fade effect using the built-in default (usually makes the transition as long as the effect strip)"""
        ...
    @use_default_fade.setter
    def use_default_fade(self, value: bool):
        ...
    @property
    def color_tag(self) -> Literal['NONE', 'COLOR_01', 'COLOR_02', 'COLOR_03', 'COLOR_04', 'COLOR_05', 'COLOR_06', 'COLOR_07', 'COLOR_08', 'COLOR_09']:
        """Color tag for a strip"""
        ...
    @color_tag.setter
    def color_tag(self, value: Literal['NONE', 'COLOR_01', 'COLOR_02', 'COLOR_03', 'COLOR_04', 'COLOR_05', 'COLOR_06', 'COLOR_07', 'COLOR_08', 'COLOR_09']):
        ...
    @property
    def modifiers(self) -> Annotated['StripModifiers', "is_animatable=False"]:
        """Modifiers affecting this strip"""
        ...
    @property
    def show_retiming_keys(self) -> bool:
        """Show retiming keys, so they can be moved"""
        ...
    @show_retiming_keys.setter
    def show_retiming_keys(self, value: bool):
        ...
    @property
    def sound(self) -> Annotated[Optional['Sound'], "is_animatable=False"]:
        """Sound data-block used by this strip"""
        ...
    @sound.setter
    def sound(self, value: Annotated[Optional['Sound'], "is_animatable=False"]):
        ...
    @property
    def volume(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Playback volume of the sound"""
        ...
    @volume.setter
    def volume(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def pan(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Playback panning of the sound (only for Mono sources)"""
        ...
    @pan.setter
    def pan(self, value: Annotated[float, "step=1.0", "precision=2"]):
        ...
    @property
    def sound_offset(self) -> Annotated[float, "subtype='TIME_ABSOLUTE'", "unit='TIME_ABSOLUTE'", "step=1.0", "precision=3", "is_animatable=False"]:
        """Offset of the sound from the beginning of the strip, expressed in seconds"""
        ...
    @sound_offset.setter
    def sound_offset(self, value: Annotated[float, "subtype='TIME_ABSOLUTE'", "unit='TIME_ABSOLUTE'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def show_waveform(self) -> bool:
        """Display the audio waveform inside the strip"""
        ...
    @show_waveform.setter
    def show_waveform(self, value: bool):
        ...
    @property
    def pitch_correction(self) -> bool:
        """Maintain the original pitch of the audio when changing playback speed"""
        ...
    @pitch_correction.setter
    def pitch_correction(self, value: bool):
        ...
    @property
    def retiming_keys(self) -> Annotated['RetimingKeys', "is_animatable=False"]:

        ...
    @property
    def animation_offset_start(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Animation start offset (trim start)"""
        ...
    @animation_offset_start.setter
    def animation_offset_start(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def animation_offset_end(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Animation end offset (trim end)"""
        ...
    @animation_offset_end.setter
    def animation_offset_end(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def strip_elem_from_frame(self, *args, **kwargs) -> Any: ...
    def swap(self, *args, **kwargs) -> Any: ...
    def move_to_meta(self, *args, **kwargs) -> Any: ...
    def parent_meta(self, *args, **kwargs) -> Any: ...
    def invalidate_cache(self, *args, **kwargs) -> Any: ...
    def split(self, *args, **kwargs) -> Any: ...