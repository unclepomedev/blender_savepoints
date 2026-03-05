# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CameraStereoData.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class CameraStereoData(bpy_struct):

    @property
    def convergence_mode(self) -> Literal['OFFAXIS', 'PARALLEL', 'TOE']:

        ...
    @convergence_mode.setter
    def convergence_mode(self, value: Literal['OFFAXIS', 'PARALLEL', 'TOE']) -> None:
        ...
    @property
    def pivot(self) -> Literal['LEFT', 'RIGHT', 'CENTER']:

        ...
    @pivot.setter
    def pivot(self, value: Literal['LEFT', 'RIGHT', 'CENTER']) -> None:
        ...
    @property
    def interocular_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]:
        """Set the distance between the eyes - the stereo plane distance / 30 should be fine"""
        ...
    @interocular_distance.setter
    def interocular_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def convergence_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]:
        """The converge point for the stereo cameras (often the distance between a projector and the projection screen)"""
        ...
    @convergence_distance.setter
    def convergence_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def use_spherical_stereo(self) -> bool:
        """Render every pixel rotating the camera around the middle of the interocular distance"""
        ...
    @use_spherical_stereo.setter
    def use_spherical_stereo(self, value: bool) -> None:
        ...
    @property
    def use_pole_merge(self) -> bool:
        """Fade interocular distance to 0 after the given cutoff angle"""
        ...
    @use_pole_merge.setter
    def use_pole_merge(self, value: bool) -> None:
        ...
    @property
    def pole_merge_angle_from(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Angle at which interocular distance starts to fade to 0"""
        ...
    @pole_merge_angle_from.setter
    def pole_merge_angle_from(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def pole_merge_angle_to(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Angle at which interocular distance is 0"""
        ...
    @pole_merge_angle_to.setter
    def pole_merge_angle_to(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...