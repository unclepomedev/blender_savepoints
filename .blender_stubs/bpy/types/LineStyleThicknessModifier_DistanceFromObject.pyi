# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .LineStyleThicknessModifier import LineStyleThicknessModifier
from .CurveMapping import CurveMapping
from .Object import Object
class LineStyleThicknessModifier_DistanceFromObject(LineStyleThicknessModifier):
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
    mapping: Literal['LINEAR', 'CURVE']
    """Select the mapping type"""
    invert: bool
    """Invert the fade-out direction of the linear mapping"""
    @property
    def curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for the curve mapping"""
        ...
    range_min: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Lower bound of the input range the mapping is applied"""
    range_max: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Upper bound of the input range the mapping is applied"""
    value_min: Annotated[float, "step=10.0", "precision=3"]
    """Minimum output value of the mapping"""
    value_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum output value of the mapping"""
    target: Annotated[Optional['Object'], "is_animatable=False"]
    """Target object from which the distance is measured"""