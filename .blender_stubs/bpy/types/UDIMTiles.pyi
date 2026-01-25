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
from .UDIMTile import UDIMTile
class UDIMTiles(bpy_struct):
    active_index: int
    active: 'UDIMTile'
    def new(self, *args, **kwargs) -> Any: ...
    def get(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...