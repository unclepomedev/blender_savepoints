# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Text import Text
class FreestyleModuleSettings(bpy_struct):
    script: Annotated[Optional['Text'], "is_animatable=False"]
    """Python script to define a style module"""
    use: bool
    """Enable or disable this style module during stroke rendering"""