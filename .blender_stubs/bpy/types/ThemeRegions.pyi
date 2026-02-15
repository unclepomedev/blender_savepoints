# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeRegions.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ThemeRegionsAssetShelf import ThemeRegionsAssetShelf
from .ThemeRegionsChannels import ThemeRegionsChannels
from .ThemeRegionsScrubbing import ThemeRegionsScrubbing
from .ThemeRegionsSidebars import ThemeRegionsSidebars

class ThemeRegions(bpy_struct):

    @property
    def asset_shelf(self) -> Annotated['ThemeRegionsAssetShelf', "is_animatable=False"]:

        ...
    @property
    def channels(self) -> Annotated['ThemeRegionsChannels', "is_animatable=False"]:

        ...
    @property
    def scrubbing(self) -> Annotated['ThemeRegionsScrubbing', "is_animatable=False"]:

        ...
    @property
    def sidebars(self) -> Annotated['ThemeRegionsSidebars', "is_animatable=False"]:

        ...