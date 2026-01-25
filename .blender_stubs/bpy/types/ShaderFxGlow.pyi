# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .ShaderFx import ShaderFx
class ShaderFxGlow(ShaderFx):
    name: str
    type: str
    show_viewport: bool
    show_render: bool
    show_in_editmode: bool
    show_expanded: bool
    glow_color: float
    opacity: float
    select_color: float
    mode: str
    threshold: float
    size: float
    samples: int
    use_glow_under: bool
    rotation: float
    blend_mode: str