# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.XrActionMap.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .XrActionMapItem import XrActionMapItem
from .XrActionMapItems import XrActionMapItems
from .bpy_prop_collection import bpy_prop_collection

class XrActionMap(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the action map"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def actionmap_items(self) -> Annotated['XrActionMapItems', "is_animatable=False"]:
        """Items in the action map, mapping an XR event to an operator, pose, or haptic output"""
        ...
    @property
    def selected_item(self) -> Annotated[int, "step=1", "is_animatable=False"]:

        ...
    @selected_item.setter
    def selected_item(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...