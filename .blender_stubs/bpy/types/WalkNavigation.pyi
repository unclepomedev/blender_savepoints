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
class WalkNavigation(bpy_struct):
    mouse_speed: float
    walk_speed: float
    walk_speed_factor: float
    view_height: float
    jump_height: float
    teleport_time: float
    use_gravity: bool
    use_mouse_reverse: bool