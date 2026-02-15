# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.TextBox.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class TextBox(bpy_struct):

    x: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]

    y: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]

    width: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]

    height: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
