# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceGraphEditor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space
from .DopeSheet import DopeSheet

class SpaceGraphEditor(Space):

    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    show_locked_time: bool
    """Synchronize the visible timeline range with other time-based editors"""
    show_region_header: bool

    show_region_footer: bool

    show_region_channels: bool

    show_region_ui: bool

    show_region_hud: bool

    mode: Literal['FCURVES', 'DRIVERS']
    """Editing context being displayed"""
    show_seconds: bool
    """Show timing as a timecode instead of frames"""
    show_sliders: bool
    """Show sliders beside F-Curve channels"""
    show_handles: bool
    """Show handles of Bézier control points"""
    use_auto_lock_translation_axis: bool
    """Automatically locks the movement of keyframes to the dominant axis"""
    use_only_selected_keyframe_handles: bool
    """Only show and edit handles of selected keyframes"""
    show_markers: bool
    """If any exists, show markers in a separate row at the bottom of the editor"""
    show_extrapolation: bool

    use_auto_merge_keyframes: bool
    """Automatically merge nearby keyframes"""
    use_realtime_update: bool
    """When transforming keyframes, changes to the animation data are flushed to other views"""
    show_cursor: bool
    """Show 2D cursor"""
    cursor_position_x: Annotated[float, "step=10.0", "precision=3"]
    """Graph Editor 2D-Value cursor - X-Value component"""
    cursor_position_y: Annotated[float, "step=10.0", "precision=3"]
    """Graph Editor 2D-Value cursor - Y-Value component"""
    pivot_point: Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS']
    """Pivot center for rotation/scaling"""
    @property
    def dopesheet(self) -> Annotated[Optional['DopeSheet'], "is_animatable=False"]:
        """Settings for filtering animation data"""
        ...
    @property
    def has_ghost_curves(self) -> bool:
        """Graph Editor instance has some ghost curves stored"""
        ...
    use_normalization: bool
    """Display curves in normalized range from -1 to 1, for easier editing of multiple curves with different ranges"""
    use_auto_normalization: bool
    """Automatically recalculate curve normalization on every curve edit"""