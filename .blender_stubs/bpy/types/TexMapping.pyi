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
class TexMapping(bpy_struct):
    vector_type: str
    translation: float
    rotation: float
    scale: float
    min: float
    max: float
    use_min: bool
    use_max: bool
    mapping_x: str
    mapping_y: str
    mapping_z: str
    mapping: str