# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ConstraintTargetBone.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Object import Object

class ConstraintTargetBone(bpy_struct):

    @property
    def target(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Target armature"""
        ...
    @target.setter
    def target(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def subtarget(self) -> Annotated[str, "is_animatable=False"]:
        """Target armature bone"""
        ...
    @subtarget.setter
    def subtarget(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def weight(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Blending weight of this bone"""
        ...
    @weight.setter
    def weight(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...