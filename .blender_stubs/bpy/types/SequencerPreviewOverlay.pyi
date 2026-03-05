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

    @property
    def show_safe_areas(self) -> bool:
        """Show TV title safe and action safe areas in preview"""
        ...
    @show_safe_areas.setter
    def show_safe_areas(self, value: bool) -> None:
        ...
    @property
    def show_safe_center(self) -> bool:
        """Show safe areas to fit content in a different aspect ratio"""
        ...
    @show_safe_center.setter
    def show_safe_center(self, value: bool) -> None:
        ...
    @property
    def show_metadata(self) -> bool:
        """Show metadata of first visible strip"""
        ...
    @show_metadata.setter
    def show_metadata(self, value: bool) -> None:
        ...
    @property
    def show_annotation(self) -> bool:
        """Show annotations for this view"""
        ...
    @show_annotation.setter
    def show_annotation(self, value: bool) -> None:
        ...
    @property
    def show_image_outline(self) -> bool:

        ...
    @show_image_outline.setter
    def show_image_outline(self, value: bool) -> None:
        ...
    @property
    def show_cursor(self) -> bool:

        ...
    @show_cursor.setter
    def show_cursor(self, value: bool) -> None:
        ...