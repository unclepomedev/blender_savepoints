# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Timer.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class Timer(bpy_struct):

    @property
    def time_step(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @property
    def time_delta(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Time since last step in seconds"""
        ...
    @property
    def time_duration(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Time since the timer started seconds"""
        ...