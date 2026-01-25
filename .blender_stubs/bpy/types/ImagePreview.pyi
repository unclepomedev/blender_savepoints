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
    image_size: list[int]
    image_pixels: list[int]
    image_pixels_float: list[float]
    is_icon_custom: bool
    icon_size: list[int]
    icon_pixels: list[int]
    icon_pixels_float: list[float]
    icon_id: int
    def reload(self, *args, **kwargs) -> Any: ...