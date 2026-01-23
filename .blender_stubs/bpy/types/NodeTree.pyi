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
from .Annotation import Annotation
from .AssetMetaData import AssetMetaData
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Node import Node
from .NodeLink import NodeLink
from .NodeTreeInterface import NodeTreeInterface
class NodeTree(ID):
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
    color_tag: str
    default_group_node_width: int
    view_center: list[float]
    description: str
    animation_data: 'AnimData'
    nodes: bpy_prop_collection['Node']
    links: bpy_prop_collection['NodeLink']
    annotation: 'Annotation'
    type: str
    interface: 'NodeTreeInterface'
    bl_idname: str
    bl_label: str
    bl_description: str
    bl_icon: str
    bl_use_group_interface: bool
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
    def interface_update(self, *args, **kwargs) -> Any: ...
    def contains_tree(self, *args, **kwargs) -> Any: ...
    def poll(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def get_from_context(self, *args, **kwargs) -> Any: ...
    def valid_socket_type(self, *args, **kwargs) -> Any: ...
    def debug_lazy_function_graph(self, *args, **kwargs) -> Any: ...