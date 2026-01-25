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
from .CurvePaintSettings import CurvePaintSettings
from .CurveProfile import CurveProfile
from .CurvesSculpt import CurvesSculpt
from .GPencilInterpolateSettings import GPencilInterpolateSettings
from .GPencilSculptSettings import GPencilSculptSettings
from .GpPaint import GpPaint
from .GpSculptPaint import GpSculptPaint
from .GpVertexPaint import GpVertexPaint
from .GpWeightPaint import GpWeightPaint
from .ImagePaint import ImagePaint
from .MeshStatVis import MeshStatVis
from .Object import Object
from .PaintModeSettings import PaintModeSettings
from .ParticleEdit import ParticleEdit
from .Sculpt import Sculpt
from .SequencerToolSettings import SequencerToolSettings
from .UvSculpt import UvSculpt
from .VertexPaint import VertexPaint
class ToolSettings(bpy_struct):
    sculpt: 'Sculpt'
    curves_sculpt: 'CurvesSculpt'
    use_auto_normalize: bool
    use_lock_relative: bool
    use_multipaint: bool
    vertex_group_user: str
    vertex_group_subset: str
    vertex_paint: 'VertexPaint'
    weight_paint: 'VertexPaint'
    image_paint: 'ImagePaint'
    paint_mode: 'PaintModeSettings'
    uv_sculpt: 'UvSculpt'
    gpencil_paint: 'GpPaint'
    gpencil_vertex_paint: 'GpVertexPaint'
    gpencil_sculpt_paint: 'GpSculptPaint'
    gpencil_weight_paint: 'GpWeightPaint'
    particle_edit: 'ParticleEdit'
    uv_sculpt_lock_borders: bool
    uv_sculpt_all_islands: bool
    lock_object_mode: bool
    workspace_tool_type: str
    use_proportional_edit: bool
    use_proportional_edit_objects: bool
    use_proportional_projected: bool
    use_proportional_connected: bool
    use_proportional_edit_mask: bool
    use_proportional_action: bool
    use_proportional_fcurve: bool
    lock_markers: bool
    proportional_edit_falloff: str
    proportional_size: float
    proportional_distance: float
    double_threshold: float
    transform_pivot_point: str
    use_transform_pivot_point_align: bool
    use_transform_data_origin: bool
    use_transform_skip_children: bool
    use_transform_correct_face_attributes: bool
    use_transform_correct_keep_connected: bool
    use_mesh_automerge: bool
    use_mesh_automerge_and_split: bool
    use_snap: bool
    use_snap_node: bool
    use_snap_sequencer: bool
    use_snap_uv: bool
    use_snap_align_rotation: bool
    use_snap_grid_absolute: bool
    snap_angle_increment_2d: float
    snap_angle_increment_2d_precision: float
    snap_angle_increment_3d: float
    snap_angle_increment_3d_precision: float
    snap_elements: str
    snap_elements_base: str
    snap_elements_individual: str
    snap_face_nearest_steps: int
    use_snap_to_same_target: bool
    use_snap_anim: bool
    use_snap_driver: bool
    use_snap_time_absolute: bool
    use_snap_driver_absolute: bool
    snap_anim_element: str
    use_snap_playhead: bool
    snap_playhead_element: str
    snap_playhead_frame_step: int
    snap_playhead_second_step: int
    playhead_snap_distance: int
    snap_uv_element: str
    snap_target: str
    use_snap_peel_object: bool
    use_snap_backface_culling: bool
    use_snap_self: bool
    use_snap_edit: bool
    use_snap_nonedit: bool
    use_snap_selectable: bool
    use_snap_translate: bool
    use_snap_rotate: bool
    use_snap_scale: bool
    plane_axis: str
    plane_axis_auto: bool
    plane_depth: str
    plane_orientation: str
    snap_elements_tool: str
    use_gpencil_draw_additive: bool
    use_gpencil_draw_onback: bool
    use_gpencil_thumbnail_list: bool
    use_gpencil_weight_data_add: bool
    use_gpencil_automerge_strokes: bool
    gpencil_sculpt: 'GPencilSculptSettings'
    gpencil_interpolate: 'GPencilInterpolateSettings'
    gpencil_stroke_placement_view3d: str
    gpencil_stroke_snap_mode: str
    gpencil_surface_offset: float
    use_gpencil_project_only_selected: bool
    gpencil_selectmode_edit: str
    use_gpencil_select_mask_point: bool
    use_gpencil_select_mask_stroke: bool
    use_gpencil_select_mask_segment: bool
    use_gpencil_vertex_select_mask_point: bool
    use_gpencil_vertex_select_mask_stroke: bool
    use_gpencil_vertex_select_mask_segment: bool
    use_grease_pencil_multi_frame_editing: bool
    annotation_stroke_placement_view2d: str
    annotation_stroke_placement_view3d: str
    use_annotation_stroke_endpoints: bool
    use_annotation_project_only_selected: bool
    annotation_thickness: int
    use_keyframe_insert_auto: bool
    auto_keying_mode: str
    use_record_with_nla: bool
    use_keyframe_insert_keyingset: bool
    use_keyframe_cycle_aware: bool
    keyframe_type: str
    anim_mirror_object: 'Object'
    anim_mirror_bone: str
    anim_relative_object: 'Object'
    anim_fix_to_cam_use_loc: bool
    anim_fix_to_cam_use_rot: bool
    anim_fix_to_cam_use_scale: bool
    uv_select_mode: str
    uv_sticky_select_mode: str
    use_uv_select_sync: bool
    use_uv_select_island: bool
    show_uv_local_view: bool
    use_uv_custom_region: bool
    mesh_select_mode: bool
    vertex_group_weight: float
    use_edge_path_live_unwrap: bool
    normal_vector: float
    curve_paint_settings: 'CurvePaintSettings'
    statvis: 'MeshStatVis'
    custom_bevel_profile_preset: 'CurveProfile'
    sequencer_tool_settings: 'SequencerToolSettings'