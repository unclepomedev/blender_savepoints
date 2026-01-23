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
class FFmpegSettings(bpy_struct):
    format: str
    codec: str
    video_bitrate: int
    minrate: int
    maxrate: int
    muxrate: int
    gopsize: int
    max_b_frames: int
    use_max_b_frames: bool
    buffersize: int
    packetsize: int
    constant_rate_factor: str
    custom_constant_rate_factor: int
    ffmpeg_preset: str
    ffmpeg_prores_profile: str
    use_autosplit: bool
    use_lossless_output: bool
    audio_codec: str
    audio_bitrate: int
    audio_volume: float
    audio_mixrate: int
    audio_channels: str