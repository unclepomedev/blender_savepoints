# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ParticleHairKey.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ParticleHairKey(bpy_struct):

    @property
    def time(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]:
        """Relative time of key over hair length"""
        ...
    @time.setter
    def time(self, value: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]):
        ...
    @property
    def weight(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]:
        """Weight for cloth simulation"""
        ...
    @weight.setter
    def weight(self, value: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]):
        ...
    @property
    def co(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Location of the hair key in object space"""
        ...
    @co.setter
    def co(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def co_local(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Location of the hair key in its local coordinate system, relative to the emitting face"""
        ...
    @co_local.setter
    def co_local(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    def co_object(self, *args, **kwargs) -> Any: ...
    def co_object_set(self, *args, **kwargs) -> Any: ...