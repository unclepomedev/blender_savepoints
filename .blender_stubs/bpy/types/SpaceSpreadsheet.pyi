# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
from .SpreadsheetRowFilter import SpreadsheetRowFilter
from .SpreadsheetTable import SpreadsheetTable
from .ViewerPath import ViewerPath
class SpaceSpreadsheet(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    show_region_footer: bool
    show_region_toolbar: bool
    show_region_channels: bool
    show_region_ui: bool
    is_pinned: bool
    show_internal_attributes: bool
    use_filter: bool
    viewer_path: 'ViewerPath'
    show_only_selected: bool
    geometry_item_type: str
    geometry_component_type: str
    attribute_domain: str
    object_eval_state: str
    tables: bpy_prop_collection['SpreadsheetTable']
    row_filters: bpy_prop_collection['SpreadsheetRowFilter']