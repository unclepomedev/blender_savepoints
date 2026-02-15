# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.NodeTreePath.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .NodeTree import NodeTree

class NodeTreePath(bpy_struct):

    @property
    def node_tree(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Base node tree from context"""
        ...