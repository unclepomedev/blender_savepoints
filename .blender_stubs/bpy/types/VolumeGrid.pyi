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
class VolumeGrid(bpy_struct):
    name: str
    data_type: str
    channels: int
    matrix_object: float
    is_loaded: bool
    def load(self, *args, **kwargs) -> Any: ...
    def unload(self, *args, **kwargs) -> Any: ...