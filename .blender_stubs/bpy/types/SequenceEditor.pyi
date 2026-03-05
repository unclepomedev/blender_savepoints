# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SequenceEditor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .SequenceTimelineChannel import SequenceTimelineChannel
from .Strip import Strip
from .StripsTopLevel import StripsTopLevel
from .bpy_prop_collection import bpy_prop_collection

class SequenceEditor(bpy_struct):

    @property
    def strips(self) -> Annotated['StripsTopLevel', "is_animatable=False"]:
        """Top-level strips only"""
        ...
    @property
    def strips_all(self) -> Annotated[bpy_prop_collection['Strip'], "is_animatable=False"]:
        """All strips, recursively including those inside metastrips"""
        ...
    @property
    def meta_stack(self) -> Annotated[bpy_prop_collection['Strip'], "is_animatable=False"]:
        """Meta strip stack, last is currently edited meta strip"""
        ...
    @property
    def channels(self) -> Annotated[bpy_prop_collection['SequenceTimelineChannel'], "is_animatable=False"]:

        ...
    @property
    def active_strip(self) -> Annotated[Optional['Strip'], "is_animatable=False"]:
        """Sequencer's active strip"""
        ...
    @active_strip.setter
    def active_strip(self, value: Annotated[Optional['Strip'], "is_animatable=False"]):
        ...
    @property
    def selected_retiming_keys(self) -> bool:

        ...
    @property
    def show_overlay_frame(self) -> bool:
        """Partial overlay on top of the sequencer with a frame offset"""
        ...
    @show_overlay_frame.setter
    def show_overlay_frame(self, value: bool):
        ...
    @property
    def use_overlay_frame_lock(self) -> bool:

        ...
    @use_overlay_frame_lock.setter
    def use_overlay_frame_lock(self, value: bool):
        ...
    @property
    def show_missing_media(self) -> bool:
        """Render missing images/movies with a solid magenta color"""
        ...
    @show_missing_media.setter
    def show_missing_media(self, value: bool):
        ...
    @property
    def overlay_frame(self) -> Annotated[int, "step=1"]:
        """Number of frames to offset"""
        ...
    @overlay_frame.setter
    def overlay_frame(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def proxy_storage(self) -> Literal['PER_STRIP', 'PROJECT']:
        """How to store proxies for this project"""
        ...
    @proxy_storage.setter
    def proxy_storage(self, value: Literal['PER_STRIP', 'PROJECT']):
        ...
    @property
    def proxy_dir(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:

        ...
    @proxy_dir.setter
    def proxy_dir(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]):
        ...
    @property
    def use_cache_raw(self) -> bool:
        """Cache raw images read from disk, for faster tweaking of strip parameters at the cost of memory usage"""
        ...
    @use_cache_raw.setter
    def use_cache_raw(self, value: bool):
        ...
    @property
    def use_cache_final(self) -> bool:
        """Cache final image for each frame"""
        ...
    @use_cache_final.setter
    def use_cache_final(self, value: bool):
        ...
    @property
    def use_prefetch(self) -> bool:
        """Render frames ahead of current frame in the background for faster playback"""
        ...
    @use_prefetch.setter
    def use_prefetch(self, value: bool):
        ...
    @property
    def cache_raw_size(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Size of raw source images cache in megabytes"""
        ...
    @property
    def cache_final_size(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Size of final rendered images cache in megabytes"""
        ...
    def display_stack(self, *args, **kwargs) -> Any: ...