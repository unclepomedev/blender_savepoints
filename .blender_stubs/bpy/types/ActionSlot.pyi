# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ActionSlot.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ActionSlot(bpy_struct):

    @property
    def identifier(self) -> Annotated[str, "is_animatable=False"]:
        """Used when connecting an Action to a data-block, to find the correct slot handle. This is the display name, prefixed by two characters determined by the slot's ID type"""
        ...
    @identifier.setter
    def identifier(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def target_id_type(self) -> Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD', 'UNSPECIFIED']:
        """Type of data-block that this slot is intended to animate; can be set when 'UNSPECIFIED' but is otherwise read-only"""
        ...
    @target_id_type.setter
    def target_id_type(self, value: Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD', 'UNSPECIFIED']):
        ...
    @property
    def target_id_type_icon(self) -> Annotated[int, "step=1"]:

        ...
    @property
    def name_display(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the slot, for display in the user interface. This name combined with the slot's data-block type is unique within its Action"""
        ...
    @name_display.setter
    def name_display(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def handle(self) -> Annotated[int, "step=1"]:
        """Number specific to this Slot, unique within the Action.
This is used, for example, on a ActionKeyframeStrip to look up the ActionChannelbag for this Slot"""
        ...
    @property
    def active(self) -> Annotated[bool, "is_animatable=False"]:
        """Whether this is the active slot, can be set by assigning to action.slots.active"""
        ...
    @property
    def select(self) -> Annotated[bool, "is_animatable=False"]:
        """Selection state of the slot"""
        ...
    @select.setter
    def select(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_expanded(self) -> Annotated[bool, "is_animatable=False"]:
        """Expanded state of the slot"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    def users(self, *args, **kwargs) -> Any: ...
    def duplicate(self, *args, **kwargs) -> Any: ...