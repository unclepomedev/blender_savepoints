# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Struct.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .EnumPropertyItem import EnumPropertyItem
from .Function import Function
from .Property import Property
from .StringProperty import StringProperty
from .bpy_prop_collection import bpy_prop_collection

class Struct(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Human readable name"""
        ...
    @property
    def identifier(self) -> Annotated[str, "is_animatable=False"]:
        """Unique name used in the code and scripting"""
        ...
    @property
    def description(self) -> Annotated[str, "is_animatable=False"]:
        """Description of the Struct's purpose"""
        ...
    @property
    def translation_context(self) -> Annotated[str, "is_animatable=False"]:
        """Translation context of the struct's name"""
        ...
    @property
    def base(self) -> Annotated[Optional['Struct'], "is_animatable=False"]:
        """Struct definition this is derived from"""
        ...
    @property
    def nested(self) -> Annotated[Optional['Struct'], "is_animatable=False"]:
        """Struct in which this struct is always nested, and to which it logically belongs"""
        ...
    @property
    def name_property(self) -> Annotated[Optional['StringProperty'], "is_animatable=False"]:
        """Property that gives the name of the struct"""
        ...
    @property
    def properties(self) -> Annotated[bpy_prop_collection['Property'], "is_animatable=False"]:
        """Properties in the struct"""
        ...
    @property
    def functions(self) -> Annotated[bpy_prop_collection['Function'], "is_animatable=False"]:

        ...
    @property
    def property_tags(self) -> Annotated[bpy_prop_collection['EnumPropertyItem'], "is_animatable=False"]:
        """Tags that properties can use to influence behavior"""
        ...