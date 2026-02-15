# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MeshUVLoopLayer.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .BoolAttributeValue import BoolAttributeValue
from .Float2AttributeValue import Float2AttributeValue
from .MeshUVLoop import MeshUVLoop
from .bpy_prop_collection import bpy_prop_collection

class MeshUVLoopLayer(bpy_struct):

    @property
    def data(self) -> Annotated[bpy_prop_collection['MeshUVLoop'], "is_animatable=False"]:
        """Deprecated, use 'uv', 'vertex_select', 'edge_select' or 'pin' properties instead"""
        ...
    name: Annotated[str, "is_animatable=False"]
    """Name of UV map"""
    active: Annotated[bool, "is_animatable=False"]
    """Set the map as active for display and editing"""
    active_render: Annotated[bool, "is_animatable=False"]
    """Set the UV map as active for rendering"""
    active_clone: Annotated[bool, "is_animatable=False"]
    """Set the map as active for cloning"""
    @property
    def uv(self) -> Annotated[bpy_prop_collection['Float2AttributeValue'], "is_animatable=False"]:
        """UV coordinates on face corners"""
        ...
    @property
    def pin(self) -> Annotated[bpy_prop_collection['BoolAttributeValue'], "is_animatable=False"]:
        """UV pinned state in the UV editor"""
        ...
    def pin_ensure(self, *args, **kwargs) -> Any: ...