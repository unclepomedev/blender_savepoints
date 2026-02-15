# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SelectedUvElement.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .PropertyGroup import PropertyGroup

class SelectedUvElement(PropertyGroup):

    name: Annotated[str, "is_animatable=False"]
    """Unique name used in the code and scripting"""
    element_index: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]

    face_index: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]

    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...