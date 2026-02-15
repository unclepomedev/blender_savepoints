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
class LineStyleGeometryModifier_Blueprint(LineStyleGeometryModifier):
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
    shape: Literal['CIRCLES', 'ELLIPSES', 'SQUARES']
    """Select the shape of blueprint contour strokes"""
    rounds: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Number of rounds in contour strokes"""
    backbone_length: Annotated[float, "step=10.0", "precision=3"]
    """Amount of backbone stretching"""
    random_radius: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Randomness of the radius"""
    random_center: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Randomness of the center"""
    random_backbone: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Randomness of the backbone stretching"""