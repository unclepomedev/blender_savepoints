# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceNodeEditor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space
from .ID import ID
from .NodeTree import NodeTree
from .NodeTreePath import NodeTreePath
from .SpaceNodeEditorPath import SpaceNodeEditorPath
from .SpaceNodeOverlay import SpaceNodeOverlay
from .bpy_prop_collection import bpy_prop_collection

class SpaceNodeEditor(Space):

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
    def show_region_toolbar(self) -> bool:

        ...
    @show_region_toolbar.setter
    def show_region_toolbar(self, value: bool):
        ...
    @property
    def show_region_ui(self) -> bool:

        ...
    @show_region_ui.setter
    def show_region_ui(self, value: bool):
        ...
    @property
    def show_region_asset_shelf(self) -> bool:
        """Display a region with assets that may currently be relevant (such as brushes in paint modes, or poses in Pose Mode)"""
        ...
    @show_region_asset_shelf.setter
    def show_region_asset_shelf(self, value: bool):
        ...
    @property
    def tree_type(self) -> Literal['GeometryNodeTree', 'CompositorNodeTree', 'ShaderNodeTree', 'TextureNodeTree']:
        """Node tree type to display and edit"""
        ...
    @tree_type.setter
    def tree_type(self, value: Literal['GeometryNodeTree', 'CompositorNodeTree', 'ShaderNodeTree', 'TextureNodeTree']):
        ...
    @property
    def texture_type(self) -> Literal['WORLD', 'BRUSH', 'LINESTYLE']:
        """Type of data to take texture from"""
        ...
    @texture_type.setter
    def texture_type(self, value: Literal['WORLD', 'BRUSH', 'LINESTYLE']):
        ...
    @property
    def shader_type(self) -> Literal['OBJECT', 'WORLD', 'LINESTYLE']:
        """Type of data to take shader from"""
        ...
    @shader_type.setter
    def shader_type(self, value: Literal['OBJECT', 'WORLD', 'LINESTYLE']):
        ...
    @property
    def node_tree_sub_type(self) -> str:

        ...
    @node_tree_sub_type.setter
    def node_tree_sub_type(self, value: str):
        ...
    @property
    def id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """Data-block whose nodes are being edited"""
        ...
    @property
    def id_from(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """Data-block from which the edited data-block is linked"""
        ...
    @property
    def path(self) -> Annotated['SpaceNodeEditorPath', "is_animatable=False"]:
        """Path from the data-block to the currently edited node tree"""
        ...
    @property
    def node_tree(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Base node tree from context"""
        ...
    @node_tree.setter
    def node_tree(self, value: Annotated[Optional['NodeTree'], "is_animatable=False"]):
        ...
    @property
    def edit_tree(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Node tree being displayed and edited"""
        ...
    @property
    def pin(self) -> bool:
        """Use the pinned node tree"""
        ...
    @pin.setter
    def pin(self, value: bool):
        ...
    @property
    def show_backdrop(self) -> bool:
        """Use active Viewer Node output as backdrop for compositing nodes"""
        ...
    @show_backdrop.setter
    def show_backdrop(self, value: bool):
        ...
    @property
    def selected_node_group(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Node group to edit"""
        ...
    @selected_node_group.setter
    def selected_node_group(self, value: Annotated[Optional['NodeTree'], "is_animatable=False"]):
        ...
    @property
    def show_annotation(self) -> bool:
        """Show annotations for this view"""
        ...
    @show_annotation.setter
    def show_annotation(self, value: bool):
        ...
    @property
    def backdrop_zoom(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Backdrop zoom factor"""
        ...
    @backdrop_zoom.setter
    def backdrop_zoom(self, value: Annotated[float, "step=1.0", "precision=2"]):
        ...
    @property
    def backdrop_offset(self) -> Annotated[list[float], "step=10.0", "precision=3"]:
        """Backdrop offset"""
        ...
    @backdrop_offset.setter
    def backdrop_offset(self, value: Annotated[list[float], "step=10.0", "precision=3"]):
        ...
    @property
    def backdrop_channels(self) -> Literal['COLOR_ALPHA', 'COLOR', 'ALPHA', 'RED', 'GREEN', 'BLUE']:
        """Channels of the image to draw"""
        ...
    @backdrop_channels.setter
    def backdrop_channels(self, value: Literal['COLOR_ALPHA', 'COLOR', 'ALPHA', 'RED', 'GREEN', 'BLUE']):
        ...
    @property
    def cursor_location(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Location for adding new nodes"""
        ...
    @cursor_location.setter
    def cursor_location(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]):
        ...
    @property
    def insert_offset_direction(self) -> Literal['RIGHT', 'LEFT']:
        """Direction to offset nodes on insertion"""
        ...
    @insert_offset_direction.setter
    def insert_offset_direction(self, value: Literal['RIGHT', 'LEFT']):
        ...
    @property
    def show_gizmo(self) -> bool:
        """Show gizmos of all types"""
        ...
    @show_gizmo.setter
    def show_gizmo(self, value: bool):
        ...
    @property
    def show_gizmo_active_node(self) -> bool:
        """Context sensitive gizmo for the active node"""
        ...
    @show_gizmo_active_node.setter
    def show_gizmo_active_node(self, value: bool):
        ...
    @property
    def overlay(self) -> Annotated['SpaceNodeOverlay', "is_animatable=False"]:
        """Settings for display of overlays in the Node Editor"""
        ...
    @property
    def supports_previews(self) -> bool:
        """Whether the node editor's type supports displaying node previews"""
        ...
    def cursor_location_from_region(self, *args, **kwargs) -> Any: ...