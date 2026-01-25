# Blender Probe Generated Stub for Blender 5.0.1
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
    grid: float
    vertex: float
    vertex_select: float
    vertex_size: int
    face: float
    face_select: float
    face_mode_select: float
    facedot_size: int
    editmesh_active: float
    wire_edit: float
    edge_width: int
    edge_select: float
    scope_back: float
    preview_stitch_face: float
    preview_stitch_edge: float
    preview_stitch_vert: float
    preview_stitch_stitchable: float
    preview_stitch_unstitchable: float
    preview_stitch_active: float
    uv_shadow: float
    metadatabg: float
    metadatatext: float