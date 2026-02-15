# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Window.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Operator import Operator
from .Scene import Scene
from .Screen import Screen
from .Stereo3dDisplay import Stereo3dDisplay
from .ViewLayer import ViewLayer
from .WorkSpace import WorkSpace
from .bpy_prop_collection import bpy_prop_collection

class Window(bpy_struct):

    @property
    def parent(self) -> Annotated[Optional['Window'], "is_animatable=False"]:
        """Active workspace and scene follow this window"""
        ...
    scene: Annotated['Scene', "is_animatable=False"]
    """Active scene to be edited in the window"""
    workspace: Annotated['WorkSpace', "is_animatable=False"]
    """Active workspace showing in the window"""
    screen: Annotated['Screen', "is_animatable=False"]
    """Active workspace screen showing in the window"""
    view_layer: Annotated['ViewLayer', "is_animatable=False"]
    """The active workspace view layer showing in the window"""
    @property
    def x(self) -> Annotated[int, "step=1"]:
        """Horizontal location of the window"""
        ...
    @property
    def y(self) -> Annotated[int, "step=1"]:
        """Vertical location of the window"""
        ...
    @property
    def width(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Window width"""
        ...
    @property
    def height(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Window height"""
        ...
    @property
    def stereo_3d_display(self) -> Annotated['Stereo3dDisplay', "is_animatable=False"]:
        """Settings for stereo 3D display"""
        ...
    @property
    def support_hdr_color(self) -> bool:
        """The window has a HDR graphics buffer that wide gamut and high dynamic range colors can be written to, in extended sRGB color space."""
        ...
    @property
    def modal_operators(self) -> Annotated[bpy_prop_collection['Operator'], "is_animatable=False"]:
        """A list of currently running modal operators"""
        ...
    def cursor_warp(self, *args, **kwargs) -> Any: ...
    def cursor_set(self, *args, **kwargs) -> Any: ...
    def cursor_modal_set(self, *args, **kwargs) -> Any: ...
    def cursor_modal_restore(self, *args, **kwargs) -> Any: ...
    def event_simulate(self, *args, **kwargs) -> Any: ...