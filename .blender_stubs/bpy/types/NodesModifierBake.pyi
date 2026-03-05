# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.NodesModifierBake.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Node import Node
from .NodesModifierBakeDataBlocks import NodesModifierBakeDataBlocks
from .NodesModifierDataBlock import NodesModifierDataBlock
from .bpy_prop_collection import bpy_prop_collection

class NodesModifierBake(bpy_struct):

    @property
    def directory(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """Location on disk where the bake data is stored"""
        ...
    @directory.setter
    def directory(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]):
        ...
    @property
    def frame_start(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """Frame where the baking starts"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]):
        ...
    @property
    def frame_end(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """Frame where the baking ends"""
        ...
    @frame_end.setter
    def frame_end(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]):
        ...
    @property
    def use_custom_simulation_frame_range(self) -> bool:
        """Override the simulation frame range from the scene"""
        ...
    @use_custom_simulation_frame_range.setter
    def use_custom_simulation_frame_range(self, value: bool):
        ...
    @property
    def use_custom_path(self) -> bool:
        """Specify a path where the baked data should be stored manually"""
        ...
    @use_custom_path.setter
    def use_custom_path(self, value: bool):
        ...
    @property
    def bake_target(self) -> Literal['INHERIT', 'PACKED', 'DISK']:
        """Where to store the baked data"""
        ...
    @bake_target.setter
    def bake_target(self, value: Literal['INHERIT', 'PACKED', 'DISK']):
        ...
    @property
    def bake_mode(self) -> Literal['ANIMATION', 'STILL']:

        ...
    @bake_mode.setter
    def bake_mode(self, value: Literal['ANIMATION', 'STILL']):
        ...
    @property
    def bake_id(self) -> Annotated[int, "step=1"]:
        """Identifier for this bake which remains unchanged even when the bake node is renamed, grouped or ungrouped"""
        ...
    @property
    def node(self) -> Annotated[Optional['Node'], "is_animatable=False"]:
        """Bake node or simulation output node that corresponds to this bake. This node may be deeply nested in the modifier node group. It can be none in some cases like missing linked data blocks."""
        ...
    @property
    def data_blocks(self) -> Annotated['NodesModifierBakeDataBlocks', "is_animatable=False"]:

        ...