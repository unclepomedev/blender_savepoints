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
class XrEventData(bpy_struct):
    action_set: str
    action: str
    user_path: str
    user_path_other: str
    type: str
    state: list[float]
    state_other: list[float]
    float_threshold: float
    controller_location: list[float]
    controller_rotation: list[float]
    controller_location_other: list[float]
    controller_rotation_other: list[float]
    bimanual: bool