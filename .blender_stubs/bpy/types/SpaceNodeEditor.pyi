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
    show_locked_time: bool
    """Synchronize the visible timeline range with other time-based editors"""
    show_region_header: bool

    show_region_toolbar: bool

    show_region_ui: bool

    show_region_asset_shelf: bool
    """Display a region with assets that may currently be relevant (such as brushes in paint modes, or poses in Pose Mode)"""
    tree_type: Literal['GeometryNodeTree', 'CompositorNodeTree', 'ShaderNodeTree', 'TextureNodeTree']
    """Node tree type to display and edit"""
    texture_type: Literal['WORLD', 'BRUSH', 'LINESTYLE']
    """Type of data to take texture from"""
    shader_type: Literal['OBJECT', 'WORLD', 'LINESTYLE']
    """Type of data to take shader from"""
    node_tree_sub_type: str

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
    node_tree: Annotated[Optional['NodeTree'], "is_animatable=False"]
    """Base node tree from context"""
    @property
    def edit_tree(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Node tree being displayed and edited"""
        ...
    pin: bool
    """Use the pinned node tree"""
    show_backdrop: bool
    """Use active Viewer Node output as backdrop for compositing nodes"""
    selected_node_group: Annotated[Optional['NodeTree'], "is_animatable=False"]
    """Node group to edit"""
    show_annotation: bool
    """Show annotations for this view"""
    backdrop_zoom: Annotated[float, "step=1.0", "precision=2"]
    """Backdrop zoom factor"""
    backdrop_offset: Annotated[list[float], "step=10.0", "precision=3"]
    """Backdrop offset"""
    backdrop_channels: Literal['COLOR_ALPHA', 'COLOR', 'ALPHA', 'RED', 'GREEN', 'BLUE']
    """Channels of the image to draw"""
    cursor_location: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Location for adding new nodes"""
    insert_offset_direction: Literal['RIGHT', 'LEFT']
    """Direction to offset nodes on insertion"""
    show_gizmo: bool
    """Show gizmos of all types"""
    show_gizmo_active_node: bool
    """Context sensitive gizmo for the active node"""
    @property
    def overlay(self) -> Annotated['SpaceNodeOverlay', "is_animatable=False"]:
        """Settings for display of overlays in the Node Editor"""
        ...
    @property
    def supports_previews(self) -> bool:
        """Whether the node editor's type supports displaying node previews"""
        ...
    def cursor_location_from_region(self, *args, **kwargs) -> Any: ...