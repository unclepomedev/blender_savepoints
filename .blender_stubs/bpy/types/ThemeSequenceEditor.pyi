# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ThemeSpaceGeneric import ThemeSpaceGeneric
class ThemeSequenceEditor(bpy_struct):
    space: 'ThemeSpaceGeneric'
    grid: float
    movie_strip: float
    movieclip_strip: float
    image_strip: float
    scene_strip: float
    audio_strip: float
    effect_strip: float
    transition_strip: float
    color_strip: float
    meta_strip: float
    mask_strip: float
    text_strip: float
    active_strip: float
    selected_strip: float
    keyframe_border: float
    keyframe_border_selected: float
    preview_back: float
    metadatabg: float
    metadatatext: float
    row_alternate: float
    text_strip_cursor: float
    selected_text: float