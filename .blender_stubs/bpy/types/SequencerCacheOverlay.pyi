# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SequencerCacheOverlay.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SequencerCacheOverlay(bpy_struct):

    @property
    def show_cache(self) -> bool:
        """Visualize cached images on the timeline"""
        ...
    @show_cache.setter
    def show_cache(self, value: bool):
        ...
    @property
    def show_cache_final_out(self) -> bool:
        """Visualize cached complete frames"""
        ...
    @show_cache_final_out.setter
    def show_cache_final_out(self, value: bool):
        ...
    @property
    def show_cache_raw(self) -> bool:
        """Visualize cached raw images"""
        ...
    @show_cache_raw.setter
    def show_cache_raw(self, value: bool):
        ...