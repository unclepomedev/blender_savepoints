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
from .AnyType import AnyType
from .View2D import View2D
class Region(bpy_struct):
    type: str
    x: int
    y: int
    width: int
    height: int
    view2d: 'View2D'
    alignment: str
    data: 'AnyType'
    active_panel_category: str
    def tag_redraw(self, *args, **kwargs) -> Any: ...
    def tag_refresh_ui(self, *args, **kwargs) -> Any: ...