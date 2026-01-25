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
from .RenderLayer import RenderLayer
from .RenderView import RenderView
class RenderResult(bpy_struct):
    resolution_x: int
    resolution_y: int
    layers: bpy_prop_collection['RenderLayer']
    views: bpy_prop_collection['RenderView']
    def load_from_file(self, *args, **kwargs) -> Any: ...
    def stamp_data_add_field(self, *args, **kwargs) -> Any: ...