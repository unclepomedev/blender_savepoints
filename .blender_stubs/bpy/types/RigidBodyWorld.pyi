# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.RigidBodyWorld.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Collection import Collection
from .EffectorWeights import EffectorWeights
from .PointCache import PointCache

class RigidBodyWorld(bpy_struct):

    @property
    def collection(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Collection containing objects participating in this simulation"""
        ...
    @collection.setter
    def collection(self, value: Annotated[Optional['Collection'], "is_animatable=False"]):
        ...
    @property
    def constraints(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Collection containing rigid body constraint objects"""
        ...
    @constraints.setter
    def constraints(self, value: Annotated[Optional['Collection'], "is_animatable=False"]):
        ...
    @property
    def enabled(self) -> bool:
        """Simulation will be evaluated"""
        ...
    @enabled.setter
    def enabled(self, value: bool):
        ...
    @property
    def time_scale(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Change the speed of the simulation"""
        ...
    @time_scale.setter
    def time_scale(self, value: Annotated[float, "step=1.0", "precision=3"]):
        ...
    @property
    def substeps_per_frame(self) -> Annotated[int, "step=1"]:
        """Number of simulation steps taken per frame (higher values are more accurate but slower)"""
        ...
    @substeps_per_frame.setter
    def substeps_per_frame(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def solver_iterations(self) -> Annotated[int, "step=1"]:
        """Number of constraint solver iterations made per simulation step (higher values are more accurate but slower)"""
        ...
    @solver_iterations.setter
    def solver_iterations(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def use_split_impulse(self) -> bool:
        """Reduce extra velocity that can build up when objects collide (lowers simulation stability a little so use only when necessary)"""
        ...
    @use_split_impulse.setter
    def use_split_impulse(self, value: bool):
        ...
    @property
    def point_cache(self) -> Annotated['PointCache', "is_animatable=False"]:

        ...
    @property
    def effector_weights(self) -> Annotated[Optional['EffectorWeights'], "is_animatable=False"]:

        ...
    def convex_sweep_test(self, *args, **kwargs) -> Any: ...