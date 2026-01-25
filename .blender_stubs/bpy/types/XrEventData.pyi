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
class XrEventData(bpy_struct):
    action_set: str
    action: str
    user_path: str
    user_path_other: str
    type: str
    state: float
    state_other: float
    float_threshold: float
    controller_location: float
    controller_rotation: float
    controller_location_other: float
    controller_rotation_other: float
    bimanual: bool