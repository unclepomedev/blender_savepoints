# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.OperatorFileListElement.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .PropertyGroup import PropertyGroup

class OperatorFileListElement(PropertyGroup):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique name used in the code and scripting"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def name(self) -> Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]:
        """Name of a file or directory within a file list"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "subtype='FILE_NAME'", "is_animatable=False"]) -> None:
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...