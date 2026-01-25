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
class RegionView3D(bpy_struct):
    lock_rotation: bool
    show_sync_view: bool
    use_box_clip: bool
    perspective_matrix: float
    window_matrix: float
    view_matrix: float
    view_perspective: str
    is_perspective: bool
    is_orthographic_side_view: bool
    use_clip_planes: bool
    clip_planes: float
    view_location: float
    view_rotation: float
    view_distance: float
    view_camera_zoom: float
    view_camera_offset: float
    def update(self, *args, **kwargs) -> Any: ...