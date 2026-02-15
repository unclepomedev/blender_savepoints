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
class ColorManagedDisplaySettings(bpy_struct):
    display_device: Literal['NONE']
    """Display name. For viewing, this is the display device that will be emulated by limiting the gamut and HDR colors. For image and video output, this is the display space used for writing."""
    emulation: Literal['OFF', 'AUTO']
    """Control how images in the chosen display are mapped to the physical display"""