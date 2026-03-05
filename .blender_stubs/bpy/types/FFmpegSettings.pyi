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

    @property
    def format(self) -> Annotated[Literal['MPEG4', 'MKV', 'WEBM', 'AVI', 'DV', 'FLASH', 'MPEG1', 'MPEG2', 'OGG', 'QUICKTIME'], "is_animatable=False"]:
        """Output file container"""
        ...
    @format.setter
    def format(self, value: Annotated[Literal['MPEG4', 'MKV', 'WEBM', 'AVI', 'DV', 'FLASH', 'MPEG1', 'MPEG2', 'OGG', 'QUICKTIME'], "is_animatable=False"]):
        ...
    @property
    def codec(self) -> Annotated[Literal['NONE', 'AV1', 'H264', 'H265', 'WEBM', 'DNXHD', 'DV', 'FFV1', 'FLASH', 'HUFFYUV', 'MPEG1', 'MPEG2', 'MPEG4', 'PNG', 'PRORES', 'QTRLE', 'THEORA'], "is_animatable=False"]:
        """FFmpeg codec to use for video output"""
        ...
    @codec.setter
    def codec(self, value: Annotated[Literal['NONE', 'AV1', 'H264', 'H265', 'WEBM', 'DNXHD', 'DV', 'FFV1', 'FLASH', 'HUFFYUV', 'MPEG1', 'MPEG2', 'MPEG4', 'PNG', 'PRORES', 'QTRLE', 'THEORA'], "is_animatable=False"]):
        ...
    @property
    def video_bitrate(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Video bitrate (kbit/s)"""
        ...
    @video_bitrate.setter
    def video_bitrate(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def minrate(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Rate control: min rate (kbit/s)"""
        ...
    @minrate.setter
    def minrate(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def maxrate(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Rate control: max rate (kbit/s)"""
        ...
    @maxrate.setter
    def maxrate(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def muxrate(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Mux rate (bits/second)"""
        ...
    @muxrate.setter
    def muxrate(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def gopsize(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Distance between key frames, also known as GOP size; influences file size and seekability"""
        ...
    @gopsize.setter
    def gopsize(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def max_b_frames(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Maximum number of B-frames between non-B-frames; influences file size and seekability"""
        ...
    @max_b_frames.setter
    def max_b_frames(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def use_max_b_frames(self) -> Annotated[bool, "is_animatable=False"]:
        """Set a maximum number of B-frames"""
        ...
    @use_max_b_frames.setter
    def use_max_b_frames(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def buffersize(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Rate control: buffer size (kb)"""
        ...
    @buffersize.setter
    def buffersize(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def packetsize(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Mux packet size (byte)"""
        ...
    @packetsize.setter
    def packetsize(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def constant_rate_factor(self) -> Annotated[Literal['NONE', 'LOSSLESS', 'PERC_LOSSLESS', 'HIGH', 'MEDIUM', 'LOW', 'VERYLOW', 'LOWEST'], "is_animatable=False"]:
        """Constant Rate Factor (CRF); tradeoff between video quality and file size"""
        ...
    @constant_rate_factor.setter
    def constant_rate_factor(self, value: Annotated[Literal['NONE', 'LOSSLESS', 'PERC_LOSSLESS', 'HIGH', 'MEDIUM', 'LOW', 'VERYLOW', 'LOWEST'], "is_animatable=False"]):
        ...
    @property
    def ffmpeg_preset(self) -> Annotated[Literal['BEST', 'GOOD', 'REALTIME'], "is_animatable=False"]:
        """Tradeoff between encoding speed and compression ratio"""
        ...
    @ffmpeg_preset.setter
    def ffmpeg_preset(self, value: Annotated[Literal['BEST', 'GOOD', 'REALTIME'], "is_animatable=False"]):
        ...
    @property
    def ffmpeg_prores_profile(self) -> Annotated[Literal['422_PROXY', '422_LT', '422_STD', '422_HQ', '4444', '4444_XQ'], "is_animatable=False"]:
        """ProRes Profile"""
        ...
    @ffmpeg_prores_profile.setter
    def ffmpeg_prores_profile(self, value: Annotated[Literal['422_PROXY', '422_LT', '422_STD', '422_HQ', '4444', '4444_XQ'], "is_animatable=False"]):
        ...
    @property
    def use_autosplit(self) -> Annotated[bool, "is_animatable=False"]:
        """Autosplit output at 2GB boundary"""
        ...
    @use_autosplit.setter
    def use_autosplit(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_lossless_output(self) -> Annotated[bool, "is_animatable=False"]:
        """Use lossless output for video streams"""
        ...
    @use_lossless_output.setter
    def use_lossless_output(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def audio_codec(self) -> Annotated[Literal['NONE', 'AAC', 'AC3', 'FLAC', 'MP2', 'MP3', 'OPUS', 'PCM', 'VORBIS'], "is_animatable=False"]:
        """FFmpeg audio codec to use"""
        ...
    @audio_codec.setter
    def audio_codec(self, value: Annotated[Literal['NONE', 'AAC', 'AC3', 'FLAC', 'MP2', 'MP3', 'OPUS', 'PCM', 'VORBIS'], "is_animatable=False"]):
        ...
    @property
    def audio_bitrate(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Audio bitrate (kb/s)"""
        ...
    @audio_bitrate.setter
    def audio_bitrate(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def audio_volume(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Audio volume"""
        ...
    @audio_volume.setter
    def audio_volume(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def audio_mixrate(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Audio sample rate (samples/s)"""
        ...
    @audio_mixrate.setter
    def audio_mixrate(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def audio_channels(self) -> Annotated[Literal['MONO', 'STEREO', 'SURROUND4', 'SURROUND51', 'SURROUND71'], "is_animatable=False"]:
        """Audio channel count"""
        ...
    @audio_channels.setter
    def audio_channels(self, value: Annotated[Literal['MONO', 'STEREO', 'SURROUND4', 'SURROUND51', 'SURROUND71'], "is_animatable=False"]):
        ...