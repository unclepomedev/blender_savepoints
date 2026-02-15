# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.AnimViz.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .AnimVizMotionPaths import AnimVizMotionPaths

class AnimViz(bpy_struct):

    @property
    def motion_path(self) -> Annotated['AnimVizMotionPaths', "is_animatable=False"]:
        """Motion Path settings for visualization"""
        ...