# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Function.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Property import Property
from .bpy_prop_collection import bpy_prop_collection

class Function(bpy_struct):

    @property
    def identifier(self) -> Annotated[str, "is_animatable=False"]:
        """Unique name used in the code and scripting"""
        ...
    @property
    def description(self) -> Annotated[str, "is_animatable=False"]:
        """Description of the Function's purpose"""
        ...
    @property
    def parameters(self) -> Annotated[bpy_prop_collection['Property'], "is_animatable=False"]:
        """Parameters for the function"""
        ...
    @property
    def is_registered(self) -> bool:
        """Function is registered as callback as part of type registration"""
        ...
    @property
    def is_registered_optional(self) -> bool:
        """Function is optionally registered as callback part of type registration"""
        ...
    @property
    def use_self(self) -> bool:
        """Function does not pass itself as an argument (becomes a static method in Python)"""
        ...
    @property
    def use_self_type(self) -> bool:
        """Function passes itself type as an argument (becomes a class method in Python if use_self is false)"""
        ...