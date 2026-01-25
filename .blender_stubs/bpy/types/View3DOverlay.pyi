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
class View3DOverlay(bpy_struct):
    show_overlays: bool
    show_ortho_grid: bool
    show_floor: bool
    show_axis_x: bool
    show_axis_y: bool
    show_axis_z: bool
    grid_scale: float
    grid_lines: int
    grid_subdivisions: int
    grid_scale_unit: float
    show_outline_selected: bool
    show_object_origins: bool
    show_object_origins_all: bool
    show_relationship_lines: bool
    show_cursor: bool
    show_text: bool
    show_stats: bool
    show_camera_guides: bool
    show_camera_passepartout: bool
    show_extras: bool
    show_light_colors: bool
    show_bones: bool
    show_face_orientation: bool
    show_fade_inactive: bool
    fade_inactive_alpha: float
    show_xray_bone: bool
    xray_alpha_bone: float
    bone_wire_alpha: float
    show_motion_paths: bool
    show_onion_skins: bool
    show_look_dev: bool
    show_wireframes: bool
    wireframe_threshold: float
    wireframe_opacity: float
    show_viewer_attribute: bool
    viewer_attribute_opacity: float
    show_viewer_text: bool
    show_paint_wire: bool
    show_wpaint_contours: bool
    show_weight: bool
    show_retopology: bool
    retopology_offset: float
    show_face_normals: bool
    show_vertex_normals: bool
    show_split_normals: bool
    show_faces: bool
    show_face_center: bool
    show_edge_crease: bool
    show_edge_bevel_weight: bool
    show_edge_seams: bool
    show_edge_sharp: bool
    show_freestyle_edge_marks: bool
    show_freestyle_face_marks: bool
    show_statvis: bool
    show_extra_edge_length: bool
    show_extra_edge_angle: bool
    show_extra_face_angle: bool
    show_extra_face_area: bool
    show_extra_indices: bool
    display_handle: str
    show_curve_normals: bool
    normals_length: float
    normals_constant_screen_size: float
    use_normals_constant_screen_size: bool
    texture_paint_mode_opacity: float
    vertex_paint_mode_opacity: float
    weight_paint_mode_opacity: float
    sculpt_mode_mask_opacity: float
    show_sculpt_curves_cage: bool
    sculpt_curves_cage_opacity: float
    sculpt_mode_face_sets_opacity: float
    show_sculpt_mask: bool
    show_sculpt_face_sets: bool
    show_annotation: bool
    use_gpencil_fade_objects: bool
    use_gpencil_grid: bool
    use_gpencil_fade_layers: bool
    use_gpencil_fade_gp_objects: bool
    use_gpencil_canvas_xray: bool
    use_gpencil_show_directions: bool
    use_gpencil_show_material_name: bool
    gpencil_grid_opacity: float
    gpencil_grid_color: list[float]
    gpencil_grid_scale: list[float]
    gpencil_grid_offset: list[float]
    gpencil_grid_subdivisions: int
    gpencil_fade_objects: float
    gpencil_fade_layer: float
    use_gpencil_edit_lines: bool
    use_gpencil_multiedit_line_only: bool
    use_gpencil_onion_skin: bool
    use_gpencil_onion_skin_active_object: bool
    vertex_opacity: float
    gpencil_vertex_paint_opacity: float
    use_debug_freeze_view_culling: bool