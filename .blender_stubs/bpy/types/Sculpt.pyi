# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Paint import Paint
from .AssetWeakReference import AssetWeakReference
from .Brush import Brush
from .CurveMapping import CurveMapping
from .Object import Object
from .Palette import Palette
from .UnifiedPaintSettings import UnifiedPaintSettings
class Sculpt(Paint):
    brush: 'Brush'
    brush_asset_reference: 'AssetWeakReference'
    eraser_brush: 'Brush'
    eraser_brush_asset_reference: 'AssetWeakReference'
    palette: 'Palette'
    show_brush: bool
    show_brush_on_surface: bool
    show_low_resolution: bool
    use_sculpt_delay_updates: bool
    use_symmetry_x: bool
    use_symmetry_y: bool
    use_symmetry_z: bool
    use_symmetry_feather: bool
    cavity_curve: 'CurveMapping'
    use_cavity: bool
    tile_offset: float
    tile_x: bool
    tile_y: bool
    tile_z: bool
    show_strength_curve: bool
    show_size_curve: bool
    show_jitter_curve: bool
    unified_paint_settings: 'UnifiedPaintSettings'
    lock_x: bool
    lock_y: bool
    lock_z: bool
    use_deform_only: bool
    detail_size: float
    detail_percent: float
    constant_detail_resolution: float
    use_automasking_topology: bool
    use_automasking_face_sets: bool
    use_automasking_boundary_edges: bool
    use_automasking_boundary_face_sets: bool
    use_automasking_cavity: bool
    use_automasking_cavity_inverted: bool
    use_automasking_custom_cavity_curve: bool
    automasking_boundary_edges_propagation_steps: int
    automasking_cavity_factor: float
    automasking_cavity_blur_steps: int
    automasking_cavity_curve: 'CurveMapping'
    automasking_cavity_curve_op: 'CurveMapping'
    use_automasking_start_normal: bool
    use_automasking_view_normal: bool
    use_automasking_view_occlusion: bool
    automasking_start_normal_limit: float
    automasking_start_normal_falloff: float
    automasking_view_normal_limit: float
    automasking_view_normal_falloff: float
    symmetrize_direction: str
    detail_refine_method: str
    detail_type_method: str
    gravity: float
    transform_mode: str
    gravity_object: 'Object'