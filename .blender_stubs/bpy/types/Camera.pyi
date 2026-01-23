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
from .AssetMetaData import AssetMetaData
from .CameraBackgroundImage import CameraBackgroundImage
from .CameraDOFSettings import CameraDOFSettings
from .CameraStereoData import CameraStereoData
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Text import Text
class Camera(ID):
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
    type: str
    sensor_fit: str
    passepartout_alpha: float
    angle_x: float
    angle_y: float
    angle: float
    clip_start: float
    clip_end: float
    lens: float
    sensor_width: float
    sensor_height: float
    ortho_scale: float
    display_size: float
    shift_x: float
    shift_y: float
    stereo: 'CameraStereoData'
    show_limits: bool
    show_mist: bool
    show_passepartout: bool
    show_safe_areas: bool
    show_safe_center: bool
    show_name: bool
    show_sensor: bool
    show_background_images: bool
    lens_unit: str
    composition_guide_color: float
    show_composition_center: bool
    show_composition_center_diagonal: bool
    show_composition_thirds: bool
    show_composition_golden: bool
    show_composition_golden_tria_a: bool
    show_composition_golden_tria_b: bool
    show_composition_harmony_tri_a: bool
    show_composition_harmony_tri_b: bool
    panorama_type: str
    fisheye_fov: float
    fisheye_lens: float
    latitude_min: float
    latitude_max: float
    longitude_min: float
    longitude_max: float
    fisheye_polynomial_k0: float
    fisheye_polynomial_k1: float
    fisheye_polynomial_k2: float
    fisheye_polynomial_k3: float
    fisheye_polynomial_k4: float
    central_cylindrical_range_u_min: float
    central_cylindrical_range_u_max: float
    central_cylindrical_range_v_min: float
    central_cylindrical_range_v_max: float
    central_cylindrical_radius: float
    custom_filepath: str
    custom_shader: 'Text'
    custom_mode: str
    custom_bytecode: str
    custom_bytecode_hash: str
    dof: 'CameraDOFSettings'
    background_images: bpy_prop_collection['CameraBackgroundImage']
    animation_data: 'AnimData'
    cycles_custom: 'CyclesCustomCameraSettings'
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
    def view_frame(self, *args, **kwargs) -> Any: ...