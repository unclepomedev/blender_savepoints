# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpacePreferences.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space

class SpacePreferences(Space):

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
    def show_region_ui(self) -> bool:

        ...
    @show_region_ui.setter
    def show_region_ui(self, value: bool):
        ...
    @property
    def filter_type(self) -> Literal['NAME', 'KEY']:
        """Filter method"""
        ...
    @filter_type.setter
    def filter_type(self, value: Literal['NAME', 'KEY']):
        ...
    @property
    def filter_text(self) -> Annotated[str, "is_animatable=False"]:
        """Search term for filtering in the UI"""
        ...
    @filter_text.setter
    def filter_text(self, value: Annotated[str, "is_animatable=False"]):
        ...