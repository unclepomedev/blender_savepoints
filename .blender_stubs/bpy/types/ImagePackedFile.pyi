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
from .PackedFile import PackedFile
class ImagePackedFile(bpy_struct):
    @property
    def packed_file(self) -> Annotated[Optional['PackedFile'], "is_animatable=False"]:
        ...
    filepath: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    @property
    def view(self) -> Annotated[int, "step=1"]:
        ...
    @property
    def tile_number(self) -> Annotated[int, "step=1"]:
        ...
    def save(self, *args, **kwargs) -> Any: ...