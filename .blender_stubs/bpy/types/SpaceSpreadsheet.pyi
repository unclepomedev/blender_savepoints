# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceSpreadsheet.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space
from .SpreadsheetRowFilter import SpreadsheetRowFilter
from .SpreadsheetTable import SpreadsheetTable
from .SpreadsheetTables import SpreadsheetTables
from .ViewerPath import ViewerPath
from .bpy_prop_collection import bpy_prop_collection

class SpaceSpreadsheet(Space):

    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    @property
    def show_locked_time(self) -> bool:
        """Synchronize the visible timeline range with other time-based editors"""
        ...
    @show_locked_time.setter
    def show_locked_time(self, value: bool):
        ...
    @property
    def show_region_header(self) -> bool:

        ...
    @show_region_header.setter
    def show_region_header(self, value: bool):
        ...
    @property
    def show_region_footer(self) -> bool:

        ...
    @show_region_footer.setter
    def show_region_footer(self, value: bool):
        ...
    @property
    def show_region_toolbar(self) -> bool:

        ...
    @show_region_toolbar.setter
    def show_region_toolbar(self, value: bool):
        ...
    @property
    def show_region_channels(self) -> bool:

        ...
    @show_region_channels.setter
    def show_region_channels(self, value: bool):
        ...
    @property
    def show_region_ui(self) -> bool:

        ...
    @show_region_ui.setter
    def show_region_ui(self, value: bool):
        ...
    @property
    def is_pinned(self) -> bool:
        """Context path is pinned"""
        ...
    @is_pinned.setter
    def is_pinned(self, value: bool):
        ...
    @property
    def show_internal_attributes(self) -> bool:
        """Display attributes with names starting with a period that are meant for internal use"""
        ...
    @show_internal_attributes.setter
    def show_internal_attributes(self, value: bool):
        ...
    @property
    def use_filter(self) -> bool:

        ...
    @use_filter.setter
    def use_filter(self, value: bool):
        ...
    @property
    def viewer_path(self) -> Annotated[Optional['ViewerPath'], "is_animatable=False"]:
        """Path to the data that is displayed in the spreadsheet"""
        ...
    @property
    def show_only_selected(self) -> bool:
        """Only include rows that correspond to selected elements"""
        ...
    @show_only_selected.setter
    def show_only_selected(self, value: bool):
        ...
    @property
    def geometry_component_type(self) -> Literal['MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'GREASEPENCIL']:
        """Part of the geometry to display data from"""
        ...
    @geometry_component_type.setter
    def geometry_component_type(self, value: Literal['MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'GREASEPENCIL']):
        ...
    @property
    def attribute_domain(self) -> Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']:
        """Attribute domain to display"""
        ...
    @attribute_domain.setter
    def attribute_domain(self, value: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']):
        ...
    @property
    def object_eval_state(self) -> Literal['EVALUATED', 'ORIGINAL', 'VIEWER_NODE']:

        ...
    @object_eval_state.setter
    def object_eval_state(self, value: Literal['EVALUATED', 'ORIGINAL', 'VIEWER_NODE']):
        ...
    @property
    def tables(self) -> Annotated['SpreadsheetTables', "is_animatable=False"]:
        """Persistent data for the tables shown in this spreadsheet editor"""
        ...
    @property
    def row_filters(self) -> Annotated[bpy_prop_collection['SpreadsheetRowFilter'], "is_animatable=False"]:
        """Filters to remove rows from the displayed data"""
        ...