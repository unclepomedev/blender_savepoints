# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .ShowHideMenu import ShowHideMenu
from .Menu import Menu
from .UILayout import UILayout
class VIEW3D_MT_pose_showhide(ShowHideMenu, Menu):
    layout: 'UILayout'
    bl_idname: str
    bl_label: str
    bl_translation_context: str
    bl_description: str
    bl_owner_id: str
    bl_options: set[str]
    def poll(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...