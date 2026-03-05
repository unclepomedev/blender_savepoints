# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.XrComponentPath.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class XrComponentPath(bpy_struct):

    @property
    def path(self) -> Annotated[str, "is_animatable=False"]:
        """OpenXR component path"""
        ...
    @path.setter
    def path(self, value: Annotated[str, "is_animatable=False"]):
        ...