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
class ThemeRegionsScrubbing(bpy_struct):
    back: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    text: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    time_marker: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    time_marker_selected: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]