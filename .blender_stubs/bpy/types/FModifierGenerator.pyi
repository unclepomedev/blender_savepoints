# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .FModifier import FModifier
class FModifierGenerator(FModifier):
    name: str
    type: str
    show_expanded: bool
    mute: bool
    is_valid: bool
    active: bool
    use_restricted_range: bool
    frame_start: float
    frame_end: float
    blend_in: float
    blend_out: float
    use_influence: bool
    influence: float
    use_additive: bool
    mode: str
    poly_order: int
    coefficients: float