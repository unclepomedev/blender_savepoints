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
class UnifiedPaintSettings(bpy_struct):
    use_unified_size: bool
    use_unified_strength: bool
    use_unified_weight: bool
    use_unified_color: bool
    use_unified_input_samples: bool
    size: int
    unprojected_size: float
    strength: float
    weight: float
    color: float
    secondary_color: float
    use_color_jitter: bool
    hue_jitter: float
    saturation_jitter: float
    value_jitter: float
    use_stroke_random_hue: bool
    use_stroke_random_sat: bool
    use_stroke_random_val: bool
    use_random_press_hue: bool
    use_random_press_sat: bool
    use_random_press_val: bool
    input_samples: int
    use_locked_size: str