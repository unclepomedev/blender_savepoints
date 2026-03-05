# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceClipEditor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space
from .Mask import Mask
from .MovieClip import MovieClip
from .MovieClipScopes import MovieClipScopes
from .MovieClipUser import MovieClipUser
from .SpaceClipOverlay import SpaceClipOverlay

class SpaceClipEditor(Space):

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
    def clip(self) -> Annotated[Optional['MovieClip'], "is_animatable=False"]:
        """Movie clip displayed and edited in this space"""
        ...
    @clip.setter
    def clip(self, value: Annotated[Optional['MovieClip'], "is_animatable=False"]):
        ...
    @property
    def clip_user(self) -> Annotated['MovieClipUser', "is_animatable=False"]:
        """Parameters defining which frame of the movie clip is displayed"""
        ...
    @property
    def mask(self) -> Annotated[Optional['Mask'], "is_animatable=False"]:
        """Mask displayed and edited in this space"""
        ...
    @mask.setter
    def mask(self, value: Annotated[Optional['Mask'], "is_animatable=False"]):
        ...
    @property
    def mask_display_type(self) -> Literal['OUTLINE', 'DASH', 'BLACK', 'WHITE']:
        """Display type for mask splines"""
        ...
    @mask_display_type.setter
    def mask_display_type(self, value: Literal['OUTLINE', 'DASH', 'BLACK', 'WHITE']):
        ...
    @property
    def show_mask_spline(self) -> bool:

        ...
    @show_mask_spline.setter
    def show_mask_spline(self, value: bool):
        ...
    @property
    def show_mask_overlay(self) -> bool:

        ...
    @show_mask_overlay.setter
    def show_mask_overlay(self, value: bool):
        ...
    @property
    def mask_overlay_mode(self) -> Literal['ALPHACHANNEL', 'COMBINED']:
        """Overlay mode of rasterized mask"""
        ...
    @mask_overlay_mode.setter
    def mask_overlay_mode(self, value: Literal['ALPHACHANNEL', 'COMBINED']):
        ...
    @property
    def blend_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=1"]:
        """Overlay blending factor of rasterized mask"""
        ...
    @blend_factor.setter
    def blend_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=1"]):
        ...
    @property
    def mode(self) -> Literal['TRACKING', 'MASK']:
        """Editing context being displayed"""
        ...
    @mode.setter
    def mode(self, value: Literal['TRACKING', 'MASK']):
        ...
    @property
    def view(self) -> Literal['CLIP', 'GRAPH', 'DOPESHEET']:
        """Type of the clip editor view"""
        ...
    @view.setter
    def view(self, value: Literal['CLIP', 'GRAPH', 'DOPESHEET']):
        ...
    @property
    def show_marker_pattern(self) -> bool:
        """Show pattern boundbox for markers"""
        ...
    @show_marker_pattern.setter
    def show_marker_pattern(self, value: bool):
        ...
    @property
    def show_marker_search(self) -> bool:
        """Show search boundbox for markers"""
        ...
    @show_marker_search.setter
    def show_marker_search(self, value: bool):
        ...
    @property
    def lock_selection(self) -> bool:
        """Lock viewport to selected markers during playback"""
        ...
    @lock_selection.setter
    def lock_selection(self, value: bool):
        ...
    @property
    def lock_time_cursor(self) -> bool:
        """Lock curves view to time cursor during playback and tracking"""
        ...
    @lock_time_cursor.setter
    def lock_time_cursor(self, value: bool):
        ...
    @property
    def show_track_path(self) -> bool:
        """Show path of how track moves"""
        ...
    @show_track_path.setter
    def show_track_path(self, value: bool):
        ...
    @property
    def path_length(self) -> Annotated[int, "step=1"]:
        """Length of displaying path, in frames"""
        ...
    @path_length.setter
    def path_length(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def show_tiny_markers(self) -> bool:
        """Show markers in a more compact manner"""
        ...
    @show_tiny_markers.setter
    def show_tiny_markers(self, value: bool):
        ...
    @property
    def show_bundles(self) -> bool:
        """Show projection of 3D markers into footage"""
        ...
    @show_bundles.setter
    def show_bundles(self, value: bool):
        ...
    @property
    def use_mute_footage(self) -> bool:
        """Mute footage and show black background instead"""
        ...
    @use_mute_footage.setter
    def use_mute_footage(self, value: bool):
        ...
    @property
    def show_disabled(self) -> bool:
        """Show disabled tracks from the footage"""
        ...
    @show_disabled.setter
    def show_disabled(self, value: bool):
        ...
    @property
    def show_metadata(self) -> bool:
        """Show metadata of clip"""
        ...
    @show_metadata.setter
    def show_metadata(self, value: bool):
        ...
    @property
    def scopes(self) -> Annotated[Optional['MovieClipScopes'], "is_animatable=False"]:
        """Scopes to visualize movie clip statistics"""
        ...
    @property
    def show_names(self) -> bool:
        """Show track names and status"""
        ...
    @show_names.setter
    def show_names(self, value: bool):
        ...
    @property
    def show_grid(self) -> bool:
        """Show grid showing lens distortion"""
        ...
    @show_grid.setter
    def show_grid(self, value: bool):
        ...
    @property
    def show_stable(self) -> bool:
        """Show stable footage in editor (if stabilization is enabled)"""
        ...
    @show_stable.setter
    def show_stable(self, value: bool):
        ...
    @property
    def use_manual_calibration(self) -> bool:
        """Use manual calibration helpers"""
        ...
    @use_manual_calibration.setter
    def use_manual_calibration(self, value: bool):
        ...
    @property
    def show_annotation(self) -> bool:
        """Show annotations for this view"""
        ...
    @show_annotation.setter
    def show_annotation(self, value: bool):
        ...
    @property
    def show_filters(self) -> bool:
        """Show filters for graph editor"""
        ...
    @show_filters.setter
    def show_filters(self, value: bool):
        ...
    @property
    def show_graph_frames(self) -> bool:
        """Show curve for per-frame average error (camera motion should be solved first)"""
        ...
    @show_graph_frames.setter
    def show_graph_frames(self, value: bool):
        ...
    @property
    def show_graph_tracks_motion(self) -> bool:
        """Display speed curves for the selected tracks"""
        ...
    @show_graph_tracks_motion.setter
    def show_graph_tracks_motion(self, value: bool):
        ...
    @property
    def show_graph_tracks_error(self) -> bool:
        """Display the reprojection error curve for selected tracks"""
        ...
    @show_graph_tracks_error.setter
    def show_graph_tracks_error(self, value: bool):
        ...
    @property
    def show_graph_only_selected(self) -> bool:
        """Only include channels relating to selected objects and data"""
        ...
    @show_graph_only_selected.setter
    def show_graph_only_selected(self, value: bool):
        ...
    @property
    def show_graph_hidden(self) -> bool:
        """Include channels from objects/bone that are not visible"""
        ...
    @show_graph_hidden.setter
    def show_graph_hidden(self, value: bool):
        ...
    @property
    def show_red_channel(self) -> bool:
        """Show red channel in the frame"""
        ...
    @show_red_channel.setter
    def show_red_channel(self, value: bool):
        ...
    @property
    def show_green_channel(self) -> bool:
        """Show green channel in the frame"""
        ...
    @show_green_channel.setter
    def show_green_channel(self, value: bool):
        ...
    @property
    def show_blue_channel(self) -> bool:
        """Show blue channel in the frame"""
        ...
    @show_blue_channel.setter
    def show_blue_channel(self, value: bool):
        ...
    @property
    def use_grayscale_preview(self) -> bool:
        """Display frame in grayscale mode"""
        ...
    @use_grayscale_preview.setter
    def use_grayscale_preview(self, value: bool):
        ...
    @property
    def show_seconds(self) -> bool:
        """Show timing as a timecode instead of frames"""
        ...
    @show_seconds.setter
    def show_seconds(self, value: bool):
        ...
    @property
    def annotation_source(self) -> Literal['CLIP', 'TRACK']:
        """Where the annotation comes from"""
        ...
    @annotation_source.setter
    def annotation_source(self, value: Literal['CLIP', 'TRACK']):
        ...
    @property
    def cursor_location(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """2D cursor location for this view"""
        ...
    @cursor_location.setter
    def cursor_location(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]):
        ...
    @property
    def pivot_point(self) -> Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT']:
        """Pivot center for rotation/scaling"""
        ...
    @pivot_point.setter
    def pivot_point(self, value: Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT']):
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
    def zoom_percentage(self) -> Annotated[float, "subtype='PERCENTAGE'", "step=100.0", "precision=0"]:
        """Zoom percentage"""
        ...
    @zoom_percentage.setter
    def zoom_percentage(self, value: Annotated[float, "subtype='PERCENTAGE'", "step=100.0", "precision=0"]):
        ...
    @property
    def overlay(self) -> Annotated['SpaceClipOverlay', "is_animatable=False"]:
        """Settings for display of overlays in the Movie Clip editor"""
        ...