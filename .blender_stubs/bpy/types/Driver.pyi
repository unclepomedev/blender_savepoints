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
from .ChannelDriverVariables import ChannelDriverVariables
from .DriverVariable import DriverVariable
class Driver(bpy_struct):
    type: str
    expression: str
    variables: 'ChannelDriverVariables'
    use_self: bool
    is_valid: bool
    is_simple_expression: bool