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
class View3DCursor(bpy_struct):
    location: float
    rotation_quaternion: float
    rotation_axis_angle: float
    rotation_euler: float
    rotation_mode: str
    matrix: float