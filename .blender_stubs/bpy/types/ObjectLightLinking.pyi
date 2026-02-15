# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ObjectLightLinking.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Collection import Collection

class ObjectLightLinking(bpy_struct):

    receiver_collection: Annotated[Optional['Collection'], "is_animatable=False"]
    """Collection which defines light linking relation of this emitter"""
    blocker_collection: Annotated[Optional['Collection'], "is_animatable=False"]
    """Collection which defines objects which block light from this emitter"""