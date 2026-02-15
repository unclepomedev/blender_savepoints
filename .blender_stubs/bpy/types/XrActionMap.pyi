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
from .XrActionMapItem import XrActionMapItem
from .XrActionMapItems import XrActionMapItems
class XrActionMap(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    """Name of the action map"""
    @property
    def actionmap_items(self) -> Annotated['XrActionMapItems', "is_animatable=False"]:
        """Items in the action map, mapping an XR event to an operator, pose, or haptic output"""
        ...
    selected_item: Annotated[int, "step=1", "is_animatable=False"]