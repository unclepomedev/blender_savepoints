# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.WorldLighting.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class WorldLighting(bpy_struct):

    @property
    def ao_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]:
        """Factor for ambient occlusion blending"""
        ...
    @ao_factor.setter
    def ao_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]):
        ...
    @property
    def distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Length of rays, defines how far away other faces give occlusion effect"""
        ...
    @distance.setter
    def distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...