# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.DisplaySafeAreas.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class DisplaySafeAreas(bpy_struct):

    @property
    def title(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Safe area for text and graphics"""
        ...
    @title.setter
    def title(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def action(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Safe area for general elements"""
        ...
    @action.setter
    def action(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def title_center(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Safe area for text and graphics in a different aspect ratio"""
        ...
    @title_center.setter
    def title_center(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def action_center(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Safe area for general elements in a different aspect ratio"""
        ...
    @action_center.setter
    def action_center(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...