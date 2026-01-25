# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def align(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, axis: str = ..., position_mode: str = ...) -> set[str]:
    """Aligns selected UV vertices on a line"""
    ...

def align_rotation(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, method: str = ..., axis: str = ..., correct_aspect: bool = ...) -> set[str]:
    """Align the UV island's rotation"""
    ...

def arrange_islands(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, initial_position: str = ..., axis: str = ..., align: str = ..., order: str = ..., margin: float = ...) -> set[str]:
    """Arrange selected UV islands on a line"""
    ...

def average_islands_scale(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, scale_uv: bool = ..., shear: bool = ...) -> set[str]:
    """Average the size of separate UV islands, based on their area in 3D space"""
    ...

def copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy selected UV vertices"""
    ...

def copy_mirrored_faces(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., precision: int = ...) -> set[str]:
    """Copy mirror UV coordinates on the X axis based on a mirrored mesh"""
    ...

def cube_project(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, cube_size: float = ..., correct_aspect: bool = ..., clip_to_bounds: bool = ..., scale_to_bounds: bool = ...) -> set[str]:
    """Project the UV vertices of the mesh over the six faces of a cube"""
    ...

def cursor_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[float] = ...) -> set[str]:
    """Set 2D cursor location"""
    ...

def custom_region_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ...) -> set[str]:
    """Set the boundaries of the user region"""
    ...

def cylinder_project(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., align: str = ..., pole: str = ..., seam: bool = ..., radius: float = ..., correct_aspect: bool = ..., clip_to_bounds: bool = ..., scale_to_bounds: bool = ...) -> set[str]:
    """Project the UV vertices of the mesh over the curved wall of a cylinder"""
    ...

def export_layout(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., export_all: bool = ..., export_tiles: str = ..., modified: bool = ..., mode: str = ..., size: list[int] = ..., opacity: float = ..., check_existing: bool = ...) -> set[str]:
    """Export UV layout to file"""
    ...

def follow_active_quads(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ...) -> set[str]:
    """Follow UVs from active quads along continuous face loops"""
    ...

def hide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> set[str]:
    """Hide (un)selected UV vertices"""
    ...

def lightmap_pack(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, PREF_CONTEXT: str = ..., PREF_PACK_IN_ONE: bool = ..., PREF_NEW_UVLAYER: bool = ..., PREF_BOX_DIV: int = ..., PREF_MARGIN_DIV: float = ...) -> set[str]:
    """Pack each face's UVs into the UV bounds"""
    ...

def mark_seam(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, clear: bool = ...) -> set[str]:
    """Mark selected UV edges as seams"""
    ...

def minimize_stretch(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, fill_holes: bool = ..., blend: float = ..., iterations: int = ...) -> set[str]:
    """Reduce UV stretching by relaxing angles"""
    ...

def move_on_axis(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., axis: str = ..., distance: int = ...) -> set[str]:
    """Move UVs on an axis"""
    ...

def pack_islands(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, udim_source: str = ..., rotate: bool = ..., rotate_method: str = ..., scale: bool = ..., merge_overlap: bool = ..., margin_method: str = ..., margin: float = ..., pin: bool = ..., pin_method: str = ..., shape_method: str = ...) -> set[str]:
    """Transform all islands so that they fill up the UV/UDIM space as much as possible"""
    ...

def paste(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Paste selected UV vertices"""
    ...

def pin(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, clear: bool = ..., invert: bool = ...) -> set[str]:
    """Set/clear selected UV vertices as anchored between multiple unwrap operations"""
    ...

def project_from_view(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, orthographic: bool = ..., camera_bounds: bool = ..., correct_aspect: bool = ..., clip_to_bounds: bool = ..., scale_to_bounds: bool = ...) -> set[str]:
    """Project the UV vertices of the mesh as seen in current 3D view"""
    ...

def randomize_uv_transform(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, random_seed: int = ..., use_loc: bool = ..., loc: list[float] = ..., use_rot: bool = ..., rot: float = ..., use_scale: bool = ..., scale_even: bool = ..., scale: list[float] = ...) -> set[str]:
    """Randomize the UV island's location, rotation, and scale"""
    ...

def remove_doubles(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, threshold: float = ..., use_unselected: bool = ..., use_shared_vertex: bool = ...) -> set[str]:
    """Selected UV vertices that are within a radius of each other are welded together"""
    ...

def reset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reset UV projection"""
    ...

def reveal(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ...) -> set[str]:
    """Reveal all hidden UV vertices"""
    ...

def rip(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mirror: bool = ..., release_confirm: bool = ..., use_accurate: bool = ..., location: list[float] = ...) -> set[str]:
    """Rip selected vertices or a selected region"""
    ...

def rip_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, UV_OT_rip: 'UV_OT_rip' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Unstitch UVs and move the result"""
    ...

def seams_from_islands(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mark_seams: bool = ..., mark_sharp: bool = ...) -> set[str]:
    """Set mesh seams according to island setup in the UV editor"""
    ...

def select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., deselect: bool = ..., toggle: bool = ..., deselect_all: bool = ..., select_passthrough: bool = ..., location: list[float] = ...) -> set[str]:
    """Select UV vertices"""
    ...

def select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Change selection of all UV vertices"""
    ...

def select_box(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, pinned: bool = ..., xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., mode: str = ...) -> set[str]:
    """Select UV vertices using box selection"""
    ...

def select_circle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, x: int = ..., y: int = ..., radius: int = ..., wait_for_input: bool = ..., mode: str = ...) -> set[str]:
    """Select UV vertices using circle selection"""
    ...

def select_edge_ring(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., location: list[float] = ...) -> set[str]:
    """Select an edge ring of connected UV vertices"""
    ...

def select_lasso(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_smooth_stroke: bool = ..., smooth_stroke_factor: float = ..., smooth_stroke_radius: int = ..., mode: str = ...) -> set[str]:
    """Select UVs using lasso selection"""
    ...

def select_less(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Deselect UV vertices at the boundary of each selection region"""
    ...

def select_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select all UV vertices linked to the active UV map"""
    ...

def select_linked_pick(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., deselect: bool = ..., location: list[float] = ...) -> set[str]:
    """Select all UV vertices linked under the mouse"""
    ...

def select_loop(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., location: list[float] = ...) -> set[str]:
    """Select a loop of connected UV vertices"""
    ...

def select_mode(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Change UV selection mode"""
    ...

def select_more(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select more UV vertices connected to initial selection"""
    ...

def select_overlap(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ...) -> set[str]:
    """Select all UV faces which overlap each other"""
    ...

def select_pinned(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select all pinned UV vertices"""
    ...

def select_similar(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., compare: str = ..., threshold: float = ...) -> set[str]:
    """Select similar UVs by property types"""
    ...

def select_split(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select only entirely selected faces"""
    ...

def shortest_path_pick(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_face_step: bool = ..., use_topology_distance: bool = ..., use_fill: bool = ..., skip: int = ..., nth: int = ..., offset: int = ..., object_index: int = ..., index: int = ...) -> set[str]:
    """Select shortest path between two selections"""
    ...

def shortest_path_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_face_step: bool = ..., use_topology_distance: bool = ..., use_fill: bool = ..., skip: int = ..., nth: int = ..., offset: int = ...) -> set[str]:
    """Selected shortest path between two vertices/edges/faces"""
    ...

def smart_project(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, angle_limit: float = ..., margin_method: str = ..., rotate_method: str = ..., island_margin: float = ..., area_weight: float = ..., correct_aspect: bool = ..., scale_to_bounds: bool = ...) -> set[str]:
    """Projection unwraps the selected faces of mesh objects"""
    ...

def snap_cursor(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, target: str = ...) -> set[str]:
    """Snap cursor to target type"""
    ...

def snap_selected(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, target: str = ...) -> set[str]:
    """Snap selected UV vertices to target type"""
    ...

def sphere_project(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., align: str = ..., pole: str = ..., seam: bool = ..., correct_aspect: bool = ..., clip_to_bounds: bool = ..., scale_to_bounds: bool = ...) -> set[str]:
    """Project the UV vertices of the mesh over the curved surface of a sphere"""
    ...

def stitch(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_limit: bool = ..., snap_islands: bool = ..., limit: float = ..., static_island: int = ..., active_object_index: int = ..., midpoint_snap: bool = ..., clear_seams: bool = ..., mode: str = ..., stored_mode: str = ..., selection: bpy_prop_collection['SelectedUvElement'] = ..., objects_selection_count: list[int] = ...) -> set[str]:
    """Stitch selected UV vertices by proximity"""
    ...

def unwrap(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, method: str = ..., fill_holes: bool = ..., correct_aspect: bool = ..., use_subsurf_data: bool = ..., margin_method: str = ..., margin: float = ..., no_flip: bool = ..., iterations: int = ..., use_weights: bool = ..., weight_group: str = ..., weight_factor: float = ...) -> set[str]:
    """Unwrap the mesh of the object being edited"""
    ...

def weld(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Weld selected UV vertices together"""
    ...
