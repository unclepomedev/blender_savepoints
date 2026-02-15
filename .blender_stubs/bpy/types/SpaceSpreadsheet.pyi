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
from .SpreadsheetRowFilter import SpreadsheetRowFilter
from .SpreadsheetTable import SpreadsheetTable
from .SpreadsheetTables import SpreadsheetTables
from .ViewerPath import ViewerPath
class SpaceSpreadsheet(Space):
    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    show_locked_time: bool
    """Synchronize the visible timeline range with other time-based editors"""
    show_region_header: bool
    show_region_footer: bool
    show_region_toolbar: bool
    show_region_channels: bool
    show_region_ui: bool
    is_pinned: bool
    """Context path is pinned"""
    show_internal_attributes: bool
    """Display attributes with names starting with a period that are meant for internal use"""
    use_filter: bool
    @property
    def viewer_path(self) -> Annotated[Optional['ViewerPath'], "is_animatable=False"]:
        """Path to the data that is displayed in the spreadsheet"""
        ...
    show_only_selected: bool
    """Only include rows that correspond to selected elements"""
    geometry_component_type: Literal['MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'GREASEPENCIL']
    """Part of the geometry to display data from"""
    attribute_domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']
    """Attribute domain to display"""
    object_eval_state: Literal['EVALUATED', 'ORIGINAL', 'VIEWER_NODE']
    @property
    def tables(self) -> Annotated['SpreadsheetTables', "is_animatable=False"]:
        """Persistent data for the tables shown in this spreadsheet editor"""
        ...
    @property
    def row_filters(self) -> Annotated[bpy_prop_collection['SpreadsheetRowFilter'], "is_animatable=False"]:
        """Filters to remove rows from the displayed data"""
        ...