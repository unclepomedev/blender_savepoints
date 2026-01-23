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
from .ID import ID
class KeyingSetPath(bpy_struct):
    id: 'ID'
    id_type: str
    group: str
    group_method: str
    data_path: str
    array_index: int
    use_entire_array: bool
    use_insertkey_override_needed: bool
    use_insertkey_override_visual: bool
    use_insertkey_needed: bool
    use_insertkey_visual: bool