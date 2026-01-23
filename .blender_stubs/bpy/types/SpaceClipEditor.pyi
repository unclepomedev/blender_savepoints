# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
from .Mask import Mask
from .MovieClip import MovieClip
from .MovieClipScopes import MovieClipScopes
from .MovieClipUser import MovieClipUser
from .SpaceClipOverlay import SpaceClipOverlay
class SpaceClipEditor(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    show_region_toolbar: bool
    show_region_channels: bool
    show_region_ui: bool
    show_region_hud: bool
    clip: 'MovieClip'
    clip_user: 'MovieClipUser'
    mask: 'Mask'
    mask_display_type: str
    show_mask_spline: bool
    show_mask_overlay: bool
    mask_overlay_mode: str
    blend_factor: float
    mode: str
    view: str
    show_marker_pattern: bool
    show_marker_search: bool
    lock_selection: bool
    lock_time_cursor: bool
    show_track_path: bool
    path_length: int
    show_tiny_markers: bool
    show_bundles: bool
    use_mute_footage: bool
    show_disabled: bool
    show_metadata: bool
    scopes: 'MovieClipScopes'
    show_names: bool
    show_grid: bool
    show_stable: bool
    use_manual_calibration: bool
    show_annotation: bool
    show_filters: bool
    show_graph_frames: bool
    show_graph_tracks_motion: bool
    show_graph_tracks_error: bool
    show_graph_only_selected: bool
    show_graph_hidden: bool
    show_red_channel: bool
    show_green_channel: bool
    show_blue_channel: bool
    use_grayscale_preview: bool
    show_seconds: bool
    annotation_source: str
    cursor_location: list[float]
    pivot_point: str
    show_gizmo: bool
    show_gizmo_navigate: bool
    zoom_percentage: float
    overlay: 'SpaceClipOverlay'