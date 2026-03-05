# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LineStyleColorModifier_Noise.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .LineStyleColorModifier import LineStyleColorModifier
from .ColorRamp import ColorRamp

class LineStyleColorModifier_Noise(LineStyleColorModifier):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the modifier"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Literal['ALONG_STROKE', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT']:
        """Type of the modifier"""
        ...
    @property
    def blend(self) -> Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']:
        """Specify how the modifier value is blended into the base value"""
        ...
    @blend.setter
    def blend(self, value: Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']):
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
    def color_ramp(self) -> Annotated[Optional['ColorRamp'], "is_animatable=False"]:
        """Color ramp used to change line color"""
        ...
    @property
    def amplitude(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amplitude of the noise"""
        ...
    @amplitude.setter
    def amplitude(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def period(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Period of the noise"""
        ...
    @period.setter
    def period(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def seed(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Seed for the noise generation"""
        ...
    @seed.setter
    def seed(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...