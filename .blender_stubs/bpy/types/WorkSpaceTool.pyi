# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.WorkSpaceTool.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class WorkSpaceTool(bpy_struct):

    @property
    def idname(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @idname.setter
    def idname(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def idname_fallback(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @idname_fallback.setter
    def idname_fallback(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def index(self) -> Annotated[int, "step=1"]:

        ...
    @property
    def space_type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:

        ...
    @property
    def mode(self) -> Literal['DEFAULT']:

        ...
    @property
    def use_paint_canvas(self) -> bool:
        """Does this tool use a painting canvas"""
        ...
    @property
    def has_datablock(self) -> bool:

        ...
    @property
    def use_brushes(self) -> bool:

        ...
    @property
    def brush_type(self) -> Literal['DEFAULT']:
        """If the tool uses brushes and is limited to a specific brush type, the identifier of the brush type"""
        ...
    @property
    def widget(self) -> Annotated[str, "is_animatable=False"]:

        ...
    def setup(self, *args, **kwargs) -> Any: ...
    def operator_properties(self, *args, **kwargs) -> Any: ...
    def gizmo_group_properties(self, *args, **kwargs) -> Any: ...
    def refresh_from_context(self, *args, **kwargs) -> Any: ...