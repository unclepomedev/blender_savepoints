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
class PackedFile(bpy_struct):
    @property
    def size(self) -> Annotated[int, "step=1"]:
        """Size of packed file in bytes"""
        ...
    @property
    def data(self) -> Annotated[str, "subtype='BYTE_STRING'", "is_animatable=False"]:
        """Raw data (bytes, exact content of the embedded file)"""
        ...