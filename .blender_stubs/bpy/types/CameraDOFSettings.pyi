# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CameraDOFSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Object import Object

class CameraDOFSettings(bpy_struct):

    @property
    def use_dof(self) -> bool:
        """Use Depth of Field"""
        ...
    @use_dof.setter
    def use_dof(self, value: bool) -> None:
        ...
    @property
    def focus_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Use this object to define the depth of field focal point"""
        ...
    @focus_object.setter
    def focus_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def focus_subtarget(self) -> Annotated[str, "is_animatable=False"]:
        """Use this armature bone to define the depth of field focal point"""
        ...
    @focus_subtarget.setter
    def focus_subtarget(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def focus_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=4"]:
        """Distance to the focus point for depth of field"""
        ...
    @focus_distance.setter
    def focus_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=4"]) -> None:
        ...
    @property
    def aperture_fstop(self) -> Annotated[float, "step=10.0", "precision=1"]:
        """F-Stop ratio (lower numbers give more defocus, higher numbers give a sharper image)"""
        ...
    @aperture_fstop.setter
    def aperture_fstop(self, value: Annotated[float, "step=10.0", "precision=1"]) -> None:
        ...
    @property
    def aperture_blades(self) -> Annotated[int, "step=1"]:
        """Number of blades in aperture for polygonal bokeh (at least 3)"""
        ...
    @aperture_blades.setter
    def aperture_blades(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def aperture_rotation(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]:
        """Rotation of blades in aperture"""
        ...
    @aperture_rotation.setter
    def aperture_rotation(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def aperture_ratio(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Distortion to simulate anamorphic lens bokeh"""
        ...
    @aperture_ratio.setter
    def aperture_ratio(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...