# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.KeyingSet.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .KeyingSetInfo import KeyingSetInfo
from .KeyingSetPath import KeyingSetPath
from .KeyingSetPaths import KeyingSetPaths
from .bpy_prop_collection import bpy_prop_collection

class KeyingSet(bpy_struct):

    @property
    def bl_idname(self) -> Annotated[str, "is_animatable=False"]:
        """If this is set, the Keying Set gets a custom ID, otherwise it takes the name of the class used to define the Keying Set (for example, if the class name is "BUILTIN_KSI_location", and bl_idname is not set by the script, then bl_idname = "BUILTIN_KSI_location")"""
        ...
    @bl_idname.setter
    def bl_idname(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_label(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_label.setter
    def bl_label(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_description(self) -> Annotated[str, "is_animatable=False"]:
        """A short description of the keying set"""
        ...
    @bl_description.setter
    def bl_description(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type_info(self) -> Annotated[Optional['KeyingSetInfo'], "is_animatable=False"]:
        """Callback function defines for built-in Keying Sets"""
        ...
    @property
    def paths(self) -> Annotated['KeyingSetPaths', "is_animatable=False"]:
        """Keying Set Paths to define settings that get keyframed together"""
        ...
    @property
    def is_path_absolute(self) -> bool:
        """Keying Set defines specific paths/settings to be keyframed (i.e. is not reliant on context info)"""
        ...
    @property
    def use_insertkey_override_needed(self) -> bool:
        """Override default setting to only insert keyframes where they're needed in the relevant F-Curves"""
        ...
    @use_insertkey_override_needed.setter
    def use_insertkey_override_needed(self, value: bool):
        ...
    @property
    def use_insertkey_override_visual(self) -> bool:
        """Override default setting to insert keyframes based on 'visual transforms'"""
        ...
    @use_insertkey_override_visual.setter
    def use_insertkey_override_visual(self, value: bool):
        ...
    @property
    def use_insertkey_needed(self) -> bool:
        """Only insert keyframes where they're needed in the relevant F-Curves"""
        ...
    @use_insertkey_needed.setter
    def use_insertkey_needed(self, value: bool):
        ...
    @property
    def use_insertkey_visual(self) -> bool:
        """Insert keyframes based on 'visual transforms'"""
        ...
    @use_insertkey_visual.setter
    def use_insertkey_visual(self, value: bool):
        ...
    def refresh(self, *args, **kwargs) -> Any: ...