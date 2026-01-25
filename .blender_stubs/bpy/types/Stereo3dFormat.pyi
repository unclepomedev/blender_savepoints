# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class Stereo3dFormat(bpy_struct):
    display_mode: str
    anaglyph_type: str
    interlace_type: str
    use_interlace_swap: bool
    use_sidebyside_crosseyed: bool
    use_squeezed_frame: bool