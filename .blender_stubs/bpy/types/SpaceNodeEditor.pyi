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
from .ID import ID
from .NodeTree import NodeTree
from .NodeTreePath import NodeTreePath
from .SpaceNodeOverlay import SpaceNodeOverlay
class SpaceNodeEditor(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    show_region_toolbar: bool
    show_region_ui: bool
    show_region_asset_shelf: bool
    tree_type: str
    texture_type: str
    shader_type: str
    node_tree_sub_type: str
    id: 'ID'
    id_from: 'ID'
    path: bpy_prop_collection['NodeTreePath']
    node_tree: 'NodeTree'
    edit_tree: 'NodeTree'
    pin: bool
    show_backdrop: bool
    selected_node_group: 'NodeTree'
    show_annotation: bool
    backdrop_zoom: float
    backdrop_offset: list[float]
    backdrop_channels: str
    cursor_location: list[float]
    insert_offset_direction: str
    show_gizmo: bool
    show_gizmo_active_node: bool
    overlay: 'SpaceNodeOverlay'
    supports_previews: bool
    def cursor_location_from_region(self, *args, **kwargs) -> Any: ...