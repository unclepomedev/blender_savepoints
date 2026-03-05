# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceInfo.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space

class SpaceInfo(Space):

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
    def show_report_debug(self) -> bool:
        """Display debug reporting info"""
        ...
    @show_report_debug.setter
    def show_report_debug(self, value: bool) -> None:
        ...
    @property
    def show_report_info(self) -> bool:
        """Display general information"""
        ...
    @show_report_info.setter
    def show_report_info(self, value: bool) -> None:
        ...
    @property
    def show_report_operator(self) -> bool:
        """Display the operator log"""
        ...
    @show_report_operator.setter
    def show_report_operator(self, value: bool) -> None:
        ...
    @property
    def show_report_warning(self) -> bool:
        """Display warnings"""
        ...
    @show_report_warning.setter
    def show_report_warning(self, value: bool) -> None:
        ...
    @property
    def show_report_error(self) -> bool:
        """Display error text"""
        ...
    @show_report_error.setter
    def show_report_error(self, value: bool) -> None:
        ...