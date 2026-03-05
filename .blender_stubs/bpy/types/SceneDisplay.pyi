# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SceneDisplay.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .View3DShading import View3DShading

class SceneDisplay(bpy_struct):

    @property
    def light_direction(self) -> Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Direction of the light for shadows and highlights"""
        ...
    @light_direction.setter
    def light_direction(self, value: Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def shadow_shift(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=1.0", "precision=2", "is_animatable=False"]:
        """Shadow termination angle"""
        ...
    @shadow_shift.setter
    def shadow_shift(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=1.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def shadow_focus(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2", "is_animatable=False"]:
        """Shadow factor hardness"""
        ...
    @shadow_focus.setter
    def shadow_focus(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def matcap_ssao_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]:
        """Distance of object that contribute to the cavity/edge effect"""
        ...
    @matcap_ssao_distance.setter
    def matcap_ssao_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def matcap_ssao_attenuation(self) -> Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]:
        """Attenuation constant"""
        ...
    @matcap_ssao_attenuation.setter
    def matcap_ssao_attenuation(self, value: Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def matcap_ssao_samples(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Number of samples"""
        ...
    @matcap_ssao_samples.setter
    def matcap_ssao_samples(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def render_aa(self) -> Annotated[Literal['OFF', 'FXAA', '5', '8', '11', '16', '32'], "is_animatable=False"]:
        """Method of anti-aliasing when rendering final image"""
        ...
    @render_aa.setter
    def render_aa(self, value: Annotated[Literal['OFF', 'FXAA', '5', '8', '11', '16', '32'], "is_animatable=False"]):
        ...
    @property
    def viewport_aa(self) -> Annotated[Literal['OFF', 'FXAA', '5', '8', '11', '16', '32'], "is_animatable=False"]:
        """Method of anti-aliasing when rendering 3d viewport"""
        ...
    @viewport_aa.setter
    def viewport_aa(self, value: Annotated[Literal['OFF', 'FXAA', '5', '8', '11', '16', '32'], "is_animatable=False"]):
        ...
    @property
    def shading(self) -> Annotated[Optional['View3DShading'], "is_animatable=False"]:
        """Shading settings for OpenGL render engine"""
        ...