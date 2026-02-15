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
class TransformOrientation(bpy_struct):
    matrix: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3", "is_animatable=False"]
    name: Annotated[str, "is_animatable=False"]
    """Name of the custom transform orientation"""