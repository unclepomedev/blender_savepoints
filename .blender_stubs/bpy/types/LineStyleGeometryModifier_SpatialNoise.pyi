# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_SpatialNoise.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .LineStyleGeometryModifier import LineStyleGeometryModifier

class LineStyleGeometryModifier_SpatialNoise(LineStyleGeometryModifier):

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
    amplitude: Annotated[float, "step=10.0", "precision=3"]
    """Amplitude of the spatial noise"""
    scale: Annotated[float, "step=10.0", "precision=3"]
    """Scale of the spatial noise"""
    octaves: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Number of octaves (i.e., the amount of detail of the spatial noise)"""
    smooth: bool
    """If true, the spatial noise is smooth"""
    use_pure_random: bool
    """If true, the spatial noise does not show any coherence"""