# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceConsole.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space
from .ConsoleLine import ConsoleLine
from .bpy_prop_collection import bpy_prop_collection

class SpaceConsole(Space):

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
    def font_size(self) -> Annotated[int, "step=1"]:
        """Font size to use for displaying the text"""
        ...
    @font_size.setter
    def font_size(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def select_start(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:

        ...
    @select_start.setter
    def select_start(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def select_end(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:

        ...
    @select_end.setter
    def select_end(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def prompt(self) -> Annotated[str, "is_animatable=False"]:
        """Command line prompt"""
        ...
    @prompt.setter
    def prompt(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def language(self) -> Annotated[str, "is_animatable=False"]:
        """Command line prompt language"""
        ...
    @language.setter
    def language(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def history(self) -> Annotated[bpy_prop_collection['ConsoleLine'], "is_animatable=False"]:
        """Command history"""
        ...
    @property
    def scrollback(self) -> Annotated[bpy_prop_collection['ConsoleLine'], "is_animatable=False"]:
        """Command output"""
        ...