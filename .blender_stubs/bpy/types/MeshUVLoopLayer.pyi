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
from .BoolAttributeValue import BoolAttributeValue
from .Float2AttributeValue import Float2AttributeValue
from .MeshUVLoop import MeshUVLoop
class MeshUVLoopLayer(bpy_struct):
    data: bpy_prop_collection['MeshUVLoop']
    name: str
    active: bool
    active_render: bool
    active_clone: bool
    uv: bpy_prop_collection['Float2AttributeValue']
    pin: bpy_prop_collection['BoolAttributeValue']
    def pin_ensure(self, *args, **kwargs) -> Any: ...