# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CurveProfile.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .CurveProfilePoint import CurveProfilePoint
from .CurveProfilePoints import CurveProfilePoints
from .bpy_prop_collection import bpy_prop_collection

class CurveProfile(bpy_struct):

    @property
    def preset(self) -> Literal['LINE', 'SUPPORTS', 'CORNICE', 'CROWN', 'STEPS']:

        ...
    @preset.setter
    def preset(self, value: Literal['LINE', 'SUPPORTS', 'CORNICE', 'CROWN', 'STEPS']) -> None:
        ...
    @property
    def use_clip(self) -> bool:
        """Force the path view to fit a defined boundary"""
        ...
    @use_clip.setter
    def use_clip(self, value: bool) -> None:
        ...
    @property
    def use_sample_straight_edges(self) -> bool:
        """Sample edges with vector handles"""
        ...
    @use_sample_straight_edges.setter
    def use_sample_straight_edges(self, value: bool) -> None:
        ...
    @property
    def use_sample_even_lengths(self) -> bool:
        """Sample edges with even lengths"""
        ...
    @use_sample_even_lengths.setter
    def use_sample_even_lengths(self, value: bool) -> None:
        ...
    @property
    def points(self) -> Annotated['CurveProfilePoints', "is_animatable=False"]:
        """Profile control points"""
        ...
    @property
    def segments(self) -> Annotated[bpy_prop_collection['CurveProfilePoint'], "is_animatable=False"]:
        """Segments sampled from control points"""
        ...
    def update(self, *args, **kwargs) -> Any: ...
    def reset_view(self, *args, **kwargs) -> Any: ...
    def initialize(self, *args, **kwargs) -> Any: ...
    def evaluate(self, *args, **kwargs) -> Any: ...