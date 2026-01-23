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
from .DriverVariable import DriverVariable
class Driver(bpy_struct):
    type: str
    expression: str
    variables: bpy_prop_collection['DriverVariable']
    use_self: bool
    is_valid: bool
    is_simple_expression: bool