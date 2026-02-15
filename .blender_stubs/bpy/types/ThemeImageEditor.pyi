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
from .ThemeSpaceGeneric import ThemeSpaceGeneric
class ThemeImageEditor(bpy_struct):
    @property
    def space(self) -> Annotated['ThemeSpaceGeneric', "is_animatable=False"]:
        """Settings for space"""
        ...
    grid: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    vertex: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    vertex_select: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    vertex_size: Annotated[int, "subtype='PIXEL'", "step=1"]
    face: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    face_select: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    face_mode_select: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    facedot_size: Annotated[int, "subtype='PIXEL'", "step=1"]
    editmesh_active: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    wire_edit: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    edge_width: Annotated[int, "subtype='PIXEL'", "step=1"]
    edge_select: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    scope_back: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    preview_stitch_face: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    preview_stitch_edge: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    preview_stitch_vert: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    preview_stitch_stitchable: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    preview_stitch_unstitchable: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    preview_stitch_active: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    uv_shadow: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    metadatabg: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    metadatatext: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]