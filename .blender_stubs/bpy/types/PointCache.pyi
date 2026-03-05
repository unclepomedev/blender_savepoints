# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PointCache.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .PointCacheItem import PointCacheItem
from .PointCaches import PointCaches
from .bpy_prop_collection import bpy_prop_collection

class PointCache(bpy_struct):

    @property
    def frame_start(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """Frame on which the simulation starts"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]):
        ...
    @property
    def frame_end(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """Frame on which the simulation stops"""
        ...
    @frame_end.setter
    def frame_end(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]):
        ...
    @property
    def frame_step(self) -> Annotated[int, "step=1"]:
        """Number of frames between cached frames"""
        ...
    @frame_step.setter
    def frame_step(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def index(self) -> Annotated[int, "step=1"]:
        """Index number of cache files"""
        ...
    @index.setter
    def index(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def is_baked(self) -> bool:
        """The cache is baked"""
        ...
    @property
    def is_baking(self) -> bool:
        """The cache is being baked"""
        ...
    @property
    def use_disk_cache(self) -> bool:
        """Save cache files to disk (.blend file must be saved first)"""
        ...
    @use_disk_cache.setter
    def use_disk_cache(self, value: bool):
        ...
    @property
    def is_outdated(self) -> bool:

        ...
    @property
    def is_frame_skip(self) -> bool:
        """Some frames were skipped while baking/saving that cache"""
        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Cache name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def filepath(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """Cache file path"""
        ...
    @filepath.setter
    def filepath(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]):
        ...
    @property
    def info(self) -> Annotated[str, "is_animatable=False"]:
        """Info on current cache status"""
        ...
    @property
    def use_external(self) -> bool:
        """Read cache from an external location"""
        ...
    @use_external.setter
    def use_external(self, value: bool):
        ...
    @property
    def use_library_path(self) -> bool:
        """Use this file's path for the disk cache when library linked into another file (for local bakes per scene file, disable this option)"""
        ...
    @use_library_path.setter
    def use_library_path(self, value: bool):
        ...
    @property
    def point_caches(self) -> Annotated['PointCaches', "is_animatable=False"]:

        ...