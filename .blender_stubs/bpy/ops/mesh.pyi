# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def attribute_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value_float: float = ..., value_float_vector_2d: list[float] = ..., value_float_vector_3d: list[float] = ..., value_int: int = ..., value_int_vector_2d: list[int] = ..., value_color: list[float] = ..., value_bool: bool = ...) -> set[str]:
    """Set values of the active attribute for selected elements"""
    ...

def average_normals(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, average_type: str = ..., weight: int = ..., threshold: float = ...) -> set[str]:
    """Average custom normals of selected vertices"""
    ...

def beautify_fill(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, angle_limit: float = ...) -> set[str]:
    """Rearrange some faces to try to get less degenerated geometry"""
    ...

def bevel(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, offset_type: str = ..., offset: float = ..., profile_type: str = ..., offset_pct: float = ..., segments: int = ..., profile: float = ..., affect: str = ..., clamp_overlap: bool = ..., loop_slide: bool = ..., mark_seam: bool = ..., mark_sharp: bool = ..., material: int = ..., harden_normals: bool = ..., face_strength_mode: str = ..., miter_outer: str = ..., miter_inner: str = ..., spread: float = ..., vmesh_method: str = ..., release_confirm: bool = ...) -> set[str]:
    """Cut into selected items at an angle to create bevel or chamfer"""
    ...

def bisect(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, plane_co: list[float] = ..., plane_no: list[float] = ..., use_fill: bool = ..., clear_inner: bool = ..., clear_outer: bool = ..., threshold: float = ..., xstart: int = ..., xend: int = ..., ystart: int = ..., yend: int = ..., flip: bool = ..., cursor: int = ...) -> set[str]:
    """Cut geometry along a plane (click-drag to define plane)"""
    ...

def blend_from_shape(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, shape: str = ..., blend: float = ..., add: bool = ...) -> set[str]:
    """Blend in shape from a shape key"""
    ...

def bridge_edge_loops(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., use_merge: bool = ..., merge_factor: float = ..., twist_offset: int = ..., number_cuts: int = ..., interpolation: str = ..., smoothness: float = ..., profile_shape_factor: float = ..., profile_shape: str = ...) -> set[str]:
    """Create a bridge of faces between two or more selected edge loops"""
    ...

def colors_reverse(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Flip direction of face corner color attribute inside faces"""
    ...

def colors_rotate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_ccw: bool = ...) -> set[str]:
    """Rotate face corner color attribute inside faces"""
    ...

def convex_hull(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, delete_unused: bool = ..., use_existing_faces: bool = ..., make_holes: bool = ..., join_triangles: bool = ..., face_threshold: float = ..., shape_threshold: float = ..., topology_influence: float = ..., uvs: bool = ..., vcols: bool = ..., seam: bool = ..., sharp: bool = ..., materials: bool = ..., deselect_joined: bool = ...) -> set[str]:
    """Enclose selected vertices in a convex polyhedron"""
    ...

def customdata_custom_splitnormals_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add a custom normals layer, if none exists yet"""
    ...

def customdata_custom_splitnormals_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove the custom normals layer, if it exists"""
    ...

def customdata_mask_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear vertex sculpt masking data from the mesh"""
    ...

def customdata_skin_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add a vertex skin layer"""
    ...

def customdata_skin_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear vertex skin layer"""
    ...

def decimate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ratio: float = ..., use_vertex_group: bool = ..., vertex_group_factor: float = ..., invert_vertex_group: bool = ..., use_symmetry: bool = ..., symmetry_axis: str = ...) -> set[str]:
    """Simplify geometry by collapsing edges"""
    ...

def delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Delete selected vertices, edges or faces"""
    ...

def delete_edgeloop(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_face_split: bool = ...) -> set[str]:
    """Delete an edge loop by merging the faces on each side"""
    ...

def delete_loose(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_verts: bool = ..., use_edges: bool = ..., use_faces: bool = ...) -> set[str]:
    """Delete loose vertices, edges or faces"""
    ...

def dissolve_degenerate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, threshold: float = ...) -> set[str]:
    """Dissolve zero area faces and zero length edges"""
    ...

def dissolve_edges(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_verts: bool = ..., angle_threshold: float = ..., use_face_split: bool = ...) -> set[str]:
    """Dissolve edges, merging faces"""
    ...

def dissolve_faces(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_verts: bool = ...) -> set[str]:
    """Dissolve faces"""
    ...

def dissolve_limited(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, angle_limit: float = ..., use_dissolve_boundaries: bool = ..., delimit: set[str] = ...) -> set[str]:
    """Dissolve selected edges and vertices, limited by the angle of surrounding geometry"""
    ...

def dissolve_mode(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_verts: bool = ..., angle_threshold: float = ..., use_face_split: bool = ..., use_boundary_tear: bool = ...) -> set[str]:
    """Dissolve geometry based on the selection mode"""
    ...

def dissolve_verts(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_face_split: bool = ..., use_boundary_tear: bool = ...) -> set[str]:
    """Dissolve vertices, merge edges and faces"""
    ...

def dupli_extrude_cursor(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, rotate_source: bool = ...) -> set[str]:
    """Duplicate and extrude selected vertices, edges or faces towards the mouse cursor"""
    ...

def duplicate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: int = ...) -> set[str]:
    """Duplicate selected vertices, edges or faces"""
    ...

def duplicate_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_duplicate: 'MESH_OT_duplicate' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Duplicate mesh and move"""
    ...

def edge_collapse(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Collapse isolated edge and face regions, merging data such as UVs and color attributes. This can collapse edge-rings as well as regions of connected faces into vertices"""
    ...

def edge_face_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add an edge or face to selected"""
    ...

def edge_rotate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_ccw: bool = ...) -> set[str]:
    """Rotate selected edge or adjoining faces"""
    ...

def edge_split(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Split selected edges so that each neighbor face gets its own copy"""
    ...

def edgering_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., deselect: bool = ..., toggle: bool = ..., ring: bool = ...) -> set[str]:
    """Select an edge ring"""
    ...

def edges_select_sharp(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, sharpness: float = ...) -> set[str]:
    """Select all sharp enough edges"""
    ...

def extrude_context(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_normal_flip: bool = ..., use_dissolve_ortho_edges: bool = ..., mirror: bool = ...) -> set[str]:
    """Extrude selection"""
    ...

def extrude_context_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_extrude_context: 'MESH_OT_extrude_context' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Extrude region together along the average normal"""
    ...

def extrude_edges_indiv(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_normal_flip: bool = ..., mirror: bool = ...) -> set[str]:
    """Extrude individual edges only"""
    ...

def extrude_edges_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_extrude_edges_indiv: 'MESH_OT_extrude_edges_indiv' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Extrude edges and move result"""
    ...

def extrude_faces_indiv(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mirror: bool = ...) -> set[str]:
    """Extrude individual faces only"""
    ...

def extrude_faces_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_extrude_faces_indiv: 'MESH_OT_extrude_faces_indiv' = ..., TRANSFORM_OT_shrink_fatten: 'TRANSFORM_OT_shrink_fatten' = ...) -> set[str]:
    """Extrude each individual face separately along local normals"""
    ...

def extrude_manifold(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_extrude_region: 'MESH_OT_extrude_region' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Extrude, dissolves edges whose faces form a flat surface and intersect new edges"""
    ...

def extrude_region(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_normal_flip: bool = ..., use_dissolve_ortho_edges: bool = ..., mirror: bool = ...) -> set[str]:
    """Extrude region of faces"""
    ...

def extrude_region_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_extrude_region: 'MESH_OT_extrude_region' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Extrude region and move result"""
    ...

def extrude_region_shrink_fatten(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_extrude_region: 'MESH_OT_extrude_region' = ..., TRANSFORM_OT_shrink_fatten: 'TRANSFORM_OT_shrink_fatten' = ...) -> set[str]:
    """Extrude region together along local normals"""
    ...

def extrude_repeat(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, steps: int = ..., offset: list[float] = ..., scale_offset: float = ...) -> set[str]:
    """Extrude selected vertices, edges or faces repeatedly"""
    ...

def extrude_vertices_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_extrude_verts_indiv: 'MESH_OT_extrude_verts_indiv' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Extrude vertices and move result"""
    ...

def extrude_verts_indiv(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mirror: bool = ...) -> set[str]:
    """Extrude individual vertices only"""
    ...

def face_make_planar(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ..., repeat: int = ...) -> set[str]:
    """Flatten selected faces"""
    ...

def face_split_by_edges(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Weld loose edges into faces (splitting them into new faces)"""
    ...

def faces_select_linked_flat(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, sharpness: float = ...) -> set[str]:
    """Select linked faces by angle"""
    ...

def faces_shade_flat(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Display faces flat"""
    ...

def faces_shade_smooth(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Display faces smooth (using vertex normals)"""
    ...

def fill(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_beauty: bool = ...) -> set[str]:
    """Fill a selected edge loop with faces"""
    ...

def fill_grid(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, span: int = ..., offset: int = ..., use_interp_simple: bool = ...) -> set[str]:
    """Fill grid from two loops"""
    ...

def fill_holes(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, sides: int = ...) -> set[str]:
    """Fill in holes (boundary edge loops)"""
    ...

def flip_normals(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, only_clnors: bool = ...) -> set[str]:
    """Flip the direction of selected faces' normals (and of their vertices)"""
    ...

def flip_quad_tessellation(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Flips the tessellation of selected quads"""
    ...

def hide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> set[str]:
    """Hide (un)selected vertices, edges or faces"""
    ...

def inset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_boundary: bool = ..., use_even_offset: bool = ..., use_relative_offset: bool = ..., use_edge_rail: bool = ..., thickness: float = ..., depth: float = ..., use_outset: bool = ..., use_select_inset: bool = ..., use_individual: bool = ..., use_interpolate: bool = ..., release_confirm: bool = ...) -> set[str]:
    """Inset new faces into selected faces"""
    ...

def intersect(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., separate_mode: str = ..., threshold: float = ..., solver: str = ...) -> set[str]:
    """Cut an intersection into faces"""
    ...

def intersect_boolean(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, operation: str = ..., use_swap: bool = ..., use_self: bool = ..., threshold: float = ..., solver: str = ...) -> set[str]:
    """Cut solid geometry from selected to unselected"""
    ...

def knife_project(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, cut_through: bool = ...) -> set[str]:
    """Use other objects outlines and boundaries to project knife cuts"""
    ...

def knife_tool(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_occlude_geometry: bool = ..., only_selected: bool = ..., xray: bool = ..., visible_measurements: str = ..., angle_snapping: str = ..., angle_snapping_increment: float = ..., wait_for_input: bool = ...) -> set[str]:
    """Cut new topology"""
    ...

def loop_multi_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ring: bool = ...) -> set[str]:
    """Select a loop of connected edges by connection type"""
    ...

def loop_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., deselect: bool = ..., toggle: bool = ..., ring: bool = ...) -> set[str]:
    """Select a loop of connected edges"""
    ...

def loop_to_region(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select_bigger: bool = ...) -> set[str]:
    """Select region of faces inside of a selected loop of edges"""
    ...

def loopcut(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, number_cuts: int = ..., smoothness: float = ..., falloff: str = ..., object_index: int = ..., edge_index: int = ..., mesh_select_mode_init: list[bool] = ...) -> set[str]:
    """Add a new loop between existing loops"""
    ...

def loopcut_slide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_loopcut: 'MESH_OT_loopcut' = ..., TRANSFORM_OT_edge_slide: 'TRANSFORM_OT_edge_slide' = ...) -> set[str]:
    """Cut mesh loop and slide it"""
    ...

def mark_freestyle_edge(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, clear: bool = ...) -> set[str]:
    """(Un)mark selected edges as Freestyle feature edges"""
    ...

def mark_freestyle_face(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, clear: bool = ...) -> set[str]:
    """(Un)mark selected faces for exclusion from Freestyle feature edge detection"""
    ...

def mark_seam(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, clear: bool = ...) -> set[str]:
    """(Un)mark selected edges as a seam"""
    ...

def mark_sharp(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, clear: bool = ..., use_verts: bool = ...) -> set[str]:
    """(Un)mark selected edges as sharp"""
    ...

def merge(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., uvs: bool = ...) -> set[str]:
    """Merge selected vertices"""
    ...

def merge_normals(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Merge custom normals of selected vertices"""
    ...

def mod_weighted_strength(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, set: bool = ..., face_strength: str = ...) -> set[str]:
    """Set/Get strength of face (used in Weighted Normal modifier)"""
    ...

def normals_make_consistent(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, inside: bool = ...) -> set[str]:
    """Make face and vertex normals point either outside or inside the mesh"""
    ...

def normals_tools(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., absolute: bool = ...) -> set[str]:
    """Custom normals tools using Normal Vector of UI"""
    ...

def offset_edge_loops(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_cap_endpoint: bool = ...) -> set[str]:
    """Create offset edge loop from the current selection"""
    ...

def offset_edge_loops_slide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_offset_edge_loops: 'MESH_OT_offset_edge_loops' = ..., TRANSFORM_OT_edge_slide: 'TRANSFORM_OT_edge_slide' = ...) -> set[str]:
    """Offset edge loop slide"""
    ...

def point_normals(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., invert: bool = ..., align: bool = ..., target_location: list[float] = ..., spherize: bool = ..., spherize_strength: float = ...) -> set[str]:
    """Point selected custom normals to specified Target"""
    ...

def poke(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, offset: float = ..., use_relative_offset: bool = ..., center_mode: str = ...) -> set[str]:
    """Split a face into a fan"""
    ...

def polybuild_delete_at_cursor(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def polybuild_dissolve_at_cursor(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(undocumented operator)"""
    ...

def polybuild_extrude_at_cursor_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_polybuild_transform_at_cursor: 'MESH_OT_polybuild_transform_at_cursor' = ..., MESH_OT_extrude_edges_indiv: 'MESH_OT_extrude_edges_indiv' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def polybuild_face_at_cursor(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, create_quads: bool = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def polybuild_face_at_cursor_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_polybuild_face_at_cursor: 'MESH_OT_polybuild_face_at_cursor' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def polybuild_split_at_cursor(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def polybuild_split_at_cursor_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_polybuild_split_at_cursor: 'MESH_OT_polybuild_split_at_cursor' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def polybuild_transform_at_cursor(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def polybuild_transform_at_cursor_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_polybuild_transform_at_cursor: 'MESH_OT_polybuild_transform_at_cursor' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def primitive_circle_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, vertices: int = ..., radius: float = ..., fill_type: str = ..., calc_uvs: bool = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a circle mesh"""
    ...

def primitive_cone_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, vertices: int = ..., radius1: float = ..., radius2: float = ..., depth: float = ..., end_fill_type: str = ..., calc_uvs: bool = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a conic mesh"""
    ...

def primitive_cube_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, size: float = ..., calc_uvs: bool = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a cube mesh that consists of six square faces"""
    ...

def primitive_cube_add_gizmo(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, calc_uvs: bool = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ..., matrix: list[float] = ...) -> set[str]:
    """Construct a cube mesh"""
    ...

def primitive_cylinder_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, vertices: int = ..., radius: float = ..., depth: float = ..., end_fill_type: str = ..., calc_uvs: bool = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a cylinder mesh"""
    ...

def primitive_grid_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, x_subdivisions: int = ..., y_subdivisions: int = ..., size: float = ..., calc_uvs: bool = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a subdivided plane mesh"""
    ...

def primitive_ico_sphere_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, subdivisions: int = ..., radius: float = ..., calc_uvs: bool = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a spherical mesh that consists of equally sized triangles"""
    ...

def primitive_monkey_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, size: float = ..., calc_uvs: bool = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a Suzanne mesh"""
    ...

def primitive_plane_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, size: float = ..., calc_uvs: bool = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a filled planar mesh with 4 vertices"""
    ...

def primitive_torus_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, align: str = ..., location: list[float] = ..., rotation: list[float] = ..., major_segments: int = ..., minor_segments: int = ..., mode: str = ..., major_radius: float = ..., minor_radius: float = ..., abso_major_rad: float = ..., abso_minor_rad: float = ..., generate_uvs: bool = ...) -> set[str]:
    """Construct a torus mesh"""
    ...

def primitive_uv_sphere_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, segments: int = ..., ring_count: int = ..., radius: float = ..., calc_uvs: bool = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a spherical mesh with quad faces, except for triangle faces at the top and bottom"""
    ...

def quads_convert_to_tris(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, quad_method: str = ..., ngon_method: str = ...) -> set[str]:
    """Triangulate selected faces"""
    ...

def region_to_loop(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select boundary edges around the selected faces"""
    ...

def remove_doubles(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, threshold: float = ..., use_centroid: bool = ..., use_unselected: bool = ..., use_sharp_edge_from_normals: bool = ...) -> set[str]:
    """Merge vertices based on their proximity"""
    ...

def reorder_vertices_spatial(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reorder mesh faces and vertices based on their spatial position for better BVH building and sculpting performance."""
    ...

def reveal(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ...) -> set[str]:
    """Reveal all hidden vertices, edges and faces"""
    ...

def rip(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., release_confirm: bool = ..., use_accurate: bool = ..., use_fill: bool = ...) -> set[str]:
    """Disconnect vertex or edges from connected geometry"""
    ...

def rip_edge(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Extend vertices along the edge closest to the cursor"""
    ...

def rip_edge_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_rip_edge: 'MESH_OT_rip_edge' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Extend vertices and move the result"""
    ...

def rip_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MESH_OT_rip: 'MESH_OT_rip' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Rip polygons and move the result"""
    ...

def screw(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, steps: int = ..., turns: int = ..., center: list[float] = ..., axis: list[float] = ...) -> set[str]:
    """Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport"""
    ...

def select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """(De)select all vertices, edges or faces"""
    ...

def select_axis(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, orientation: str = ..., sign: str = ..., axis: str = ..., threshold: float = ...) -> set[str]:
    """Select all data in the mesh on a single axis"""
    ...

def select_by_attribute(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select elements based on the active boolean attribute"""
    ...

def select_by_pole_count(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, pole_count: int = ..., type: str = ..., extend: bool = ..., exclude_nonmanifold: bool = ...) -> set[str]:
    """Select vertices at poles by the number of connected edges. In edge and face mode the geometry connected to the vertices is selected"""
    ...

def select_face_by_sides(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, number: int = ..., type: str = ..., extend: bool = ...) -> set[str]:
    """Select vertices or faces by the number of face sides"""
    ...

def select_interior_faces(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select faces where all edges have more than 2 face users"""
    ...

def select_less(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_face_step: bool = ...) -> set[str]:
    """Deselect vertices, edges or faces at the boundary of each selection region"""
    ...

def select_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, delimit: set[str] = ...) -> set[str]:
    """Select all vertices connected to the current selection"""
    ...

def select_linked_pick(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, deselect: bool = ..., delimit: set[str] = ..., object_index: int = ..., index: int = ...) -> set[str]:
    """(De)select all vertices linked to the edge under the mouse cursor"""
    ...

def select_loose(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ...) -> set[str]:
    """Select loose geometry based on the selection mode"""
    ...

def select_mirror(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, axis: set[str] = ..., extend: bool = ...) -> set[str]:
    """Select mesh items at mirrored locations"""
    ...

def select_mode(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_extend: bool = ..., use_expand: bool = ..., type: str = ..., action: str = ...) -> set[str]:
    """Change selection mode"""
    ...

def select_more(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_face_step: bool = ...) -> set[str]:
    """Select more vertices, edges or faces connected to initial selection"""
    ...

def select_next_item(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select the next element (using selection order)"""
    ...

def select_non_manifold(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., use_wire: bool = ..., use_boundary: bool = ..., use_multi_face: bool = ..., use_non_contiguous: bool = ..., use_verts: bool = ...) -> set[str]:
    """Select all non-manifold vertices or edges"""
    ...

def select_nth(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, skip: int = ..., nth: int = ..., offset: int = ...) -> set[str]:
    """Deselect every Nth element starting from the active vertex, edge or face"""
    ...

def select_prev_item(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select the previous element (using selection order)"""
    ...

def select_random(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ratio: float = ..., seed: int = ..., action: str = ...) -> set[str]:
    """Randomly select vertices"""
    ...

def select_similar(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., compare: str = ..., threshold: float = ...) -> set[str]:
    """Select similar vertices, edges or faces by property types"""
    ...

def select_similar_region(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select similar face regions to the current selection"""
    ...

def select_ungrouped(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ...) -> set[str]:
    """Select vertices without a group"""
    ...

def separate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Separate selected geometry into a new mesh"""
    ...

def set_normals_from_faces(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, keep_sharp: bool = ...) -> set[str]:
    """Set the custom normals from the selected faces ones"""
    ...

def set_sharpness_by_angle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, angle: float = ..., extend: bool = ...) -> set[str]:
    """Set edge sharpness based on the angle between neighboring faces"""
    ...

def shape_propagate_to_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Apply selected vertex locations to all other shape keys"""
    ...

def shortest_path_pick(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, edge_mode: str = ..., use_face_step: bool = ..., use_topology_distance: bool = ..., use_fill: bool = ..., skip: int = ..., nth: int = ..., offset: int = ..., index: int = ...) -> set[str]:
    """Select shortest path between two selections"""
    ...

def shortest_path_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, edge_mode: str = ..., use_face_step: bool = ..., use_topology_distance: bool = ..., use_fill: bool = ..., skip: int = ..., nth: int = ..., offset: int = ...) -> set[str]:
    """Selected shortest path between two vertices/edges/faces"""
    ...

def smooth_normals(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ...) -> set[str]:
    """Smooth custom normals based on adjacent vertex normals"""
    ...

def solidify(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, thickness: float = ...) -> set[str]:
    """Create a solid skin by extruding, compensating for sharp angles"""
    ...

def sort_elements(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., elements: set[str] = ..., reverse: bool = ..., seed: int = ...) -> set[str]:
    """The order of selected vertices/edges/faces is modified, based on a given method"""
    ...

def spin(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, steps: int = ..., dupli: bool = ..., angle: float = ..., use_auto_merge: bool = ..., use_normal_flip: bool = ..., center: list[float] = ..., axis: list[float] = ...) -> set[str]:
    """Extrude selected vertices in a circle around the cursor in indicated viewport"""
    ...

def split(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Split off selected geometry from connected unselected geometry"""
    ...

def split_normals(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Split custom normals of selected vertices"""
    ...

def subdivide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, number_cuts: int = ..., smoothness: float = ..., ngon: bool = ..., quadcorner: str = ..., fractal: float = ..., fractal_along_normal: float = ..., seed: int = ...) -> set[str]:
    """Subdivide selected edges"""
    ...

def subdivide_edgering(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, number_cuts: int = ..., interpolation: str = ..., smoothness: float = ..., profile_shape_factor: float = ..., profile_shape: str = ...) -> set[str]:
    """Subdivide perpendicular edges to the selected edge-ring"""
    ...

def symmetrize(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., threshold: float = ...) -> set[str]:
    """Enforce symmetry (both form and topological) across an axis"""
    ...

def symmetry_snap(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., threshold: float = ..., factor: float = ..., use_center: bool = ...) -> set[str]:
    """Snap vertex pairs to their mirrored locations"""
    ...

def tris_convert_to_quads(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, face_threshold: float = ..., shape_threshold: float = ..., topology_influence: float = ..., uvs: bool = ..., vcols: bool = ..., seam: bool = ..., sharp: bool = ..., materials: bool = ..., deselect_joined: bool = ...) -> set[str]:
    """Merge triangles into four sided polygons where possible"""
    ...

def unsubdivide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, iterations: int = ...) -> set[str]:
    """Un-subdivide selected edges and faces"""
    ...

def uv_texture_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add UV map"""
    ...

def uv_texture_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove UV map"""
    ...

def uvs_reverse(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Flip direction of UV coordinates inside faces"""
    ...

def uvs_rotate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_ccw: bool = ...) -> set[str]:
    """Rotate UV coordinates inside faces"""
    ...

def vert_connect(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Connect selected vertices of faces, splitting the face"""
    ...

def vert_connect_concave(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Make all faces convex"""
    ...

def vert_connect_nonplanar(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, angle_limit: float = ...) -> set[str]:
    """Split non-planar faces that exceed the angle threshold"""
    ...

def vert_connect_path(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Connect vertices by their selection order, creating edges, splitting faces"""
    ...

def vertices_smooth(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ..., repeat: int = ..., xaxis: bool = ..., yaxis: bool = ..., zaxis: bool = ..., wait_for_input: bool = ...) -> set[str]:
    """Flatten angles of selected vertices"""
    ...

def vertices_smooth_laplacian(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, repeat: int = ..., lambda_factor: float = ..., lambda_border: float = ..., use_x: bool = ..., use_y: bool = ..., use_z: bool = ..., preserve_volume: bool = ...) -> set[str]:
    """Laplacian smooth of selected vertices"""
    ...

def wireframe(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_boundary: bool = ..., use_even_offset: bool = ..., use_relative_offset: bool = ..., use_replace: bool = ..., thickness: float = ..., offset: float = ..., use_crease: bool = ..., crease_weight: float = ...) -> set[str]:
    """Create a solid wireframe from faces"""
    ...
