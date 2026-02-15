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
from .FileBrowserFSMenuEntry import FileBrowserFSMenuEntry
from .FileSelectParams import FileSelectParams
from .Operator import Operator
class SpaceFileBrowser(Space):
    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    show_locked_time: bool
    """Synchronize the visible timeline range with other time-based editors"""
    show_region_header: bool
    show_region_toolbar: bool
    show_region_tool_props: bool
    show_region_ui: bool
    browse_mode: Literal['FILES', 'ASSETS']
    """Type of the File Editor view (regular file browsing or asset browsing)"""
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
    system_folders_active: Annotated[int, "step=1"]
    """Index of active system folder (-1 if none)"""
    @property
    def system_bookmarks(self) -> Annotated[bpy_prop_collection['FileBrowserFSMenuEntry'], "is_animatable=False"]:
        """System's bookmarks"""
        ...
    system_bookmarks_active: Annotated[int, "step=1"]
    """Index of active system bookmark (-1 if none)"""
    bookmarks: Annotated[bpy_prop_collection['FileBrowserFSMenuEntry'], "is_animatable=False"]
    """User's bookmarks"""
    bookmarks_active: Annotated[int, "step=1"]
    """Index of active bookmark (-1 if none)"""
    recent_folders: Annotated[bpy_prop_collection['FileBrowserFSMenuEntry'], "is_animatable=False"]
    recent_folders_active: Annotated[int, "step=1"]
    """Index of active recent folder (-1 if none)"""
    def activate_asset_by_id(self, *args, **kwargs) -> Any: ...
    def activate_file_by_relative_path(self, *args, **kwargs) -> Any: ...
    def deselect_all(self, *args, **kwargs) -> Any: ...