# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
from .FileBrowserFSMenuEntry import FileBrowserFSMenuEntry
from .FileSelectParams import FileSelectParams
from .Operator import Operator
class SpaceFileBrowser(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    show_region_toolbar: bool
    show_region_tool_props: bool
    show_region_ui: bool
    browse_mode: str
    params: 'FileSelectParams'
    active_operator: 'Operator'
    operator: 'Operator'
    system_folders: bpy_prop_collection['FileBrowserFSMenuEntry']
    system_folders_active: int
    system_bookmarks: bpy_prop_collection['FileBrowserFSMenuEntry']
    system_bookmarks_active: int
    bookmarks: bpy_prop_collection['FileBrowserFSMenuEntry']
    bookmarks_active: int
    recent_folders: bpy_prop_collection['FileBrowserFSMenuEntry']
    recent_folders_active: int
    def activate_asset_by_id(self, *args, **kwargs) -> Any: ...
    def activate_file_by_relative_path(self, *args, **kwargs) -> Any: ...
    def deselect_all(self, *args, **kwargs) -> Any: ...