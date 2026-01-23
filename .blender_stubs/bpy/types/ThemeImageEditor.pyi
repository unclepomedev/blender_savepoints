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
class ThemeImageEditor(bpy_struct):
    space: 'ThemeSpaceGeneric'
    grid: list[float]
    vertex: list[float]
    vertex_select: list[float]
    vertex_size: int
    face: list[float]
    face_select: list[float]
    face_mode_select: list[float]
    facedot_size: int
    editmesh_active: list[float]
    wire_edit: list[float]
    edge_width: int
    edge_select: list[float]
    scope_back: list[float]
    preview_stitch_face: list[float]
    preview_stitch_edge: list[float]
    preview_stitch_vert: list[float]
    preview_stitch_stitchable: list[float]
    preview_stitch_unstitchable: list[float]
    preview_stitch_active: list[float]
    uv_shadow: list[float]
    metadatabg: list[float]
    metadatatext: list[float]