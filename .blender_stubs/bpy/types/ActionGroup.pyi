# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ActionGroup.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .FCurve import FCurve
from .ThemeBoneColorSet import ThemeBoneColorSet
from .bpy_prop_collection import bpy_prop_collection

class ActionGroup(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def channels(self) -> Annotated[bpy_prop_collection['FCurve'], "is_animatable=False"]:
        """F-Curves in this group"""
        ...
    @property
    def select(self) -> bool:
        """Action group is selected"""
        ...
    @select.setter
    def select(self, value: bool):
        ...
    @property
    def lock(self) -> bool:
        """Action group is locked"""
        ...
    @lock.setter
    def lock(self, value: bool):
        ...
    @property
    def mute(self) -> bool:
        """Action group is muted"""
        ...
    @mute.setter
    def mute(self, value: bool):
        ...
    @property
    def show_expanded(self) -> bool:
        """Action group is expanded except in graph editor"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool):
        ...
    @property
    def show_expanded_graph(self) -> bool:
        """Action group is expanded in graph editor"""
        ...
    @show_expanded_graph.setter
    def show_expanded_graph(self, value: bool):
        ...
    @property
    def use_pin(self) -> bool:

        ...
    @use_pin.setter
    def use_pin(self, value: bool):
        ...
    @property
    def color_set(self) -> Literal['DEFAULT', 'THEME01', 'THEME02', 'THEME03', 'THEME04', 'THEME05', 'THEME06', 'THEME07', 'THEME08', 'THEME09', 'THEME10', 'THEME11', 'THEME12', 'THEME13', 'THEME14', 'THEME15', 'THEME16', 'THEME17', 'THEME18', 'THEME19', 'THEME20', 'CUSTOM']:
        """Custom color set to use"""
        ...
    @color_set.setter
    def color_set(self, value: Literal['DEFAULT', 'THEME01', 'THEME02', 'THEME03', 'THEME04', 'THEME05', 'THEME06', 'THEME07', 'THEME08', 'THEME09', 'THEME10', 'THEME11', 'THEME12', 'THEME13', 'THEME14', 'THEME15', 'THEME16', 'THEME17', 'THEME18', 'THEME19', 'THEME20', 'CUSTOM']):
        ...
    @property
    def is_custom_color_set(self) -> bool:
        """Color set is user-defined instead of a fixed theme color set"""
        ...
    @property
    def colors(self) -> Annotated['ThemeBoneColorSet', "is_animatable=False"]:
        """Copy of the colors associated with the group's color set"""
        ...