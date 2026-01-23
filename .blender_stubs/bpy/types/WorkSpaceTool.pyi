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
class WorkSpaceTool(bpy_struct):
    idname: str
    idname_fallback: str
    index: int
    space_type: str
    mode: str
    use_paint_canvas: bool
    has_datablock: bool
    use_brushes: bool
    brush_type: str
    widget: str
    def setup(self, *args, **kwargs) -> Any: ...
    def operator_properties(self, *args, **kwargs) -> Any: ...
    def gizmo_group_properties(self, *args, **kwargs) -> Any: ...
    def refresh_from_context(self, *args, **kwargs) -> Any: ...