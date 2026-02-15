# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .CurveMapping import CurveMapping
class BrushCurvesSculptSettings(bpy_struct):
    add_amount: Annotated[int, "step=1"]
    """Number of curves added by the Add brush"""
    points_per_curve: Annotated[int, "step=1"]
    """Number of control points in a newly added curve"""
    use_uniform_scale: bool
    """Grow or shrink curves by changing their size uniformly instead of using trimming or extrapolation"""
    minimum_length: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Avoid shrinking curves shorter than this length"""
    use_length_interpolate: bool
    """Use length of the curves in close proximity"""
    use_radius_interpolate: bool
    """Use radius of the curves in close proximity"""
    use_point_count_interpolate: bool
    """Use the number of points from the curves in close proximity"""
    use_shape_interpolate: bool
    """Use shape of the curves in close proximity"""
    curve_length: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Length of newly added curves when it is not interpolated from other curves"""
    minimum_distance: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=2"]
    """Goal distance between curve roots for the Density brush"""
    curve_radius: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=2"]
    """Radius of newly added curves when it is not interpolated from other curves"""
    density_add_attempts: Annotated[int, "step=1"]
    """How many times the Density brush tries to add a new curve"""
    density_mode: Literal['AUTO', 'ADD', 'REMOVE']
    """Determines whether the brush adds or removes curves"""
    @property
    def curve_parameter_falloff(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Falloff that is applied from the tip to the root of each curve"""
        ...