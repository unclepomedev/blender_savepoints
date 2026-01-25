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
from .ThemeSpaceGradient import ThemeSpaceGradient
class ThemeView3D(bpy_struct):
    space: 'ThemeSpaceGradient'
    grid: list[float]
    clipping_border_3d: list[float]
    wire: list[float]
    wire_edit: list[float]
    edge_width: int
    gp_vertex: list[float]
    gp_vertex_select: list[float]
    gp_vertex_size: int
    text_grease_pencil: list[float]
    object_selected: list[float]
    object_active: list[float]
    camera: list[float]
    empty: list[float]
    light: list[float]
    speaker: list[float]
    vertex: list[float]
    vertex_select: list[float]
    vertex_size: int
    edge_select: list[float]
    edge_mode_select: list[float]
    face: list[float]
    face_select: list[float]
    face_mode_select: list[float]
    facedot_size: int
    face_back: list[float]
    face_front: list[float]
    bevel: list[float]
    seam: list[float]
    sharp: list[float]
    crease: list[float]
    freestyle: list[float]
    extra_edge_len: list[float]
    extra_edge_angle: list[float]
    extra_face_angle: list[float]
    extra_face_area: list[float]
    editmesh_active: list[float]
    normal: list[float]
    vertex_normal: list[float]
    split_normal: list[float]
    vertex_unreferenced: list[float]
    face_retopology: list[float]
    nurb_uline: list[float]
    nurb_vline: list[float]
    nurb_sel_uline: list[float]
    nurb_sel_vline: list[float]
    bone_pose: list[float]
    bone_pose_active: list[float]
    bone_solid: list[float]
    bone_locked_weight: list[float]
    before_current_frame: list[float]
    after_current_frame: list[float]
    bundle_solid: list[float]
    camera_path: list[float]
    camera_passepartout: list[float]
    skin_root: list[float]
    view_overlay: list[float]
    transform: list[float]
    outline_width: int
    object_origin_size: int