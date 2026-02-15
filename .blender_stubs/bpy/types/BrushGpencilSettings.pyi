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
from .Material import Material
class BrushGpencilSettings(bpy_struct):
    pen_strength: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]
    """Color strength for new strokes (affect alpha factor of color)"""
    pen_jitter: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]
    """Jitter factor of brush radius for new strokes"""
    random_pressure: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Randomness factor for pressure in new strokes"""
    random_strength: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Randomness factor strength in new strokes"""
    angle: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Direction of the stroke at which brush gives maximal thickness (0° for horizontal)"""
    angle_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Reduce brush thickness by this factor when stroke is perpendicular to 'Angle' direction"""
    pen_smooth_factor: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Amount of smoothing to apply after finish newly created strokes, to reduce jitter/noise"""
    pen_smooth_steps: Annotated[int, "step=1", "is_animatable=False"]
    """Number of times to smooth newly created strokes"""
    pen_subdivision_steps: Annotated[int, "step=1", "is_animatable=False"]
    """Number of times to subdivide newly created strokes, for less jagged strokes"""
    simplify_factor: Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]
    """Factor of Simplify using adaptive algorithm"""
    simplify_pixel_threshold: Annotated[float, "subtype='PIXEL'", "step=1.0", "precision=1", "is_animatable=False"]
    """Threshold in screen space used for the simplify algorithm. Points within this threshold are treated as if they were in a straight line."""
    @property
    def curve_sensitivity(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for the sensitivity"""
        ...
    @property
    def curve_strength(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for the strength"""
        ...
    @property
    def curve_jitter(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for the jitter effect"""
        ...
    @property
    def curve_random_pressure(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for modulating effect"""
        ...
    @property
    def curve_random_strength(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for modulating effect"""
        ...
    @property
    def curve_random_uv(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for modulating effect"""
        ...
    @property
    def curve_random_hue(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for modulating effect"""
        ...
    @property
    def curve_random_saturation(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for modulating effect"""
        ...
    @property
    def curve_random_value(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for modulating effect"""
        ...
    fill_threshold: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Threshold to consider color transparent for filling"""
    fill_factor: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Factor for fill boundary accuracy, higher values are more accurate but slower"""
    fill_simplify_level: Annotated[int, "step=1", "is_animatable=False"]
    """Number of simplify steps (large values reduce fill accuracy)"""
    uv_random: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Random factor for auto-generated UV rotation"""
    hardness: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Gradient from the center of Dot and Box strokes (set to 1 for a solid stroke)"""
    aspect: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]
    input_samples: Annotated[int, "step=1", "is_animatable=False"]
    """Generated intermediate points for very fast mouse movements (Set to 0 to disable)"""
    active_smooth_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Amount of smoothing while drawing"""
    eraser_strength_factor: Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=1", "is_animatable=False"]
    """Amount of erasing for strength"""
    eraser_thickness_factor: Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=1", "is_animatable=False"]
    """Amount of erasing for thickness"""
    vertex_mode: Annotated[Literal['STROKE', 'FILL', 'BOTH'], "is_animatable=False"]
    """Defines how vertex color affect to the strokes"""
    vertex_color_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Factor used to mix vertex color to get final color"""
    random_hue_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Random factor to modify original hue"""
    random_saturation_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Random factor to modify original saturation"""
    random_value_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Random factor to modify original value"""
    extend_stroke_factor: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Strokes end extension for closing gaps, use zero to disable"""
    fill_extend_mode: Annotated[Literal['EXTEND', 'RADIUS'], "is_animatable=False"]
    """Types of stroke extensions used for closing gaps"""
    dilate: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Number of pixels to expand or contract fill area"""
    outline_thickness_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Thickness of the outline stroke relative to current brush thickness"""
    use_pressure: Annotated[bool, "is_animatable=False"]
    """Use tablet pressure"""
    use_strength_pressure: Annotated[bool, "is_animatable=False"]
    """Use tablet pressure for color strength"""
    use_jitter_pressure: Annotated[bool, "is_animatable=False"]
    """Use tablet pressure for jitter"""
    use_stroke_random_hue: Annotated[bool, "is_animatable=False"]
    """Use randomness at stroke level"""
    use_stroke_random_sat: Annotated[bool, "is_animatable=False"]
    """Use randomness at stroke level"""
    use_stroke_random_val: Annotated[bool, "is_animatable=False"]
    """Use randomness at stroke level"""
    use_stroke_random_radius: Annotated[bool, "is_animatable=False"]
    """Use randomness at stroke level"""
    use_stroke_random_strength: Annotated[bool, "is_animatable=False"]
    """Use randomness at stroke level"""
    use_stroke_random_uv: Annotated[bool, "is_animatable=False"]
    """Use randomness at stroke level"""
    use_random_press_hue: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate randomness"""
    use_random_press_sat: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate randomness"""
    use_random_press_val: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate randomness"""
    use_random_press_radius: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate randomness"""
    use_random_press_strength: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate randomness"""
    use_random_press_uv: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate randomness"""
    use_settings_stabilizer: Annotated[bool, "is_animatable=False"]
    """Draw lines with a delay to allow smooth strokes (press Shift key to override while drawing)"""
    eraser_mode: Annotated[Literal['SOFT', 'HARD', 'STROKE'], "is_animatable=False"]
    """Eraser Mode"""
    caps_type: Annotated[Literal['ROUND', 'FLAT'], "is_animatable=False"]
    """The shape of the start and end of the stroke"""
    fill_draw_mode: Annotated[Literal['BOTH', 'STROKE', 'CONTROL'], "is_animatable=False"]
    """Mode to draw boundary limits"""
    fill_layer_mode: Annotated[Literal['VISIBLE', 'ACTIVE', 'ABOVE', 'BELOW', 'ALL_ABOVE', 'ALL_BELOW'], "is_animatable=False"]
    """Layers used as boundaries"""
    fill_direction: Annotated[Literal['NORMAL', 'INVERT'], "is_animatable=False"]
    """Direction of the fill"""
    pin_draw_mode: Annotated[bool, "is_animatable=False"]
    """Pin the mode to the brush"""
    brush_draw_mode: Annotated[Literal['ACTIVE', 'MATERIAL', 'VERTEXCOLOR'], "is_animatable=False"]
    """Preselected mode when using this brush"""
    use_trim: Annotated[bool, "is_animatable=False"]
    """Trim intersecting stroke ends"""
    use_settings_outline: Annotated[bool, "is_animatable=False"]
    """Convert stroke to outline"""
    use_edit_position: Annotated[bool, "is_animatable=False"]
    """The brush affects the position of the point"""
    use_edit_strength: Annotated[bool, "is_animatable=False"]
    """The brush affects the color strength of the point"""
    use_edit_thickness: Annotated[bool, "is_animatable=False"]
    """The brush affects the thickness of the point"""
    use_edit_uv: Annotated[bool, "is_animatable=False"]
    """The brush affects the UV rotation of the point"""
    material: Annotated[Optional['Material'], "is_animatable=False"]
    """Material used for strokes drawn using this brush"""
    material_alt: Annotated[Optional['Material'], "is_animatable=False"]
    """Material used for secondary uses for this brush"""
    show_fill_boundary: Annotated[bool, "is_animatable=False"]
    """Show help lines for filling to see boundaries"""
    show_fill_extend: Annotated[bool, "is_animatable=False"]
    """Show help lines for stroke extension"""
    use_collide_strokes: Annotated[bool, "is_animatable=False"]
    """Check if extend lines collide with strokes"""
    show_fill: Annotated[bool, "is_animatable=False"]
    """Show transparent lines to use as boundary for filling"""
    use_auto_remove_fill_guides: Annotated[bool, "is_animatable=False"]
    """Automatically remove fill guide strokes after fill operation"""
    use_fill_limit: Annotated[bool, "is_animatable=False"]
    """Fill only visible areas in viewport"""
    use_settings_postprocess: Annotated[bool, "is_animatable=False"]
    """Additional post processing options for new strokes"""
    use_settings_random: Annotated[bool, "is_animatable=False"]
    """Random brush settings"""
    use_material_pin: Annotated[bool, "is_animatable=False"]
    """Keep material assigned to brush"""
    show_lasso: Annotated[bool, "is_animatable=False"]
    """Do not display fill color while drawing the stroke"""
    use_occlude_eraser: Annotated[bool, "is_animatable=False"]
    """Erase only strokes visible and not occluded"""
    use_keep_caps_eraser: Annotated[bool, "is_animatable=False"]
    """Keep the caps as they are and don't flatten them when erasing"""
    use_active_layer_only: Annotated[bool, "is_animatable=False"]
    """Only edit the active layer of the object"""