# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ObjectLineArt.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ObjectLineArt(bpy_struct):

    usage: Annotated[Literal['INHERIT', 'INCLUDE', 'OCCLUSION_ONLY', 'EXCLUDE', 'INTERSECTION_ONLY', 'NO_INTERSECTION', 'FORCE_INTERSECTION'], "is_animatable=False"]
    """How to use this object in Line Art calculation"""
    use_crease_override: Annotated[bool, "is_animatable=False"]
    """Use this object's crease setting to overwrite scene global"""
    crease_threshold: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.009999999776482582", "precision=1", "is_animatable=False"]
    """Angles smaller than this will be treated as creases"""
    use_intersection_priority_override: Annotated[bool, "is_animatable=False"]
    """Use this object's intersection priority to override collection setting"""
    intersection_priority: Annotated[int, "step=1", "is_animatable=False"]
    """The intersection line will be included into the object with the higher intersection priority value"""