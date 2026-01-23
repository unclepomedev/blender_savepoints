# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def brush_stroke(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, stroke: bpy_prop_collection['OperatorStrokeElement'] = ..., mode: str = ..., pen_flip: bool = ..., override_location: bool = ..., ignore_background_click: bool = ...) -> Set[str]:
    """Sculpt a stroke into the geometry"""
    ...

def cloth_filter(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, start_mouse: int = ..., area_normal_radius: float = ..., strength: float = ..., iteration_count: int = ..., event_history: bpy_prop_collection['OperatorStrokeElement'] = ..., type: str = ..., force_axis: str = ..., orientation: str = ..., cloth_mass: float = ..., cloth_damping: float = ..., use_face_sets: bool = ..., use_collisions: bool = ...) -> Set[str]:
    """Applies a cloth simulation deformation to the entire mesh"""
    ...

def color_filter(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, start_mouse: int = ..., area_normal_radius: float = ..., strength: float = ..., iteration_count: int = ..., event_history: bpy_prop_collection['OperatorStrokeElement'] = ..., type: str = ..., fill_color: float = ...) -> Set[str]:
    """Applies a filter to modify the active color attribute"""
    ...

def detail_flood_fill(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Flood fill the mesh with the selected detail setting"""
    ...

def dynamic_topology_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Dynamic topology alters the mesh topology while sculpting"""
    ...

def dyntopo_detail_size_edit(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Modify the detail size of dyntopo interactively"""
    ...

def expand(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, target: str = ..., falloff_type: str = ..., invert: bool = ..., use_mask_preserve: bool = ..., use_falloff_gradient: bool = ..., use_modify_active: bool = ..., use_reposition_pivot: bool = ..., max_geodesic_move_preview: int = ..., use_auto_mask: bool = ..., normal_falloff_smooth: int = ...) -> Set[str]:
    """Generic sculpt expand operator"""
    ...

def face_set_box_gesture(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., use_front_faces_only: bool = ...) -> Set[str]:
    """Add a face set in a rectangle defined by the cursor"""
    ...

def face_set_change_visibility(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ...) -> Set[str]:
    """Change the visibility of the face sets of the sculpt"""
    ...

def face_set_edit(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, active_face_set: int = ..., mode: str = ..., strength: float = ..., modify_hidden: bool = ...) -> Set[str]:
    """Edits the current active face set"""
    ...

def face_set_extract(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, add_boundary_loop: bool = ..., smooth_iterations: int = ..., apply_shrinkwrap: bool = ..., add_solidify: bool = ...) -> Set[str]:
    """Create a new mesh object from the selected face set"""
    ...

def face_set_lasso_gesture(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_smooth_stroke: bool = ..., smooth_stroke_factor: float = ..., smooth_stroke_radius: int = ..., use_front_faces_only: bool = ...) -> Set[str]:
    """Add a face set in a shape defined by the cursor"""
    ...

def face_set_line_gesture(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xstart: int = ..., xend: int = ..., ystart: int = ..., yend: int = ..., flip: bool = ..., cursor: int = ..., use_front_faces_only: bool = ..., use_limit_to_segment: bool = ...) -> Set[str]:
    """Add a face set to one side of a line defined by the cursor"""
    ...

def face_set_polyline_gesture(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_front_faces_only: bool = ...) -> Set[str]:
    """Add a face set in a shape defined by the cursor"""
    ...

def face_sets_create(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ...) -> Set[str]:
    """Create a new face set"""
    ...

def face_sets_init(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., threshold: float = ...) -> Set[str]:
    """Initializes all face sets in the mesh"""
    ...

def face_sets_randomize_colors(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Generates a new set of random colors to render the face sets in the viewport"""
    ...

def mask_by_color(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, contiguous: bool = ..., invert: bool = ..., preserve_previous_mask: bool = ..., threshold: float = ..., location: int = ...) -> Set[str]:
    """Creates a mask based on the active color attribute"""
    ...

def mask_filter(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filter_type: str = ..., iterations: int = ..., auto_iteration_count: bool = ...) -> Set[str]:
    """Applies a filter to modify the current mask"""
    ...

def mask_from_boundary(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mix_mode: str = ..., mix_factor: float = ..., settings_source: str = ..., boundary_mode: str = ..., propagation_steps: int = ...) -> Set[str]:
    """Creates a mask based on the boundaries of the surface"""
    ...

def mask_from_cavity(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mix_mode: str = ..., mix_factor: float = ..., settings_source: str = ..., factor: float = ..., blur_steps: int = ..., use_curve: bool = ..., invert: bool = ...) -> Set[str]:
    """Creates a mask based on the curvature of the surface"""
    ...

def mask_init(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ...) -> Set[str]:
    """Creates a new mask for the entire mesh"""
    ...

def mesh_filter(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, start_mouse: int = ..., area_normal_radius: float = ..., strength: float = ..., iteration_count: int = ..., event_history: bpy_prop_collection['OperatorStrokeElement'] = ..., type: str = ..., deform_axis: str = ..., orientation: str = ..., surface_smooth_shape_preservation: float = ..., surface_smooth_current_vertex: float = ..., sharpen_smooth_ratio: float = ..., sharpen_intensify_detail_strength: float = ..., sharpen_curvature_smooth_iterations: int = ...) -> Set[str]:
    """Applies a filter to modify the current mesh"""
    ...

def optimize(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Recalculate the sculpt BVH to improve performance"""
    ...

def paint_mask_extract(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mask_threshold: float = ..., add_boundary_loop: bool = ..., smooth_iterations: int = ..., apply_shrinkwrap: bool = ..., add_solidify: bool = ...) -> Set[str]:
    """Create a new mesh object from the current paint mask"""
    ...

def paint_mask_slice(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mask_threshold: float = ..., fill_holes: bool = ..., new_object: bool = ...) -> Set[str]:
    """Slices the paint mask from the mesh"""
    ...

def project_line_gesture(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xstart: int = ..., xend: int = ..., ystart: int = ..., yend: int = ..., flip: bool = ..., cursor: int = ..., use_front_faces_only: bool = ..., use_limit_to_segment: bool = ...) -> Set[str]:
    """Project the geometry onto a plane defined by a line"""
    ...

def sample_detail_size(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: int = ..., mode: str = ...) -> Set[str]:
    """Sample the mesh detail on clicked point"""
    ...

def sculptmode_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Toggle sculpt mode in 3D view"""
    ...

def set_persistent_base(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reset the copy of the mesh that is being sculpted on"""
    ...

def set_pivot_position(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., mouse_x: float = ..., mouse_y: float = ...) -> Set[str]:
    """Sets the sculpt transform pivot position"""
    ...

def symmetrize(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, merge_tolerance: float = ...) -> Set[str]:
    """Symmetrize the topology modifications"""
    ...

def trim_box_gesture(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., use_front_faces_only: bool = ..., location: int = ..., trim_mode: str = ..., use_cursor_depth: bool = ..., trim_orientation: str = ..., trim_extrude_mode: str = ..., trim_solver: str = ...) -> Set[str]:
    """Execute a boolean operation on the mesh and a rectangle defined by the cursor"""
    ...

def trim_lasso_gesture(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_smooth_stroke: bool = ..., smooth_stroke_factor: float = ..., smooth_stroke_radius: int = ..., use_front_faces_only: bool = ..., location: int = ..., trim_mode: str = ..., use_cursor_depth: bool = ..., trim_orientation: str = ..., trim_extrude_mode: str = ..., trim_solver: str = ...) -> Set[str]:
    """Execute a boolean operation on the mesh and a shape defined by the cursor"""
    ...

def trim_line_gesture(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xstart: int = ..., xend: int = ..., ystart: int = ..., yend: int = ..., flip: bool = ..., cursor: int = ..., use_front_faces_only: bool = ..., use_limit_to_segment: bool = ..., location: int = ..., trim_mode: str = ..., use_cursor_depth: bool = ..., trim_orientation: str = ..., trim_extrude_mode: str = ..., trim_solver: str = ...) -> Set[str]:
    """Remove a portion of the mesh on one side of a line"""
    ...

def trim_polyline_gesture(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_front_faces_only: bool = ..., location: int = ..., trim_mode: str = ..., use_cursor_depth: bool = ..., trim_orientation: str = ..., trim_extrude_mode: str = ..., trim_solver: str = ...) -> Set[str]:
    """Execute a boolean operation on the mesh and a polygonal shape defined by the cursor"""
    ...

def uv_sculpt_grab(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_invert: bool = ...) -> Set[str]:
    """Grab UVs"""
    ...

def uv_sculpt_pinch(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_invert: bool = ...) -> Set[str]:
    """Pinch UVs"""
    ...

def uv_sculpt_relax(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_invert: bool = ..., relax_method: str = ...) -> Set[str]:
    """Relax UVs"""
    ...
