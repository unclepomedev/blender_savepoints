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
    grid: list[float]
    movie_strip: list[float]
    movieclip_strip: list[float]
    image_strip: list[float]
    scene_strip: list[float]
    audio_strip: list[float]
    effect_strip: list[float]
    transition_strip: list[float]
    color_strip: list[float]
    meta_strip: list[float]
    mask_strip: list[float]
    text_strip: list[float]
    active_strip: list[float]
    selected_strip: list[float]
    keyframe_border: list[float]
    keyframe_border_selected: list[float]
    preview_back: list[float]
    metadatabg: list[float]
    metadatatext: list[float]
    row_alternate: list[float]
    text_strip_cursor: list[float]
    selected_text: list[float]