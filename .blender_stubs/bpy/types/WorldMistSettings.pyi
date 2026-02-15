# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.WorldMistSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class WorldMistSettings(bpy_struct):

    use_mist: bool
    """Occlude objects with the environment color as they are further away"""
    intensity: Annotated[float, "step=10.0", "precision=3"]
    """Overall minimum intensity of the mist effect"""
    start: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]
    """Starting distance of the mist, measured from the camera"""
    depth: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=2"]
    """Distance over which the mist effect fades in"""
    height: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Control how much mist density decreases with height"""
    falloff: Literal['QUADRATIC', 'LINEAR', 'INVERSE_QUADRATIC']
    """Type of transition used to fade mist"""