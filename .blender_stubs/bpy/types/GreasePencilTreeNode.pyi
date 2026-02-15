# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GreasePencilTreeNode.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .GreasePencilLayerGroup import GreasePencilLayerGroup

class GreasePencilTreeNode(bpy_struct):

    name: Annotated[str, "is_animatable=False"]
    """The name of the tree node"""
    hide: bool
    """Set tree node visibility"""
    lock: bool
    """Protect tree node from editing"""
    select: bool
    """Tree node is selected"""
    use_onion_skinning: bool
    """Display onion skins before and after the current frame"""
    use_masks: bool
    """The visibility of drawings in this tree node is affected by the layers in the masks list"""
    channel_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color of the channel in the dope sheet"""
    @property
    def next_node(self) -> Annotated[Optional['GreasePencilTreeNode'], "is_animatable=False"]:
        """The layer tree node after (i.e. above) this one"""
        ...
    @property
    def prev_node(self) -> Annotated[Optional['GreasePencilTreeNode'], "is_animatable=False"]:
        """The layer tree node before (i.e. below) this one"""
        ...
    @property
    def parent_group(self) -> Annotated[Optional['GreasePencilLayerGroup'], "is_animatable=False"]:
        """The parent group of this layer tree node"""
        ...