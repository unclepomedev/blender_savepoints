# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .KeyConfigPreferences import KeyConfigPreferences
from .KeyMap import KeyMap
from .KeyMaps import KeyMaps
class KeyConfig(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    """Name of the key configuration"""
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