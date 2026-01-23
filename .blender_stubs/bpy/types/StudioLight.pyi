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
from .UserSolidLight import UserSolidLight
class StudioLight(bpy_struct):
    index: int
    is_user_defined: bool
    has_specular_highlight_pass: bool
    type: str
    name: str
    path: str
    solid_lights: bpy_prop_collection['UserSolidLight']
    light_ambient: float