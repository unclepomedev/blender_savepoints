# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.AssetTag.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class AssetTag(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """The identifier that makes up this tag"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...