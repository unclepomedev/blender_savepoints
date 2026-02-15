# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GreasePencilDrawing.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Attribute import Attribute
from .AttributeGroupGreasePencilDrawing import AttributeGroupGreasePencilDrawing
from .IntAttributeValue import IntAttributeValue
from .bpy_prop_collection import bpy_prop_collection

class GreasePencilDrawing(bpy_struct):

    @property
    def type(self) -> Literal['DRAWING', 'REFERENCE']:
        """Drawing type"""
        ...
    @property
    def user_count(self) -> Annotated[int, "step=1"]:
        """The number of keyframes this drawing is used by"""
        ...
    @property
    def curve_offsets(self) -> Annotated[bpy_prop_collection['IntAttributeValue'], "is_animatable=False"]:
        """Offset indices of the first point of each curve"""
        ...
    @property
    def attributes(self) -> Annotated['AttributeGroupGreasePencilDrawing', "is_animatable=False"]:
        """Geometry attributes"""
        ...
    @property
    def color_attributes(self) -> Annotated['AttributeGroupGreasePencilDrawing', "is_animatable=False"]:
        """Geometry color attributes"""
        ...
    def add_strokes(self, *args, **kwargs) -> Any: ...
    def remove_strokes(self, *args, **kwargs) -> Any: ...
    def resize_strokes(self, *args, **kwargs) -> Any: ...
    def reorder_strokes(self, *args, **kwargs) -> Any: ...
    def set_types(self, *args, **kwargs) -> Any: ...
    def tag_positions_changed(self, *args, **kwargs) -> Any: ...
    def vertex_group_assign(self, *args, **kwargs) -> Any: ...
    def vertex_group_remove(self, *args, **kwargs) -> Any: ...
    def set_vertex_weights(self, *args, **kwargs) -> Any: ...