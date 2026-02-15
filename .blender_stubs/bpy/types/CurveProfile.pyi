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
from .CurveProfilePoint import CurveProfilePoint
from .CurveProfilePoints import CurveProfilePoints
class CurveProfile(bpy_struct):
    preset: Literal['LINE', 'SUPPORTS', 'CORNICE', 'CROWN', 'STEPS']
    use_clip: bool
    """Force the path view to fit a defined boundary"""
    use_sample_straight_edges: bool
    """Sample edges with vector handles"""
    use_sample_even_lengths: bool
    """Sample edges with even lengths"""
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