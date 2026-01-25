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
class BrushTextureSlot(TextureSlot):
    texture: 'Texture'
    name: str
    offset: list[float]
    scale: list[float]
    color: list[float]
    blend_type: str
    default_value: float
    output_node: str
    angle: float
    map_mode: str
    mask_map_mode: str
    use_rake: bool
    use_random: bool
    random_angle: float
    has_texture_angle_source: bool
    has_random_texture_angle: bool
    has_texture_angle: bool