# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Node import Node
from .NodesModifierDataBlock import NodesModifierDataBlock
class NodesModifierBake(bpy_struct):
    directory: str
    frame_start: int
    frame_end: int
    use_custom_simulation_frame_range: bool
    use_custom_path: bool
    bake_target: str
    bake_mode: str
    bake_id: int
    node: 'Node'
    data_blocks: bpy_prop_collection['NodesModifierDataBlock']