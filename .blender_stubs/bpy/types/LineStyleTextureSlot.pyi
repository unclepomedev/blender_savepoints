# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .TextureSlot import TextureSlot
from .Texture import Texture
class LineStyleTextureSlot(TextureSlot):
    texture: 'Texture'
    name: str
    offset: float
    scale: float
    color: float
    blend_type: str
    default_value: float
    output_node: str
    mapping_x: str
    mapping_y: str
    mapping_z: str
    mapping: str
    use_map_color_diffuse: bool
    use_map_alpha: bool
    texture_coords: str
    alpha_factor: float
    diffuse_color_factor: float