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
class TimelineMarker(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    frame: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """The frame on which the timeline marker appears"""
    select: bool
    """Marker selection state"""
    camera: Annotated[Optional['Object'], "is_animatable=False"]
    """Camera that becomes active on this frame"""
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...