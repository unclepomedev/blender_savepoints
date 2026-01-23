# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Menu import Menu
from .UILayout import UILayout
class UI_MT_button_context_menu(Menu):
    """
    UI button context menu definition. Scripts can append/prepend this to
    add own operators to the context menu. They must check context though, so
    their items only draw in a valid context and for the correct buttons.
    """
    layout: 'UILayout'
    bl_idname: str
    bl_label: str
    bl_translation_context: str
    bl_description: str
    bl_owner_id: str
    bl_options: str
    def poll(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...