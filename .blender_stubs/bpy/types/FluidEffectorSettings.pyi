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
class FluidEffectorSettings(bpy_struct):
    effector_type: str
    surface_distance: float
    use_plane_init: bool
    velocity_factor: float
    guide_mode: str
    use_effector: bool
    subframes: int