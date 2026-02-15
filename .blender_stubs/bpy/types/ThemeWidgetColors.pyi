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
class ThemeWidgetColors(bpy_struct):
    outline: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    outline_sel: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    inner: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    inner_sel: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    item: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    text: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    text_sel: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    show_shaded: bool
    shadetop: Annotated[int, "step=1"]
    shadedown: Annotated[int, "step=1"]
    roundness: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Amount of edge rounding"""