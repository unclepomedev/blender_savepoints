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
from .KeyConfig import KeyConfig
class KeyConfigurations(bpy_struct):
    active: 'KeyConfig'
    default: 'KeyConfig'
    addon: 'KeyConfig'
    user: 'KeyConfig'
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def find_item_from_operator(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    # --- Injected Methods ---
    addon: Any
    user: Any
    active: Any