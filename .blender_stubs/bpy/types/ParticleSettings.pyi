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
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .BoidSettings import BoidSettings
from .Collection import Collection
from .CurveMapping import CurveMapping
from .EffectorWeights import EffectorWeights
from .FieldSettings import FieldSettings
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Object import Object
from .ParticleDupliWeight import ParticleDupliWeight
from .ParticleSettingsTextureSlot import ParticleSettingsTextureSlot
from .SPHFluidSettings import SPHFluidSettings
from .Texture import Texture
class ParticleSettings(ID):
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
    texture_slots: bpy_prop_collection['ParticleSettingsTextureSlot']
    active_texture: 'Texture'
    active_texture_index: int
    is_fluid: bool
    use_react_start_end: bool
    use_react_multiple: bool
    use_regrow_hair: bool
    show_unborn: bool
    use_dead: bool
    use_emit_random: bool
    use_even_distribution: bool
    use_die_on_collision: bool
    use_size_deflect: bool
    use_rotations: bool
    use_dynamic_rotation: bool
    use_multiply_size_mass: bool
    use_advanced_hair: bool
    lock_boids_to_surface: bool
    use_hair_bspline: bool
    invert_grid: bool
    hexagonal_grid: bool
    apply_effector_to_children: bool
    create_long_hair_children: bool
    apply_guide_to_children: bool
    use_self_effect: bool
    type: str
    emit_from: str
    distribution: str
    physics_type: str
    rotation_mode: str
    angular_velocity_mode: str
    react_event: str
    show_guide_hairs: bool
    show_hair_grid: bool
    show_velocity: bool
    show_size: bool
    show_health: bool
    use_absolute_path_time: bool
    use_parent_particles: bool
    show_number: bool
    use_collection_pick_random: bool
    use_collection_count: bool
    use_global_instance: bool
    use_rotation_instance: bool
    use_scale_instance: bool
    use_render_adaptive: bool
    use_velocity_length: bool
    use_whole_collection: bool
    use_strand_primitive: bool
    display_method: str
    render_type: str
    display_color: str
    display_size: float
    child_type: str
    display_step: int
    render_step: int
    hair_step: int
    bending_random: float
    keys_step: int
    adaptive_angle: int
    adaptive_pixel: int
    display_percentage: int
    material: int
    material_slot: str
    integrator: str
    kink: str
    kink_axis: str
    color_maximum: float
    frame_start: float
    frame_end: float
    lifetime: float
    lifetime_random: float
    time_tweak: float
    timestep: float
    use_adaptive_subframes: bool
    subframes: int
    courant_target: float
    jitter_factor: float
    effect_hair: float
    count: int
    userjit: int
    grid_resolution: int
    grid_random: float
    effector_amount: int
    normal_factor: float
    object_factor: float
    factor_random: float
    particle_factor: float
    tangent_factor: float
    tangent_phase: float
    reactor_factor: float
    object_align_factor: float
    angular_velocity_factor: float
    phase_factor: float
    rotation_factor_random: float
    phase_factor_random: float
    hair_length: float
    mass: float
    particle_size: float
    size_random: float
    collision_collection: 'Collection'
    drag_factor: float
    brownian_factor: float
    damping: float
    length_random: float
    child_percent: int
    rendered_child_count: int
    virtual_parents: float
    child_size: float
    child_size_random: float
    child_radius: float
    child_roundness: float
    clump_factor: float
    clump_shape: float
    use_clump_curve: bool
    clump_curve: 'CurveMapping'
    use_clump_noise: bool
    clump_noise_size: float
    kink_amplitude: float
    kink_amplitude_clump: float
    kink_amplitude_random: float
    kink_frequency: float
    kink_shape: float
    kink_flat: float
    kink_extra_steps: int
    kink_axis_random: float
    roughness_1: float
    roughness_1_size: float
    roughness_2: float
    roughness_2_size: float
    roughness_2_threshold: float
    roughness_endpoint: float
    roughness_end_shape: float
    use_roughness_curve: bool
    roughness_curve: 'CurveMapping'
    child_length: float
    child_length_threshold: float
    child_parting_factor: float
    child_parting_min: float
    child_parting_max: float
    branch_threshold: float
    line_length_tail: float
    line_length_head: float
    path_start: float
    path_end: float
    trail_count: int
    keyed_loops: int
    use_modifier_stack: bool
    instance_collection: 'Collection'
    instance_weights: bpy_prop_collection['ParticleDupliWeight']
    active_instanceweight: 'ParticleDupliWeight'
    active_instanceweight_index: int
    instance_object: 'Object'
    boids: 'BoidSettings'
    fluid: 'SPHFluidSettings'
    effector_weights: 'EffectorWeights'
    animation_data: 'AnimData'
    force_field_1: 'FieldSettings'
    force_field_2: 'FieldSettings'
    twist: float
    use_twist_curve: bool
    twist_curve: 'CurveMapping'
    use_close_tip: bool
    shape: float
    root_radius: float
    tip_radius: float
    radius_scale: float
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