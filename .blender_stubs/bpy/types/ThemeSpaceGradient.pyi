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
from .ThemeGradientColors import ThemeGradientColors
class ThemeSpaceGradient(bpy_struct):
    @property
    def gradients(self) -> Annotated['ThemeGradientColors', "is_animatable=False"]:
        ...
    title: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    text: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    text_hi: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    header: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    header_text: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    header_text_hi: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]