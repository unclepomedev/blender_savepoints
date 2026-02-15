# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .Attribute import Attribute
from .Float4x4AttributeValue import Float4x4AttributeValue
class Float4x4Attribute(Attribute):
    name: Annotated[str, "is_animatable=False"]
    """Name of the Attribute"""
    @property
    def data_type(self) -> Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'STRING', 'INT8', 'INT16_2D', 'INT32_2D', 'FLOAT2', 'BYTE_COLOR']:
        """Type of data stored in attribute"""
        ...
    @property
    def storage_type(self) -> Literal['ARRAY', 'SINGLE']:
        """Method used to store the data"""
        ...
    @property
    def domain(self) -> Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']:
        """Domain of the Attribute"""
        ...
    @property
    def is_internal(self) -> bool:
        """The attribute is meant for internal use by Blender"""
        ...
    @property
    def is_required(self) -> bool:
        """Whether the attribute can be removed or renamed"""
        ...
    @property
    def data(self) -> Annotated[bpy_prop_collection['Float4x4AttributeValue'], "is_animatable=False"]:
        ...