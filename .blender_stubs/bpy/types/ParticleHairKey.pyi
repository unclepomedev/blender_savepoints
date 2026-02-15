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
class ParticleHairKey(bpy_struct):
    time: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    """Relative time of key over hair length"""
    weight: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]
    """Weight for cloth simulation"""
    co: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Location of the hair key in object space"""
    co_local: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Location of the hair key in its local coordinate system, relative to the emitting face"""
    def co_object(self, *args, **kwargs) -> Any: ...
    def co_object_set(self, *args, **kwargs) -> Any: ...