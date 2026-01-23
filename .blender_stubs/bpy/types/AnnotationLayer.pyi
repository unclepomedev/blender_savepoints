# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .AnnotationFrame import AnnotationFrame
class AnnotationLayer(bpy_struct):
    info: str
    frames: bpy_prop_collection['AnnotationFrame']
    active_frame: 'AnnotationFrame'
    annotation_opacity: float
    color: float
    thickness: int
    use_annotation_onion_skinning: bool
    annotation_onion_before_range: int
    annotation_onion_after_range: int
    annotation_onion_before_color: float
    annotation_onion_after_color: float
    annotation_onion_use_custom_color: bool
    annotation_hide: bool
    lock: bool
    lock_frame: bool
    is_ruler: bool
    select: bool
    show_in_front: bool