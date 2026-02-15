# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CollectionObject.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .CollectionLightLinking import CollectionLightLinking

class CollectionObject(bpy_struct):

    @property
    def light_linking(self) -> Annotated['CollectionLightLinking', "is_animatable=False"]:
        """Light linking settings of the collection"""
        ...