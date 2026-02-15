# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Region.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .AnyType import AnyType
from .View2D import View2D

class Region(bpy_struct):

    @property
    def type(self) -> Literal['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'ASSET_SHELF', 'ASSET_SHELF_HEADER', 'PREVIEW', 'HUD', 'NAVIGATION_BAR', 'EXECUTE', 'FOOTER', 'TOOL_HEADER', 'XR']:
        """Type of this region"""
        ...
    @property
    def x(self) -> Annotated[int, "step=1"]:
        """The window relative vertical location of the region"""
        ...
    @property
    def y(self) -> Annotated[int, "step=1"]:
        """The window relative horizontal location of the region"""
        ...
    @property
    def width(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Region width"""
        ...
    @property
    def height(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Region height"""
        ...
    @property
    def view2d(self) -> Annotated['View2D', "is_animatable=False"]:
        """2D view of the region"""
        ...
    @property
    def alignment(self) -> Literal['NONE', 'TOP', 'BOTTOM', 'LEFT', 'RIGHT', 'HORIZONTAL_SPLIT', 'VERTICAL_SPLIT', 'FLOAT', 'QUAD_SPLIT']:
        """Alignment of the region within the area"""
        ...
    @property
    def data(self) -> Annotated[Optional['AnyType'], "is_animatable=False"]:
        """Region specific data (the type depends on the region type)"""
        ...
    active_panel_category: Literal['UNSUPPORTED']
    """The current active panel category, may be Null if the region does not support this feature (NOTE: these categories are generated at runtime, so list may be empty at initialization, before any drawing took place)"""
    def tag_redraw(self, *args, **kwargs) -> Any: ...
    def tag_refresh_ui(self, *args, **kwargs) -> Any: ...