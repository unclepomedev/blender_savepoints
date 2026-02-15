# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeOutliner.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ThemeSpaceGeneric import ThemeSpaceGeneric

class ThemeOutliner(bpy_struct):

    @property
    def space(self) -> Annotated['ThemeSpaceGeneric', "is_animatable=False"]:
        """Settings for space"""
        ...
    match: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    selected_highlight: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    active: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    selected_object: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    active_object: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    edited_object: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    row_alternate: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Overlay color on every other row"""