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
from .Attribute import Attribute
from .CurvePoint import CurvePoint
from .CurveSlice import CurveSlice
from .FloatVectorAttributeValue import FloatVectorAttributeValue
from .FloatVectorValueReadOnly import FloatVectorValueReadOnly
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .IntAttributeValue import IntAttributeValue
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Material import Material
from .Object import Object
class Curves(ID):
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
    curves: bpy_prop_collection['CurveSlice']
    points: bpy_prop_collection['CurvePoint']
    position_data: bpy_prop_collection['FloatVectorAttributeValue']
    curve_offset_data: bpy_prop_collection['IntAttributeValue']
    normals: bpy_prop_collection['FloatVectorValueReadOnly']
    materials: bpy_prop_collection['Material']
    surface: 'Object'
    surface_uv_map: str
    use_mirror_x: bool
    use_mirror_y: bool
    use_mirror_z: bool
    selection_domain: str
    use_sculpt_collision: bool
    surface_collision_distance: float
    attributes: bpy_prop_collection['Attribute']
    color_attributes: bpy_prop_collection['Attribute']
    animation_data: 'AnimData'
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
    def add_curves(self, *args, **kwargs) -> Any: ...
    def remove_curves(self, *args, **kwargs) -> Any: ...
    def resize_curves(self, *args, **kwargs) -> Any: ...
    def reorder_curves(self, *args, **kwargs) -> Any: ...
    def set_types(self, *args, **kwargs) -> Any: ...
    def unit_test_compare(self, *args, **kwargs) -> Any: ...