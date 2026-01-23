# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .SwapNodeMenu import SwapNodeMenu
from .NODE_MT_gn_geometry_read_base import NODE_MT_gn_geometry_read_base
from .UILayout import UILayout
class NODE_MT_gn_geometry_read_swap(SwapNodeMenu, NODE_MT_gn_geometry_read_base):
    layout: 'UILayout'
    bl_idname: str
    bl_label: str
    bl_translation_context: str
    bl_description: str
    bl_owner_id: str
    bl_options: str
    def poll(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...