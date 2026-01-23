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
class RegionView3D(bpy_struct):
    lock_rotation: bool
    show_sync_view: bool
    use_box_clip: bool
    perspective_matrix: list[float]
    window_matrix: list[float]
    view_matrix: list[float]
    view_perspective: str
    is_perspective: bool
    is_orthographic_side_view: bool
    use_clip_planes: bool
    clip_planes: list[float]
    view_location: list[float]
    view_rotation: list[float]
    view_distance: float
    view_camera_zoom: float
    view_camera_offset: list[float]
    def update(self, *args, **kwargs) -> Any: ...