# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FILEBROWSER_HT_header.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Header import Header
from .UILayout import UILayout

class FILEBROWSER_HT_header(Header):

    @property
    def layout(self) -> Annotated[Optional['UILayout'], "is_animatable=False"]:
        """Structure of the header in the UI"""
        ...
    @property
    def bl_idname(self) -> Annotated[str, "is_animatable=False"]:
        """If this is set, the header gets a custom ID, otherwise it takes the name of the class used to define the header; for example, if the class name is "OBJECT_HT_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_HT_hello" """
        ...
    @bl_idname.setter
    def bl_idname(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_space_type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """The space where the header is going to be used in"""
        ...
    @bl_space_type.setter
    def bl_space_type(self, value: Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']):
        ...
    @property
    def bl_region_type(self) -> Literal['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'ASSET_SHELF', 'ASSET_SHELF_HEADER', 'PREVIEW', 'HUD', 'NAVIGATION_BAR', 'EXECUTE', 'FOOTER', 'TOOL_HEADER', 'XR']:
        """The region where the header is going to be used in (defaults to header region)"""
        ...
    @bl_region_type.setter
    def bl_region_type(self, value: Literal['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'ASSET_SHELF', 'ASSET_SHELF_HEADER', 'PREVIEW', 'HUD', 'NAVIGATION_BAR', 'EXECUTE', 'FOOTER', 'TOOL_HEADER', 'XR']):
        ...
    def draw(self, *args, **kwargs) -> Any: ...