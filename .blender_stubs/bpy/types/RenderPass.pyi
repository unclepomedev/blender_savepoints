# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.RenderPass.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class RenderPass(bpy_struct):

    @property
    def fullname(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @property
    def channel_id(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @property
    def channels(self) -> Annotated[int, "step=1"]:

        ...
    rect: Annotated[list[float], "step=10.0", "precision=3"]

    @property
    def view_id(self) -> Annotated[int, "step=1"]:

        ...