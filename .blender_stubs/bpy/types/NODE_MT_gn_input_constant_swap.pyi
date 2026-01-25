# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .SwapNodeMenu import SwapNodeMenu
from .NODE_MT_gn_input_constant_base import NODE_MT_gn_input_constant_base
from .UILayout import UILayout
class NODE_MT_gn_input_constant_swap(SwapNodeMenu, NODE_MT_gn_input_constant_base):
    layout: 'UILayout'
    bl_idname: str
    bl_label: str
    bl_translation_context: str
    bl_description: str
    bl_owner_id: str
    bl_options: str
    def poll(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...