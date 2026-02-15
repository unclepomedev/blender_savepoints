# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SceneHydra.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SceneHydra(bpy_struct):

    export_method: Annotated[Literal['HYDRA', 'USD'], "is_animatable=False"]
    """How to export the Blender scene to the Hydra render engine"""