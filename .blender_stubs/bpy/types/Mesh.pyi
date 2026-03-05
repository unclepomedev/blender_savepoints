# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Mesh.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AnimData import AnimData
from .AssetMetaData import AssetMetaData
from .Attribute import Attribute
from .AttributeGroupMesh import AttributeGroupMesh
from .IDMaterials import IDMaterials
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Key import Key
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .LoopColors import LoopColors
from .Material import Material
from .MeshEdge import MeshEdge
from .MeshEdges import MeshEdges
from .MeshLoop import MeshLoop
from .MeshLoopColorLayer import MeshLoopColorLayer
from .MeshLoopTriangle import MeshLoopTriangle
from .MeshLoopTriangles import MeshLoopTriangles
from .MeshLoops import MeshLoops
from .MeshNormalValue import MeshNormalValue
from .MeshPolygon import MeshPolygon
from .MeshPolygons import MeshPolygons
from .MeshSkinVertexLayer import MeshSkinVertexLayer
from .MeshUVLoopLayer import MeshUVLoopLayer
from .MeshVertex import MeshVertex
from .MeshVertices import MeshVertices
from .ReadOnlyInteger import ReadOnlyInteger
from .UVLoopLayers import UVLoopLayers
from .bpy_prop_collection import bpy_prop_collection

class Mesh(ID):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique data-block ID name (within a same type and library)"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def name_full(self) -> Annotated[str, "is_animatable=False"]:
        """Unique data-block ID name, including library one if any"""
        ...
    @property
    def id_type(self) -> Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']:
        """Type identifier of this data-block"""
        ...
    @property
    def session_uid(self) -> Annotated[int, "step=1"]:
        """A session-wide unique identifier for the data block that remains the same across renames and internal reallocations, unchanged when reloading the file"""
        ...
    @property
    def is_evaluated(self) -> bool:
        """Whether this ID is runtime-only, evaluated data-block, or actual data from .blend file"""
        ...
    @property
    def original(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """Actual data-block from .blend file (Main database) that generated that evaluated one"""
        ...
    @property
    def users(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of times this data-block is referenced"""
        ...
    @property
    def use_fake_user(self) -> bool:
        """Save this data-block even if it has no users"""
        ...
    @use_fake_user.setter
    def use_fake_user(self, value: bool) -> None:
        ...
    @property
    def use_extra_user(self) -> bool:
        """Indicates whether an extra user is set or not (mainly for internal/debug usages)"""
        ...
    @use_extra_user.setter
    def use_extra_user(self, value: bool) -> None:
        ...
    @property
    def is_embedded_data(self) -> bool:
        """This data-block is not an independent one, but is actually a sub-data of another ID (typical example: root node trees or master collections)"""
        ...
    @property
    def is_linked_packed(self) -> bool:
        """This data-block is linked and packed into the .blend file"""
        ...
    @property
    def is_missing(self) -> bool:
        """This data-block is a place-holder for missing linked data (i.e. it is [an override of] a linked data that could not be found anymore)"""
        ...
    @property
    def is_runtime_data(self) -> bool:
        """This data-block is runtime data, i.e. it won't be saved in .blend file. Note that e.g. evaluated IDs are always runtime, so this value is only editable for data-blocks in Main data-base."""
        ...
    @is_runtime_data.setter
    def is_runtime_data(self, value: bool) -> None:
        ...
    @property
    def is_editable(self) -> bool:
        """This data-block is editable in the user interface. Linked data-blocks are not editable, except if they were loaded as editable assets."""
        ...
    @property
    def tag(self) -> bool:
        """Tools can use this to tag data for their own purposes (initial state is undefined)"""
        ...
    @tag.setter
    def tag(self, value: bool) -> None:
        ...
    @property
    def is_library_indirect(self) -> bool:
        """Is this ID block linked indirectly"""
        ...
    @property
    def library(self) -> Annotated[Optional['Library'], "is_animatable=False"]:
        """Library file the data-block is linked from"""
        ...
    @property
    def library_weak_reference(self) -> Annotated[Optional['LibraryWeakReference'], "is_animatable=False"]:
        """Weak reference to a data-block in another library .blend file (used to re-use already appended data instead of appending new copies)"""
        ...
    @property
    def asset_data(self) -> Annotated[Optional['AssetMetaData'], "is_animatable=False"]:
        """Additional data for an asset data-block"""
        ...
    @asset_data.setter
    def asset_data(self, value: Annotated[Optional['AssetMetaData'], "is_animatable=False"]) -> None:
        ...
    @property
    def override_library(self) -> Annotated[Optional['IDOverrideLibrary'], "is_animatable=False"]:
        """Library override data"""
        ...
    @property
    def preview(self) -> Annotated[Optional['ImagePreview'], "is_animatable=False"]:
        """Preview image and icon of this data-block (always None if not supported for this type of data)"""
        ...
    @property
    def vertices(self) -> Annotated['MeshVertices', "is_animatable=False"]:
        """Vertices of the mesh"""
        ...
    @property
    def edges(self) -> Annotated['MeshEdges', "is_animatable=False"]:
        """Edges of the mesh"""
        ...
    @property
    def loops(self) -> Annotated['MeshLoops', "is_animatable=False"]:
        """Loops of the mesh (face corners)"""
        ...
    @property
    def polygons(self) -> Annotated['MeshPolygons', "is_animatable=False"]:
        """Polygons of the mesh"""
        ...
    @property
    def normals_domain(self) -> Literal['POINT', 'FACE', 'CORNER']:
        """The attribute domain that gives enough information to represent the mesh's normals"""
        ...
    @property
    def vertex_normals(self) -> Annotated[bpy_prop_collection['MeshNormalValue'], "is_animatable=False"]:
        """The normal direction of each vertex, defined as the average of the surrounding face normals"""
        ...
    @property
    def polygon_normals(self) -> Annotated[bpy_prop_collection['MeshNormalValue'], "is_animatable=False"]:
        """The normal direction of each face, defined by the winding order and position of its vertices"""
        ...
    @property
    def corner_normals(self) -> Annotated[bpy_prop_collection['MeshNormalValue'], "is_animatable=False"]:
        """The "slit" normal direction of each face corner, influenced by vertex normals, sharp faces, sharp edges, and custom normals. May be empty."""
        ...
    @property
    def loop_triangles(self) -> Annotated['MeshLoopTriangles', "is_animatable=False"]:
        """Tessellation of mesh polygons into triangles"""
        ...
    @property
    def loop_triangle_polygons(self) -> Annotated[bpy_prop_collection['ReadOnlyInteger'], "is_animatable=False"]:
        """The face index for each loop triangle"""
        ...
    @property
    def texture_mesh(self) -> Annotated[Optional['Mesh'], "is_animatable=False"]:
        """Use another mesh for texture indices (vertex indices must be aligned)"""
        ...
    @texture_mesh.setter
    def texture_mesh(self, value: Annotated[Optional['Mesh'], "is_animatable=False"]) -> None:
        ...
    @property
    def uv_layers(self) -> Annotated['UVLoopLayers', "is_animatable=False"]:
        """All UV loop layers"""
        ...
    @property
    def uv_layer_clone(self) -> Annotated[Optional['MeshUVLoopLayer'], "is_animatable=False"]:
        """UV loop layer to be used as cloning source"""
        ...
    @uv_layer_clone.setter
    def uv_layer_clone(self, value: Annotated[Optional['MeshUVLoopLayer'], "is_animatable=False"]) -> None:
        ...
    @property
    def uv_layer_clone_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Clone UV loop layer index"""
        ...
    @uv_layer_clone_index.setter
    def uv_layer_clone_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def uv_layer_stencil(self) -> Annotated[Optional['MeshUVLoopLayer'], "is_animatable=False"]:
        """UV loop layer to mask the painted area"""
        ...
    @uv_layer_stencil.setter
    def uv_layer_stencil(self, value: Annotated[Optional['MeshUVLoopLayer'], "is_animatable=False"]) -> None:
        ...
    @property
    def uv_layer_stencil_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Mask UV loop layer index"""
        ...
    @uv_layer_stencil_index.setter
    def uv_layer_stencil_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def vertex_colors(self) -> Annotated['LoopColors', "is_animatable=False"]:
        """Legacy vertex color layers. Deprecated, use color attributes instead."""
        ...
    @property
    def skin_vertices(self) -> Annotated[bpy_prop_collection['MeshSkinVertexLayer'], "is_animatable=False"]:
        """All skin vertices"""
        ...
    @property
    def attributes(self) -> Annotated['AttributeGroupMesh', "is_animatable=False"]:
        """Geometry attributes"""
        ...
    @property
    def color_attributes(self) -> Annotated['AttributeGroupMesh', "is_animatable=False"]:
        """Geometry color attributes"""
        ...
    @property
    def remesh_voxel_size(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=4", "is_animatable=False"]:
        """Size of the voxel in object space used for volume evaluation. Lower values preserve finer details."""
        ...
    @remesh_voxel_size.setter
    def remesh_voxel_size(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=4", "is_animatable=False"]) -> None:
        ...
    @property
    def remesh_voxel_adaptivity(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=4", "is_animatable=False"]:
        """Reduces the final face count by simplifying geometry where detail is not needed, generating triangles. A value greater than 0 disables Fix Poles."""
        ...
    @remesh_voxel_adaptivity.setter
    def remesh_voxel_adaptivity(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=4", "is_animatable=False"]) -> None:
        ...
    @property
    def use_remesh_fix_poles(self) -> Annotated[bool, "is_animatable=False"]:
        """Produces fewer poles and a better topology flow"""
        ...
    @use_remesh_fix_poles.setter
    def use_remesh_fix_poles(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_remesh_preserve_volume(self) -> Annotated[bool, "is_animatable=False"]:
        """Projects the mesh to preserve the volume and details of the original mesh"""
        ...
    @use_remesh_preserve_volume.setter
    def use_remesh_preserve_volume(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_remesh_preserve_attributes(self) -> Annotated[bool, "is_animatable=False"]:
        """Transfer all attributes to the new mesh"""
        ...
    @use_remesh_preserve_attributes.setter
    def use_remesh_preserve_attributes(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def remesh_mode(self) -> Annotated[Literal['VOXEL', 'QUAD'], "is_animatable=False"]:

        ...
    @remesh_mode.setter
    def remesh_mode(self, value: Annotated[Literal['VOXEL', 'QUAD'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_mirror_x(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable symmetry in the X axis"""
        ...
    @use_mirror_x.setter
    def use_mirror_x(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_mirror_y(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable symmetry in the Y axis"""
        ...
    @use_mirror_y.setter
    def use_mirror_y(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_mirror_z(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable symmetry in the Z axis"""
        ...
    @use_mirror_z.setter
    def use_mirror_z(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_mirror_vertex_groups(self) -> Annotated[bool, "is_animatable=False"]:
        """Mirror the left/right vertex groups when painting. The symmetry axis is determined by the symmetry settings."""
        ...
    @use_mirror_vertex_groups.setter
    def use_mirror_vertex_groups(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def radial_symmetry(self) -> Annotated[list[int], "subtype='XYZ'", "step=1", "is_animatable=False"]:
        """Number of mirrored regions around a central axis"""
        ...
    @radial_symmetry.setter
    def radial_symmetry(self, value: Annotated[list[int], "subtype='XYZ'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def has_custom_normals(self) -> bool:
        """True if there is custom normal data for this mesh"""
        ...
    @property
    def texco_mesh(self) -> Annotated[Optional['Mesh'], "is_animatable=False"]:
        """Derive texture coordinates from another mesh"""
        ...
    @texco_mesh.setter
    def texco_mesh(self, value: Annotated[Optional['Mesh'], "is_animatable=False"]) -> None:
        ...
    @property
    def shape_keys(self) -> Annotated[Optional['Key'], "is_animatable=False"]:

        ...
    @property
    def use_auto_texspace(self) -> bool:
        """Adjust active object's texture space automatically when transforming object"""
        ...
    @use_auto_texspace.setter
    def use_auto_texspace(self, value: bool) -> None:
        ...
    @property
    def use_mirror_topology(self) -> Annotated[bool, "is_animatable=False"]:
        """Use topology based mirroring (for when both sides of mesh have matching, unique topology)"""
        ...
    @use_mirror_topology.setter
    def use_mirror_topology(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_paint_bone_selection(self) -> Annotated[bool, "is_animatable=False"]:
        """Bone selection during painting"""
        ...
    @use_paint_bone_selection.setter
    def use_paint_bone_selection(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_paint_mask(self) -> Annotated[bool, "is_animatable=False"]:
        """Face selection masking for painting"""
        ...
    @use_paint_mask.setter
    def use_paint_mask(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_paint_mask_vertex(self) -> Annotated[bool, "is_animatable=False"]:
        """Vertex selection masking for painting"""
        ...
    @use_paint_mask_vertex.setter
    def use_paint_mask_vertex(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def total_vert_sel(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Selected vertex count in editmode"""
        ...
    @property
    def total_edge_sel(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Selected edge count in editmode"""
        ...
    @property
    def total_face_sel(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Selected face count in editmode"""
        ...
    @property
    def is_editmode(self) -> bool:
        """True when used in editmode"""
        ...
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def auto_texspace(self) -> bool:
        """Adjust active object's texture space automatically when transforming object"""
        ...
    @auto_texspace.setter
    def auto_texspace(self, value: bool) -> None:
        ...
    @property
    def texspace_location(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Texture space location"""
        ...
    @texspace_location.setter
    def texspace_location(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def texspace_size(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Texture space size"""
        ...
    @texspace_size.setter
    def texspace_size(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def materials(self) -> Annotated['IDMaterials', "is_animatable=False"]:

        ...
    @property
    def cycles(self) -> Annotated[Optional['CyclesMeshSettings'], "is_animatable=False"]:
        """Cycles mesh settings"""
        ...
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