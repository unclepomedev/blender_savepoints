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
from .KeyingSetInfo import KeyingSetInfo
from .KeyingSetPath import KeyingSetPath
class KeyingSet(bpy_struct):
    bl_idname: str
    bl_label: str
    bl_description: str
    type_info: 'KeyingSetInfo'
    paths: bpy_prop_collection['KeyingSetPath']
    is_path_absolute: bool
    use_insertkey_override_needed: bool
    use_insertkey_override_visual: bool
    use_insertkey_needed: bool
    use_insertkey_visual: bool
    def refresh(self, *args, **kwargs) -> Any: ...