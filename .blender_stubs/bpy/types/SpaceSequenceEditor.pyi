# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceSequenceEditor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

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
    @property
    def show_locked_time(self) -> bool:
        """Synchronize the visible timeline range with other time-based editors"""
        ...
    @show_locked_time.setter
    def show_locked_time(self, value: bool):
        ...
    @property
    def show_region_header(self) -> bool:

        ...
    @show_region_header.setter
    def show_region_header(self, value: bool):
        ...
    @property
    def show_region_tool_header(self) -> bool:

        ...
    @show_region_tool_header.setter
    def show_region_tool_header(self, value: bool):
        ...
    @property
    def show_region_footer(self) -> bool:

        ...
    @show_region_footer.setter
    def show_region_footer(self, value: bool):
        ...
    @property
    def show_region_toolbar(self) -> bool:

        ...
    @show_region_toolbar.setter
    def show_region_toolbar(self, value: bool):
        ...
    @property
    def show_region_channels(self) -> bool:

        ...
    @show_region_channels.setter
    def show_region_channels(self, value: bool):
        ...
    @property
    def show_region_ui(self) -> bool:

        ...
    @show_region_ui.setter
    def show_region_ui(self, value: bool):
        ...
    @property
    def show_region_hud(self) -> bool:

        ...
    @show_region_hud.setter
    def show_region_hud(self, value: bool):
        ...
    @property
    def view_type(self) -> Literal['SEQUENCER', 'PREVIEW', 'SEQUENCER_PREVIEW']:
        """Type of the Sequencer view (sequencer, preview or both)"""
        ...
    @view_type.setter
    def view_type(self, value: Literal['SEQUENCER', 'PREVIEW', 'SEQUENCER_PREVIEW']):
        ...
    @property
    def display_mode(self) -> Literal['IMAGE', 'WAVEFORM', 'RGB_PARADE', 'VECTOR_SCOPE', 'HISTOGRAM']:
        """View mode to use for displaying sequencer output"""
        ...
    @display_mode.setter
    def display_mode(self, value: Literal['IMAGE', 'WAVEFORM', 'RGB_PARADE', 'VECTOR_SCOPE', 'HISTOGRAM']):
        ...
    @property
    def show_frames(self) -> bool:
        """Display frames rather than seconds"""
        ...
    @show_frames.setter
    def show_frames(self, value: bool):
        ...
    @property
    def use_marker_sync(self) -> bool:
        """Transform markers as well as strips"""
        ...
    @use_marker_sync.setter
    def use_marker_sync(self, value: bool):
        ...
    @property
    def show_seconds(self) -> bool:
        """Show timing as a timecode instead of frames"""
        ...
    @show_seconds.setter
    def show_seconds(self, value: bool):
        ...
    @property
    def show_markers(self) -> bool:
        """If any exists, show markers in a separate row at the bottom of the editor"""
        ...
    @show_markers.setter
    def show_markers(self, value: bool):
        ...
    @property
    def display_channel(self) -> Annotated[int, "step=1"]:
        """Preview all channels less than or equal to this value. 0 shows every channel, and negative values climb that many meta-strip levels if applicable, showing every channel there."""
        ...
    @display_channel.setter
    def display_channel(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def preview_channels(self) -> Literal['COLOR_ALPHA', 'COLOR']:
        """Channels of the preview to display"""
        ...
    @preview_channels.setter
    def preview_channels(self, value: Literal['COLOR_ALPHA', 'COLOR']):
        ...
    @property
    def use_zoom_to_fit(self) -> bool:
        """Automatically zoom preview image to make it fully fit the region"""
        ...
    @use_zoom_to_fit.setter
    def use_zoom_to_fit(self, value: bool):
        ...
    @property
    def show_overexposed(self) -> Annotated[int, "step=1"]:
        """Show overexposed areas with zebra stripes"""
        ...
    @show_overexposed.setter
    def show_overexposed(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def proxy_render_size(self) -> Literal['NONE', 'SCENE', 'PROXY_25', 'PROXY_50', 'PROXY_75', 'PROXY_100']:
        """Display preview using full resolution or different proxy resolutions"""
        ...
    @proxy_render_size.setter
    def proxy_render_size(self, value: Literal['NONE', 'SCENE', 'PROXY_25', 'PROXY_50', 'PROXY_75', 'PROXY_100']):
        ...
    @property
    def use_proxies(self) -> bool:
        """Use optimized files for faster scrubbing when available"""
        ...
    @use_proxies.setter
    def use_proxies(self, value: bool):
        ...
    @property
    def use_clamp_view(self) -> bool:
        """Limit timeline height to maximum used channel slot"""
        ...
    @use_clamp_view.setter
    def use_clamp_view(self, value: bool):
        ...
    @property
    def annotation(self) -> Annotated[Optional['Annotation'], "is_animatable=False"]:
        """Annotation data for this Preview region"""
        ...
    @annotation.setter
    def annotation(self, value: Annotated[Optional['Annotation'], "is_animatable=False"]):
        ...
    @property
    def overlay_frame_type(self) -> Literal['RECTANGLE', 'REFERENCE', 'CURRENT']:
        """Overlay display method"""
        ...
    @overlay_frame_type.setter
    def overlay_frame_type(self, value: Literal['RECTANGLE', 'REFERENCE', 'CURRENT']):
        ...
    @property
    def show_transform_preview(self) -> bool:
        """Show a preview of the start or end frame of a strip while transforming its respective handle"""
        ...
    @show_transform_preview.setter
    def show_transform_preview(self, value: bool):
        ...
    @property
    def show_gizmo(self) -> bool:
        """Show gizmos of all types"""
        ...
    @show_gizmo.setter
    def show_gizmo(self, value: bool):
        ...
    @property
    def show_gizmo_navigate(self) -> bool:
        """Viewport navigation gizmo"""
        ...
    @show_gizmo_navigate.setter
    def show_gizmo_navigate(self, value: bool):
        ...
    @property
    def show_gizmo_context(self) -> bool:
        """Context sensitive gizmos for the active item"""
        ...
    @show_gizmo_context.setter
    def show_gizmo_context(self, value: bool):
        ...
    @property
    def show_gizmo_tool(self) -> bool:
        """Active tool gizmo"""
        ...
    @show_gizmo_tool.setter
    def show_gizmo_tool(self, value: bool):
        ...
    @property
    def show_overlays(self) -> bool:

        ...
    @show_overlays.setter
    def show_overlays(self, value: bool):
        ...
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
    @property
    def cursor_location(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """2D cursor location for this view"""
        ...
    @cursor_location.setter
    def cursor_location(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]):
        ...
    @property
    def zoom_percentage(self) -> Annotated[float, "subtype='PERCENTAGE'", "step=100.0", "precision=0"]:
        """Zoom percentage"""
        ...
    @zoom_percentage.setter
    def zoom_percentage(self, value: Annotated[float, "subtype='PERCENTAGE'", "step=100.0", "precision=0"]):
        ...