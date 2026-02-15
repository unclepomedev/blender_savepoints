# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeView3D.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ThemeSpaceGradient import ThemeSpaceGradient

class ThemeView3D(bpy_struct):

    @property
    def space(self) -> Annotated['ThemeSpaceGradient', "is_animatable=False"]:
        """Settings for space"""
        ...
    grid: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    clipping_border_3d: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    wire: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    wire_edit: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color for wireframe when in edit mode, but edge selection is active"""
    edge_width: Annotated[int, "subtype='PIXEL'", "step=1"]

    gp_vertex: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    gp_vertex_select: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    gp_vertex_size: Annotated[int, "subtype='PIXEL'", "step=1"]

    text_grease_pencil: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color for indicating Grease Pencil keyframes"""
    object_selected: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    object_active: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    camera: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    empty: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    light: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    speaker: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    vertex: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    vertex_select: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    vertex_size: Annotated[int, "subtype='PIXEL'", "step=1"]

    edge_select: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    edge_mode_select: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    face: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    face_select: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    face_mode_select: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    facedot_size: Annotated[int, "subtype='PIXEL'", "step=1"]

    face_back: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    face_front: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    bevel: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    seam: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    sharp: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    crease: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    freestyle: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    extra_edge_len: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    extra_edge_angle: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    extra_face_angle: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    extra_face_area: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    editmesh_active: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    normal: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    vertex_normal: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    split_normal: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    vertex_unreferenced: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    face_retopology: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    nurb_uline: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    nurb_vline: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    nurb_sel_uline: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    nurb_sel_vline: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    bone_pose: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Outline color of selected pose bones"""
    bone_pose_active: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Outline color of active pose bones"""
    bone_solid: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Default color of the solid shapes of bones"""
    bone_locked_weight: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Shade for bones corresponding to a locked weight group during painting"""
    before_current_frame: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """The color for things before the current frame (for onion skinning, motion paths, etc.)"""
    after_current_frame: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """The color for things after the current frame (for onion skinning, motion paths, etc.)"""
    bundle_solid: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    camera_path: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    camera_passepartout: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    skin_root: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    view_overlay: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    transform: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    outline_width: Annotated[int, "subtype='PIXEL'", "step=1"]

    object_origin_size: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Diameter in pixels for object/light origin display"""