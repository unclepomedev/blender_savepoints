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
from .ConsoleLine import ConsoleLine
class SpaceConsole(Space):
    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    show_locked_time: bool
    """Synchronize the visible timeline range with other time-based editors"""
    show_region_header: bool
    font_size: Annotated[int, "step=1"]
    """Font size to use for displaying the text"""
    select_start: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    select_end: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    prompt: Annotated[str, "is_animatable=False"]
    """Command line prompt"""
    language: Annotated[str, "is_animatable=False"]
    """Command line prompt language"""
    @property
    def history(self) -> Annotated[bpy_prop_collection['ConsoleLine'], "is_animatable=False"]:
        """Command history"""
        ...
    @property
    def scrollback(self) -> Annotated[bpy_prop_collection['ConsoleLine'], "is_animatable=False"]:
        """Command output"""
        ...