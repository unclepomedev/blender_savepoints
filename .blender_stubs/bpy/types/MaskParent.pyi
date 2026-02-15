# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MaskParent.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ID import ID

class MaskParent(bpy_struct):

    id: Annotated[Optional['ID'], "is_animatable=False"]
    """ID-block to which masking element would be parented to or to its property"""
    id_type: Literal['MOVIECLIP']
    """Type of ID-block that can be used"""
    type: Literal['POINT_TRACK', 'PLANE_TRACK']
    """Parent Type"""
    parent: Annotated[str, "is_animatable=False"]
    """Name of parent object in specified data-block to which parenting happens"""
    sub_parent: Annotated[str, "is_animatable=False"]
    """Name of parent sub-object in specified data-block to which parenting happens"""