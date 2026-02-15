# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.VIEW3D_MT_edit_mesh_clean.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Menu import Menu
from .UILayout import UILayout

class VIEW3D_MT_edit_mesh_clean(Menu):

    @property
    def layout(self) -> Annotated[Optional['UILayout'], "is_animatable=False"]:
        """Defines the structure of the menu in the UI"""
        ...
    bl_idname: Annotated[str, "is_animatable=False"]
    """If this is set, the menu gets a custom ID, otherwise it takes the name of the class used to define the menu (for example, if the class name is "OBJECT_MT_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_MT_hello")"""
    bl_label: Annotated[str, "is_animatable=False"]
    """The menu label"""
    bl_translation_context: Annotated[str, "is_animatable=False"]

    bl_description: Annotated[str, "is_animatable=False"]

    bl_owner_id: Annotated[str, "is_animatable=False"]

    bl_options: set[str]
    """Options for this menu type"""
    def poll(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...