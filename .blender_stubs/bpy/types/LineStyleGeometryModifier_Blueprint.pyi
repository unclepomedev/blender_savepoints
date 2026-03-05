# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_Blueprint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .LineStyleGeometryModifier import LineStyleGeometryModifier

class LineStyleGeometryModifier_Blueprint(LineStyleGeometryModifier):

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
    def shape(self) -> Literal['CIRCLES', 'ELLIPSES', 'SQUARES']:
        """Select the shape of blueprint contour strokes"""
        ...
    @shape.setter
    def shape(self, value: Literal['CIRCLES', 'ELLIPSES', 'SQUARES']) -> None:
        ...
    @property
    def rounds(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of rounds in contour strokes"""
        ...
    @rounds.setter
    def rounds(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def backbone_length(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of backbone stretching"""
        ...
    @backbone_length.setter
    def backbone_length(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def random_radius(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Randomness of the radius"""
        ...
    @random_radius.setter
    def random_radius(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def random_center(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Randomness of the center"""
        ...
    @random_center.setter
    def random_center(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def random_backbone(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Randomness of the backbone stretching"""
        ...
    @random_backbone.setter
    def random_backbone(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...