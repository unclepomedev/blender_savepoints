# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GreasePencilLayerGroup.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .GreasePencilTreeNode import GreasePencilTreeNode

class GreasePencilLayerGroup(GreasePencilTreeNode):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """The name of the tree node"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def hide(self) -> bool:
        """Set tree node visibility"""
        ...
    @hide.setter
    def hide(self, value: bool) -> None:
        ...
    @property
    def lock(self) -> bool:
        """Protect tree node from editing"""
        ...
    @lock.setter
    def lock(self, value: bool) -> None:
        ...
    @property
    def select(self) -> bool:
        """Tree node is selected"""
        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...
    @property
    def use_onion_skinning(self) -> bool:
        """Display onion skins before and after the current frame"""
        ...
    @use_onion_skinning.setter
    def use_onion_skinning(self, value: bool) -> None:
        ...
    @property
    def use_masks(self) -> bool:
        """The visibility of drawings in this tree node is affected by the layers in the masks list"""
        ...
    @use_masks.setter
    def use_masks(self, value: bool) -> None:
        ...
    @property
    def channel_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color of the channel in the dope sheet"""
        ...
    @channel_color.setter
    def channel_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
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
    @property
    def is_expanded(self) -> bool:
        """The layer group is expanded in the UI"""
        ...
    @is_expanded.setter
    def is_expanded(self, value: bool) -> None:
        ...
    @property
    def color_tag(self) -> Literal['NONE', 'COLOR1', 'COLOR2', 'COLOR3', 'COLOR4', 'COLOR5', 'COLOR6', 'COLOR7', 'COLOR8']:

        ...
    @color_tag.setter
    def color_tag(self, value: Literal['NONE', 'COLOR1', 'COLOR2', 'COLOR3', 'COLOR4', 'COLOR5', 'COLOR6', 'COLOR7', 'COLOR8']) -> None:
        ...