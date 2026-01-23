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
from .Gizmo import Gizmo
class GizmoGroup(bpy_struct):
    bl_idname: str
    bl_label: str
    bl_space_type: str
    bl_region_type: str
    bl_owner_id: str
    bl_options: set[str]
    name: str
    gizmos: bpy_prop_collection['Gizmo']
    def poll(self, *args, **kwargs) -> Any: ...
    def setup_keymap(self, *args, **kwargs) -> Any: ...
    def setup(self, *args, **kwargs) -> Any: ...
    def refresh(self, *args, **kwargs) -> Any: ...
    def draw_prepare(self, *args, **kwargs) -> Any: ...
    def invoke_prepare(self, *args, **kwargs) -> Any: ...