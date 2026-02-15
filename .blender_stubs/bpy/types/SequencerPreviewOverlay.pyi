# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SequencerPreviewOverlay.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SequencerPreviewOverlay(bpy_struct):

    show_safe_areas: bool
    """Show TV title safe and action safe areas in preview"""
    show_safe_center: bool
    """Show safe areas to fit content in a different aspect ratio"""
    show_metadata: bool
    """Show metadata of first visible strip"""
    show_annotation: bool
    """Show annotations for this view"""
    show_image_outline: bool

    show_cursor: bool
