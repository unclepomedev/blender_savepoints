# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieTrackingDopesheet.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MovieTrackingDopesheet(bpy_struct):

    @property
    def sort_method(self) -> Literal['NAME', 'LONGEST', 'TOTAL', 'AVERAGE_ERROR', 'START', 'END']:
        """Method to be used to sort channels in dopesheet view"""
        ...
    @sort_method.setter
    def sort_method(self, value: Literal['NAME', 'LONGEST', 'TOTAL', 'AVERAGE_ERROR', 'START', 'END']):
        ...
    @property
    def use_invert_sort(self) -> bool:
        """Invert sort order of dopesheet channels"""
        ...
    @use_invert_sort.setter
    def use_invert_sort(self, value: bool):
        ...
    @property
    def show_only_selected(self) -> bool:
        """Only include channels relating to selected objects and data"""
        ...
    @show_only_selected.setter
    def show_only_selected(self, value: bool):
        ...
    @property
    def show_hidden(self) -> bool:
        """Include channels from objects/bone that are not visible"""
        ...
    @show_hidden.setter
    def show_hidden(self, value: bool):
        ...