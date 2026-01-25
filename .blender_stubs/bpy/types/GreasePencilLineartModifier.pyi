# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Modifier import Modifier
from .Collection import Collection
from .Material import Material
from .Object import Object
class GreasePencilLineartModifier(Modifier):
    name: str
    type: str
    show_viewport: bool
    show_render: bool
    show_in_editmode: bool
    show_on_cage: bool
    show_expanded: bool
    is_active: bool
    use_pin_to_last: bool
    is_override_data: bool
    use_apply_on_spline: bool
    execution_time: float
    persistent_uid: int
    use_custom_camera: bool
    use_fuzzy_intersections: bool
    use_fuzzy_all: bool
    use_object_instances: bool
    use_edge_overlap: bool
    use_clip_plane_boundaries: bool
    crease_threshold: float
    split_angle: float
    smooth_tolerance: float
    use_loose_as_contour: bool
    invert_source_vertex_group: bool
    use_output_vertex_group_match_by_name: bool
    use_face_mark: bool
    use_face_mark_invert: bool
    use_face_mark_boundaries: bool
    use_face_mark_keep_contour: bool
    chaining_image_threshold: float
    use_loose_edge_chain: bool
    use_geometry_space_chain: bool
    use_detail_preserve: bool
    use_overlap_edge_type_support: bool
    stroke_depth_offset: float
    use_offset_towards_custom_camera: bool
    source_camera: 'Object'
    light_contour_object: 'Object'
    source_type: str
    source_object: 'Object'
    source_collection: 'Collection'
    use_contour: bool
    use_loose: bool
    use_crease: bool
    use_material: bool
    use_edge_mark: bool
    use_intersection: bool
    use_light_contour: bool
    use_shadow: bool
    shadow_region_filtering: str
    silhouette_filtering: str
    use_multiple_levels: bool
    level_start: int
    level_end: int
    target_layer: str
    target_material: 'Material'
    source_vertex_group: str
    vertex_group: str
    is_baked: bool
    use_cache: bool
    overscan: float
    radius: float
    opacity: float
    use_material_mask: bool
    use_material_mask_match: bool
    use_material_mask_bits: bool
    use_intersection_match: bool
    use_intersection_mask: bool
    use_crease_on_smooth: bool
    use_crease_on_sharp: bool
    use_image_boundary_trimming: bool
    use_back_face_culling: bool
    shadow_camera_near: float
    shadow_camera_far: float
    shadow_camera_size: float
    use_invert_collection: bool
    use_invert_silhouette: bool