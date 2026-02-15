# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeClipEditor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ThemeSpaceGeneric import ThemeSpaceGeneric

class ThemeClipEditor(bpy_struct):

    @property
    def space(self) -> Annotated['ThemeSpaceGeneric', "is_animatable=False"]:
        """Settings for space"""
        ...
    grid: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    marker_outline: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of marker's outline"""
    marker: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of marker"""
    active_marker: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of active marker"""
    selected_marker: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of selected marker"""
    disabled_marker: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of disabled marker"""
    locked_marker: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of locked marker"""
    path_before: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of path before current frame"""
    path_after: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of path after current frame"""
    path_keyframe_before: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of keyframes on a path before current frame"""
    path_keyframe_after: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of keyframes on a path after current frame"""
    metadatabg: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    metadatatext: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
