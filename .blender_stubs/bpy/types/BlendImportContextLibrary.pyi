# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BlendImportContextLibrary.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class BlendImportContextLibrary(bpy_struct):

    @property
    def filepath(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:

        ...