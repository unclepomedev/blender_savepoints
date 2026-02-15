# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.XrNavigation.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class XrNavigation(bpy_struct):

    vignette_intensity: Annotated[float, "subtype='PERCENTAGE'", "step=1000.0", "precision=0"]
    """Intensity of vignette that appears when moving"""
    turn_speed: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=1000.0", "precision=0"]
    """Turn speed in degrees per second"""
    turn_amount: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=1000.0", "precision=0"]
    """Amount in degrees per turn when using snap turn"""
    snap_turn: bool
    """Instantly rotates the camera by a fixed angle instead of smoothly turning"""
    invert_rotation: bool
    """Reverses the direction of rotation input"""