# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .FileHandler import FileHandler
class NODE_FH_image_node(FileHandler):
    bl_idname: Annotated[str, "is_animatable=False"]
    """If this is set, the file handler gets a custom ID, otherwise it takes the name of the class used to define the file handler (for example, if the class name is "OBJECT_FH_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_FH_hello")"""
    bl_import_operator: Annotated[str, "is_animatable=False"]
    """Operator that can handle import for files with the extensions given in bl_file_extensions"""
    bl_export_operator: Annotated[str, "is_animatable=False"]
    """Operator that can handle export for files with the extensions given in bl_file_extensions"""
    bl_label: Annotated[str, "is_animatable=False"]
    """The file handler label"""
    bl_file_extensions: Annotated[str, "is_animatable=False"]
    """Formatted string of file extensions supported by the file handler, each extension should start with a "." and be separated by ";".
For Example: ``".blend;.ble"``"""
    def poll_drop(self, *args, **kwargs) -> Any: ...