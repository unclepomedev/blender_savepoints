# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .View3DShading import View3DShading
class SceneDisplay(bpy_struct):
    light_direction: Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Direction of the light for shadows and highlights"""
    shadow_shift: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=1.0", "precision=2", "is_animatable=False"]
    """Shadow termination angle"""
    shadow_focus: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2", "is_animatable=False"]
    """Shadow factor hardness"""
    matcap_ssao_distance: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]
    """Distance of object that contribute to the cavity/edge effect"""
    matcap_ssao_attenuation: Annotated[float, "step=1.0", "precision=3", "is_animatable=False"]
    """Attenuation constant"""
    matcap_ssao_samples: Annotated[int, "step=1", "is_animatable=False"]
    """Number of samples"""
    render_aa: Annotated[Literal['OFF', 'FXAA', '5', '8', '11', '16', '32'], "is_animatable=False"]
    """Method of anti-aliasing when rendering final image"""
    viewport_aa: Annotated[Literal['OFF', 'FXAA', '5', '8', '11', '16', '32'], "is_animatable=False"]
    """Method of anti-aliasing when rendering 3d viewport"""
    @property
    def shading(self) -> Annotated[Optional['View3DShading'], "is_animatable=False"]:
        """Shading settings for OpenGL render engine"""
        ...