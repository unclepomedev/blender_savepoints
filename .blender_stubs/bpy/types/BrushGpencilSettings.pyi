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
from .Material import Material
class BrushGpencilSettings(bpy_struct):
    pen_strength: float
    pen_jitter: float
    random_pressure: float
    random_strength: float
    angle: float
    angle_factor: float
    pen_smooth_factor: float
    pen_smooth_steps: int
    pen_subdivision_steps: int
    simplify_factor: float
    simplify_pixel_threshold: float
    curve_sensitivity: 'CurveMapping'
    curve_strength: 'CurveMapping'
    curve_jitter: 'CurveMapping'
    curve_random_pressure: 'CurveMapping'
    curve_random_strength: 'CurveMapping'
    curve_random_uv: 'CurveMapping'
    curve_random_hue: 'CurveMapping'
    curve_random_saturation: 'CurveMapping'
    curve_random_value: 'CurveMapping'
    fill_threshold: float
    fill_factor: float
    fill_simplify_level: int
    uv_random: float
    hardness: float
    aspect: list[float]
    input_samples: int
    active_smooth_factor: float
    eraser_strength_factor: float
    eraser_thickness_factor: float
    vertex_mode: str
    vertex_color_factor: float
    random_hue_factor: float
    random_saturation_factor: float
    random_value_factor: float
    extend_stroke_factor: float
    fill_extend_mode: str
    dilate: int
    outline_thickness_factor: float
    use_pressure: bool
    use_strength_pressure: bool
    use_jitter_pressure: bool
    use_stroke_random_hue: bool
    use_stroke_random_sat: bool
    use_stroke_random_val: bool
    use_stroke_random_radius: bool
    use_stroke_random_strength: bool
    use_stroke_random_uv: bool
    use_random_press_hue: bool
    use_random_press_sat: bool
    use_random_press_val: bool
    use_random_press_radius: bool
    use_random_press_strength: bool
    use_random_press_uv: bool
    use_settings_stabilizer: bool
    eraser_mode: str
    caps_type: str
    fill_draw_mode: str
    fill_layer_mode: str
    fill_direction: str
    pin_draw_mode: bool
    brush_draw_mode: str
    use_trim: bool
    use_settings_outline: bool
    use_edit_position: bool
    use_edit_strength: bool
    use_edit_thickness: bool
    use_edit_uv: bool
    material: 'Material'
    material_alt: 'Material'
    show_fill_boundary: bool
    show_fill_extend: bool
    use_collide_strokes: bool
    show_fill: bool
    use_auto_remove_fill_guides: bool
    use_fill_limit: bool
    use_settings_postprocess: bool
    use_settings_random: bool
    use_material_pin: bool
    show_lasso: bool
    use_occlude_eraser: bool
    use_keep_caps_eraser: bool
    use_active_layer_only: bool