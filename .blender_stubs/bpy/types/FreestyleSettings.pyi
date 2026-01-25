# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .FreestyleLineSet import FreestyleLineSet
from .FreestyleModuleSettings import FreestyleModuleSettings
class FreestyleSettings(bpy_struct):
    modules: bpy_prop_collection['FreestyleModuleSettings']
    mode: str
    use_culling: bool
    use_suggestive_contours: bool
    use_ridges_and_valleys: bool
    use_material_boundaries: bool
    use_smoothness: bool
    use_view_map_cache: bool
    as_render_pass: bool
    sphere_radius: float
    kr_derivative_epsilon: float
    crease_angle: float
    linesets: bpy_prop_collection['FreestyleLineSet']