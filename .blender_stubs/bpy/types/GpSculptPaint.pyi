# Blender Probe Generated Stub for Blender 5.1.0 Alpha
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
from .Palette import Palette
from .UnifiedPaintSettings import UnifiedPaintSettings
class GpSculptPaint(Paint):
    brush: 'Brush'
    brush_asset_reference: 'AssetWeakReference'
    eraser_brush: 'Brush'
    eraser_brush_asset_reference: 'AssetWeakReference'
    palette: 'Palette'
    show_brush: bool
    show_brush_on_surface: bool
    show_low_resolution: bool
    use_sculpt_delay_updates: bool
    show_bvh_nodes: bool
    use_symmetry_x: bool
    use_symmetry_y: bool
    use_symmetry_z: bool
    use_symmetry_feather: bool
    cavity_curve: 'CurveMapping'
    use_cavity: bool
    tile_offset: list[float]
    tile_x: bool
    tile_y: bool
    tile_z: bool
    show_strength_curve: bool
    show_size_curve: bool
    show_jitter_curve: bool
    unified_paint_settings: 'UnifiedPaintSettings'