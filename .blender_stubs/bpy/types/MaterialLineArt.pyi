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
class MaterialLineArt(bpy_struct):
    use_material_mask: bool
    use_material_mask_bits: bool
    mat_occlusion: int
    intersection_priority: int
    use_intersection_priority_override: bool