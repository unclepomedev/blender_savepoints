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
from .SequenceTimelineChannel import SequenceTimelineChannel
from .Strip import Strip
class SequenceEditor(bpy_struct):
    strips: bpy_prop_collection['Strip']
    strips_all: bpy_prop_collection['Strip']
    meta_stack: bpy_prop_collection['Strip']
    channels: bpy_prop_collection['SequenceTimelineChannel']
    active_strip: 'Strip'
    selected_retiming_keys: bool
    show_overlay_frame: bool
    use_overlay_frame_lock: bool
    show_missing_media: bool
    overlay_frame: int
    proxy_storage: str
    proxy_dir: str
    use_cache_raw: bool
    use_cache_final: bool
    use_prefetch: bool
    cache_raw_size: int
    cache_final_size: int
    def display_stack(self, *args, **kwargs) -> Any: ...