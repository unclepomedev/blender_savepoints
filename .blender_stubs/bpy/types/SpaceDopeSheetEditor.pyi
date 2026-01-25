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
from .SpaceDopeSheetOverlay import SpaceDopeSheetOverlay
class SpaceDopeSheetEditor(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    show_region_footer: bool
    show_region_channels: bool
    show_region_ui: bool
    show_region_hud: bool
    mode: str
    ui_mode: str
    show_seconds: bool
    show_sliders: bool
    show_pose_markers: bool
    show_interpolation: bool
    show_extremes: bool
    show_markers: bool
    use_auto_merge_keyframes: bool
    use_realtime_update: bool
    use_marker_sync: bool
    dopesheet: 'DopeSheet'
    show_cache: bool
    cache_softbody: bool
    cache_particles: bool
    cache_cloth: bool
    cache_smoke: bool
    cache_simulation_nodes: bool
    cache_dynamicpaint: bool
    cache_rigidbody: bool
    overlays: 'SpaceDopeSheetOverlay'