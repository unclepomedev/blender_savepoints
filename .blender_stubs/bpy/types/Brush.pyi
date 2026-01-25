# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .ID import ID
from .AssetMetaData import AssetMetaData
from .BrushCapabilities import BrushCapabilities
from .BrushCapabilitiesImagePaint import BrushCapabilitiesImagePaint
from .BrushCapabilitiesSculpt import BrushCapabilitiesSculpt
from .BrushCapabilitiesVertexPaint import BrushCapabilitiesVertexPaint
from .BrushCapabilitiesWeightPaint import BrushCapabilitiesWeightPaint
from .BrushCurvesSculptSettings import BrushCurvesSculptSettings
from .BrushGpencilSettings import BrushGpencilSettings
from .BrushTextureSlot import BrushTextureSlot
from .ColorRamp import ColorRamp
from .CurveMapping import CurveMapping
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .PaintCurve import PaintCurve
from .Texture import Texture
class Brush(ID):
    name: str
    name_full: str
    id_type: str
    session_uid: int
    is_evaluated: bool
    original: 'ID'
    users: int
    use_fake_user: bool
    use_extra_user: bool
    is_embedded_data: bool
    is_linked_packed: bool
    is_missing: bool
    is_runtime_data: bool
    is_editable: bool
    tag: bool
    is_library_indirect: bool
    library: 'Library'
    library_weak_reference: 'LibraryWeakReference'
    asset_data: 'AssetMetaData'
    override_library: 'IDOverrideLibrary'
    preview: 'ImagePreview'
    has_unsaved_changes: bool
    blend: str
    sculpt_brush_type: str
    vertex_brush_type: str
    weight_brush_type: str
    image_brush_type: str
    gpencil_brush_type: str
    gpencil_vertex_brush_type: str
    gpencil_sculpt_brush_type: str
    gpencil_weight_brush_type: str
    curves_sculpt_brush_type: str
    direction: str
    stroke_method: str
    sculpt_plane: str
    mask_tool: str
    curve_distance_falloff_preset: str
    deform_target: str
    elastic_deform_type: str
    snake_hook_deform_type: str
    plane_inversion_mode: str
    cloth_deform_type: str
    cloth_force_falloff_type: str
    cloth_simulation_area_type: str
    boundary_falloff_type: str
    smooth_deform_type: str
    smear_deform_type: str
    slide_deform_type: str
    boundary_deform_type: str
    pose_deform_type: str
    pose_origin_type: str
    jitter_unit: str
    falloff_shape: str
    size: int
    unprojected_size: float
    input_samples: int
    jitter: float
    jitter_absolute: int
    spacing: int
    grad_spacing: int
    use_color_jitter: bool
    hue_jitter: float
    saturation_jitter: float
    value_jitter: float
    use_stroke_random_hue: bool
    use_stroke_random_sat: bool
    use_stroke_random_val: bool
    use_random_press_hue: bool
    use_random_press_sat: bool
    use_random_press_val: bool
    curve_random_hue: 'CurveMapping'
    curve_random_saturation: 'CurveMapping'
    curve_random_value: 'CurveMapping'
    curve_size: 'CurveMapping'
    curve_strength: 'CurveMapping'
    curve_jitter: 'CurveMapping'
    smooth_stroke_radius: int
    smooth_stroke_factor: float
    rate: float
    color: list[float]
    secondary_color: list[float]
    weight: float
    strength: float
    flow: float
    wet_mix: float
    wet_persistence: float
    density: float
    tip_scale_x: float
    use_hardness_pressure: bool
    invert_hardness_pressure: bool
    use_flow_pressure: bool
    invert_flow_pressure: bool
    use_wet_mix_pressure: bool
    invert_wet_mix_pressure: bool
    use_wet_persistence_pressure: bool
    invert_wet_persistence_pressure: bool
    use_density_pressure: bool
    invert_density_pressure: bool
    dash_ratio: float
    dash_samples: int
    plane_offset: float
    plane_trim: float
    height: float
    plane_depth: float
    plane_height: float
    stabilize_normal: float
    stabilize_plane: float
    texture_sample_bias: float
    use_color_as_displacement: bool
    normal_weight: float
    elastic_deform_volume_preservation: float
    rake_factor: float
    crease_pinch_factor: float
    pose_offset: float
    disconnected_distance_max: float
    boundary_offset: float
    surface_smooth_shape_preservation: float
    surface_smooth_current_vertex: float
    surface_smooth_iterations: int
    multiplane_scrape_angle: float
    pose_smooth_iterations: int
    pose_ik_segments: int
    tip_roundness: float
    cloth_mass: float
    cloth_damping: float
    cloth_sim_limit: float
    cloth_sim_falloff: float
    cloth_constraint_softbody_strength: float
    hardness: float
    automasking_boundary_edges_propagation_steps: int
    auto_smooth_factor: float
    topology_rake_factor: float
    tilt_strength_factor: float
    normal_radius_factor: float
    area_radius_factor: float
    wet_paint_radius_factor: float
    stencil_pos: list[float]
    stencil_dimension: list[float]
    mask_stencil_pos: list[float]
    mask_stencil_dimension: list[float]
    sharp_threshold: float
    fill_threshold: float
    blur_kernel_radius: int
    blur_mode: str
    falloff_angle: float
    use_airbrush: bool
    use_original_normal: bool
    use_original_plane: bool
    use_automasking_topology: bool
    use_automasking_face_sets: bool
    use_automasking_boundary_edges: bool
    use_automasking_boundary_face_sets: bool
    use_automasking_cavity: bool
    use_automasking_cavity_inverted: bool
    use_automasking_custom_cavity_curve: bool
    automasking_cavity_factor: float
    automasking_cavity_blur_steps: int
    automasking_cavity_curve: 'CurveMapping'
    use_automasking_start_normal: bool
    automasking_start_normal_limit: float
    automasking_start_normal_falloff: float
    use_automasking_view_normal: bool
    use_automasking_view_occlusion: bool
    automasking_view_normal_limit: float
    automasking_view_normal_falloff: float
    use_scene_spacing: str
    use_grab_active_vertex: bool
    use_grab_silhouette: bool
    use_paint_antialiasing: bool
    use_multiplane_scrape_dynamic: bool
    show_multiplane_scrape_planes_preview: bool
    use_pose_ik_anchored: bool
    use_pose_lock_rotation: bool
    use_connected_only: bool
    use_cloth_pin_simulation_boundary: bool
    use_cloth_collision: bool
    invert_to_scrape_fill: bool
    use_pressure_strength: bool
    use_offset_pressure: bool
    use_pressure_area_radius: bool
    use_pressure_size: bool
    use_pressure_jitter: bool
    use_pressure_spacing: bool
    use_pressure_masking: str
    use_inverse_smooth_pressure: bool
    use_plane_trim: bool
    use_frontface: bool
    use_frontface_falloff: bool
    use_anchor: bool
    use_space: bool
    use_line: bool
    use_curve: bool
    use_smooth_stroke: bool
    use_persistent: bool
    use_accumulate: bool
    use_space_attenuation: bool
    use_adaptive_space: bool
    use_locked_size: str
    color_type: str
    use_edge_to_edge: bool
    use_restore_mesh: bool
    use_alpha: bool
    curve_distance_falloff: 'CurveMapping'
    paint_curve: 'PaintCurve'
    gradient: 'ColorRamp'
    gradient_stroke_mode: str
    gradient_fill_mode: str
    use_primary_overlay: bool
    use_secondary_overlay: bool
    use_cursor_overlay: bool
    use_cursor_overlay_override: bool
    use_primary_overlay_override: bool
    use_secondary_overlay_override: bool
    use_paint_sculpt: bool
    use_paint_uv_sculpt: bool
    use_paint_vertex: bool
    use_paint_weight: bool
    use_paint_image: bool
    use_paint_grease_pencil: bool
    use_vertex_grease_pencil: bool
    use_paint_sculpt_curves: bool
    texture_slot: 'BrushTextureSlot'
    texture: 'Texture'
    mask_texture_slot: 'BrushTextureSlot'
    mask_texture: 'Texture'
    texture_overlay_alpha: int
    mask_overlay_alpha: int
    cursor_overlay_alpha: int
    cursor_color_add: list[float]
    cursor_color_subtract: list[float]
    brush_capabilities: 'BrushCapabilities'
    sculpt_capabilities: 'BrushCapabilitiesSculpt'
    image_paint_capabilities: 'BrushCapabilitiesImagePaint'
    vertex_paint_capabilities: 'BrushCapabilitiesVertexPaint'
    weight_paint_capabilities: 'BrushCapabilitiesWeightPaint'
    gpencil_settings: 'BrushGpencilSettings'
    curves_sculpt_settings: 'BrushCurvesSculptSettings'
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def rename(self, *args, **kwargs) -> Any: ...
    def evaluated_get(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def asset_mark(self, *args, **kwargs) -> Any: ...
    def asset_clear(self, *args, **kwargs) -> Any: ...
    def asset_generate_preview(self, *args, **kwargs) -> Any: ...
    def override_create(self, *args, **kwargs) -> Any: ...
    def override_hierarchy_create(self, *args, **kwargs) -> Any: ...
    def user_clear(self, *args, **kwargs) -> Any: ...
    def user_remap(self, *args, **kwargs) -> Any: ...
    def make_local(self, *args, **kwargs) -> Any: ...
    def user_of_id(self, *args, **kwargs) -> Any: ...
    def animation_data_create(self, *args, **kwargs) -> Any: ...
    def animation_data_clear(self, *args, **kwargs) -> Any: ...
    def update_tag(self, *args, **kwargs) -> Any: ...
    def preview_ensure(self, *args, **kwargs) -> Any: ...