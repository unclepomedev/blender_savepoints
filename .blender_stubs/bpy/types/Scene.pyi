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
from .Annotation import Annotation
from .AssetMetaData import AssetMetaData
from .Collection import Collection
from .ColorManagedDisplaySettings import ColorManagedDisplaySettings
from .ColorManagedSequencerColorspaceSettings import ColorManagedSequencerColorspaceSettings
from .ColorManagedViewSettings import ColorManagedViewSettings
from .DisplaySafeAreas import DisplaySafeAreas
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .KeyingSet import KeyingSet
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .MovieClip import MovieClip
from .NodeTree import NodeTree
from .Object import Object
from .RenderSettings import RenderSettings
from .RigidBodyWorld import RigidBodyWorld
from .SceneDisplay import SceneDisplay
from .SceneEEVEE import SceneEEVEE
from .SceneGpencil import SceneGpencil
from .SceneHydra import SceneHydra
from .SequenceEditor import SequenceEditor
from .TimelineMarker import TimelineMarker
from .ToolSettings import ToolSettings
from .TransformOrientationSlot import TransformOrientationSlot
from .UnitSettings import UnitSettings
from .View3DCursor import View3DCursor
from .ViewLayer import ViewLayer
from .World import World
class Scene(ID):
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
    camera: 'Object'
    background_set: 'Scene'
    world: 'World'
    objects: bpy_prop_collection['Object']
    frame_current: int
    frame_subframe: float
    frame_float: float
    frame_start: int
    frame_end: int
    frame_step: int
    time_jump_unit: str
    time_jump_delta: float
    frame_current_final: float
    lock_frame_selection_to_range: bool
    use_preview_range: bool
    frame_preview_start: int
    frame_preview_end: int
    show_subframe: bool
    show_keys_from_selected_only: bool
    use_stamp_note: str
    animation_data: 'AnimData'
    is_nla_tweakmode: bool
    use_custom_simulation_range: bool
    simulation_frame_start: int
    simulation_frame_end: int
    sync_mode: str
    compositing_node_group: 'NodeTree'
    use_nodes: bool
    sequence_editor: 'SequenceEditor'
    keying_sets: bpy_prop_collection['KeyingSet']
    keying_sets_all: bpy_prop_collection['KeyingSet']
    rigidbody_world: 'RigidBodyWorld'
    tool_settings: 'ToolSettings'
    unit_settings: 'UnitSettings'
    gravity: float
    use_gravity: bool
    render: 'RenderSettings'
    safe_areas: 'DisplaySafeAreas'
    timeline_markers: bpy_prop_collection['TimelineMarker']
    transform_orientation_slots: bpy_prop_collection['TransformOrientationSlot']
    cursor: 'View3DCursor'
    use_audio: bool
    use_audio_scrub: bool
    audio_doppler_speed: float
    audio_doppler_factor: float
    audio_distance_model: str
    audio_volume: float
    annotation: 'Annotation'
    active_clip: 'MovieClip'
    view_settings: 'ColorManagedViewSettings'
    display_settings: 'ColorManagedDisplaySettings'
    sequencer_colorspace_settings: 'ColorManagedSequencerColorspaceSettings'
    view_layers: bpy_prop_collection['ViewLayer']
    collection: 'Collection'
    display: 'SceneDisplay'
    eevee: 'SceneEEVEE'
    grease_pencil_settings: 'SceneGpencil'
    hydra: 'SceneHydra'
    cycles: 'CyclesRenderSettings'
    cycles_curves: 'CyclesCurveRenderSettings'
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
    def update_render_engine(self, *args, **kwargs) -> Any: ...
    def statistics(self, *args, **kwargs) -> Any: ...
    def frame_set(self, *args, **kwargs) -> Any: ...
    def uvedit_aspect(self, *args, **kwargs) -> Any: ...
    def ray_cast(self, *args, **kwargs) -> Any: ...
    def sequence_editor_create(self, *args, **kwargs) -> Any: ...
    def sequence_editor_clear(self, *args, **kwargs) -> Any: ...