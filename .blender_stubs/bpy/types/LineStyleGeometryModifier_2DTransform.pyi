# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LineStyleGeometryModifier_2DTransform.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .LineStyleGeometryModifier import LineStyleGeometryModifier

class LineStyleGeometryModifier_2DTransform(LineStyleGeometryModifier):

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
    def pivot(self) -> Literal['CENTER', 'START', 'END', 'PARAM', 'ABSOLUTE']:
        """Pivot of scaling and rotation operations"""
        ...
    @pivot.setter
    def pivot(self, value: Literal['CENTER', 'START', 'END', 'PARAM', 'ABSOLUTE']) -> None:
        ...
    @property
    def scale_x(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Scaling factor that is applied along the X axis"""
        ...
    @scale_x.setter
    def scale_x(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def scale_y(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Scaling factor that is applied along the Y axis"""
        ...
    @scale_y.setter
    def scale_y(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Rotation angle"""
        ...
    @angle.setter
    def angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def pivot_u(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Pivot in terms of the stroke point parameter u (0 <= u <= 1)"""
        ...
    @pivot_u.setter
    def pivot_u(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def pivot_x(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """2D X coordinate of the absolute pivot"""
        ...
    @pivot_x.setter
    def pivot_x(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def pivot_y(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """2D Y coordinate of the absolute pivot"""
        ...
    @pivot_y.setter
    def pivot_y(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...