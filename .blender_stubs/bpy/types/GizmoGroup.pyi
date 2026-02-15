# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Gizmo import Gizmo
from .Gizmos import Gizmos
class GizmoGroup(bpy_struct):
    bl_idname: Annotated[str, "is_animatable=False"]
    bl_label: Annotated[str, "is_animatable=False"]
    bl_space_type: Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']
    """The space where the panel is going to be used in"""
    bl_region_type: Literal['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'ASSET_SHELF', 'ASSET_SHELF_HEADER', 'PREVIEW', 'HUD', 'NAVIGATION_BAR', 'EXECUTE', 'FOOTER', 'TOOL_HEADER', 'XR']
    """The region where the panel is going to be used in"""
    bl_owner_id: Annotated[str, "is_animatable=False"]
    bl_options: set[str]
    """Options for this operator type"""
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