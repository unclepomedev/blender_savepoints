# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ActionChannelbag.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ActionChannelbagFCurves import ActionChannelbagFCurves
from .ActionChannelbagGroups import ActionChannelbagGroups
from .ActionGroup import ActionGroup
from .ActionSlot import ActionSlot
from .FCurve import FCurve
from .bpy_prop_collection import bpy_prop_collection

class ActionChannelbag(bpy_struct):

    @property
    def slot_handle(self) -> Annotated[int, "step=1"]:

        ...
    @property
    def slot(self) -> Annotated[Optional['ActionSlot'], "is_animatable=False"]:
        """The Slot that the Channelbag's animation data is for"""
        ...
    @property
    def fcurves(self) -> Annotated['ActionChannelbagFCurves', "is_animatable=False"]:
        """The individual F-Curves that animate the slot"""
        ...
    @property
    def groups(self) -> Annotated['ActionChannelbagGroups', "is_animatable=False"]:
        """Groupings of F-Curves for display purposes, in e.g. the dopesheet and graph editor"""
        ...