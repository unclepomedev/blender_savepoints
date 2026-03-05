# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PreferencesKeymap.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class PreferencesKeymap(bpy_struct):

    @property
    def show_ui_keyconfig(self) -> bool:

        ...
    @show_ui_keyconfig.setter
    def show_ui_keyconfig(self, value: bool) -> None:
        ...
    @property
    def active_keyconfig(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """The name of the active key configuration"""
        ...
    @active_keyconfig.setter
    def active_keyconfig(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]) -> None:
        ...