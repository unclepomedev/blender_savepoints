# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SequencerTimelineOverlay.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SequencerTimelineOverlay(bpy_struct):

    @property
    def waveform_display_type(self) -> Literal['ALL_WAVEFORMS', 'DEFAULT_WAVEFORMS', 'NO_WAVEFORMS']:
        """How Waveforms are displayed"""
        ...
    @waveform_display_type.setter
    def waveform_display_type(self, value: Literal['ALL_WAVEFORMS', 'DEFAULT_WAVEFORMS', 'NO_WAVEFORMS']) -> None:
        ...
    @property
    def waveform_display_style(self) -> Literal['FULL_WAVEFORMS', 'HALF_WAVEFORMS']:
        """How Waveforms are displayed"""
        ...
    @waveform_display_style.setter
    def waveform_display_style(self, value: Literal['FULL_WAVEFORMS', 'HALF_WAVEFORMS']) -> None:
        ...
    @property
    def show_fcurves(self) -> bool:
        """Display strip opacity/volume curve"""
        ...
    @show_fcurves.setter
    def show_fcurves(self, value: bool) -> None:
        ...
    @property
    def show_strip_name(self) -> bool:

        ...
    @show_strip_name.setter
    def show_strip_name(self, value: bool) -> None:
        ...
    @property
    def show_strip_source(self) -> bool:
        """Display path to source file, or name of source data-block"""
        ...
    @show_strip_source.setter
    def show_strip_source(self, value: bool) -> None:
        ...
    @property
    def show_strip_duration(self) -> bool:

        ...
    @show_strip_duration.setter
    def show_strip_duration(self, value: bool) -> None:
        ...
    @property
    def show_grid(self) -> bool:
        """Show vertical grid lines"""
        ...
    @show_grid.setter
    def show_grid(self, value: bool) -> None:
        ...
    @property
    def show_strip_offset(self) -> bool:
        """Display strip in/out offsets"""
        ...
    @show_strip_offset.setter
    def show_strip_offset(self, value: bool) -> None:
        ...
    @property
    def show_thumbnails(self) -> bool:
        """Show strip thumbnails"""
        ...
    @show_thumbnails.setter
    def show_thumbnails(self, value: bool) -> None:
        ...
    @property
    def show_strip_tag_color(self) -> bool:
        """Display the strip color tags in the sequencer"""
        ...
    @show_strip_tag_color.setter
    def show_strip_tag_color(self, value: bool) -> None:
        ...
    @property
    def show_strip_retiming(self) -> bool:
        """Display retiming keys on top of strips"""
        ...
    @show_strip_retiming.setter
    def show_strip_retiming(self, value: bool) -> None:
        ...