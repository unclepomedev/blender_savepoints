# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class CurvePaintSettings(bpy_struct):
    curve_type: str
    use_corners_detect: bool
    use_pressure_radius: bool
    use_stroke_endpoints: bool
    use_offset_absolute: bool
    use_project_only_selected: bool
    error_threshold: int
    fit_method: str
    corner_angle: float
    radius_min: float
    radius_max: float
    radius_taper_start: float
    radius_taper_end: float
    surface_offset: float
    depth_mode: str
    surface_plane: str