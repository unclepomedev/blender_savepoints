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

    name: Annotated[str, "is_animatable=False"]
    """Name of the action map binding"""
    profile: Annotated[str, "is_animatable=False"]
    """OpenXR interaction profile path"""
    @property
    def component_paths(self) -> Annotated['XrComponentPaths', "is_animatable=False"]:
        """OpenXR component paths"""
        ...
    threshold: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Input threshold for button/axis actions"""
    axis0_region: Annotated[Literal['ANY', 'POSITIVE', 'NEGATIVE'], "is_animatable=False"]
    """Action execution region for the first input axis"""
    axis1_region: Annotated[Literal['ANY', 'POSITIVE', 'NEGATIVE'], "is_animatable=False"]
    """Action execution region for the second input axis"""
    pose_location: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]

    pose_rotation: Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
