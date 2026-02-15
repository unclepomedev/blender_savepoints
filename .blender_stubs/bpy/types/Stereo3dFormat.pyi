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
class Stereo3dFormat(bpy_struct):
    display_mode: Annotated[Literal['ANAGLYPH', 'INTERLACE', 'SIDEBYSIDE', 'TOPBOTTOM'], "is_animatable=False"]
    anaglyph_type: Annotated[Literal['RED_CYAN', 'GREEN_MAGENTA', 'YELLOW_BLUE'], "is_animatable=False"]
    interlace_type: Annotated[Literal['ROW_INTERLEAVED', 'COLUMN_INTERLEAVED', 'CHECKERBOARD_INTERLEAVED'], "is_animatable=False"]
    use_interlace_swap: Annotated[bool, "is_animatable=False"]
    """Swap left and right stereo channels"""
    use_sidebyside_crosseyed: Annotated[bool, "is_animatable=False"]
    """Right eye should see left image and vice versa"""
    use_squeezed_frame: Annotated[bool, "is_animatable=False"]
    """Combine both views in a squeezed image"""