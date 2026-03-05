# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifier_DistanceFromCamera.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .LineStyleThicknessModifier import LineStyleThicknessModifier
from .CurveMapping import CurveMapping

class LineStyleThicknessModifier_DistanceFromCamera(LineStyleThicknessModifier):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the modifier"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Literal['ALONG_STROKE', 'CALLIGRAPHY', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT']:
        """Type of the modifier"""
        ...
    @property
    def blend(self) -> Literal['MIX', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'DIFFERENCE', 'MINIMUM', 'MAXIMUM']:
        """Specify how the modifier value is blended into the base value"""
        ...
    @blend.setter
    def blend(self, value: Literal['MIX', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'DIFFERENCE', 'MINIMUM', 'MAXIMUM']):
        ...
    @property
    def influence(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Influence factor by which the modifier changes the property"""
        ...
    @influence.setter
    def influence(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
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
    def mapping(self) -> Literal['LINEAR', 'CURVE']:
        """Select the mapping type"""
        ...
    @mapping.setter
    def mapping(self, value: Literal['LINEAR', 'CURVE']):
        ...
    @property
    def invert(self) -> bool:
        """Invert the fade-out direction of the linear mapping"""
        ...
    @invert.setter
    def invert(self, value: bool):
        ...
    @property
    def curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for the curve mapping"""
        ...
    @property
    def range_min(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Lower bound of the input range the mapping is applied"""
        ...
    @range_min.setter
    def range_min(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def range_max(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Upper bound of the input range the mapping is applied"""
        ...
    @range_max.setter
    def range_max(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def value_min(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Minimum output value of the mapping"""
        ...
    @value_min.setter
    def value_min(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def value_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum output value of the mapping"""
        ...
    @value_max.setter
    def value_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...