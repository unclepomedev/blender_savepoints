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
from .Histogram import Histogram
class Scopes(bpy_struct):
    use_full_resolution: bool
    accuracy: float
    histogram: 'Histogram'
    waveform_mode: str
    waveform_alpha: float
    vectorscope_mode: str
    vectorscope_alpha: float