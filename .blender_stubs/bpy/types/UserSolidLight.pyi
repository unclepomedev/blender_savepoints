# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.UserSolidLight.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class UserSolidLight(bpy_struct):

    use: bool
    """Enable this light in solid shading mode"""
    smooth: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Smooth the lighting from this light"""
    direction: Annotated[list[float], "subtype='DIRECTION'", "step=10.0", "precision=3"]
    """Direction that the light is shining"""
    specular_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color of the light's specular highlight"""
    diffuse_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color of the light's diffuse highlight"""