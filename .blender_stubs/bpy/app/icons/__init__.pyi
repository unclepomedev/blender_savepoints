# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.app.icons.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


def new_triangles(*args, **kwargs) -> Any:
    """.. function:: new_triangles(range, coords, colors)

   Create a new icon from triangle geometry.

   :arg range: Pair of ints.
   :type range: tuple[int, int]
   :arg coords: Sequence of bytes (6 floats for one triangle) for (X, Y) coordinates.
   :type coords: bytes
   :arg colors: Sequence of bytes (12 for one triangles) for RGBA.
   :type colors: bytes
   :return: Unique icon value (pass to interface ``icon_value`` argument).
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.icons.html"""
    ...

def new_triangles_from_file(*args, **kwargs) -> Any:
    """.. function:: new_triangles_from_file(filepath)

   Create a new icon from triangle geometry.

   :arg filepath: File path.
   :type filepath: str | bytes.
   :return: Unique icon value (pass to interface ``icon_value`` argument).
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.icons.html"""
    ...

def release(*args, **kwargs) -> Any:
    """.. function:: release(icon_id)

   Release the icon.


    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.icons.html"""
    ...
