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
    precision: Annotated[float, "step=10.0", "precision=3"]
    """Precision of convergence in case of reiteration"""
    iterations: Annotated[int, "step=1"]
    """Maximum number of iterations for convergence in case of reiteration"""
    step_count: Annotated[int, "step=1"]
    """Divide the frame interval into this many steps"""
    translate_root_bones: bool
    """Translate root (i.e. parentless) bones to the armature origin"""
    mode: Literal['ANIMATION', 'SIMULATION']

    reiteration_method: Literal['NEVER', 'INITIAL', 'ALWAYS']
    """Defines if the solver is allowed to reiterate (converge until precision is met) on none, first or all frames"""
    use_auto_step: bool
    """Automatically determine the optimal number of steps for best performance/accuracy trade off"""
    step_min: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Lower bound for timestep in second in case of automatic substeps"""
    step_max: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Higher bound for timestep in second in case of automatic substeps"""
    feedback: Annotated[float, "step=10.0", "precision=3"]
    """Feedback coefficient for error correction, average response time is 1/feedback"""
    velocity_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum joint velocity in radians/second"""
    solver: Literal['SDLS', 'DLS']
    """Solving method selection: automatic damping or manual damping"""
    damping_max: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Maximum damping coefficient when singular value is nearly 0 (higher values produce results with more stability, less reactivity)"""
    damping_epsilon: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Singular value under which damping is progressively applied (higher values produce results with more stability, less reactivity)"""