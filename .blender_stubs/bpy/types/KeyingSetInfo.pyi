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
class KeyingSetInfo(bpy_struct):
    bl_idname: str
    bl_label: str
    bl_description: str
    bl_options: str
    def poll(self, *args, **kwargs) -> Any: ...
    def iterator(self, *args, **kwargs) -> Any: ...
    def generate(self, *args, **kwargs) -> Any: ...