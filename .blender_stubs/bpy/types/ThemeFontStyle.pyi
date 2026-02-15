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
class ThemeFontStyle(bpy_struct):
    points: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=1"]
    """Font size in points"""
    character_weight: Annotated[int, "step=50"]
    """Weight of the characters. 100-900, 400 is normal."""
    shadow: Annotated[int, "step=1"]
    """Shadow type (0 none, 3, 5 blur, 6 outline)"""
    shadow_offset_x: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Shadow offset in pixels"""
    shadow_offset_y: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Shadow offset in pixels"""
    shadow_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    shadow_value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Shadow color in gray value"""