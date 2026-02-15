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

    waveform_display_type: Literal['ALL_WAVEFORMS', 'DEFAULT_WAVEFORMS', 'NO_WAVEFORMS']
    """How Waveforms are displayed"""
    waveform_display_style: Literal['FULL_WAVEFORMS', 'HALF_WAVEFORMS']
    """How Waveforms are displayed"""
    show_fcurves: bool
    """Display strip opacity/volume curve"""
    show_strip_name: bool

    show_strip_source: bool
    """Display path to source file, or name of source data-block"""
    show_strip_duration: bool

    show_grid: bool
    """Show vertical grid lines"""
    show_strip_offset: bool
    """Display strip in/out offsets"""
    show_thumbnails: bool
    """Show strip thumbnails"""
    show_strip_tag_color: bool
    """Display the strip color tags in the sequencer"""
    show_strip_retiming: bool
    """Display retiming keys on top of strips"""