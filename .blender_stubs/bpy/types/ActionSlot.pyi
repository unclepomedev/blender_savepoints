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
class ActionSlot(bpy_struct):
    identifier: Annotated[str, "is_animatable=False"]
    """Used when connecting an Action to a data-block, to find the correct slot handle. This is the display name, prefixed by two characters determined by the slot's ID type"""
    target_id_type: Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD', 'UNSPECIFIED']
    """Type of data-block that this slot is intended to animate; can be set when 'UNSPECIFIED' but is otherwise read-only"""
    @property
    def target_id_type_icon(self) -> Annotated[int, "step=1"]:
        ...
    name_display: Annotated[str, "is_animatable=False"]
    """Name of the slot, for display in the user interface. This name combined with the slot's data-block type is unique within its Action"""
    @property
    def handle(self) -> Annotated[int, "step=1"]:
        """Number specific to this Slot, unique within the Action.
This is used, for example, on a ActionKeyframeStrip to look up the ActionChannelbag for this Slot"""
        ...
    @property
    def active(self) -> Annotated[bool, "is_animatable=False"]:
        """Whether this is the active slot, can be set by assigning to action.slots.active"""
        ...
    select: Annotated[bool, "is_animatable=False"]
    """Selection state of the slot"""
    show_expanded: Annotated[bool, "is_animatable=False"]
    """Expanded state of the slot"""
    def users(self, *args, **kwargs) -> Any: ...
    def duplicate(self, *args, **kwargs) -> Any: ...