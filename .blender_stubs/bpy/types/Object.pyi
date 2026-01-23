# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .ID import ID
from .AnimData import AnimData
from .AnimViz import AnimViz
from .AssetMetaData import AssetMetaData
from .Collection import Collection
from .CollisionSettings import CollisionSettings
from .Constraint import Constraint
from .FieldSettings import FieldSettings
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .ImageUser import ImageUser
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Material import Material
from .MaterialSlot import MaterialSlot
from .Modifier import Modifier
from .MotionPath import MotionPath
from .ObjectDisplay import ObjectDisplay
from .ObjectLightLinking import ObjectLightLinking
from .ObjectLineArt import ObjectLineArt
from .ParticleSystem import ParticleSystem
from .Pose import Pose
from .RigidBodyConstraint import RigidBodyConstraint
from .RigidBodyObject import RigidBodyObject
from .ShaderFx import ShaderFx
from .ShapeKey import ShapeKey
from .SoftBodySettings import SoftBodySettings
from .VertexGroup import VertexGroup
class Object(ID):
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
    data: 'ID'
    type: str
    mode: str
    bound_box: float
    parent: 'Object'
    parent_type: str
    parent_vertices: int
    parent_bone: str
    use_parent_final_indices: bool
    use_camera_lock_parent: bool
    track_axis: str
    up_axis: str
    material_slots: bpy_prop_collection['MaterialSlot']
    active_material: 'Material'
    active_material_index: int
    location: float
    rotation_quaternion: float
    rotation_axis_angle: float
    rotation_euler: float
    rotation_mode: str
    scale: float
    dimensions: float
    delta_location: float
    delta_rotation_euler: float
    delta_rotation_quaternion: float
    delta_scale: float
    lock_location: bool
    lock_rotation: bool
    lock_rotation_w: bool
    lock_rotations_4d: bool
    lock_scale: bool
    matrix_world: float
    matrix_local: float
    matrix_basis: float
    matrix_parent_inverse: float
    modifiers: bpy_prop_collection['Modifier']
    shader_effects: bpy_prop_collection['ShaderFx']
    constraints: bpy_prop_collection['Constraint']
    vertex_groups: bpy_prop_collection['VertexGroup']
    empty_display_type: str
    empty_display_size: float
    empty_image_offset: float
    image_user: 'ImageUser'
    empty_image_depth: str
    show_empty_image_perspective: bool
    show_empty_image_orthographic: bool
    show_empty_image_only_axis_aligned: bool
    use_empty_image_alpha: bool
    empty_image_side: str
    add_rest_position_attribute: bool
    pass_index: int
    color: float
    field: 'FieldSettings'
    collision: 'CollisionSettings'
    soft_body: 'SoftBodySettings'
    particle_systems: bpy_prop_collection['ParticleSystem']
    rigid_body: 'RigidBodyObject'
    rigid_body_constraint: 'RigidBodyConstraint'
    use_simulation_cache: bool
    hide_viewport: bool
    hide_select: bool
    hide_render: bool
    hide_probe_volume: bool
    hide_probe_sphere: bool
    hide_probe_plane: bool
    hide_surface_pick: bool
    show_instancer_for_render: bool
    show_instancer_for_viewport: bool
    visible_camera: bool
    visible_diffuse: bool
    visible_glossy: bool
    visible_transmission: bool
    visible_volume_scatter: bool
    visible_shadow: bool
    is_holdout: bool
    is_shadow_catcher: bool
    instance_type: str
    use_instance_vertices_rotation: bool
    use_instance_faces_scale: bool
    instance_faces_scale: float
    instance_collection: 'Collection'
    is_instancer: bool
    display_type: str
    show_bounds: bool
    display_bounds_type: str
    show_name: bool
    show_axis: bool
    show_texture_space: bool
    show_wire: bool
    show_all_edges: bool
    use_grease_pencil_lights: bool
    show_transparent: bool
    show_in_front: bool
    pose: 'Pose'
    show_only_shape_key: bool
    use_shape_key_edit_mode: bool
    active_shape_key: 'ShapeKey'
    active_shape_key_index: int
    use_dynamic_topology_sculpting: bool
    is_from_instancer: bool
    is_from_set: bool
    display: 'ObjectDisplay'
    lineart: 'ObjectLineArt'
    use_mesh_mirror_x: bool
    use_mesh_mirror_y: bool
    use_mesh_mirror_z: bool
    lightgroup: str
    light_linking: 'ObjectLightLinking'
    shadow_terminator_normal_offset: float
    shadow_terminator_geometry_offset: float
    shadow_terminator_shading_offset: float
    animation_data: 'AnimData'
    animation_visualization: 'AnimViz'
    motion_path: 'MotionPath'
    selection_sets: bpy_prop_collection['SelectionSet']
    active_selection_set: int
    cycles: 'CyclesObjectSettings'
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
    def select_get(self, *args, **kwargs) -> Any: ...
    def select_set(self, *args, **kwargs) -> Any: ...
    def hide_get(self, *args, **kwargs) -> Any: ...
    def hide_set(self, *args, **kwargs) -> Any: ...
    def visible_get(self, *args, **kwargs) -> Any: ...
    def holdout_get(self, *args, **kwargs) -> Any: ...
    def indirect_only_get(self, *args, **kwargs) -> Any: ...
    def local_view_get(self, *args, **kwargs) -> Any: ...
    def local_view_set(self, *args, **kwargs) -> Any: ...
    def visible_in_viewport_get(self, *args, **kwargs) -> Any: ...
    def convert_space(self, *args, **kwargs) -> Any: ...
    def calc_matrix_camera(self, *args, **kwargs) -> Any: ...
    def camera_fit_coords(self, *args, **kwargs) -> Any: ...
    def crazyspace_eval(self, *args, **kwargs) -> Any: ...
    def crazyspace_displacement_to_deformed(self, *args, **kwargs) -> Any: ...
    def crazyspace_displacement_to_original(self, *args, **kwargs) -> Any: ...
    def crazyspace_eval_clear(self, *args, **kwargs) -> Any: ...
    def to_mesh(self, *args, **kwargs) -> Any: ...
    def to_mesh_clear(self, *args, **kwargs) -> Any: ...
    def to_curve(self, *args, **kwargs) -> Any: ...
    def to_curve_clear(self, *args, **kwargs) -> Any: ...
    def find_armature(self, *args, **kwargs) -> Any: ...
    def shape_key_add(self, *args, **kwargs) -> Any: ...
    def shape_key_remove(self, *args, **kwargs) -> Any: ...
    def shape_key_clear(self, *args, **kwargs) -> Any: ...
    def ray_cast(self, *args, **kwargs) -> Any: ...
    def closest_point_on_mesh(self, *args, **kwargs) -> Any: ...
    def is_modified(self, *args, **kwargs) -> Any: ...
    def is_deform_modified(self, *args, **kwargs) -> Any: ...
    def update_from_editmode(self, *args, **kwargs) -> Any: ...
    def cache_release(self, *args, **kwargs) -> Any: ...
    # --- Injected Methods ---
    def select_set(self, state: bool) -> None: ...
    def select_get(self) -> bool: ...
    def hide_set(self, state: bool) -> None: ...
    def hide_get(self) -> bool: ...
    def hide_viewport_set(self, state: bool) -> None: ...
    def hide_render_set(self, state: bool) -> None: ...
    def temp_override(self, window=None, area=None, region=None, **kwargs) -> Any: ...