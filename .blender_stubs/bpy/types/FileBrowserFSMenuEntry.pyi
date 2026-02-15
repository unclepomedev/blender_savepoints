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
class FileBrowserFSMenuEntry(bpy_struct):
    path: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    name: Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]
    icon: Annotated[int, "step=1"]
    @property
    def use_save(self) -> bool:
        """Whether this path is saved in bookmarks, or generated from OS"""
        ...