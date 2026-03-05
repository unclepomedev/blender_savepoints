# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceImageOverlay.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SpaceImageOverlay(bpy_struct):

    @property
    def show_overlays(self) -> bool:
        """Display overlays like UV Maps and Metadata"""
        ...
    @show_overlays.setter
    def show_overlays(self, value: bool) -> None:
        ...
    @property
    def show_grid_background(self) -> bool:
        """Show the grid background and borders"""
        ...
    @show_grid_background.setter
    def show_grid_background(self, value: bool) -> None:
        ...
    @property
    def show_render_size(self) -> bool:
        """Display the region of the final render"""
        ...
    @show_render_size.setter
    def show_render_size(self, value: bool) -> None:
        ...
    @property
    def show_text_info(self) -> bool:
        """Display overlay text"""
        ...
    @show_text_info.setter
    def show_text_info(self, value: bool) -> None:
        ...
    @property
    def passepartout_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Opacity of the darkened overlay outside the render region"""
        ...
    @passepartout_alpha.setter
    def passepartout_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...