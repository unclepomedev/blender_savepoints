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
from .Attribute import Attribute
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Key import Key
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Material import Material
from .MeshEdge import MeshEdge
from .MeshLoop import MeshLoop
from .MeshLoopColorLayer import MeshLoopColorLayer
from .MeshLoopTriangle import MeshLoopTriangle
from .MeshNormalValue import MeshNormalValue
from .MeshPolygon import MeshPolygon
from .MeshSkinVertexLayer import MeshSkinVertexLayer
from .MeshUVLoopLayer import MeshUVLoopLayer
from .MeshVertex import MeshVertex
from .ReadOnlyInteger import ReadOnlyInteger
class Mesh(ID):
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
    vertices: bpy_prop_collection['MeshVertex']
    edges: bpy_prop_collection['MeshEdge']
    loops: bpy_prop_collection['MeshLoop']
    polygons: bpy_prop_collection['MeshPolygon']
    normals_domain: str
    vertex_normals: bpy_prop_collection['MeshNormalValue']
    polygon_normals: bpy_prop_collection['MeshNormalValue']
    corner_normals: bpy_prop_collection['MeshNormalValue']
    loop_triangles: bpy_prop_collection['MeshLoopTriangle']
    loop_triangle_polygons: bpy_prop_collection['ReadOnlyInteger']
    texture_mesh: 'Mesh'
    uv_layers: bpy_prop_collection['MeshUVLoopLayer']
    uv_layer_clone: 'MeshUVLoopLayer'
    uv_layer_clone_index: int
    uv_layer_stencil: 'MeshUVLoopLayer'
    uv_layer_stencil_index: int
    vertex_colors: bpy_prop_collection['MeshLoopColorLayer']
    skin_vertices: bpy_prop_collection['MeshSkinVertexLayer']
    attributes: bpy_prop_collection['Attribute']
    color_attributes: bpy_prop_collection['Attribute']
    remesh_voxel_size: float
    remesh_voxel_adaptivity: float
    use_remesh_fix_poles: bool
    use_remesh_preserve_volume: bool
    use_remesh_preserve_attributes: bool
    remesh_mode: str
    use_mirror_x: bool
    use_mirror_y: bool
    use_mirror_z: bool
    use_mirror_vertex_groups: bool
    radial_symmetry: int
    has_custom_normals: bool
    texco_mesh: 'Mesh'
    shape_keys: 'Key'
    use_auto_texspace: bool
    use_mirror_topology: bool
    use_paint_bone_selection: bool
    use_paint_mask: bool
    use_paint_mask_vertex: bool
    total_vert_sel: int
    total_edge_sel: int
    total_face_sel: int
    is_editmode: bool
    animation_data: 'AnimData'
    auto_texspace: bool
    texspace_location: float
    texspace_size: float
    materials: bpy_prop_collection['Material']
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
    def flip_normals(self, *args, **kwargs) -> Any: ...
    def set_sharp_from_angle(self, *args, **kwargs) -> Any: ...
    def split_faces(self, *args, **kwargs) -> Any: ...
    def calc_tangents(self, *args, **kwargs) -> Any: ...
    def free_tangents(self, *args, **kwargs) -> Any: ...
    def calc_loop_triangles(self, *args, **kwargs) -> Any: ...
    def calc_smooth_groups(self, *args, **kwargs) -> Any: ...
    def normals_split_custom_set(self, *args, **kwargs) -> Any: ...
    def normals_split_custom_set_from_vertices(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def update_gpu_tag(self, *args, **kwargs) -> Any: ...
    def unit_test_compare(self, *args, **kwargs) -> Any: ...
    def clear_geometry(self, *args, **kwargs) -> Any: ...
    def validate(self, *args, **kwargs) -> Any: ...
    def validate_material_indices(self, *args, **kwargs) -> Any: ...
    def count_selected_items(self, *args, **kwargs) -> Any: ...