# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .LineStyleGeometryModifier import LineStyleGeometryModifier
class LineStyleGeometryModifier_PerlinNoise2D(LineStyleGeometryModifier):
    name: Annotated[str, "is_animatable=False"]
    """Name of the modifier"""
    @property
    def type(self) -> Literal['2D_OFFSET', '2D_TRANSFORM', 'BACKBONE_STRETCHER', 'BEZIER_CURVE', 'BLUEPRINT', 'GUIDING_LINES', 'PERLIN_NOISE_1D', 'PERLIN_NOISE_2D', 'POLYGONIZATION', 'SAMPLING', 'SIMPLIFICATION', 'SINUS_DISPLACEMENT', 'SPATIAL_NOISE', 'TIP_REMOVER']:
        """Type of the modifier"""
        ...
    use: bool
    """Enable or disable this modifier during stroke rendering"""
    expanded: bool
    """True if the modifier tab is expanded"""
    frequency: Annotated[float, "step=10.0", "precision=3"]
    """Frequency of the Perlin noise"""
    amplitude: Annotated[float, "step=10.0", "precision=3"]
    """Amplitude of the Perlin noise"""
    octaves: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Number of octaves (i.e., the amount of detail of the Perlin noise)"""
    angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Displacement direction"""
    seed: Annotated[int, "step=1"]
    """Seed for random number generation (if negative, time is used as a seed instead)"""