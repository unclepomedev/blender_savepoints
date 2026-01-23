# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .ShaderFx import ShaderFx
class ShaderFxRim(ShaderFx):
    name: str
    type: str
    show_viewport: bool
    show_render: bool
    show_in_editmode: bool
    show_expanded: bool
    offset: list[int]
    rim_color: list[float]
    mask_color: list[float]
    mode: str
    blur: list[int]
    samples: int