# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LayerCollection.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Collection import Collection
from .bpy_prop_collection import bpy_prop_collection

class LayerCollection(bpy_struct):

    @property
    def collection(self) -> Annotated['Collection', "is_animatable=False"]:
        """Collection this layer collection is wrapping"""
        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of this layer collection (same as its collection one)"""
        ...
    @property
    def children(self) -> Annotated[bpy_prop_collection['LayerCollection'], "is_animatable=False"]:
        """Layer collection children"""
        ...
    exclude: Annotated[bool, "is_animatable=False"]
    """Exclude from view layer"""
    holdout: Annotated[bool, "is_animatable=False"]
    """Mask out objects in collection from view layer"""
    indirect_only: Annotated[bool, "is_animatable=False"]
    """Objects in collection only contribute indirectly (through shadows and reflections) in the view layer"""
    hide_viewport: Annotated[bool, "is_animatable=False"]
    """Temporarily hide in viewport"""
    @property
    def is_visible(self) -> Annotated[bool, "is_animatable=False"]:
        """Whether this collection is visible for the view layer, take into account the collection parent"""
        ...
    def visible_get(self, *args, **kwargs) -> Any: ...
    def has_objects(self, *args, **kwargs) -> Any: ...
    def has_selected_objects(self, *args, **kwargs) -> Any: ...