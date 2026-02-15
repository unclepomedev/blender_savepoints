# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
from .Annotation import Annotation
from .SequencerCacheOverlay import SequencerCacheOverlay
from .SequencerPreviewOverlay import SequencerPreviewOverlay
from .SequencerTimelineOverlay import SequencerTimelineOverlay
class SpaceSequenceEditor(Space):
    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    show_locked_time: bool
    """Synchronize the visible timeline range with other time-based editors"""
    show_region_header: bool
    show_region_tool_header: bool
    show_region_footer: bool
    show_region_toolbar: bool
    show_region_channels: bool
    show_region_ui: bool
    show_region_hud: bool
    view_type: Literal['SEQUENCER', 'PREVIEW', 'SEQUENCER_PREVIEW']
    """Type of the Sequencer view (sequencer, preview or both)"""
    display_mode: Literal['IMAGE', 'WAVEFORM', 'RGB_PARADE', 'VECTOR_SCOPE', 'HISTOGRAM']
    """View mode to use for displaying sequencer output"""
    show_frames: bool
    """Display frames rather than seconds"""
    use_marker_sync: bool
    """Transform markers as well as strips"""
    show_seconds: bool
    """Show timing as a timecode instead of frames"""
    show_markers: bool
    """If any exists, show markers in a separate row at the bottom of the editor"""
    display_channel: Annotated[int, "step=1"]
    """Preview all channels less than or equal to this value. 0 shows every channel, and negative values climb that many meta-strip levels if applicable, showing every channel there."""
    preview_channels: Literal['COLOR_ALPHA', 'COLOR']
    """Channels of the preview to display"""
    use_zoom_to_fit: bool
    """Automatically zoom preview image to make it fully fit the region"""
    show_overexposed: Annotated[int, "step=1"]
    """Show overexposed areas with zebra stripes"""
    proxy_render_size: Literal['NONE', 'SCENE', 'PROXY_25', 'PROXY_50', 'PROXY_75', 'PROXY_100']
    """Display preview using full resolution or different proxy resolutions"""
    use_proxies: bool
    """Use optimized files for faster scrubbing when available"""
    use_clamp_view: bool
    """Limit timeline height to maximum used channel slot"""
    annotation: Annotated[Optional['Annotation'], "is_animatable=False"]
    """Annotation data for this Preview region"""
    overlay_frame_type: Literal['RECTANGLE', 'REFERENCE', 'CURRENT']
    """Overlay display method"""
    show_transform_preview: bool
    """Show a preview of the start or end frame of a strip while transforming its respective handle"""
    show_gizmo: bool
    """Show gizmos of all types"""
    show_gizmo_navigate: bool
    """Viewport navigation gizmo"""
    show_gizmo_context: bool
    """Context sensitive gizmos for the active item"""
    show_gizmo_tool: bool
    """Active tool gizmo"""
    show_overlays: bool
    @property
    def preview_overlay(self) -> Annotated['SequencerPreviewOverlay', "is_animatable=False"]:
        """Settings for display of overlays"""
        ...
    @property
    def timeline_overlay(self) -> Annotated['SequencerTimelineOverlay', "is_animatable=False"]:
        """Settings for display of overlays"""
        ...
    @property
    def cache_overlay(self) -> Annotated['SequencerCacheOverlay', "is_animatable=False"]:
        """Settings for display of overlays"""
        ...
    cursor_location: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """2D cursor location for this view"""
    zoom_percentage: Annotated[float, "subtype='PERCENTAGE'", "step=100.0", "precision=0"]
    """Zoom percentage"""