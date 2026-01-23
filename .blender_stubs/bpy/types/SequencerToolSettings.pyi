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
class SequencerToolSettings(bpy_struct):
    fit_method: str
    snap_to_current_frame: bool
    snap_to_hold_offset: bool
    snap_to_markers: bool
    snap_to_retiming_keys: bool
    snap_to_frame_range: bool
    snap_to_borders: bool
    snap_to_center: bool
    snap_to_strips_preview: bool
    snap_ignore_muted: bool
    snap_ignore_sound: bool
    use_snap_current_frame_to_strips: bool
    snap_distance: int
    overlap_mode: str
    pivot_point: str