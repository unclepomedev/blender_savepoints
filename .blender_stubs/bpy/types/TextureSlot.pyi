# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.TextureSlot.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Texture import Texture

class TextureSlot(bpy_struct):

    @property
    def texture(self) -> Annotated[Optional['Texture'], "is_animatable=False"]:
        """Texture data-block used by this texture slot"""
        ...
    @texture.setter
    def texture(self, value: Annotated[Optional['Texture'], "is_animatable=False"]) -> None:
        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Texture slot name"""
        ...
    @property
    def offset(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5"]:
        """Fine tune of the texture mapping X, Y and Z locations"""
        ...
    @offset.setter
    def offset(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=5"]) -> None:
        ...
    @property
    def scale(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=2"]:
        """Set scaling for the texture's X, Y and Z sizes"""
        ...
    @scale.setter
    def scale(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=2"]) -> None:
        ...
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Default color for textures that don't return RGB or when RGB to intensity is enabled"""
        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def blend_type(self) -> Literal['MIX', 'DARKEN', 'MULTIPLY', 'LIGHTEN', 'SCREEN', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']:
        """Mode used to apply the texture"""
        ...
    @blend_type.setter
    def blend_type(self, value: Literal['MIX', 'DARKEN', 'MULTIPLY', 'LIGHTEN', 'SCREEN', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE']) -> None:
        ...
    @property
    def default_value(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Value to use for Ref, Spec, Amb, Emit, Alpha, RayMir, TransLu and Hard"""
        ...
    @default_value.setter
    def default_value(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def output_node(self) -> Literal['DEFAULT']:
        """Which output node to use, for node-based textures"""
        ...
    @output_node.setter
    def output_node(self, value: Literal['DEFAULT']) -> None:
        ...