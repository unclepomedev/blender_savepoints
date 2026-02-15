# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ParticleSystems.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ParticleSystem import ParticleSystem

class ParticleSystems(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['ParticleSystem'], "is_animatable=False"]:
        """Active particle system being displayed"""
        ...
    active_index: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Index of active particle system slot"""
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['ParticleSystem']: ...
    def __getitem__(self, key: Union[str, int]) -> 'ParticleSystem': ...
    def __len__(self) -> int: ...