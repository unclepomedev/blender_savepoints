# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Bone import Bone
class BoneCollection(bpy_struct):
    name: str
    is_expanded: bool
    is_visible: bool
    is_visible_ancestors: bool
    is_visible_effectively: bool
    is_solo: bool
    is_local_override: bool
    is_editable: bool
    bones: bpy_prop_collection['Bone']
    children: bpy_prop_collection['BoneCollection']
    parent: 'BoneCollection'
    index: int
    child_number: int
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def assign(self, *args, **kwargs) -> Any: ...
    def unassign(self, *args, **kwargs) -> Any: ...