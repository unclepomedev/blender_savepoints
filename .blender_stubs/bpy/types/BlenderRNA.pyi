# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BlenderRNA.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Struct import Struct
from .bpy_prop_collection import bpy_prop_collection

class BlenderRNA(bpy_struct):

    @property
    def structs(self) -> Annotated[bpy_prop_collection['Struct'], "is_animatable=False"]:

        ...