# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ViewerPath.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ViewerPathElem import ViewerPathElem
from .bpy_prop_collection import bpy_prop_collection

class ViewerPath(bpy_struct):

    @property
    def path(self) -> Annotated[bpy_prop_collection['ViewerPathElem'], "is_animatable=False"]:

        ...