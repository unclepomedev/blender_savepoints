# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ParticleTarget.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Object import Object

class ParticleTarget(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Particle target name"""
        ...
    object: Annotated[Optional['Object'], "is_animatable=False"]
    """The object that has the target particle system (empty if same object)"""
    system: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """The index of particle system on the target object"""
    time: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]

    duration: Annotated[float, "step=10.0", "precision=3"]

    is_valid: Annotated[bool, "is_animatable=False"]
    """Keyed particles target is valid"""
    alliance: Annotated[Literal['FRIEND', 'NEUTRAL', 'ENEMY'], "is_animatable=False"]
