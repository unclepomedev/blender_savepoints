# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CollectionExport.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .PropertyGroup import PropertyGroup

class CollectionExport(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def is_open(self) -> bool:
        """Whether the panel is expanded or closed"""
        ...
    @is_open.setter
    def is_open(self, value: bool):
        ...
    @property
    def export_properties(self) -> Annotated[Optional['PropertyGroup'], "is_animatable=False"]:
        """Properties associated with the configured exporter"""
        ...
    @property
    def filepath(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """The file path used for exporting"""
        ...
    @filepath.setter
    def filepath(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]):
        ...