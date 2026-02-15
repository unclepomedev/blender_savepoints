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
from .PointCacheItem import PointCacheItem
from .PointCaches import PointCaches
class PointCache(bpy_struct):
    frame_start: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """Frame on which the simulation starts"""
    frame_end: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """Frame on which the simulation stops"""
    frame_step: Annotated[int, "step=1"]
    """Number of frames between cached frames"""
    index: Annotated[int, "step=1"]
    """Index number of cache files"""
    @property
    def is_baked(self) -> bool:
        """The cache is baked"""
        ...
    @property
    def is_baking(self) -> bool:
        """The cache is being baked"""
        ...
    use_disk_cache: bool
    """Save cache files to disk (.blend file must be saved first)"""
    @property
    def is_outdated(self) -> bool:
        ...
    @property
    def is_frame_skip(self) -> bool:
        """Some frames were skipped while baking/saving that cache"""
        ...
    name: Annotated[str, "is_animatable=False"]
    """Cache name"""
    filepath: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """Cache file path"""
    @property
    def info(self) -> Annotated[str, "is_animatable=False"]:
        """Info on current cache status"""
        ...
    use_external: bool
    """Read cache from an external location"""
    use_library_path: bool
    """Use this file's path for the disk cache when library linked into another file (for local bakes per scene file, disable this option)"""
    @property
    def point_caches(self) -> Annotated['PointCaches', "is_animatable=False"]:
        ...