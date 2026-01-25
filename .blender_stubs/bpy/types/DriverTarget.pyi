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
from .ID import ID
class DriverTarget(bpy_struct):
    id: 'ID'
    id_type: str
    data_path: str
    bone_target: str
    transform_type: str
    rotation_mode: str
    transform_space: str
    context_property: str
    use_fallback_value: bool
    fallback_value: float
    is_fallback_used: bool