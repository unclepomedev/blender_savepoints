# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.TimelineMarker.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Object import Object

class TimelineMarker(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def frame(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """The frame on which the timeline marker appears"""
        ...
    @frame.setter
    def frame(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]):
        ...
    @property
    def select(self) -> bool:
        """Marker selection state"""
        ...
    @select.setter
    def select(self, value: bool):
        ...
    @property
    def camera(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Camera that becomes active on this frame"""
        ...
    @camera.setter
    def camera(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...