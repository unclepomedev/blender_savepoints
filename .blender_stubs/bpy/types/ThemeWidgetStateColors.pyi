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
class ThemeWidgetStateColors(bpy_struct):
    error: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color for error items"""
    warning: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color for warning items"""
    info: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color for informational items"""
    success: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color for successful items"""
    inner_anim: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    inner_anim_sel: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    inner_key: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    inner_key_sel: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    inner_driven: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    inner_driven_sel: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    inner_overridden: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    inner_overridden_sel: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    inner_changed: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    inner_changed_sel: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    blend: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]