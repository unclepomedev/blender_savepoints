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
class ParticleKey(bpy_struct):
    location: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Key location"""
    velocity: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]
    """Key velocity"""
    rotation: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]
    """Key rotation quaternion"""
    angular_velocity: Annotated[list[float], "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3"]
    """Key angular velocity"""
    time: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    """Time of key over the simulation"""