# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.VIEW3D_MT_edit_mesh_edges.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Menu import Menu
from .UILayout import UILayout

class VIEW3D_MT_edit_mesh_edges(Menu):

    @property
    def layout(self) -> Annotated[Optional['UILayout'], "is_animatable=False"]:
        """Defines the structure of the menu in the UI"""
        ...
    @property
    def bl_idname(self) -> Annotated[str, "is_animatable=False"]:
        """If this is set, the menu gets a custom ID, otherwise it takes the name of the class used to define the menu (for example, if the class name is "OBJECT_MT_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_MT_hello")"""
        ...
    @bl_idname.setter
    def bl_idname(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_label(self) -> Annotated[str, "is_animatable=False"]:
        """The menu label"""
        ...
    @bl_label.setter
    def bl_label(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_translation_context(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_translation_context.setter
    def bl_translation_context(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_description(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_description.setter
    def bl_description(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_owner_id(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @bl_owner_id.setter
    def bl_owner_id(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_options(self) -> set[str]:
        """Options for this menu type"""
        ...
    @bl_options.setter
    def bl_options(self, value: set[str]):
        ...
    def poll(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...