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
class ImagePreview(bpy_struct):
    is_image_custom: bool
    image_size: int
    image_pixels: int
    image_pixels_float: float
    is_icon_custom: bool
    icon_size: int
    icon_pixels: int
    icon_pixels_float: float
    icon_id: int
    def reload(self, *args, **kwargs) -> Any: ...