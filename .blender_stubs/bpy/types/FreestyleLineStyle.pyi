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
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .LineStyleAlphaModifier import LineStyleAlphaModifier
from .LineStyleColorModifier import LineStyleColorModifier
from .LineStyleGeometryModifier import LineStyleGeometryModifier
from .LineStyleTextureSlot import LineStyleTextureSlot
from .LineStyleThicknessModifier import LineStyleThicknessModifier
from .NodeTree import NodeTree
from .Texture import Texture
class FreestyleLineStyle(ID):
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
    texture_slots: bpy_prop_collection['LineStyleTextureSlot']
    active_texture: 'Texture'
    active_texture_index: int
    panel: str
    color: list[float]
    alpha: float
    thickness: float
    thickness_position: str
    thickness_ratio: float
    color_modifiers: bpy_prop_collection['LineStyleColorModifier']
    alpha_modifiers: bpy_prop_collection['LineStyleAlphaModifier']
    thickness_modifiers: bpy_prop_collection['LineStyleThicknessModifier']
    geometry_modifiers: bpy_prop_collection['LineStyleGeometryModifier']
    use_chaining: bool
    chaining: str
    rounds: int
    use_same_object: bool
    use_split_length: bool
    split_length: float
    use_angle_min: bool
    angle_min: float
    use_angle_max: bool
    angle_max: float
    use_length_min: bool
    length_min: float
    use_length_max: bool
    length_max: float
    use_chain_count: bool
    chain_count: int
    use_split_pattern: bool
    split_dash1: int
    split_gap1: int
    split_dash2: int
    split_gap2: int
    split_dash3: int
    split_gap3: int
    material_boundary: bool
    use_sorting: bool
    sort_key: str
    sort_order: str
    integration_type: str
    use_dashed_line: bool
    caps: str
    dash1: int
    gap1: int
    dash2: int
    gap2: int
    dash3: int
    gap3: int
    use_texture: bool
    texture_spacing: float
    animation_data: 'AnimData'
    node_tree: 'NodeTree'
    use_nodes: bool
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