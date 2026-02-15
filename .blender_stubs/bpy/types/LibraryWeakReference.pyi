# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.LibraryWeakReference.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class LibraryWeakReference(bpy_struct):

    filepath: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """Path to the library .blend file"""
    id_name: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """Full ID name in the library .blend file (including the two leading 'id type' chars)"""