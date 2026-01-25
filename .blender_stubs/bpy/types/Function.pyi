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
from .Property import Property
class Function(bpy_struct):
    identifier: str
    description: str
    parameters: bpy_prop_collection['Property']
    is_registered: bool
    is_registered_optional: bool
    use_self: bool
    use_self_type: bool