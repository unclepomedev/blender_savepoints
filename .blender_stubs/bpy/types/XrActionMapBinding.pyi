# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.XrActionMapBinding.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .XrComponentPath import XrComponentPath
from .XrComponentPaths import XrComponentPaths
from .bpy_prop_collection import bpy_prop_collection

class XrActionMapBinding(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the action map binding"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def profile(self) -> Annotated[str, "is_animatable=False"]:
        """OpenXR interaction profile path"""
        ...
    @profile.setter
    def profile(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def component_paths(self) -> Annotated['XrComponentPaths', "is_animatable=False"]:
        """OpenXR component paths"""
        ...
    @property
    def threshold(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Input threshold for button/axis actions"""
        ...
    @threshold.setter
    def threshold(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def axis0_region(self) -> Annotated[Literal['ANY', 'POSITIVE', 'NEGATIVE'], "is_animatable=False"]:
        """Action execution region for the first input axis"""
        ...
    @axis0_region.setter
    def axis0_region(self, value: Annotated[Literal['ANY', 'POSITIVE', 'NEGATIVE'], "is_animatable=False"]) -> None:
        ...
    @property
    def axis1_region(self) -> Annotated[Literal['ANY', 'POSITIVE', 'NEGATIVE'], "is_animatable=False"]:
        """Action execution region for the second input axis"""
        ...
    @axis1_region.setter
    def axis1_region(self, value: Annotated[Literal['ANY', 'POSITIVE', 'NEGATIVE'], "is_animatable=False"]) -> None:
        ...
    @property
    def pose_location(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]:

        ...
    @pose_location.setter
    def pose_location(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def pose_rotation(self) -> Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:

        ...
    @pose_rotation.setter
    def pose_rotation(self, value: Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...