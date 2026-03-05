# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.UserAssetLibrary.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class UserAssetLibrary(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Identifier (not necessarily unique) for the asset library"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def path(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """Path to a directory with .blend files to use as an asset library"""
        ...
    @path.setter
    def path(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]):
        ...
    @property
    def import_method(self) -> Literal['LINK', 'APPEND', 'APPEND_REUSE', 'PACK']:
        """Determine how the asset will be imported, unless overridden by the Asset Browser"""
        ...
    @import_method.setter
    def import_method(self, value: Literal['LINK', 'APPEND', 'APPEND_REUSE', 'PACK']):
        ...
    @property
    def use_relative_path(self) -> bool:
        """Use relative path when linking assets from this asset library"""
        ...
    @use_relative_path.setter
    def use_relative_path(self, value: bool):
        ...