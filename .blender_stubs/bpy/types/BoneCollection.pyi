# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BoneCollection.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Bone import Bone
from .bpy_prop_collection import bpy_prop_collection

class BoneCollection(bpy_struct):

    name: Annotated[str, "is_animatable=False"]
    """Unique within the Armature"""
    is_expanded: bool
    """This bone collection is expanded in the bone collections tree view"""
    is_visible: bool
    """Bones in this collection will be visible in pose/object mode"""
    @property
    def is_visible_ancestors(self) -> bool:
        """True when all of the ancestors of this bone collection are marked as visible; always True for root bone collections"""
        ...
    @property
    def is_visible_effectively(self) -> bool:
        """Whether this bone collection is effectively visible in the viewport. This is True when this bone collection and all of its ancestors are visible, or when it is marked as 'solo'."""
        ...
    is_solo: bool
    """Show only this bone collection, and others also marked as 'solo'"""
    @property
    def is_local_override(self) -> bool:
        """This collection was added via a library override in the current blend file"""
        ...
    @property
    def is_editable(self) -> bool:
        """This collection is owned by a local Armature, or was added via a library override in the current blend file"""
        ...
    @property
    def bones(self) -> Annotated[bpy_prop_collection['Bone'], "is_animatable=False"]:
        """Bones assigned to this bone collection. In armature edit mode this will always return an empty list of bones, as the bone collection memberships are only synchronized when exiting edit mode."""
        ...
    @property
    def children(self) -> Annotated[bpy_prop_collection['BoneCollection'], "is_animatable=False"]:

        ...
    parent: Annotated[Optional['BoneCollection'], "is_animatable=False"]
    """Parent bone collection. Note that accessing this requires a scan of all the bone collections to find the parent."""
    @property
    def index(self) -> Annotated[int, "step=1"]:
        """Index of this bone collection in the armature.collections_all array. Note that finding this index requires a scan of all the bone collections, so do access this with care."""
        ...
    child_number: Annotated[int, "step=1"]
    """Index of this collection into its parent's list of children. Note that finding this index requires a scan of all the bone collections, so do access this with care."""
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def assign(self, *args, **kwargs) -> Any: ...
    def unassign(self, *args, **kwargs) -> Any: ...