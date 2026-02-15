# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.AOV.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class AOV(bpy_struct):

    name: Annotated[str, "is_animatable=False"]
    """Name of the AOV"""
    is_valid: Annotated[bool, "is_animatable=False"]
    """Is the name of the AOV conflicting"""
    type: Annotated[Literal['COLOR', 'VALUE'], "is_animatable=False"]
    """Data type of the AOV"""