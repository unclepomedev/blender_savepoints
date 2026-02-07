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
from .ParticleSystem import ParticleSystem
class ParticleSystems(bpy_struct):
    active: 'ParticleSystem'
    active_index: int
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['ParticleSystem']: ...
    def __getitem__(self, key: Union[str, int]) -> 'ParticleSystem': ...
    def __len__(self) -> int: ...