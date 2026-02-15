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
class WorldLighting(bpy_struct):
    ao_factor: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]
    """Factor for ambient occlusion blending"""
    distance: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Length of rays, defines how far away other faces give occlusion effect"""