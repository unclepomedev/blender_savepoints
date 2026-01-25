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
class ClothSolverResult(bpy_struct):
    status: set[str]
    max_error: float
    min_error: float
    avg_error: float
    max_iterations: int
    min_iterations: int
    avg_iterations: float