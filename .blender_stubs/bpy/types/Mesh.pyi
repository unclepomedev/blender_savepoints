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

    name: Annotated[str, "is_animatable=False"]
    """Unique data-block ID name (within a same type and library)"""
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
    use_fake_user: bool
    """Save this data-block even if it has no users"""
    use_extra_user: bool
    """Indicates whether an extra user is set or not (mainly for internal/debug usages)"""
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
    is_runtime_data: bool
    """This data-block is runtime data, i.e. it won't be saved in .blend file. Note that e.g. evaluated IDs are always runtime, so this value is only editable for data-blocks in Main data-base."""
    @property
    def is_editable(self) -> bool:
        """This data-block is editable in the user interface. Linked data-blocks are not editable, except if they were loaded as editable assets."""
        ...
    tag: bool
    """Tools can use this to tag data for their own purposes (initial state is undefined)"""
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
    asset_data: Annotated[Optional['AssetMetaData'], "is_animatable=False"]
    """Additional data for an asset data-block"""
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
    texture_mesh: Annotated[Optional['Mesh'], "is_animatable=False"]
    """Use another mesh for texture indices (vertex indices must be aligned)"""
    @property
    def uv_layers(self) -> Annotated['UVLoopLayers', "is_animatable=False"]:
        """All UV loop layers"""
        ...
    uv_layer_clone: Annotated[Optional['MeshUVLoopLayer'], "is_animatable=False"]
    """UV loop layer to be used as cloning source"""
    uv_layer_clone_index: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Clone UV loop layer index"""
    uv_layer_stencil: Annotated[Optional['MeshUVLoopLayer'], "is_animatable=False"]
    """UV loop layer to mask the painted area"""
    uv_layer_stencil_index: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Mask UV loop layer index"""
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
    remesh_voxel_size: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=4", "is_animatable=False"]
    """Size of the voxel in object space used for volume evaluation. Lower values preserve finer details."""
    remesh_voxel_adaptivity: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=4", "is_animatable=False"]
    """Reduces the final face count by simplifying geometry where detail is not needed, generating triangles. A value greater than 0 disables Fix Poles."""
    use_remesh_fix_poles: Annotated[bool, "is_animatable=False"]
    """Produces fewer poles and a better topology flow"""
    use_remesh_preserve_volume: Annotated[bool, "is_animatable=False"]
    """Projects the mesh to preserve the volume and details of the original mesh"""
    use_remesh_preserve_attributes: Annotated[bool, "is_animatable=False"]
    """Transfer all attributes to the new mesh"""
    remesh_mode: Annotated[Literal['VOXEL', 'QUAD'], "is_animatable=False"]

    use_mirror_x: Annotated[bool, "is_animatable=False"]
    """Enable symmetry in the X axis"""
    use_mirror_y: Annotated[bool, "is_animatable=False"]
    """Enable symmetry in the Y axis"""
    use_mirror_z: Annotated[bool, "is_animatable=False"]
    """Enable symmetry in the Z axis"""
    use_mirror_vertex_groups: Annotated[bool, "is_animatable=False"]
    """Mirror the left/right vertex groups when painting. The symmetry axis is determined by the symmetry settings."""
    radial_symmetry: Annotated[list[int], "subtype='XYZ'", "step=1", "is_animatable=False"]
    """Number of mirrored regions around a central axis"""
    @property
    def has_custom_normals(self) -> bool:
        """True if there is custom normal data for this mesh"""
        ...
    texco_mesh: Annotated[Optional['Mesh'], "is_animatable=False"]
    """Derive texture coordinates from another mesh"""
    @property
    def shape_keys(self) -> Annotated[Optional['Key'], "is_animatable=False"]:

        ...
    use_auto_texspace: bool
    """Adjust active object's texture space automatically when transforming object"""
    use_mirror_topology: Annotated[bool, "is_animatable=False"]
    """Use topology based mirroring (for when both sides of mesh have matching, unique topology)"""
    use_paint_bone_selection: Annotated[bool, "is_animatable=False"]
    """Bone selection during painting"""
    use_paint_mask: Annotated[bool, "is_animatable=False"]
    """Face selection masking for painting"""
    use_paint_mask_vertex: Annotated[bool, "is_animatable=False"]
    """Vertex selection masking for painting"""
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
    auto_texspace: bool
    """Adjust active object's texture space automatically when transforming object"""
    texspace_location: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Texture space location"""
    texspace_size: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Texture space size"""
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