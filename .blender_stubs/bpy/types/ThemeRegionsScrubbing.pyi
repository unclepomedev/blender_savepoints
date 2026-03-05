# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeRegionsScrubbing.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ThemeRegionsScrubbing(bpy_struct):

    @property
    def back(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @back.setter
    def back(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def text(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @text.setter
    def text(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def time_marker(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @time_marker.setter
    def time_marker(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...
    @property
    def time_marker_selected(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @time_marker_selected.setter
    def time_marker_selected(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]):
        ...