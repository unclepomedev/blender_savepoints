# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Area.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .AreaSpaces import AreaSpaces
from .Region import Region
from .Space import Space
from .bpy_prop_collection import bpy_prop_collection

class Area(bpy_struct):

    @property
    def spaces(self) -> Annotated['AreaSpaces', "is_animatable=False"]:
        """Spaces contained in this area, the first being the active space (NOTE: Useful for example to restore a previously used 3D view space in a certain area to get the old view orientation)"""
        ...
    @property
    def regions(self) -> Annotated[bpy_prop_collection['Region'], "is_animatable=False"]:
        """Regions this area is subdivided in"""
        ...
    @property
    def show_menus(self) -> bool:
        """Show menus in the header"""
        ...
    @show_menus.setter
    def show_menus(self, value: bool) -> None:
        ...
    @property
    def type(self) -> Annotated[Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES'], "is_animatable=False"]:
        """Current editor type for this area"""
        ...
    @type.setter
    def type(self, value: Annotated[Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES'], "is_animatable=False"]) -> None:
        ...
    @property
    def ui_type(self) -> Annotated[str, "is_animatable=False"]:
        """Current editor type for this area"""
        ...
    @ui_type.setter
    def ui_type(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def x(self) -> Annotated[int, "step=1"]:
        """The window relative vertical location of the area"""
        ...
    @property
    def y(self) -> Annotated[int, "step=1"]:
        """The window relative horizontal location of the area"""
        ...
    @property
    def width(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Area width"""
        ...
    @property
    def height(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Area height"""
        ...
    def tag_redraw(self, *args, **kwargs) -> Any: ...
    def header_text_set(self, *args, **kwargs) -> Any: ...