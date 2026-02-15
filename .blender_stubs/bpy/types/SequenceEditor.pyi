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
    active_strip: Annotated[Optional['Strip'], "is_animatable=False"]
    """Sequencer's active strip"""
    @property
    def selected_retiming_keys(self) -> bool:

        ...
    show_overlay_frame: bool
    """Partial overlay on top of the sequencer with a frame offset"""
    use_overlay_frame_lock: bool

    show_missing_media: bool
    """Render missing images/movies with a solid magenta color"""
    overlay_frame: Annotated[int, "step=1"]
    """Number of frames to offset"""
    proxy_storage: Literal['PER_STRIP', 'PROJECT']
    """How to store proxies for this project"""
    proxy_dir: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]

    use_cache_raw: bool
    """Cache raw images read from disk, for faster tweaking of strip parameters at the cost of memory usage"""
    use_cache_final: bool
    """Cache final image for each frame"""
    use_prefetch: bool
    """Render frames ahead of current frame in the background for faster playback"""
    @property
    def cache_raw_size(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Size of raw source images cache in megabytes"""
        ...
    @property
    def cache_final_size(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Size of final rendered images cache in megabytes"""
        ...
    def display_stack(self, *args, **kwargs) -> Any: ...