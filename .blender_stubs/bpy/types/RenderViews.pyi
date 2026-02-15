# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.RenderViews.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .SceneRenderView import SceneRenderView

class RenderViews(bpy_struct):

    active_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Active index in render view array"""
    active: Annotated['SceneRenderView', "is_animatable=False"]
    """Active Render View"""
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['SceneRenderView']: ...
    def __getitem__(self, key: Union[str, int]) -> 'SceneRenderView': ...
    def __len__(self) -> int: ...