# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.VIEW3D_FH_camera_background_image.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .FileHandler import FileHandler

class VIEW3D_FH_camera_background_image(FileHandler):

    @property
    def bl_idname(self) -> Annotated[str, "is_animatable=False"]:
        """If this is set, the file handler gets a custom ID, otherwise it takes the name of the class used to define the file handler (for example, if the class name is "OBJECT_FH_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_FH_hello")"""
        ...
    @bl_idname.setter
    def bl_idname(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_import_operator(self) -> Annotated[str, "is_animatable=False"]:
        """Operator that can handle import for files with the extensions given in bl_file_extensions"""
        ...
    @bl_import_operator.setter
    def bl_import_operator(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_export_operator(self) -> Annotated[str, "is_animatable=False"]:
        """Operator that can handle export for files with the extensions given in bl_file_extensions"""
        ...
    @bl_export_operator.setter
    def bl_export_operator(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_label(self) -> Annotated[str, "is_animatable=False"]:
        """The file handler label"""
        ...
    @bl_label.setter
    def bl_label(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_file_extensions(self) -> Annotated[str, "is_animatable=False"]:
        """Formatted string of file extensions supported by the file handler, each extension should start with a "." and be separated by ";".
For Example: ``".blend;.ble"``"""
        ...
    @bl_file_extensions.setter
    def bl_file_extensions(self, value: Annotated[str, "is_animatable=False"]):
        ...
    def poll_drop(self, *args, **kwargs) -> Any: ...