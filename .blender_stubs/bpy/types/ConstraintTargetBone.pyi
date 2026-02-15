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
from .Object import Object
class ConstraintTargetBone(bpy_struct):
    target: Annotated[Optional['Object'], "is_animatable=False"]
    """Target armature"""
    subtarget: Annotated[str, "is_animatable=False"]
    """Target armature bone"""
    weight: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Blending weight of this bone"""