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

    show_overlays: bool
    """Display overlays like UV Maps and Metadata"""
    show_grid_background: bool
    """Show the grid background and borders"""
    show_render_size: bool
    """Display the region of the final render"""
    show_text_info: bool
    """Display overlay text"""
    passepartout_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Opacity of the darkened overlay outside the render region"""