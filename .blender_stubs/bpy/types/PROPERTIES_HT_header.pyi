# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Header import Header
from .UILayout import UILayout
class PROPERTIES_HT_header(Header):
    layout: 'UILayout'
    bl_idname: str
    bl_space_type: str
    bl_region_type: str
    def draw(self, *args, **kwargs) -> Any: ...