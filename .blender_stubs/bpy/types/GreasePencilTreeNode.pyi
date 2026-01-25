# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .GreasePencilLayerGroup import GreasePencilLayerGroup
class GreasePencilTreeNode(bpy_struct):
    name: str
    hide: bool
    lock: bool
    select: bool
    use_onion_skinning: bool
    use_masks: bool
    channel_color: float
    next_node: 'GreasePencilTreeNode'
    prev_node: 'GreasePencilTreeNode'
    parent_group: 'GreasePencilLayerGroup'