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
class MeshUVLoop(bpy_struct):
    uv: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    pin_uv: Annotated[bool, "is_animatable=False"]