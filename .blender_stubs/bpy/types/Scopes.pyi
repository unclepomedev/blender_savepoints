# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Histogram import Histogram
class Scopes(bpy_struct):
    use_full_resolution: bool
    """Sample every pixel of the image"""
    accuracy: Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=1"]
    """Proportion of original image source pixel lines to sample"""
    @property
    def histogram(self) -> Annotated[Optional['Histogram'], "is_animatable=False"]:
        """Histogram for viewing image statistics"""
        ...
    waveform_mode: Literal['LUMA', 'PARADE', 'YCBCR601', 'YCBCR709', 'YCBCRJPG', 'RGB']
    waveform_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Opacity of the points"""
    vectorscope_mode: Literal['LUMA', 'RGB']
    vectorscope_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Opacity of the points"""