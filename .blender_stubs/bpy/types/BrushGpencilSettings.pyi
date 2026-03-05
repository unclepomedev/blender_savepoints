# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BrushGpencilSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .CurveMapping import CurveMapping
from .Material import Material

class BrushGpencilSettings(bpy_struct):

    @property
    def pen_strength(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]:
        """Color strength for new strokes (affect alpha factor of color)"""
        ...
    @pen_strength.setter
    def pen_strength(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]):
        ...
    @property
    def pen_jitter(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]:
        """Jitter factor of brush radius for new strokes"""
        ...
    @pen_jitter.setter
    def pen_jitter(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]):
        ...
    @property
    def random_pressure(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Randomness factor for pressure in new strokes"""
        ...
    @random_pressure.setter
    def random_pressure(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def random_strength(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Randomness factor strength in new strokes"""
        ...
    @random_strength.setter
    def random_strength(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Direction of the stroke at which brush gives maximal thickness (0° for horizontal)"""
        ...
    @angle.setter
    def angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def angle_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Reduce brush thickness by this factor when stroke is perpendicular to 'Angle' direction"""
        ...
    @angle_factor.setter
    def angle_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def pen_smooth_factor(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Amount of smoothing to apply after finish newly created strokes, to reduce jitter/noise"""
        ...
    @pen_smooth_factor.setter
    def pen_smooth_factor(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def pen_smooth_steps(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Number of times to smooth newly created strokes"""
        ...
    @pen_smooth_steps.setter
    def pen_smooth_steps(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def pen_subdivision_steps(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Number of times to subdivide newly created strokes, for less jagged strokes"""
        ...
    @pen_subdivision_steps.setter
    def pen_subdivision_steps(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def simplify_factor(self) -> Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]:
        """Factor of Simplify using adaptive algorithm"""
        ...
    @simplify_factor.setter
    def simplify_factor(self, value: Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def simplify_pixel_threshold(self) -> Annotated[float, "subtype='PIXEL'", "step=1.0", "precision=1", "is_animatable=False"]:
        """Threshold in screen space used for the simplify algorithm. Points within this threshold are treated as if they were in a straight line."""
        ...
    @simplify_pixel_threshold.setter
    def simplify_pixel_threshold(self, value: Annotated[float, "subtype='PIXEL'", "step=1.0", "precision=1", "is_animatable=False"]):
        ...
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
    @property
    def fill_threshold(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Threshold to consider color transparent for filling"""
        ...
    @fill_threshold.setter
    def fill_threshold(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def fill_factor(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Factor for fill boundary accuracy, higher values are more accurate but slower"""
        ...
    @fill_factor.setter
    def fill_factor(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def fill_simplify_level(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Number of simplify steps (large values reduce fill accuracy)"""
        ...
    @fill_simplify_level.setter
    def fill_simplify_level(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def uv_random(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Random factor for auto-generated UV rotation"""
        ...
    @uv_random.setter
    def uv_random(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def hardness(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Gradient from the center of Dot and Box strokes (set to 1 for a solid stroke)"""
        ...
    @hardness.setter
    def hardness(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def aspect(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]:

        ...
    @aspect.setter
    def aspect(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def input_samples(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Generated intermediate points for very fast mouse movements (Set to 0 to disable)"""
        ...
    @input_samples.setter
    def input_samples(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def active_smooth_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Amount of smoothing while drawing"""
        ...
    @active_smooth_factor.setter
    def active_smooth_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def eraser_strength_factor(self) -> Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=1", "is_animatable=False"]:
        """Amount of erasing for strength"""
        ...
    @eraser_strength_factor.setter
    def eraser_strength_factor(self, value: Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=1", "is_animatable=False"]):
        ...
    @property
    def eraser_thickness_factor(self) -> Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=1", "is_animatable=False"]:
        """Amount of erasing for thickness"""
        ...
    @eraser_thickness_factor.setter
    def eraser_thickness_factor(self, value: Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=1", "is_animatable=False"]):
        ...
    @property
    def vertex_mode(self) -> Annotated[Literal['STROKE', 'FILL', 'BOTH'], "is_animatable=False"]:
        """Defines how vertex color affect to the strokes"""
        ...
    @vertex_mode.setter
    def vertex_mode(self, value: Annotated[Literal['STROKE', 'FILL', 'BOTH'], "is_animatable=False"]):
        ...
    @property
    def vertex_color_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Factor used to mix vertex color to get final color"""
        ...
    @vertex_color_factor.setter
    def vertex_color_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def random_hue_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Random factor to modify original hue"""
        ...
    @random_hue_factor.setter
    def random_hue_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def random_saturation_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Random factor to modify original saturation"""
        ...
    @random_saturation_factor.setter
    def random_saturation_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def random_value_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Random factor to modify original value"""
        ...
    @random_value_factor.setter
    def random_value_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def extend_stroke_factor(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Strokes end extension for closing gaps, use zero to disable"""
        ...
    @extend_stroke_factor.setter
    def extend_stroke_factor(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def fill_extend_mode(self) -> Annotated[Literal['EXTEND', 'RADIUS'], "is_animatable=False"]:
        """Types of stroke extensions used for closing gaps"""
        ...
    @fill_extend_mode.setter
    def fill_extend_mode(self, value: Annotated[Literal['EXTEND', 'RADIUS'], "is_animatable=False"]):
        ...
    @property
    def dilate(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Number of pixels to expand or contract fill area"""
        ...
    @dilate.setter
    def dilate(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]):
        ...
    @property
    def outline_thickness_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Thickness of the outline stroke relative to current brush thickness"""
        ...
    @outline_thickness_factor.setter
    def outline_thickness_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def use_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Use tablet pressure"""
        ...
    @use_pressure.setter
    def use_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_strength_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Use tablet pressure for color strength"""
        ...
    @use_strength_pressure.setter
    def use_strength_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_jitter_pressure(self) -> Annotated[bool, "is_animatable=False"]:
        """Use tablet pressure for jitter"""
        ...
    @use_jitter_pressure.setter
    def use_jitter_pressure(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_stroke_random_hue(self) -> Annotated[bool, "is_animatable=False"]:
        """Use randomness at stroke level"""
        ...
    @use_stroke_random_hue.setter
    def use_stroke_random_hue(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_stroke_random_sat(self) -> Annotated[bool, "is_animatable=False"]:
        """Use randomness at stroke level"""
        ...
    @use_stroke_random_sat.setter
    def use_stroke_random_sat(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_stroke_random_val(self) -> Annotated[bool, "is_animatable=False"]:
        """Use randomness at stroke level"""
        ...
    @use_stroke_random_val.setter
    def use_stroke_random_val(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_stroke_random_radius(self) -> Annotated[bool, "is_animatable=False"]:
        """Use randomness at stroke level"""
        ...
    @use_stroke_random_radius.setter
    def use_stroke_random_radius(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_stroke_random_strength(self) -> Annotated[bool, "is_animatable=False"]:
        """Use randomness at stroke level"""
        ...
    @use_stroke_random_strength.setter
    def use_stroke_random_strength(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_stroke_random_uv(self) -> Annotated[bool, "is_animatable=False"]:
        """Use randomness at stroke level"""
        ...
    @use_stroke_random_uv.setter
    def use_stroke_random_uv(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_random_press_hue(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate randomness"""
        ...
    @use_random_press_hue.setter
    def use_random_press_hue(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_random_press_sat(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate randomness"""
        ...
    @use_random_press_sat.setter
    def use_random_press_sat(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_random_press_val(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate randomness"""
        ...
    @use_random_press_val.setter
    def use_random_press_val(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_random_press_radius(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate randomness"""
        ...
    @use_random_press_radius.setter
    def use_random_press_radius(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_random_press_strength(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate randomness"""
        ...
    @use_random_press_strength.setter
    def use_random_press_strength(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_random_press_uv(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate randomness"""
        ...
    @use_random_press_uv.setter
    def use_random_press_uv(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_settings_stabilizer(self) -> Annotated[bool, "is_animatable=False"]:
        """Draw lines with a delay to allow smooth strokes (press Shift key to override while drawing)"""
        ...
    @use_settings_stabilizer.setter
    def use_settings_stabilizer(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def eraser_mode(self) -> Annotated[Literal['SOFT', 'HARD', 'STROKE'], "is_animatable=False"]:
        """Eraser Mode"""
        ...
    @eraser_mode.setter
    def eraser_mode(self, value: Annotated[Literal['SOFT', 'HARD', 'STROKE'], "is_animatable=False"]):
        ...
    @property
    def caps_type(self) -> Annotated[Literal['ROUND', 'FLAT'], "is_animatable=False"]:
        """The shape of the start and end of the stroke"""
        ...
    @caps_type.setter
    def caps_type(self, value: Annotated[Literal['ROUND', 'FLAT'], "is_animatable=False"]):
        ...
    @property
    def fill_draw_mode(self) -> Annotated[Literal['BOTH', 'STROKE', 'CONTROL'], "is_animatable=False"]:
        """Mode to draw boundary limits"""
        ...
    @fill_draw_mode.setter
    def fill_draw_mode(self, value: Annotated[Literal['BOTH', 'STROKE', 'CONTROL'], "is_animatable=False"]):
        ...
    @property
    def fill_layer_mode(self) -> Annotated[Literal['VISIBLE', 'ACTIVE', 'ABOVE', 'BELOW', 'ALL_ABOVE', 'ALL_BELOW'], "is_animatable=False"]:
        """Layers used as boundaries"""
        ...
    @fill_layer_mode.setter
    def fill_layer_mode(self, value: Annotated[Literal['VISIBLE', 'ACTIVE', 'ABOVE', 'BELOW', 'ALL_ABOVE', 'ALL_BELOW'], "is_animatable=False"]):
        ...
    @property
    def fill_direction(self) -> Annotated[Literal['NORMAL', 'INVERT'], "is_animatable=False"]:
        """Direction of the fill"""
        ...
    @fill_direction.setter
    def fill_direction(self, value: Annotated[Literal['NORMAL', 'INVERT'], "is_animatable=False"]):
        ...
    @property
    def pin_draw_mode(self) -> Annotated[bool, "is_animatable=False"]:
        """Pin the mode to the brush"""
        ...
    @pin_draw_mode.setter
    def pin_draw_mode(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def brush_draw_mode(self) -> Annotated[Literal['ACTIVE', 'MATERIAL', 'VERTEXCOLOR'], "is_animatable=False"]:
        """Preselected mode when using this brush"""
        ...
    @brush_draw_mode.setter
    def brush_draw_mode(self, value: Annotated[Literal['ACTIVE', 'MATERIAL', 'VERTEXCOLOR'], "is_animatable=False"]):
        ...
    @property
    def use_trim(self) -> Annotated[bool, "is_animatable=False"]:
        """Trim intersecting stroke ends"""
        ...
    @use_trim.setter
    def use_trim(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_settings_outline(self) -> Annotated[bool, "is_animatable=False"]:
        """Convert stroke to outline"""
        ...
    @use_settings_outline.setter
    def use_settings_outline(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_edit_position(self) -> Annotated[bool, "is_animatable=False"]:
        """The brush affects the position of the point"""
        ...
    @use_edit_position.setter
    def use_edit_position(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_edit_strength(self) -> Annotated[bool, "is_animatable=False"]:
        """The brush affects the color strength of the point"""
        ...
    @use_edit_strength.setter
    def use_edit_strength(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_edit_thickness(self) -> Annotated[bool, "is_animatable=False"]:
        """The brush affects the thickness of the point"""
        ...
    @use_edit_thickness.setter
    def use_edit_thickness(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_edit_uv(self) -> Annotated[bool, "is_animatable=False"]:
        """The brush affects the UV rotation of the point"""
        ...
    @use_edit_uv.setter
    def use_edit_uv(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def material(self) -> Annotated[Optional['Material'], "is_animatable=False"]:
        """Material used for strokes drawn using this brush"""
        ...
    @material.setter
    def material(self, value: Annotated[Optional['Material'], "is_animatable=False"]):
        ...
    @property
    def material_alt(self) -> Annotated[Optional['Material'], "is_animatable=False"]:
        """Material used for secondary uses for this brush"""
        ...
    @material_alt.setter
    def material_alt(self, value: Annotated[Optional['Material'], "is_animatable=False"]):
        ...
    @property
    def show_fill_boundary(self) -> Annotated[bool, "is_animatable=False"]:
        """Show help lines for filling to see boundaries"""
        ...
    @show_fill_boundary.setter
    def show_fill_boundary(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_fill_extend(self) -> Annotated[bool, "is_animatable=False"]:
        """Show help lines for stroke extension"""
        ...
    @show_fill_extend.setter
    def show_fill_extend(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_collide_strokes(self) -> Annotated[bool, "is_animatable=False"]:
        """Check if extend lines collide with strokes"""
        ...
    @use_collide_strokes.setter
    def use_collide_strokes(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_fill(self) -> Annotated[bool, "is_animatable=False"]:
        """Show transparent lines to use as boundary for filling"""
        ...
    @show_fill.setter
    def show_fill(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_auto_remove_fill_guides(self) -> Annotated[bool, "is_animatable=False"]:
        """Automatically remove fill guide strokes after fill operation"""
        ...
    @use_auto_remove_fill_guides.setter
    def use_auto_remove_fill_guides(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_fill_limit(self) -> Annotated[bool, "is_animatable=False"]:
        """Fill only visible areas in viewport"""
        ...
    @use_fill_limit.setter
    def use_fill_limit(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_settings_postprocess(self) -> Annotated[bool, "is_animatable=False"]:
        """Additional post processing options for new strokes"""
        ...
    @use_settings_postprocess.setter
    def use_settings_postprocess(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_settings_random(self) -> Annotated[bool, "is_animatable=False"]:
        """Random brush settings"""
        ...
    @use_settings_random.setter
    def use_settings_random(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_material_pin(self) -> Annotated[bool, "is_animatable=False"]:
        """Keep material assigned to brush"""
        ...
    @use_material_pin.setter
    def use_material_pin(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_lasso(self) -> Annotated[bool, "is_animatable=False"]:
        """Do not display fill color while drawing the stroke"""
        ...
    @show_lasso.setter
    def show_lasso(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_occlude_eraser(self) -> Annotated[bool, "is_animatable=False"]:
        """Erase only strokes visible and not occluded"""
        ...
    @use_occlude_eraser.setter
    def use_occlude_eraser(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_keep_caps_eraser(self) -> Annotated[bool, "is_animatable=False"]:
        """Keep the caps as they are and don't flatten them when erasing"""
        ...
    @use_keep_caps_eraser.setter
    def use_keep_caps_eraser(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_active_layer_only(self) -> Annotated[bool, "is_animatable=False"]:
        """Only edit the active layer of the object"""
        ...
    @use_active_layer_only.setter
    def use_active_layer_only(self, value: Annotated[bool, "is_animatable=False"]):
        ...