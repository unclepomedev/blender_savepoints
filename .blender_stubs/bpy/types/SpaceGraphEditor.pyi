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
    @property
    def show_locked_time(self) -> bool:
        """Synchronize the visible timeline range with other time-based editors"""
        ...
    @show_locked_time.setter
    def show_locked_time(self, value: bool) -> None:
        ...
    @property
    def show_region_header(self) -> bool:

        ...
    @show_region_header.setter
    def show_region_header(self, value: bool) -> None:
        ...
    @property
    def show_region_footer(self) -> bool:

        ...
    @show_region_footer.setter
    def show_region_footer(self, value: bool) -> None:
        ...
    @property
    def show_region_channels(self) -> bool:

        ...
    @show_region_channels.setter
    def show_region_channels(self, value: bool) -> None:
        ...
    @property
    def show_region_ui(self) -> bool:

        ...
    @show_region_ui.setter
    def show_region_ui(self, value: bool) -> None:
        ...
    @property
    def show_region_hud(self) -> bool:

        ...
    @show_region_hud.setter
    def show_region_hud(self, value: bool) -> None:
        ...
    @property
    def mode(self) -> Literal['FCURVES', 'DRIVERS']:
        """Editing context being displayed"""
        ...
    @mode.setter
    def mode(self, value: Literal['FCURVES', 'DRIVERS']) -> None:
        ...
    @property
    def show_seconds(self) -> bool:
        """Show timing as a timecode instead of frames"""
        ...
    @show_seconds.setter
    def show_seconds(self, value: bool) -> None:
        ...
    @property
    def show_sliders(self) -> bool:
        """Show sliders beside F-Curve channels"""
        ...
    @show_sliders.setter
    def show_sliders(self, value: bool) -> None:
        ...
    @property
    def show_handles(self) -> bool:
        """Show handles of Bézier control points"""
        ...
    @show_handles.setter
    def show_handles(self, value: bool) -> None:
        ...
    @property
    def use_auto_lock_translation_axis(self) -> bool:
        """Automatically locks the movement of keyframes to the dominant axis"""
        ...
    @use_auto_lock_translation_axis.setter
    def use_auto_lock_translation_axis(self, value: bool) -> None:
        ...
    @property
    def use_only_selected_keyframe_handles(self) -> bool:
        """Only show and edit handles of selected keyframes"""
        ...
    @use_only_selected_keyframe_handles.setter
    def use_only_selected_keyframe_handles(self, value: bool) -> None:
        ...
    @property
    def show_markers(self) -> bool:
        """If any exists, show markers in a separate row at the bottom of the editor"""
        ...
    @show_markers.setter
    def show_markers(self, value: bool) -> None:
        ...
    @property
    def show_extrapolation(self) -> bool:

        ...
    @show_extrapolation.setter
    def show_extrapolation(self, value: bool) -> None:
        ...
    @property
    def use_auto_merge_keyframes(self) -> bool:
        """Automatically merge nearby keyframes"""
        ...
    @use_auto_merge_keyframes.setter
    def use_auto_merge_keyframes(self, value: bool) -> None:
        ...
    @property
    def use_realtime_update(self) -> bool:
        """When transforming keyframes, changes to the animation data are flushed to other views"""
        ...
    @use_realtime_update.setter
    def use_realtime_update(self, value: bool) -> None:
        ...
    @property
    def show_cursor(self) -> bool:
        """Show 2D cursor"""
        ...
    @show_cursor.setter
    def show_cursor(self, value: bool) -> None:
        ...
    @property
    def cursor_position_x(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Graph Editor 2D-Value cursor - X-Value component"""
        ...
    @cursor_position_x.setter
    def cursor_position_x(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def cursor_position_y(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Graph Editor 2D-Value cursor - Y-Value component"""
        ...
    @cursor_position_y.setter
    def cursor_position_y(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def pivot_point(self) -> Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS']:
        """Pivot center for rotation/scaling"""
        ...
    @pivot_point.setter
    def pivot_point(self, value: Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS']) -> None:
        ...
    @property
    def dopesheet(self) -> Annotated[Optional['DopeSheet'], "is_animatable=False"]:
        """Settings for filtering animation data"""
        ...
    @property
    def has_ghost_curves(self) -> bool:
        """Graph Editor instance has some ghost curves stored"""
        ...
    @property
    def use_normalization(self) -> bool:
        """Display curves in normalized range from -1 to 1, for easier editing of multiple curves with different ranges"""
        ...
    @use_normalization.setter
    def use_normalization(self, value: bool) -> None:
        ...
    @property
    def use_auto_normalization(self) -> bool:
        """Automatically recalculate curve normalization on every curve edit"""
        ...
    @use_auto_normalization.setter
    def use_auto_normalization(self, value: bool) -> None:
        ...