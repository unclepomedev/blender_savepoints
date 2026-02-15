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
class MaterialLineArt(bpy_struct):
    use_material_mask: bool
    """Use material masks to filter out occluded strokes"""
    use_material_mask_bits: list[bool]
    mat_occlusion: Annotated[int, "step=1"]
    """Faces with this material will behave as if it has set number of layers in occlusion"""
    intersection_priority: Annotated[int, "step=1"]
    """The intersection line will be included into the object with the higher intersection priority value"""
    use_intersection_priority_override: bool
    """Override object and collection intersection priority value"""