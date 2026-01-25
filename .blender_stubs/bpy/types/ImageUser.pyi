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
class ImageUser(bpy_struct):
    use_auto_refresh: bool
    frame_current: int
    use_cyclic: bool
    frame_duration: int
    frame_offset: int
    frame_start: int
    multilayer_layer: int
    multilayer_pass: int
    multilayer_view: int
    tile: int