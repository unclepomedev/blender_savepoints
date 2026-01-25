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
from .Collection import Collection
from .EffectorWeights import EffectorWeights
from .PointCache import PointCache
class RigidBodyWorld(bpy_struct):
    collection: 'Collection'
    constraints: 'Collection'
    enabled: bool
    time_scale: float
    substeps_per_frame: int
    solver_iterations: int
    use_split_impulse: bool
    point_cache: 'PointCache'
    effector_weights: 'EffectorWeights'
    def convex_sweep_test(self, *args, **kwargs) -> Any: ...