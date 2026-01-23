# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
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
    window_manager: 'WindowManager'
    window: 'Window'
    workspace: 'WorkSpace'
    screen: 'Screen'
    area: 'Area'
    space_data: 'Space'
    region: 'Region'
    region_popup: 'Region'
    region_data: 'RegionView3D'
    gizmo_group: 'GizmoGroup'
    asset: 'AssetRepresentation'
    blend_data: 'BlendData'
    scene: 'Scene'
    view_layer: 'ViewLayer'
    engine: str
    collection: 'Collection'
    layer_collection: 'LayerCollection'
    tool_settings: 'ToolSettings'
    preferences: 'Preferences'
    mode: str
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