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
class SceneRenderView(bpy_struct):
    name: Annotated[str, "is_animatable=False"]
    """Render view name"""
    file_suffix: Annotated[str, "is_animatable=False"]
    """Suffix added to the render images for this view"""
    camera_suffix: Annotated[str, "is_animatable=False"]
    """Suffix to identify the cameras to use, and added to the render images for this view"""
    use: Annotated[bool, "is_animatable=False"]
    """Disable or enable the render view"""