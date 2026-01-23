# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .FModifier import FModifier
class FModifierNoise(FModifier):
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
    blend_type: str
    scale: float
    strength: float
    phase: float
    offset: float
    lacunarity: float
    roughness: float
    depth: int
    use_legacy_noise: bool