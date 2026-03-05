# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.KeyingSetPath.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ID import ID

class KeyingSetPath(bpy_struct):

    @property
    def id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """ID-Block that keyframes for Keying Set should be added to (for Absolute Keying Sets only)"""
        ...
    @id.setter
    def id(self, value: Annotated[Optional['ID'], "is_animatable=False"]) -> None:
        ...
    @property
    def id_type(self) -> Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']:
        """Type of ID-block that can be used"""
        ...
    @id_type.setter
    def id_type(self, value: Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']) -> None:
        ...
    @property
    def group(self) -> Annotated[str, "is_animatable=False"]:
        """Name of Action Group to assign setting(s) for this path to"""
        ...
    @group.setter
    def group(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def group_method(self) -> Literal['NAMED', 'NONE', 'KEYINGSET']:
        """Method used to define which Group-name to use"""
        ...
    @group_method.setter
    def group_method(self, value: Literal['NAMED', 'NONE', 'KEYINGSET']) -> None:
        ...
    @property
    def data_path(self) -> Annotated[str, "is_animatable=False"]:
        """Path to property setting"""
        ...
    @data_path.setter
    def data_path(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def array_index(self) -> Annotated[int, "step=1"]:
        """Index to the specific setting if applicable"""
        ...
    @array_index.setter
    def array_index(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_entire_array(self) -> bool:
        """When an 'array/vector' type is chosen (Location, Rotation, Color, etc.), entire array is to be used"""
        ...
    @use_entire_array.setter
    def use_entire_array(self, value: bool) -> None:
        ...
    @property
    def use_insertkey_override_needed(self) -> bool:
        """Override default setting to only insert keyframes where they're needed in the relevant F-Curves"""
        ...
    @use_insertkey_override_needed.setter
    def use_insertkey_override_needed(self, value: bool) -> None:
        ...
    @property
    def use_insertkey_override_visual(self) -> bool:
        """Override default setting to insert keyframes based on 'visual transforms'"""
        ...
    @use_insertkey_override_visual.setter
    def use_insertkey_override_visual(self, value: bool) -> None:
        ...
    @property
    def use_insertkey_needed(self) -> bool:
        """Only insert keyframes where they're needed in the relevant F-Curves"""
        ...
    @use_insertkey_needed.setter
    def use_insertkey_needed(self, value: bool) -> None:
        ...
    @property
    def use_insertkey_visual(self) -> bool:
        """Insert keyframes based on 'visual transforms'"""
        ...
    @use_insertkey_visual.setter
    def use_insertkey_visual(self, value: bool) -> None:
        ...