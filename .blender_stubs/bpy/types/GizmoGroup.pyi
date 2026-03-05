# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GizmoGroup.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Gizmo import Gizmo
from .Gizmos import Gizmos
from .bpy_prop_collection import bpy_prop_collection

class GizmoGroup(bpy_struct):

    @property
    def bl_idname(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_idname.setter
    def bl_idname(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_label(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_label.setter
    def bl_label(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_space_type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """The space where the panel is going to be used in"""
        ...
    @bl_space_type.setter
    def bl_space_type(self, value: Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']):
        ...
    @property
    def bl_region_type(self) -> Literal['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'ASSET_SHELF', 'ASSET_SHELF_HEADER', 'PREVIEW', 'HUD', 'NAVIGATION_BAR', 'EXECUTE', 'FOOTER', 'TOOL_HEADER', 'XR']:
        """The region where the panel is going to be used in"""
        ...
    @bl_region_type.setter
    def bl_region_type(self, value: Literal['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'ASSET_SHELF', 'ASSET_SHELF_HEADER', 'PREVIEW', 'HUD', 'NAVIGATION_BAR', 'EXECUTE', 'FOOTER', 'TOOL_HEADER', 'XR']):
        ...
    @property
    def bl_owner_id(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_owner_id.setter
    def bl_owner_id(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_options(self) -> set[str]:
        """Options for this operator type"""
        ...
    @bl_options.setter
    def bl_options(self, value: set[str]):
        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @property
    def gizmos(self) -> Annotated['Gizmos', "is_animatable=False"]:
        """List of gizmos in the Gizmo Map"""
        ...
    def poll(self, *args, **kwargs) -> Any: ...
    def setup_keymap(self, *args, **kwargs) -> Any: ...
    def setup(self, *args, **kwargs) -> Any: ...
    def refresh(self, *args, **kwargs) -> Any: ...
    def draw_prepare(self, *args, **kwargs) -> Any: ...
    def invoke_prepare(self, *args, **kwargs) -> Any: ...