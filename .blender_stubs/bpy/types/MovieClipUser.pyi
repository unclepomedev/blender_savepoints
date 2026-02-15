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
class MovieClipUser(bpy_struct):
    frame_current: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1"]
    """Current frame number in movie or image sequence"""
    proxy_render_size: Literal['PROXY_25', 'PROXY_50', 'PROXY_75', 'PROXY_100', 'FULL']
    """Display preview using full resolution or different proxy resolutions"""
    use_render_undistorted: bool
    """Render preview using undistorted proxy"""