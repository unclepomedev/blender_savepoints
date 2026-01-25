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
from ._GenericUI import _GenericUI
from .UILayout import UILayout
class Header(bpy_struct, _GenericUI):
    layout: 'UILayout'
    bl_idname: str
    bl_space_type: str
    bl_region_type: str
    def draw(self, *args, **kwargs) -> Any: ...