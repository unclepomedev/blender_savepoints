# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FFmpegSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class FFmpegSettings(bpy_struct):

    format: Annotated[Literal['MPEG4', 'MKV', 'WEBM', 'AVI', 'DV', 'FLASH', 'MPEG1', 'MPEG2', 'OGG', 'QUICKTIME'], "is_animatable=False"]
    """Output file container"""
    codec: Annotated[Literal['NONE', 'AV1', 'H264', 'H265', 'WEBM', 'DNXHD', 'DV', 'FFV1', 'FLASH', 'HUFFYUV', 'MPEG1', 'MPEG2', 'MPEG4', 'PNG', 'PRORES', 'QTRLE', 'THEORA'], "is_animatable=False"]
    """FFmpeg codec to use for video output"""
    video_bitrate: Annotated[int, "step=1", "is_animatable=False"]
    """Video bitrate (kbit/s)"""
    minrate: Annotated[int, "step=1", "is_animatable=False"]
    """Rate control: min rate (kbit/s)"""
    maxrate: Annotated[int, "step=1", "is_animatable=False"]
    """Rate control: max rate (kbit/s)"""
    muxrate: Annotated[int, "step=1", "is_animatable=False"]
    """Mux rate (bits/second)"""
    gopsize: Annotated[int, "step=1", "is_animatable=False"]
    """Distance between key frames, also known as GOP size; influences file size and seekability"""
    max_b_frames: Annotated[int, "step=1", "is_animatable=False"]
    """Maximum number of B-frames between non-B-frames; influences file size and seekability"""
    use_max_b_frames: Annotated[bool, "is_animatable=False"]
    """Set a maximum number of B-frames"""
    buffersize: Annotated[int, "step=1", "is_animatable=False"]
    """Rate control: buffer size (kb)"""
    packetsize: Annotated[int, "step=1", "is_animatable=False"]
    """Mux packet size (byte)"""
    constant_rate_factor: Annotated[Literal['NONE', 'LOSSLESS', 'PERC_LOSSLESS', 'HIGH', 'MEDIUM', 'LOW', 'VERYLOW', 'LOWEST'], "is_animatable=False"]
    """Constant Rate Factor (CRF); tradeoff between video quality and file size"""
    ffmpeg_preset: Annotated[Literal['BEST', 'GOOD', 'REALTIME'], "is_animatable=False"]
    """Tradeoff between encoding speed and compression ratio"""
    ffmpeg_prores_profile: Annotated[Literal['422_PROXY', '422_LT', '422_STD', '422_HQ', '4444', '4444_XQ'], "is_animatable=False"]
    """ProRes Profile"""
    use_autosplit: Annotated[bool, "is_animatable=False"]
    """Autosplit output at 2GB boundary"""
    use_lossless_output: Annotated[bool, "is_animatable=False"]
    """Use lossless output for video streams"""
    audio_codec: Annotated[Literal['NONE', 'AAC', 'AC3', 'FLAC', 'MP2', 'MP3', 'OPUS', 'PCM', 'VORBIS'], "is_animatable=False"]
    """FFmpeg audio codec to use"""
    audio_bitrate: Annotated[int, "step=1", "is_animatable=False"]
    """Audio bitrate (kb/s)"""
    audio_volume: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Audio volume"""
    audio_mixrate: Annotated[int, "step=1", "is_animatable=False"]
    """Audio sample rate (samples/s)"""
    audio_channels: Annotated[Literal['MONO', 'STEREO', 'SURROUND4', 'SURROUND51', 'SURROUND71'], "is_animatable=False"]
    """Audio channel count"""