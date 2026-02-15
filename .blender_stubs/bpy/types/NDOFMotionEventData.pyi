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
class NDOFMotionEventData(bpy_struct):
    @property
    def translation(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """The translation of this motion event. The range on each axis is [-1 to 1], before being multiplied by the sensitivity preference. This is typically scaled by the time-delta before use."""
        ...
    @property
    def rotation(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Axis-angle rotation of this motion event. The vector magnitude is the angle where 1.0 represents 360 degrees. The angle is typically scaled by the time-delta before use."""
        ...
    @property
    def progress(self) -> Literal['STARTING', 'IN_PROGRESS', 'FINISHING']:
        """Indicates the gesture phase"""
        ...
    @property
    def time_delta(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Time since previous motion event (in seconds)"""
        ...