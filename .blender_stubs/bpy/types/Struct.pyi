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
from .EnumPropertyItem import EnumPropertyItem
from .Function import Function
from .Property import Property
from .StringProperty import StringProperty
class Struct(bpy_struct):
    name: str
    identifier: str
    description: str
    translation_context: str
    base: 'Struct'
    nested: 'Struct'
    name_property: 'StringProperty'
    properties: bpy_prop_collection['Property']
    functions: bpy_prop_collection['Function']
    property_tags: bpy_prop_collection['EnumPropertyItem']