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
from .ThemeSpaceGeneric import ThemeSpaceGeneric
class ThemeTextEditor(bpy_struct):
    @property
    def space(self) -> Annotated['ThemeSpaceGeneric', "is_animatable=False"]:
        """Settings for space"""
        ...
    line_numbers: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    line_numbers_background: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    selected_text: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    cursor: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    syntax_builtin: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    syntax_symbols: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    syntax_special: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    syntax_preprocessor: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    syntax_reserved: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    syntax_comment: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    syntax_string: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    syntax_numbers: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]