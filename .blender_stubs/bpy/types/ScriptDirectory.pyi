# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ScriptDirectory.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ScriptDirectory(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Identifier for the Python scripts directory"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """Alternate script path, matching the default layout with sub-directories: startup, add-ons, modules, and presets (requires restart)"""
        ...
    @directory.setter
    def directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]) -> None:
        ...