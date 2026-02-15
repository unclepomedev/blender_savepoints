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
from .ThemeCommonAnim import ThemeCommonAnim
from .ThemeCommonCurves import ThemeCommonCurves
class ThemeCommon(bpy_struct):
    @property
    def anim(self) -> Annotated['ThemeCommonAnim', "is_animatable=False"]:
        ...
    @property
    def curves(self) -> Annotated['ThemeCommonCurves', "is_animatable=False"]:
        ...