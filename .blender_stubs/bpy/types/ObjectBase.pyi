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
from .Object import Object
class ObjectBase(bpy_struct):
    @property
    def object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object this base links to"""
        ...
    select: Annotated[bool, "is_animatable=False"]
    """Object base selection state"""
    hide_viewport: Annotated[bool, "is_animatable=False"]
    """Temporarily hide in viewport"""