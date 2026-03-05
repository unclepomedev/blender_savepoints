# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.KeyConfig.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .KeyConfigPreferences import KeyConfigPreferences
from .KeyMap import KeyMap
from .KeyMaps import KeyMaps
from .bpy_prop_collection import bpy_prop_collection

class KeyConfig(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the key configuration"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def keymaps(self) -> Annotated['KeyMaps', "is_animatable=False"]:
        """Key maps configured as part of this configuration"""
        ...
    @property
    def is_user_defined(self) -> bool:
        """Indicates that a keyconfig was defined by the user"""
        ...
    @property
    def preferences(self) -> Annotated[Optional['KeyConfigPreferences'], "is_animatable=False"]:

        ...