# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeSequenceEditor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ThemeSpaceGeneric import ThemeSpaceGeneric

class ThemeSequenceEditor(bpy_struct):

    @property
    def space(self) -> Annotated['ThemeSpaceGeneric', "is_animatable=False"]:
        """Settings for space"""
        ...
    grid: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    movie_strip: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    movieclip_strip: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    image_strip: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    scene_strip: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    audio_strip: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    effect_strip: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    transition_strip: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    color_strip: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    meta_strip: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    mask_strip: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    text_strip: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    active_strip: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    selected_strip: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    keyframe_border: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of keyframe border"""
    keyframe_border_selected: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of selected keyframe border"""
    preview_back: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    metadatabg: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    metadatatext: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    row_alternate: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Overlay color on every other row"""
    text_strip_cursor: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Text strip editing cursor"""
    selected_text: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Text strip editing selection"""