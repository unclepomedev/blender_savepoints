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
class SequencerCacheOverlay(bpy_struct):
    show_cache: bool
    """Visualize cached images on the timeline"""
    show_cache_final_out: bool
    """Visualize cached complete frames"""
    show_cache_raw: bool
    """Visualize cached raw images"""