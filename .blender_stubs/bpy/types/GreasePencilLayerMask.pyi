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
class GreasePencilLayerMask(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    """Mask layer name"""
    hide: bool
    """Set mask Visibility"""
    invert: bool
    """Invert mask"""