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
from .Area import Area
from .AssetRepresentation import AssetRepresentation
from .BlendData import BlendData
from .Collection import Collection
from .GizmoGroup import GizmoGroup
from .LayerCollection import LayerCollection
from .Preferences import Preferences
from .Region import Region
from .RegionView3D import RegionView3D
from .Scene import Scene
from .Screen import Screen
from .Space import Space
from .ToolSettings import ToolSettings
from .ViewLayer import ViewLayer
from .Window import Window
from .WindowManager import WindowManager
from .WorkSpace import WorkSpace
class Context(bpy_struct):
    @property
    def window_manager(self) -> Annotated[Optional['WindowManager'], "is_animatable=False"]:
        ...
    @property
    def window(self) -> Annotated[Optional['Window'], "is_animatable=False"]:
        ...
    @property
    def workspace(self) -> Annotated[Optional['WorkSpace'], "is_animatable=False"]:
        ...
    @property
    def screen(self) -> Annotated[Optional['Screen'], "is_animatable=False"]:
        ...
    @property
    def area(self) -> Annotated[Optional['Area'], "is_animatable=False"]:
        ...
    @property
    def space_data(self) -> Annotated[Optional['Space'], "is_animatable=False"]:
        """The current space, may be None in background-mode, when the cursor is outside the window or when using menu-search"""
        ...
    @property
    def region(self) -> Annotated[Optional['Region'], "is_animatable=False"]:
        ...
    @property
    def region_popup(self) -> Annotated[Optional['Region'], "is_animatable=False"]:
        """The temporary region for pop-ups (including menus and pop-overs)"""
        ...
    @property
    def region_data(self) -> Annotated[Optional['RegionView3D'], "is_animatable=False"]:
        ...
    @property
    def gizmo_group(self) -> Annotated[Optional['GizmoGroup'], "is_animatable=False"]:
        ...
    @property
    def asset(self) -> Annotated[Optional['AssetRepresentation'], "is_animatable=False"]:
        ...
    @property
    def blend_data(self) -> Annotated[Optional['BlendData'], "is_animatable=False"]:
        ...
    @property
    def scene(self) -> Annotated[Optional['Scene'], "is_animatable=False"]:
        ...
    @property
    def view_layer(self) -> Annotated[Optional['ViewLayer'], "is_animatable=False"]:
        ...
    @property
    def engine(self) -> Annotated[str, "is_animatable=False"]:
        ...
    @property
    def collection(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        ...
    @property
    def layer_collection(self) -> Annotated[Optional['LayerCollection'], "is_animatable=False"]:
        ...
    @property
    def tool_settings(self) -> Annotated[Optional['ToolSettings'], "is_animatable=False"]:
        ...
    @property
    def preferences(self) -> Annotated[Optional['Preferences'], "is_animatable=False"]:
        ...
    @property
    def mode(self) -> Literal['EDIT_MESH', 'EDIT_CURVE', 'EDIT_CURVES', 'EDIT_SURFACE', 'EDIT_TEXT', 'EDIT_ARMATURE', 'EDIT_METABALL', 'EDIT_LATTICE', 'EDIT_GREASE_PENCIL', 'EDIT_POINTCLOUD', 'POSE', 'SCULPT', 'PAINT_WEIGHT', 'PAINT_VERTEX', 'PAINT_TEXTURE', 'PARTICLE', 'OBJECT', 'PAINT_GPENCIL', 'EDIT_GPENCIL', 'SCULPT_GPENCIL', 'WEIGHT_GPENCIL', 'VERTEX_GPENCIL', 'SCULPT_CURVES', 'PAINT_GREASE_PENCIL', 'SCULPT_GREASE_PENCIL', 'WEIGHT_GREASE_PENCIL', 'VERTEX_GREASE_PENCIL']:
        ...
    def evaluated_depsgraph_get(self, *args, **kwargs) -> Any: ...
    # --- Injected Methods ---
    selected_objects: list[Any]
    active_object: Any
    view_layer: Any
    scene: Any
    screen: Any
    area: Any
    region: Any
    window: Any
    window_manager: Any
    preferences: Any
    def temp_override(self, window=None, area=None, region=None, **kwargs) -> Any:
        """
        **⚠️ Warning (Stub)**:
        This method is provided by the IDE plugin.
        """
        ...
    def __getattr__(self, name) -> Any:
        """
        **⚠️ Warning (Stub)**:
        This method is provided by the IDE plugin.
        """
        ...