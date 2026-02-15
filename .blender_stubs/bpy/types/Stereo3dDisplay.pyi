# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class Stereo3dDisplay(bpy_struct):
    display_mode: Literal['ANAGLYPH', 'INTERLACE', 'TIMESEQUENTIAL', 'SIDEBYSIDE', 'TOPBOTTOM']
    anaglyph_type: Literal['RED_CYAN', 'GREEN_MAGENTA', 'YELLOW_BLUE']
    interlace_type: Literal['ROW_INTERLEAVED', 'COLUMN_INTERLEAVED', 'CHECKERBOARD_INTERLEAVED']
    use_interlace_swap: bool
    """Swap left and right stereo channels"""
    use_sidebyside_crosseyed: bool
    """Right eye should see left image and vice versa"""