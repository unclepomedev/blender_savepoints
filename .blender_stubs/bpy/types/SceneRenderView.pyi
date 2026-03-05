# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SceneRenderView.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SceneRenderView(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Render view name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def file_suffix(self) -> Annotated[str, "is_animatable=False"]:
        """Suffix added to the render images for this view"""
        ...
    @file_suffix.setter
    def file_suffix(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def camera_suffix(self) -> Annotated[str, "is_animatable=False"]:
        """Suffix to identify the cameras to use, and added to the render images for this view"""
        ...
    @camera_suffix.setter
    def camera_suffix(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def use(self) -> Annotated[bool, "is_animatable=False"]:
        """Disable or enable the render view"""
        ...
    @use.setter
    def use(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...