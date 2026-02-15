# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LineStyleColorModifier_DistanceFromCamera.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .LineStyleColorModifier import LineStyleColorModifier
from .ColorRamp import ColorRamp

class LineStyleColorModifier_DistanceFromCamera(LineStyleColorModifier):

    name: Annotated[str, "is_animatable=False"]
    """Name of the modifier"""
    @property
    def type(self) -> Literal['ALONG_STROKE', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT']:
        """Type of the modifier"""
        ...
    blend: Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']
    """Specify how the modifier value is blended into the base value"""
    influence: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Influence factor by which the modifier changes the property"""
    use: bool
    """Enable or disable this modifier during stroke rendering"""
    expanded: bool
    """True if the modifier tab is expanded"""
    @property
    def color_ramp(self) -> Annotated[Optional['ColorRamp'], "is_animatable=False"]:
        """Color ramp used to change line color"""
        ...
    range_min: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Lower bound of the input range the mapping is applied"""
    range_max: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Upper bound of the input range the mapping is applied"""