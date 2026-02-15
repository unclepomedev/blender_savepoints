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

    directory: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """Location on disk where the bake data is stored"""
    frame_start: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """Frame where the baking starts"""
    frame_end: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """Frame where the baking ends"""
    use_custom_simulation_frame_range: bool
    """Override the simulation frame range from the scene"""
    use_custom_path: bool
    """Specify a path where the baked data should be stored manually"""
    bake_target: Literal['INHERIT', 'PACKED', 'DISK']
    """Where to store the baked data"""
    bake_mode: Literal['ANIMATION', 'STILL']

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