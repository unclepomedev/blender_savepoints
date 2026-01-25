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
from .Image import Image
class MaterialGPencilStyle(bpy_struct):
    color: float
    fill_color: float
    mix_color: float
    mix_factor: float
    mix_stroke_factor: float
    texture_angle: float
    texture_scale: float
    texture_offset: float
    pixel_size: float
    hide: bool
    lock: bool
    ghost: bool
    texture_clamp: bool
    flip: bool
    use_overlap_strokes: bool
    use_stroke_holdout: bool
    use_fill_holdout: bool
    show_stroke: bool
    show_fill: bool
    alignment_mode: str
    alignment_rotation: float
    pass_index: int
    mode: str
    stroke_style: str
    stroke_image: 'Image'
    fill_style: str
    gradient_type: str
    fill_image: 'Image'
    is_stroke_visible: bool
    is_fill_visible: bool