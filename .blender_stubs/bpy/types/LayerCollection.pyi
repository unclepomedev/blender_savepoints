# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Collection import Collection
class LayerCollection(bpy_struct):
    collection: 'Collection'
    name: str
    children: bpy_prop_collection['LayerCollection']
    exclude: bool
    holdout: bool
    indirect_only: bool
    hide_viewport: bool
    is_visible: bool
    def visible_get(self, *args, **kwargs) -> Any: ...
    def has_objects(self, *args, **kwargs) -> Any: ...
    def has_selected_objects(self, *args, **kwargs) -> Any: ...