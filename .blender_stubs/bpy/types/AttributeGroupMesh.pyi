# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.AttributeGroupMesh.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Attribute import Attribute

class AttributeGroupMesh(bpy_struct):

    @property
    def active(self) -> Annotated[Optional['Attribute'], "is_animatable=False"]:
        """Active attribute"""
        ...
    @active.setter
    def active(self, value: Annotated[Optional['Attribute'], "is_animatable=False"]) -> None:
        ...
    @property
    def active_index(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Active attribute index or -1 when none are active"""
        ...
    @active_index.setter
    def active_index(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def active_color(self) -> Annotated[Optional['Attribute'], "is_animatable=False"]:
        """Active color attribute for display and editing"""
        ...
    @active_color.setter
    def active_color(self, value: Annotated[Optional['Attribute'], "is_animatable=False"]) -> None:
        ...
    @property
    def active_color_index(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Active color attribute index"""
        ...
    @active_color_index.setter
    def active_color_index(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def render_color_index(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """The index of the color attribute used as a fallback for rendering"""
        ...
    @render_color_index.setter
    def render_color_index(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def default_color_name(self) -> Annotated[str, "is_animatable=False"]:
        """The name of the default color attribute used as a fallback for rendering"""
        ...
    @default_color_name.setter
    def default_color_name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def active_color_name(self) -> Annotated[str, "is_animatable=False"]:
        """The name of the active color attribute for display and editing"""
        ...
    @active_color_name.setter
    def active_color_name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    def new(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def domain_size(self, *args, **kwargs) -> Any: ...
    def __contains__(self, key: Union[str, int]) -> bool: ...
    def __iter__(self) -> Iterator['Attribute']: ...
    def __getitem__(self, key: Union[str, int]) -> 'Attribute': ...
    def __len__(self) -> int: ...