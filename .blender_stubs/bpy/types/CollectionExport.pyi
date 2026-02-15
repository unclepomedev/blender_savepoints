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
from .PropertyGroup import PropertyGroup
class CollectionExport(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    is_open: bool
    """Whether the panel is expanded or closed"""
    @property
    def export_properties(self) -> Annotated[Optional['PropertyGroup'], "is_animatable=False"]:
        """Properties associated with the configured exporter"""
        ...
    filepath: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """The file path used for exporting"""