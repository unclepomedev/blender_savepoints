# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ActionStrip import ActionStrip
from .ActionStrips import ActionStrips
class ActionLayer(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    @property
    def strips(self) -> Annotated['ActionStrips', "is_animatable=False"]:
        """The list of strips that are on this animation layer"""
        ...