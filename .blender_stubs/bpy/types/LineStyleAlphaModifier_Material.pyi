# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LineStyleAlphaModifier_Material.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .LineStyleAlphaModifier import LineStyleAlphaModifier
from .CurveMapping import CurveMapping

class LineStyleAlphaModifier_Material(LineStyleAlphaModifier):

    name: Annotated[str, "is_animatable=False"]
    """Name of the modifier"""
    @property
    def type(self) -> Literal['ALONG_STROKE', 'CREASE_ANGLE', 'CURVATURE_3D', 'DISTANCE_FROM_CAMERA', 'DISTANCE_FROM_OBJECT', 'MATERIAL', 'NOISE', 'TANGENT']:
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
    material_attribute: Literal['LINE', 'LINE_R', 'LINE_G', 'LINE_B', 'LINE_A', 'DIFF', 'DIFF_R', 'DIFF_G', 'DIFF_B', 'SPEC', 'SPEC_R', 'SPEC_G', 'SPEC_B', 'SPEC_HARD', 'ALPHA']
    """Specify which material attribute is used"""
    mapping: Literal['LINEAR', 'CURVE']
    """Select the mapping type"""
    invert: bool
    """Invert the fade-out direction of the linear mapping"""
    @property
    def curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for the curve mapping"""
        ...