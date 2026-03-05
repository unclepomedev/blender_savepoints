# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.MovieClipUser.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class MovieClipUser(bpy_struct):

    @property
    def frame_current(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]:
        """Current frame number in movie or image sequence"""
        ...
    @frame_current.setter
    def frame_current(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]):
        ...
    @property
    def proxy_render_size(self) -> Literal['PROXY_25', 'PROXY_50', 'PROXY_75', 'PROXY_100', 'FULL']:
        """Display preview using full resolution or different proxy resolutions"""
        ...
    @proxy_render_size.setter
    def proxy_render_size(self, value: Literal['PROXY_25', 'PROXY_50', 'PROXY_75', 'PROXY_100', 'FULL']):
        ...
    @property
    def use_render_undistorted(self) -> bool:
        """Render preview using undistorted proxy"""
        ...
    @use_render_undistorted.setter
    def use_render_undistorted(self, value: bool):
        ...