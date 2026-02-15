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
class UnifiedPaintSettings(bpy_struct):
    use_unified_size: Annotated[bool, "is_animatable=False"]
    """Instead of per-brush size, the size is shared across brushes"""
    use_unified_strength: Annotated[bool, "is_animatable=False"]
    """Instead of per-brush strength, the strength is shared across brushes"""
    use_unified_weight: Annotated[bool, "is_animatable=False"]
    """Instead of per-brush weight, the weight is shared across brushes"""
    use_unified_color: Annotated[bool, "is_animatable=False"]
    """Instead of per-brush color, the color is shared across brushes"""
    use_unified_input_samples: Annotated[bool, "is_animatable=False"]
    """Instead of per-brush input samples, the value is shared across brushes"""
    size: Annotated[int, "subtype='PIXEL_DIAMETER'", "step=1", "is_animatable=False"]
    """Diameter of the brush"""
    unprojected_size: Annotated[float, "subtype='DISTANCE_DIAMETER'", "unit='LENGTH'", "step=1.0", "precision=-1", "is_animatable=False"]
    """Diameter of brush in Blender units"""
    strength: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]
    """How powerful the effect of the brush is when applied"""
    weight: Annotated[float, "subtype='FACTOR'", "step=0.0010000000474974513", "precision=3", "is_animatable=False"]
    """Weight to assign in vertex groups"""
    color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3", "is_animatable=False"]
    secondary_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3", "is_animatable=False"]
    use_color_jitter: Annotated[bool, "is_animatable=False"]
    """Jitter brush color"""
    hue_jitter: Annotated[float, "step=0.05000000074505806", "precision=2", "is_animatable=False"]
    """Color jitter effect on hue"""
    saturation_jitter: Annotated[float, "step=0.05000000074505806", "precision=2", "is_animatable=False"]
    """Color jitter effect on saturation"""
    value_jitter: Annotated[float, "step=0.05000000074505806", "precision=2", "is_animatable=False"]
    """Color jitter effect on value"""
    use_stroke_random_hue: Annotated[bool, "is_animatable=False"]
    """Use randomness at stroke level"""
    use_stroke_random_sat: Annotated[bool, "is_animatable=False"]
    """Use randomness at stroke level"""
    use_stroke_random_val: Annotated[bool, "is_animatable=False"]
    """Use randomness at stroke level"""
    use_random_press_hue: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate randomness"""
    use_random_press_sat: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate randomness"""
    use_random_press_val: Annotated[bool, "is_animatable=False"]
    """Use pressure to modulate randomness"""
    input_samples: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Number of input samples to average together to smooth the brush stroke"""
    use_locked_size: Annotated[Literal['VIEW', 'SCENE'], "is_animatable=False"]
    """Measure brush size relative to the view or the scene"""