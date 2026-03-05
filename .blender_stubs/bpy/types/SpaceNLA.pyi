# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceNLA.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space
from .DopeSheet import DopeSheet

class SpaceNLA(Space):

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
    def show_region_footer(self) -> bool:

        ...
    @show_region_footer.setter
    def show_region_footer(self, value: bool):
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
    def show_seconds(self) -> bool:
        """Show timing as a timecode instead of frames"""
        ...
    @show_seconds.setter
    def show_seconds(self, value: bool):
        ...
    @property
    def show_strip_curves(self) -> bool:
        """Show influence F-Curves on strips"""
        ...
    @show_strip_curves.setter
    def show_strip_curves(self, value: bool):
        ...
    @property
    def show_local_markers(self) -> bool:
        """Show action-local markers on the strips, useful when synchronizing timing across strips"""
        ...
    @show_local_markers.setter
    def show_local_markers(self, value: bool):
        ...
    @property
    def show_markers(self) -> bool:
        """If any exists, show markers in a separate row at the bottom of the editor"""
        ...
    @show_markers.setter
    def show_markers(self, value: bool):
        ...
    @property
    def use_realtime_update(self) -> bool:
        """When transforming strips, changes to the animation data are flushed to other views"""
        ...
    @use_realtime_update.setter
    def use_realtime_update(self, value: bool):
        ...
    @property
    def dopesheet(self) -> Annotated[Optional['DopeSheet'], "is_animatable=False"]:
        """Settings for filtering animation data"""
        ...