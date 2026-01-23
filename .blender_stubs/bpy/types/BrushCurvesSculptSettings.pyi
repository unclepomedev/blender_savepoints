# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .CurveMapping import CurveMapping
class BrushCurvesSculptSettings(bpy_struct):
    add_amount: int
    points_per_curve: int
    use_uniform_scale: bool
    minimum_length: float
    use_length_interpolate: bool
    use_radius_interpolate: bool
    use_point_count_interpolate: bool
    use_shape_interpolate: bool
    curve_length: float
    minimum_distance: float
    curve_radius: float
    density_add_attempts: int
    density_mode: str
    curve_parameter_falloff: 'CurveMapping'