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
from .GreasePencilLayer import GreasePencilLayer
class GreasePencilv3Layers(bpy_struct):
    active: 'GreasePencilLayer'
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def move(self, *args, **kwargs) -> Any: ...
    def move_top(self, *args, **kwargs) -> Any: ...
    def move_bottom(self, *args, **kwargs) -> Any: ...
    def move_to_layer_group(self, *args, **kwargs) -> Any: ...