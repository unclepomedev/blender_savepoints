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
class EnumPropertyItem(bpy_struct):
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Human readable name"""
        ...
    @property
    def description(self) -> Annotated[str, "is_animatable=False"]:
        """Description of the item's purpose"""
        ...
    @property
    def identifier(self) -> Annotated[str, "is_animatable=False"]:
        """Unique name used in the code and scripting"""
        ...
    @property
    def value(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Value of the item"""
        ...
    @property
    def icon(self) -> str:
        """Icon of the item"""
        ...