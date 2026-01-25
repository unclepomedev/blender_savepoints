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
from .Annotation import Annotation
from .SequencerCacheOverlay import SequencerCacheOverlay
from .SequencerPreviewOverlay import SequencerPreviewOverlay
from .SequencerTimelineOverlay import SequencerTimelineOverlay
class SpaceSequenceEditor(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    show_region_tool_header: bool
    show_region_footer: bool
    show_region_toolbar: bool
    show_region_channels: bool
    show_region_ui: bool
    show_region_hud: bool
    view_type: str
    display_mode: str
    show_frames: bool
    use_marker_sync: bool
    show_seconds: bool
    show_markers: bool
    display_channel: int
    preview_channels: str
    use_zoom_to_fit: bool
    show_overexposed: int
    proxy_render_size: str
    use_proxies: bool
    use_clamp_view: bool
    annotation: 'Annotation'
    overlay_frame_type: str
    show_transform_preview: bool
    show_gizmo: bool
    show_gizmo_navigate: bool
    show_gizmo_context: bool
    show_gizmo_tool: bool
    show_overlays: bool
    preview_overlay: 'SequencerPreviewOverlay'
    timeline_overlay: 'SequencerTimelineOverlay'
    cache_overlay: 'SequencerCacheOverlay'
    cursor_location: float
    zoom_percentage: float