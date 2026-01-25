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
from .Mask import Mask
from .Strip import Strip
class StripModifier(bpy_struct):
    name: str
    type: str
    mute: bool
    enable: bool
    show_expanded: bool
    input_mask_type: str
    mask_time: str
    input_mask_strip: 'Strip'
    input_mask_id: 'Mask'
    is_active: bool