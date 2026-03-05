# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MaskLayer.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .MaskSpline import MaskSpline
from .MaskSplines import MaskSplines
from .bpy_prop_collection import bpy_prop_collection

class MaskLayer(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique name of layer"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def splines(self) -> Annotated['MaskSplines', "is_animatable=False"]:
        """Collection of splines which defines this layer"""
        ...
    @property
    def hide(self) -> bool:
        """Restrict visibility in the viewport"""
        ...
    @hide.setter
    def hide(self, value: bool) -> None:
        ...
    @property
    def hide_select(self) -> bool:
        """Restrict selection in the viewport"""
        ...
    @hide_select.setter
    def hide_select(self, value: bool) -> None:
        ...
    @property
    def hide_render(self) -> bool:
        """Restrict renderability"""
        ...
    @hide_render.setter
    def hide_render(self, value: bool) -> None:
        ...
    @property
    def select(self) -> bool:
        """Layer is selected for editing in the Dope Sheet"""
        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...
    @property
    def alpha(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Render Opacity"""
        ...
    @alpha.setter
    def alpha(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def blend(self) -> Literal['MERGE_ADD', 'MERGE_SUBTRACT', 'ADD', 'SUBTRACT', 'LIGHTEN', 'DARKEN', 'MUL', 'REPLACE', 'DIFFERENCE']:
        """Method of blending mask layers"""
        ...
    @blend.setter
    def blend(self, value: Literal['MERGE_ADD', 'MERGE_SUBTRACT', 'ADD', 'SUBTRACT', 'LIGHTEN', 'DARKEN', 'MUL', 'REPLACE', 'DIFFERENCE']) -> None:
        ...
    @property
    def invert(self) -> bool:
        """Invert the mask black/white"""
        ...
    @invert.setter
    def invert(self, value: bool) -> None:
        ...
    @property
    def falloff(self) -> Literal['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR']:
        """Falloff type of the feather"""
        ...
    @falloff.setter
    def falloff(self, value: Literal['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR']) -> None:
        ...
    @property
    def use_fill_holes(self) -> bool:
        """Calculate holes when filling overlapping curves"""
        ...
    @use_fill_holes.setter
    def use_fill_holes(self, value: bool) -> None:
        ...
    @property
    def use_fill_overlap(self) -> bool:
        """Calculate self intersections and overlap before filling"""
        ...
    @use_fill_overlap.setter
    def use_fill_overlap(self, value: bool) -> None:
        ...