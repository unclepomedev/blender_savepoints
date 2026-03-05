# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MaterialLineArt.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MaterialLineArt(bpy_struct):

    @property
    def use_material_mask(self) -> bool:
        """Use material masks to filter out occluded strokes"""
        ...
    @use_material_mask.setter
    def use_material_mask(self, value: bool) -> None:
        ...
    @property
    def use_material_mask_bits(self) -> list[bool]:

        ...
    @use_material_mask_bits.setter
    def use_material_mask_bits(self, value: list[bool]) -> None:
        ...
    @property
    def mat_occlusion(self) -> Annotated[int, "step=1"]:
        """Faces with this material will behave as if it has set number of layers in occlusion"""
        ...
    @mat_occlusion.setter
    def mat_occlusion(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def intersection_priority(self) -> Annotated[int, "step=1"]:
        """The intersection line will be included into the object with the higher intersection priority value"""
        ...
    @intersection_priority.setter
    def intersection_priority(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_intersection_priority_override(self) -> bool:
        """Override object and collection intersection priority value"""
        ...
    @use_intersection_priority_override.setter
    def use_intersection_priority_override(self, value: bool) -> None:
        ...