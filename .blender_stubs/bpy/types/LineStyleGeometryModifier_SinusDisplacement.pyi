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
class LineStyleGeometryModifier_SinusDisplacement(LineStyleGeometryModifier):
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
    wavelength: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    """Wavelength of the sinus displacement"""
    amplitude: Annotated[float, "step=10.0", "precision=3"]
    """Amplitude of the sinus displacement"""
    phase: Annotated[float, "step=10.0", "precision=3"]
    """Phase of the sinus displacement"""