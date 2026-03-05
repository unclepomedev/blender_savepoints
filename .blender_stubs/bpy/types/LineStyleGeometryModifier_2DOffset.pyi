# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_2DOffset.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .LineStyleGeometryModifier import LineStyleGeometryModifier

class LineStyleGeometryModifier_2DOffset(LineStyleGeometryModifier):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the modifier"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Literal['2D_OFFSET', '2D_TRANSFORM', 'BACKBONE_STRETCHER', 'BEZIER_CURVE', 'BLUEPRINT', 'GUIDING_LINES', 'PERLIN_NOISE_1D', 'PERLIN_NOISE_2D', 'POLYGONIZATION', 'SAMPLING', 'SIMPLIFICATION', 'SINUS_DISPLACEMENT', 'SPATIAL_NOISE', 'TIP_REMOVER']:
        """Type of the modifier"""
        ...
    @property
    def use(self) -> bool:
        """Enable or disable this modifier during stroke rendering"""
        ...
    @use.setter
    def use(self, value: bool):
        ...
    @property
    def expanded(self) -> bool:
        """True if the modifier tab is expanded"""
        ...
    @expanded.setter
    def expanded(self, value: bool):
        ...
    @property
    def start(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Displacement that is applied from the beginning of the stroke"""
        ...
    @start.setter
    def start(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def end(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Displacement that is applied from the end of the stroke"""
        ...
    @end.setter
    def end(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def x(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Displacement that is applied to the X coordinates of stroke vertices"""
        ...
    @x.setter
    def x(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def y(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Displacement that is applied to the Y coordinates of stroke vertices"""
        ...
    @y.setter
    def y(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...