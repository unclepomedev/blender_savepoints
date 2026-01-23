# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Curve import Curve
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .CurveProfile import CurveProfile
from .ID import ID
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Key import Key
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Material import Material
from .Object import Object
from .Spline import Spline
class SurfaceCurve(Curve):
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
    shape_keys: 'Key'
    splines: bpy_prop_collection['Spline']
    path_duration: int
    use_path: bool
    use_path_follow: bool
    use_path_clamp: bool
    use_stretch: bool
    use_deform_bounds: bool
    use_radius: bool
    bevel_mode: str
    bevel_profile: 'CurveProfile'
    bevel_resolution: int
    offset: float
    extrude: float
    bevel_depth: float
    resolution_u: int
    resolution_v: int
    render_resolution_u: int
    render_resolution_v: int
    eval_time: float
    bevel_object: 'Object'
    taper_object: 'Object'
    dimensions: str
    fill_mode: str
    twist_mode: str
    taper_radius_mode: str
    bevel_factor_mapping_start: str
    bevel_factor_mapping_end: str
    twist_smooth: float
    use_fill_caps: bool
    use_map_taper: bool
    use_auto_texspace: bool
    texspace_location: float
    texspace_size: float
    materials: bpy_prop_collection['Material']
    bevel_factor_start: float
    bevel_factor_end: float
    is_editmode: bool
    animation_data: 'AnimData'
    cycles: 'CyclesMeshSettings'
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
    def transform(self, *args, **kwargs) -> Any: ...
    def validate_material_indices(self, *args, **kwargs) -> Any: ...
    def update_gpu_tag(self, *args, **kwargs) -> Any: ...