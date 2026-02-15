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
from .FCurve import FCurve
from .ThemeBoneColorSet import ThemeBoneColorSet
class ActionGroup(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    @property
    def channels(self) -> Annotated[bpy_prop_collection['FCurve'], "is_animatable=False"]:
        """F-Curves in this group"""
        ...
    select: bool
    """Action group is selected"""
    lock: bool
    """Action group is locked"""
    mute: bool
    """Action group is muted"""
    show_expanded: bool
    """Action group is expanded except in graph editor"""
    show_expanded_graph: bool
    """Action group is expanded in graph editor"""
    use_pin: bool
    color_set: Literal['DEFAULT', 'THEME01', 'THEME02', 'THEME03', 'THEME04', 'THEME05', 'THEME06', 'THEME07', 'THEME08', 'THEME09', 'THEME10', 'THEME11', 'THEME12', 'THEME13', 'THEME14', 'THEME15', 'THEME16', 'THEME17', 'THEME18', 'THEME19', 'THEME20', 'CUSTOM']
    """Custom color set to use"""
    @property
    def is_custom_color_set(self) -> bool:
        """Color set is user-defined instead of a fixed theme color set"""
        ...
    @property
    def colors(self) -> Annotated['ThemeBoneColorSet', "is_animatable=False"]:
        """Copy of the colors associated with the group's color set"""
        ...