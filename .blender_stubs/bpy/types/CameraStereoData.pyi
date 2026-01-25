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
class CameraStereoData(bpy_struct):
    convergence_mode: str
    pivot: str
    interocular_distance: float
    convergence_distance: float
    use_spherical_stereo: bool
    use_pole_merge: bool
    pole_merge_angle_from: float
    pole_merge_angle_to: float