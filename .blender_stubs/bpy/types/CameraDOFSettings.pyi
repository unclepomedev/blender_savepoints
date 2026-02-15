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

    use_dof: bool
    """Use Depth of Field"""
    focus_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Use this object to define the depth of field focal point"""
    focus_subtarget: Annotated[str, "is_animatable=False"]
    """Use this armature bone to define the depth of field focal point"""
    focus_distance: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=4"]
    """Distance to the focus point for depth of field"""
    aperture_fstop: Annotated[float, "step=10.0", "precision=1"]
    """F-Stop ratio (lower numbers give more defocus, higher numbers give a sharper image)"""
    aperture_blades: Annotated[int, "step=1"]
    """Number of blades in aperture for polygonal bokeh (at least 3)"""
    aperture_rotation: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Rotation of blades in aperture"""
    aperture_ratio: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Distortion to simulate anamorphic lens bokeh"""