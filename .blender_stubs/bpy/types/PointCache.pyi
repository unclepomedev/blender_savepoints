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
from .PointCacheItem import PointCacheItem
class PointCache(bpy_struct):
    frame_start: int
    frame_end: int
    frame_step: int
    index: int
    is_baked: bool
    is_baking: bool
    use_disk_cache: bool
    is_outdated: bool
    is_frame_skip: bool
    name: str
    filepath: str
    info: str
    use_external: bool
    use_library_path: bool
    point_caches: bpy_prop_collection['PointCacheItem']