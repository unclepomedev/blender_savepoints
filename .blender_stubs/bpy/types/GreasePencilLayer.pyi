# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .GreasePencilTreeNode import GreasePencilTreeNode
from .GreasePencilFrame import GreasePencilFrame
from .GreasePencilLayerGroup import GreasePencilLayerGroup
from .GreasePencilLayerMask import GreasePencilLayerMask
from .Object import Object
class GreasePencilLayer(GreasePencilTreeNode):
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
    frames: bpy_prop_collection['GreasePencilFrame']
    mask_layers: bpy_prop_collection['GreasePencilLayerMask']
    lock_frame: bool
    opacity: float
    tint_color: float
    tint_factor: float
    radius_offset: float
    use_lights: bool
    pass_index: int
    parent: 'Object'
    parent_bone: str
    translation: float
    rotation: float
    scale: float
    viewlayer_render: str
    use_viewlayer_masks: bool
    blend_mode: str
    ignore_locked_materials: bool
    matrix_local: float
    matrix_parent_inverse: float
    def get_frame_at(self, *args, **kwargs) -> Any: ...
    def current_frame(self, *args, **kwargs) -> Any: ...