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
from .Region import Region
from .Space import Space
class Area(bpy_struct):
    spaces: bpy_prop_collection['Space']
    regions: bpy_prop_collection['Region']
    show_menus: bool
    type: str
    ui_type: str
    x: int
    y: int
    width: int
    height: int
    def tag_redraw(self, *args, **kwargs) -> Any: ...
    def header_text_set(self, *args, **kwargs) -> Any: ...