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
from .Texture import Texture
class TextureSlot(bpy_struct):
    texture: 'Texture'
    name: str
    offset: float
    scale: float
    color: float
    blend_type: str
    default_value: float
    output_node: str