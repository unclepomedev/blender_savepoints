# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ViewLayerEEVEE.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ViewLayerEEVEE(bpy_struct):

    @property
    def use_pass_volume_direct(self) -> Annotated[bool, "is_animatable=False"]:
        """Deliver volume direct light pass"""
        ...
    @use_pass_volume_direct.setter
    def use_pass_volume_direct(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pass_bloom(self) -> Annotated[bool, "is_animatable=False"]:
        """Deliver bloom pass (deprecated)"""
        ...
    @use_pass_bloom.setter
    def use_pass_bloom(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pass_transparent(self) -> Annotated[bool, "is_animatable=False"]:
        """Deliver alpha blended surfaces in a separate pass"""
        ...
    @use_pass_transparent.setter
    def use_pass_transparent(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def ambient_occlusion_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]:
        """Distance of object that contribute to the ambient occlusion effect"""
        ...
    @ambient_occlusion_distance.setter
    def ambient_occlusion_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...