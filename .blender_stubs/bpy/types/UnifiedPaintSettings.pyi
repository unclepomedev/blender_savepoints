# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.UnifiedPaintSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class UnifiedPaintSettings(bpy_struct):

    @property
    def use_unified_size(self) -> Annotated[bool, "is_animatable=False"]:
        """Instead of per-brush size, the size is shared across brushes"""
        ...
    @use_unified_size.setter
    def use_unified_size(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_unified_strength(self) -> Annotated[bool, "is_animatable=False"]:
        """Instead of per-brush strength, the strength is shared across brushes"""
        ...
    @use_unified_strength.setter
    def use_unified_strength(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_unified_weight(self) -> Annotated[bool, "is_animatable=False"]:
        """Instead of per-brush weight, the weight is shared across brushes"""
        ...
    @use_unified_weight.setter
    def use_unified_weight(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_unified_color(self) -> Annotated[bool, "is_animatable=False"]:
        """Instead of per-brush color, the color is shared across brushes"""
        ...
    @use_unified_color.setter
    def use_unified_color(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_unified_input_samples(self) -> Annotated[bool, "is_animatable=False"]:
        """Instead of per-brush input samples, the value is shared across brushes"""
        ...
    @use_unified_input_samples.setter
    def use_unified_input_samples(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def size(self) -> Annotated[int, "subtype='PIXEL_DIAMETER'", "step=1", "is_animatable=False"]:
        """Diameter of the brush"""
        ...
    @size.setter
    def size(self, value: Annotated[int, "subtype='PIXEL_DIAMETER'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def unprojected_size(self) -> Annotated[float, "subtype='DISTANCE_DIAMETER'", "unit='LENGTH'", "step=1.0", "precision=-1", "is_animatable=False"]:
        """Diameter of brush in Blender units"""
        ...
    @unprojected_size.setter
    def unprojected_size(self, value: Annotated[float, "subtype='DISTANCE_DIAMETER'", "unit='LENGTH'", "step=1.0", "precision=-1", "is_animatable=False"]) -> None:
        ...
    @property
    def strength(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]:
        """How powerful the effect of the brush is when applied"""
        ...
    @strength.setter
    def strength(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def weight(self) -> Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]:
        """Weight to assign in vertex groups"""
        ...
    @weight.setter
    def weight(self, value: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3", "is_animatable=False"]:

        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def secondary_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3", "is_animatable=False"]:

        ...
    @secondary_color.setter
    def secondary_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def use_color_jitter(self) -> Annotated[bool, "is_animatable=False"]:
        """Jitter brush color"""
        ...
    @use_color_jitter.setter
    def use_color_jitter(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def hue_jitter(self) -> Annotated[float, "step=0.05000000074505806", "precision=2", "is_animatable=False"]:
        """Color jitter effect on hue"""
        ...
    @hue_jitter.setter
    def hue_jitter(self, value: Annotated[float, "step=0.05000000074505806", "precision=2", "is_animatable=False"]) -> None:
        ...
    @property
    def saturation_jitter(self) -> Annotated[float, "step=0.05000000074505806", "precision=2", "is_animatable=False"]:
        """Color jitter effect on saturation"""
        ...
    @saturation_jitter.setter
    def saturation_jitter(self, value: Annotated[float, "step=0.05000000074505806", "precision=2", "is_animatable=False"]) -> None:
        ...
    @property
    def value_jitter(self) -> Annotated[float, "step=0.05000000074505806", "precision=2", "is_animatable=False"]:
        """Color jitter effect on value"""
        ...
    @value_jitter.setter
    def value_jitter(self, value: Annotated[float, "step=0.05000000074505806", "precision=2", "is_animatable=False"]) -> None:
        ...
    @property
    def use_stroke_random_hue(self) -> Annotated[bool, "is_animatable=False"]:
        """Use randomness at stroke level"""
        ...
    @use_stroke_random_hue.setter
    def use_stroke_random_hue(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_stroke_random_sat(self) -> Annotated[bool, "is_animatable=False"]:
        """Use randomness at stroke level"""
        ...
    @use_stroke_random_sat.setter
    def use_stroke_random_sat(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_stroke_random_val(self) -> Annotated[bool, "is_animatable=False"]:
        """Use randomness at stroke level"""
        ...
    @use_stroke_random_val.setter
    def use_stroke_random_val(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_random_press_hue(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate randomness"""
        ...
    @use_random_press_hue.setter
    def use_random_press_hue(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_random_press_sat(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate randomness"""
        ...
    @use_random_press_sat.setter
    def use_random_press_sat(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_random_press_val(self) -> Annotated[bool, "is_animatable=False"]:
        """Use pressure to modulate randomness"""
        ...
    @use_random_press_val.setter
    def use_random_press_val(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def input_samples(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Number of input samples to average together to smooth the brush stroke"""
        ...
    @input_samples.setter
    def input_samples(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def use_locked_size(self) -> Annotated[Literal['VIEW', 'SCENE'], "is_animatable=False"]:
        """Measure brush size relative to the view or the scene"""
        ...
    @use_locked_size.setter
    def use_locked_size(self, value: Annotated[Literal['VIEW', 'SCENE'], "is_animatable=False"]) -> None:
        ...