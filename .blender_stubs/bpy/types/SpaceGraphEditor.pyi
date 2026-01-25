# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
from .DopeSheet import DopeSheet
class SpaceGraphEditor(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    show_region_footer: bool
    show_region_channels: bool
    show_region_ui: bool
    show_region_hud: bool
    mode: str
    show_seconds: bool
    show_sliders: bool
    show_handles: bool
    use_auto_lock_translation_axis: bool
    use_only_selected_keyframe_handles: bool
    show_markers: bool
    show_extrapolation: bool
    use_auto_merge_keyframes: bool
    use_realtime_update: bool
    show_cursor: bool
    cursor_position_x: float
    cursor_position_y: float
    pivot_point: str
    dopesheet: 'DopeSheet'
    has_ghost_curves: bool
    use_normalization: bool
    use_auto_normalization: bool