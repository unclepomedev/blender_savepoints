# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FluidEffectorSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class FluidEffectorSettings(bpy_struct):

    @property
    def effector_type(self) -> Literal['COLLISION', 'GUIDE']:
        """Change type of effector in the simulation"""
        ...
    @effector_type.setter
    def effector_type(self, value: Literal['COLLISION', 'GUIDE']) -> None:
        ...
    @property
    def surface_distance(self) -> Annotated[float, "step=0.05000000074505806", "precision=5"]:
        """Additional distance around mesh surface to consider as effector"""
        ...
    @surface_distance.setter
    def surface_distance(self, value: Annotated[float, "step=0.05000000074505806", "precision=5"]) -> None:
        ...
    @property
    def use_plane_init(self) -> bool:
        """Treat this object as a planar, unclosed mesh"""
        ...
    @use_plane_init.setter
    def use_plane_init(self, value: bool) -> None:
        ...
    @property
    def velocity_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Multiplier of obstacle velocity"""
        ...
    @velocity_factor.setter
    def velocity_factor(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def guide_mode(self) -> Literal['MAXIMUM', 'MINIMUM', 'OVERRIDE', 'AVERAGED']:
        """How to create guiding velocities"""
        ...
    @guide_mode.setter
    def guide_mode(self, value: Literal['MAXIMUM', 'MINIMUM', 'OVERRIDE', 'AVERAGED']) -> None:
        ...
    @property
    def use_effector(self) -> bool:
        """Control when to apply the effector"""
        ...
    @use_effector.setter
    def use_effector(self, value: bool) -> None:
        ...
    @property
    def subframes(self) -> Annotated[int, "step=1"]:
        """Number of additional samples to take between frames to improve quality of fast moving effector objects"""
        ...
    @subframes.setter
    def subframes(self, value: Annotated[int, "step=1"]) -> None:
        ...