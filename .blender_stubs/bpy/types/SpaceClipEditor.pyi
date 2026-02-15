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
    show_locked_time: bool
    """Synchronize the visible timeline range with other time-based editors"""
    show_region_header: bool

    show_region_toolbar: bool

    show_region_channels: bool

    show_region_ui: bool

    show_region_hud: bool

    clip: Annotated[Optional['MovieClip'], "is_animatable=False"]
    """Movie clip displayed and edited in this space"""
    @property
    def clip_user(self) -> Annotated['MovieClipUser', "is_animatable=False"]:
        """Parameters defining which frame of the movie clip is displayed"""
        ...
    mask: Annotated[Optional['Mask'], "is_animatable=False"]
    """Mask displayed and edited in this space"""
    mask_display_type: Literal['OUTLINE', 'DASH', 'BLACK', 'WHITE']
    """Display type for mask splines"""
    show_mask_spline: bool

    show_mask_overlay: bool

    mask_overlay_mode: Literal['ALPHACHANNEL', 'COMBINED']
    """Overlay mode of rasterized mask"""
    blend_factor: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=1"]
    """Overlay blending factor of rasterized mask"""
    mode: Literal['TRACKING', 'MASK']
    """Editing context being displayed"""
    view: Literal['CLIP', 'GRAPH', 'DOPESHEET']
    """Type of the clip editor view"""
    show_marker_pattern: bool
    """Show pattern boundbox for markers"""
    show_marker_search: bool
    """Show search boundbox for markers"""
    lock_selection: bool
    """Lock viewport to selected markers during playback"""
    lock_time_cursor: bool
    """Lock curves view to time cursor during playback and tracking"""
    show_track_path: bool
    """Show path of how track moves"""
    path_length: Annotated[int, "step=1"]
    """Length of displaying path, in frames"""
    show_tiny_markers: bool
    """Show markers in a more compact manner"""
    show_bundles: bool
    """Show projection of 3D markers into footage"""
    use_mute_footage: bool
    """Mute footage and show black background instead"""
    show_disabled: bool
    """Show disabled tracks from the footage"""
    show_metadata: bool
    """Show metadata of clip"""
    @property
    def scopes(self) -> Annotated[Optional['MovieClipScopes'], "is_animatable=False"]:
        """Scopes to visualize movie clip statistics"""
        ...
    show_names: bool
    """Show track names and status"""
    show_grid: bool
    """Show grid showing lens distortion"""
    show_stable: bool
    """Show stable footage in editor (if stabilization is enabled)"""
    use_manual_calibration: bool
    """Use manual calibration helpers"""
    show_annotation: bool
    """Show annotations for this view"""
    show_filters: bool
    """Show filters for graph editor"""
    show_graph_frames: bool
    """Show curve for per-frame average error (camera motion should be solved first)"""
    show_graph_tracks_motion: bool
    """Display speed curves for the selected tracks"""
    show_graph_tracks_error: bool
    """Display the reprojection error curve for selected tracks"""
    show_graph_only_selected: bool
    """Only include channels relating to selected objects and data"""
    show_graph_hidden: bool
    """Include channels from objects/bone that are not visible"""
    show_red_channel: bool
    """Show red channel in the frame"""
    show_green_channel: bool
    """Show green channel in the frame"""
    show_blue_channel: bool
    """Show blue channel in the frame"""
    use_grayscale_preview: bool
    """Display frame in grayscale mode"""
    show_seconds: bool
    """Show timing as a timecode instead of frames"""
    annotation_source: Literal['CLIP', 'TRACK']
    """Where the annotation comes from"""
    cursor_location: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """2D cursor location for this view"""
    pivot_point: Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT']
    """Pivot center for rotation/scaling"""
    show_gizmo: bool
    """Show gizmos of all types"""
    show_gizmo_navigate: bool
    """Viewport navigation gizmo"""
    zoom_percentage: Annotated[float, "subtype='PERCENTAGE'", "step=100.0", "precision=0"]
    """Zoom percentage"""
    @property
    def overlay(self) -> Annotated['SpaceClipOverlay', "is_animatable=False"]:
        """Settings for display of overlays in the Movie Clip editor"""
        ...