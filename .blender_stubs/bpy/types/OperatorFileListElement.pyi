# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .PropertyGroup import PropertyGroup
class OperatorFileListElement(PropertyGroup):
    name: Annotated[str, "is_animatable=False"]
    """Unique name used in the code and scripting"""
    name: Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]
    """Name of a file or directory within a file list"""
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...