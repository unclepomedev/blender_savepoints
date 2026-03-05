# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_PerlinNoise1D.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .LineStyleGeometryModifier import LineStyleGeometryModifier

class LineStyleGeometryModifier_PerlinNoise1D(LineStyleGeometryModifier):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the modifier"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
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
    def use(self, value: bool) -> None:
        ...
    @property
    def expanded(self) -> bool:
        """True if the modifier tab is expanded"""
        ...
    @expanded.setter
    def expanded(self, value: bool) -> None:
        ...
    @property
    def frequency(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Frequency of the Perlin noise"""
        ...
    @frequency.setter
    def frequency(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def amplitude(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amplitude of the Perlin noise"""
        ...
    @amplitude.setter
    def amplitude(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def octaves(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of octaves (i.e., the amount of detail of the Perlin noise)"""
        ...
    @octaves.setter
    def octaves(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Displacement direction"""
        ...
    @angle.setter
    def angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def seed(self) -> Annotated[int, "step=1"]:
        """Seed for random number generation (if negative, time is used as a seed instead)"""
        ...
    @seed.setter
    def seed(self, value: Annotated[int, "step=1"]) -> None:
        ...