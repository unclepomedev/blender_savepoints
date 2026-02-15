# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CollectionLightLinking.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class CollectionLightLinking(bpy_struct):

    link_state: Annotated[Literal['INCLUDE', 'EXCLUDE'], "is_animatable=False"]
    """Light or shadow receiving state of the object or collection"""