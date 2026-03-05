# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifier_Calligraphy.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .LineStyleThicknessModifier import LineStyleThicknessModifier

class LineStyleThicknessModifier_Calligraphy(LineStyleThicknessModifier):

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
    def orientation(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Angle of the main direction"""
        ...
    @orientation.setter
    def orientation(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]):
        ...
    @property
    def thickness_min(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Minimum thickness in the direction perpendicular to the main direction"""
        ...
    @thickness_min.setter
    def thickness_min(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def thickness_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum thickness in the main direction"""
        ...
    @thickness_max.setter
    def thickness_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...