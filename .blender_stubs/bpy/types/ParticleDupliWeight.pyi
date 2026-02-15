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
class ParticleDupliWeight(bpy_struct):
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Particle instance object name"""
        ...
    count: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """The number of times this object is repeated with respect to other objects"""