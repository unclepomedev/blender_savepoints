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
class LineStyleGeometryModifier_2DTransform(LineStyleGeometryModifier):
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
    pivot: Literal['CENTER', 'START', 'END', 'PARAM', 'ABSOLUTE']
    """Pivot of scaling and rotation operations"""
    scale_x: Annotated[float, "step=10.0", "precision=3"]
    """Scaling factor that is applied along the X axis"""
    scale_y: Annotated[float, "step=10.0", "precision=3"]
    """Scaling factor that is applied along the Y axis"""
    angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Rotation angle"""
    pivot_u: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Pivot in terms of the stroke point parameter u (0 <= u <= 1)"""
    pivot_x: Annotated[float, "step=10.0", "precision=3"]
    """2D X coordinate of the absolute pivot"""
    pivot_y: Annotated[float, "step=10.0", "precision=3"]
    """2D Y coordinate of the absolute pivot"""