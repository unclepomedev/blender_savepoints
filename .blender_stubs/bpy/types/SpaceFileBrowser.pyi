# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceFileBrowser.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space
from .FileBrowserFSMenuEntry import FileBrowserFSMenuEntry
from .FileSelectParams import FileSelectParams
from .Operator import Operator
from .bpy_prop_collection import bpy_prop_collection

class SpaceFileBrowser(Space):

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
    def show_region_toolbar(self) -> bool:

        ...
    @show_region_toolbar.setter
    def show_region_toolbar(self, value: bool) -> None:
        ...
    @property
    def show_region_tool_props(self) -> bool:

        ...
    @show_region_tool_props.setter
    def show_region_tool_props(self, value: bool) -> None:
        ...
    @property
    def show_region_ui(self) -> bool:

        ...
    @show_region_ui.setter
    def show_region_ui(self, value: bool) -> None:
        ...
    @property
    def browse_mode(self) -> Literal['FILES', 'ASSETS']:
        """Type of the File Editor view (regular file browsing or asset browsing)"""
        ...
    @browse_mode.setter
    def browse_mode(self, value: Literal['FILES', 'ASSETS']) -> None:
        ...
    @property
    def params(self) -> Annotated[Optional['FileSelectParams'], "is_animatable=False"]:
        """Parameters and Settings for the Filebrowser"""
        ...
    @property
    def active_operator(self) -> Annotated[Optional['Operator'], "is_animatable=False"]:

        ...
    @property
    def operator(self) -> Annotated[Optional['Operator'], "is_animatable=False"]:

        ...
    @property
    def system_folders(self) -> Annotated[bpy_prop_collection['FileBrowserFSMenuEntry'], "is_animatable=False"]:
        """System's folders (usually root, available hard drives, etc)"""
        ...
    @property
    def system_folders_active(self) -> Annotated[int, "step=1"]:
        """Index of active system folder (-1 if none)"""
        ...
    @system_folders_active.setter
    def system_folders_active(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def system_bookmarks(self) -> Annotated[bpy_prop_collection['FileBrowserFSMenuEntry'], "is_animatable=False"]:
        """System's bookmarks"""
        ...
    @property
    def system_bookmarks_active(self) -> Annotated[int, "step=1"]:
        """Index of active system bookmark (-1 if none)"""
        ...
    @system_bookmarks_active.setter
    def system_bookmarks_active(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def bookmarks(self) -> Annotated[bpy_prop_collection['FileBrowserFSMenuEntry'], "is_animatable=False"]:
        """User's bookmarks"""
        ...
    @bookmarks.setter
    def bookmarks(self, value: Annotated[bpy_prop_collection['FileBrowserFSMenuEntry'], "is_animatable=False"]) -> None:
        ...
    @property
    def bookmarks_active(self) -> Annotated[int, "step=1"]:
        """Index of active bookmark (-1 if none)"""
        ...
    @bookmarks_active.setter
    def bookmarks_active(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def recent_folders(self) -> Annotated[bpy_prop_collection['FileBrowserFSMenuEntry'], "is_animatable=False"]:

        ...
    @recent_folders.setter
    def recent_folders(self, value: Annotated[bpy_prop_collection['FileBrowserFSMenuEntry'], "is_animatable=False"]) -> None:
        ...
    @property
    def recent_folders_active(self) -> Annotated[int, "step=1"]:
        """Index of active recent folder (-1 if none)"""
        ...
    @recent_folders_active.setter
    def recent_folders_active(self, value: Annotated[int, "step=1"]) -> None:
        ...
    def activate_asset_by_id(self, *args, **kwargs) -> Any: ...
    def activate_file_by_relative_path(self, *args, **kwargs) -> Any: ...
    def deselect_all(self, *args, **kwargs) -> Any: ...