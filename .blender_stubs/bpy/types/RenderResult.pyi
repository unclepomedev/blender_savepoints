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
from .RenderLayer import RenderLayer
from .RenderView import RenderView
class RenderResult(bpy_struct):
    @property
    def resolution_x(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        ...
    @property
    def resolution_y(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        ...
    @property
    def layers(self) -> Annotated[bpy_prop_collection['RenderLayer'], "is_animatable=False"]:
        ...
    @property
    def views(self) -> Annotated[bpy_prop_collection['RenderView'], "is_animatable=False"]:
        ...
    def load_from_file(self, *args, **kwargs) -> Any: ...
    def stamp_data_add_field(self, *args, **kwargs) -> Any: ...