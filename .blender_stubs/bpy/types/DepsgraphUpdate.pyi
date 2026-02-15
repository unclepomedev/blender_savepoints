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
from .ID import ID
class DepsgraphUpdate(bpy_struct):
    @property
    def id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """Updated data-block"""
        ...
    @property
    def is_updated_transform(self) -> Annotated[bool, "is_animatable=False"]:
        """Object transformation is updated"""
        ...
    @property
    def is_updated_geometry(self) -> Annotated[bool, "is_animatable=False"]:
        """Object geometry is updated"""
        ...
    @property
    def is_updated_shading(self) -> Annotated[bool, "is_animatable=False"]:
        """Object shading is updated"""
        ...