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
class CacheFileLayer(bpy_struct):
    filepath: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """Path to the archive"""
    hide_layer: bool
    """Do not load data from this layer"""