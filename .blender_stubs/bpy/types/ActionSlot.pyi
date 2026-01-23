# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class ActionSlot(bpy_struct):
    identifier: str
    target_id_type: str
    target_id_type_icon: int
    name_display: str
    handle: int
    active: bool
    select: bool
    show_expanded: bool
    def users(self, *args, **kwargs) -> Any: ...
    def duplicate(self, *args, **kwargs) -> Any: ...