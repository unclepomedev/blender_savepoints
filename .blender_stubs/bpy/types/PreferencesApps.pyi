# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PreferencesApps.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class PreferencesApps(bpy_struct):

    @property
    def show_corner_split(self) -> bool:
        """Split and join editors by dragging from corners"""
        ...
    @show_corner_split.setter
    def show_corner_split(self, value: bool) -> None:
        ...
    @property
    def show_edge_resize(self) -> bool:
        """Resize editors by dragging from the edges"""
        ...
    @show_edge_resize.setter
    def show_edge_resize(self, value: bool) -> None:
        ...
    @property
    def show_regions_visibility_toggle(self) -> bool:
        """Header and side bars visibility toggles"""
        ...
    @show_regions_visibility_toggle.setter
    def show_regions_visibility_toggle(self, value: bool) -> None:
        ...