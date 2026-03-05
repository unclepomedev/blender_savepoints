# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Itasc.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .IKParam import IKParam

class Itasc(IKParam):

    @property
    def ik_solver(self) -> Literal['LEGACY', 'ITASC']:
        """IK solver for which these parameters are defined"""
        ...
    @property
    def precision(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Precision of convergence in case of reiteration"""
        ...
    @precision.setter
    def precision(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def iterations(self) -> Annotated[int, "step=1"]:
        """Maximum number of iterations for convergence in case of reiteration"""
        ...
    @iterations.setter
    def iterations(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def step_count(self) -> Annotated[int, "step=1"]:
        """Divide the frame interval into this many steps"""
        ...
    @step_count.setter
    def step_count(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def translate_root_bones(self) -> bool:
        """Translate root (i.e. parentless) bones to the armature origin"""
        ...
    @translate_root_bones.setter
    def translate_root_bones(self, value: bool):
        ...
    @property
    def mode(self) -> Literal['ANIMATION', 'SIMULATION']:

        ...
    @mode.setter
    def mode(self, value: Literal['ANIMATION', 'SIMULATION']):
        ...
    @property
    def reiteration_method(self) -> Literal['NEVER', 'INITIAL', 'ALWAYS']:
        """Defines if the solver is allowed to reiterate (converge until precision is met) on none, first or all frames"""
        ...
    @reiteration_method.setter
    def reiteration_method(self, value: Literal['NEVER', 'INITIAL', 'ALWAYS']):
        ...
    @property
    def use_auto_step(self) -> bool:
        """Automatically determine the optimal number of steps for best performance/accuracy trade off"""
        ...
    @use_auto_step.setter
    def use_auto_step(self, value: bool):
        ...
    @property
    def step_min(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Lower bound for timestep in second in case of automatic substeps"""
        ...
    @step_min.setter
    def step_min(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def step_max(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Higher bound for timestep in second in case of automatic substeps"""
        ...
    @step_max.setter
    def step_max(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def feedback(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Feedback coefficient for error correction, average response time is 1/feedback"""
        ...
    @feedback.setter
    def feedback(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def velocity_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum joint velocity in radians/second"""
        ...
    @velocity_max.setter
    def velocity_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def solver(self) -> Literal['SDLS', 'DLS']:
        """Solving method selection: automatic damping or manual damping"""
        ...
    @solver.setter
    def solver(self, value: Literal['SDLS', 'DLS']):
        ...
    @property
    def damping_max(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Maximum damping coefficient when singular value is nearly 0 (higher values produce results with more stability, less reactivity)"""
        ...
    @damping_max.setter
    def damping_max(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def damping_epsilon(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Singular value under which damping is progressively applied (higher values produce results with more stability, less reactivity)"""
        ...
    @damping_epsilon.setter
    def damping_epsilon(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...