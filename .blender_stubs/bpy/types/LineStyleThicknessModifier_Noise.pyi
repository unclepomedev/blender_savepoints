# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LineStyleThicknessModifier_Noise.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .LineStyleThicknessModifier import LineStyleThicknessModifier

class LineStyleThicknessModifier_Noise(LineStyleThicknessModifier):

    name: Annotated[str, "is_animatable=False"]
    """Name of the modifier"""
    @property
    def type(self) -> Literal['ALONG_STROKE', 'CALLIGRAPHY', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT']:
        """Type of the modifier"""
        ...
    blend: Literal['MIX', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'DIFFERENCE', 'MINIMUM', 'MAXIMUM']
    """Specify how the modifier value is blended into the base value"""
    influence: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Influence factor by which the modifier changes the property"""
    use: bool
    """Enable or disable this modifier during stroke rendering"""
    expanded: bool
    """True if the modifier tab is expanded"""
    amplitude: Annotated[float, "step=10.0", "precision=3"]
    """Amplitude of the noise"""
    period: Annotated[float, "step=10.0", "precision=3"]
    """Period of the noise"""
    seed: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Seed for the noise generation"""
    use_asymmetric: bool
    """Allow thickness to be assigned asymmetrically"""