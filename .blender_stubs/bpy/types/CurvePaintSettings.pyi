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
class CurvePaintSettings(bpy_struct):
    curve_type: Annotated[Literal['POLY', 'BEZIER'], "is_animatable=False"]
    """Type of curve to use for new strokes"""
    use_corners_detect: Annotated[bool, "is_animatable=False"]
    """Detect corners and use non-aligned handles"""
    use_pressure_radius: Annotated[bool, "is_animatable=False"]
    """Map tablet pressure to curve radius"""
    use_stroke_endpoints: Annotated[bool, "is_animatable=False"]
    """Use the start of the stroke for the depth"""
    use_offset_absolute: Annotated[bool, "is_animatable=False"]
    """Apply a fixed offset (don't scale by the radius)"""
    use_project_only_selected: Annotated[bool, "is_animatable=False"]
    """Project the strokes only onto selected objects"""
    error_threshold: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Allow deviation for a smoother, less precise line"""
    fit_method: Annotated[Literal['REFIT', 'SPLIT'], "subtype='PIXEL'", "is_animatable=False"]
    """Curve fitting method"""
    corner_angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Angles above this are considered corners"""
    radius_min: Annotated[float, "step=10.0", "precision=2", "is_animatable=False"]
    """Minimum radius when the minimum pressure is applied (also the minimum when tapering)"""
    radius_max: Annotated[float, "step=10.0", "precision=2", "is_animatable=False"]
    """Radius to use when the maximum pressure is applied (or when a tablet isn't used)"""
    radius_taper_start: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]
    """Taper factor for the radius of each point along the curve"""
    radius_taper_end: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]
    """Taper factor for the radius of each point along the curve"""
    surface_offset: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]
    """Offset the stroke from the surface"""
    depth_mode: Annotated[Literal['CURSOR', 'SURFACE'], "is_animatable=False"]
    """Method of projecting depth"""
    surface_plane: Annotated[Literal['NORMAL_VIEW', 'NORMAL_SURFACE', 'VIEW'], "is_animatable=False"]
    """Plane for projected stroke"""