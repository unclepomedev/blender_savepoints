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
class VolumeRender(bpy_struct):
    precision: Literal['FULL', 'HALF', 'VARIABLE']
    """Specify volume data precision. Lower values reduce memory consumption at the cost of detail."""
    space: Literal['OBJECT', 'WORLD']
    """Specify volume density and step size in object or world space"""
    step_size: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]
    """Distance between volume samples. Lower values render more detail at the cost of performance. If set to zero, the step size is automatically determined based on voxel size."""
    clipping: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Value under which voxels are considered empty space to optimize rendering"""