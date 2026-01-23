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
from .GPencilSculptGuide import GPencilSculptGuide
class GPencilSculptSettings(bpy_struct):
    guide: 'GPencilSculptGuide'
    use_multiframe_falloff: bool
    use_thickness_curve: bool
    use_scale_thickness: bool
    use_automasking_stroke: bool
    use_automasking_layer_stroke: bool
    use_automasking_material_stroke: bool
    use_automasking_layer_active: bool
    use_automasking_material_active: bool
    multiframe_falloff_curve: 'CurveMapping'
    thickness_primitive_curve: 'CurveMapping'
    lock_axis: str
    intersection_threshold: float