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
class DisplaySafeAreas(bpy_struct):
    title: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]
    """Safe area for text and graphics"""
    action: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]
    """Safe area for general elements"""
    title_center: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]
    """Safe area for text and graphics in a different aspect ratio"""
    action_center: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]
    """Safe area for general elements in a different aspect ratio"""