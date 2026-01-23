# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def bone_select_menu(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., extend: bool = ..., deselect: bool = ..., toggle: bool = ...) -> Set[str]:
    """Menu bone selection"""
    ...

def camera_background_image_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., relative_path: bool = ..., name: str = ..., session_uid: int = ...) -> Set[str]:
    """Add a new background image to the active camera"""
    ...

def camera_background_image_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, index: int = ...) -> Set[str]:
    """Remove a background image from the camera"""
    ...

def camera_to_view(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Set camera view to active view"""
    ...

def camera_to_view_selected(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Move the camera so selected objects are framed"""
    ...

def clear_render_border(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Clear the boundaries of the border render and disable border render"""
    ...

def clip_border(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ...) -> Set[str]:
    """Set the view clipping region"""
    ...

def copybuffer(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy the selected objects to the internal clipboard"""
    ...

def cursor3d(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_depth: bool = ..., orientation: str = ...) -> Set[str]:
    """Set the location of the 3D cursor"""
    ...

def dolly(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mx: int = ..., my: int = ..., delta: int = ..., use_cursor_init: bool = ...) -> Set[str]:
    """Dolly in/out in the view"""
    ...

def drop_world(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., session_uid: int = ...) -> Set[str]:
    """Drop a world into the scene"""
    ...

def edit_mesh_extrude_individual_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Extrude each individual face separately along local normals"""
    ...

def edit_mesh_extrude_manifold_normal(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Extrude manifold region along normals"""
    ...

def edit_mesh_extrude_move_normal(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, dissolve_and_intersect: bool = ...) -> Set[str]:
    """Extrude region together along the average normal"""
    ...

def edit_mesh_extrude_move_shrink_fatten(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Extrude region together along local normals"""
    ...

def fly(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Interactively fly around the scene"""
    ...

def interactive_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, primitive_type: str = ..., plane_origin_base: str = ..., plane_origin_depth: str = ..., plane_aspect_base: str = ..., plane_aspect_depth: str = ..., wait_for_input: bool = ...) -> Set[str]:
    """Interactively add an object"""
    ...

def localview(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frame_selected: bool = ...) -> Set[str]:
    """Toggle display of selected object(s) separately and centered in view"""
    ...

def localview_remove_from(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Move selected objects out of local view"""
    ...

def move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_cursor_init: bool = ...) -> Set[str]:
    """Move the view"""
    ...

def navigate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Interactively navigate around the scene (uses the mode (walk/fly) preference)"""
    ...

def ndof_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Pan and rotate the view with the 3D mouse"""
    ...

def ndof_orbit(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Orbit the view using the 3D mouse"""
    ...

def ndof_orbit_zoom(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Orbit and zoom the view using the 3D mouse"""
    ...

def ndof_pan(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Pan the view with the 3D mouse"""
    ...

def object_as_camera(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Set the active object as the active camera for this view or scene"""
    ...

def object_mode_pie_or_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """(undocumented operator)"""
    ...

def pastebuffer(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, autoselect: bool = ..., active_collection: bool = ...) -> Set[str]:
    """Paste objects from the internal clipboard"""
    ...

def render_border(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ...) -> Set[str]:
    """Set the boundaries of the border render and enable border render"""
    ...

def rotate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_cursor_init: bool = ...) -> Set[str]:
    """Rotate the view"""
    ...

def ruler_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add ruler"""
    ...

def ruler_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """(undocumented operator)"""
    ...

def select(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., deselect: bool = ..., toggle: bool = ..., deselect_all: bool = ..., select_passthrough: bool = ..., center: bool = ..., enumerate: bool = ..., object: bool = ..., location: int = ...) -> Set[str]:
    """Select and activate item(s)"""
    ...

def select_box(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., mode: str = ...) -> Set[str]:
    """Select items using box selection"""
    ...

def select_circle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, x: int = ..., y: int = ..., radius: int = ..., wait_for_input: bool = ..., mode: str = ...) -> Set[str]:
    """Select items using circle selection"""
    ...

def select_lasso(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_smooth_stroke: bool = ..., smooth_stroke_factor: float = ..., smooth_stroke_radius: int = ..., mode: str = ...) -> Set[str]:
    """Select items using lasso selection"""
    ...

def select_menu(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., extend: bool = ..., deselect: bool = ..., toggle: bool = ...) -> Set[str]:
    """Menu object selection"""
    ...

def smoothview(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """(undocumented operator)"""
    ...

def snap_cursor_to_active(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Snap 3D cursor to the active item"""
    ...

def snap_cursor_to_center(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Snap 3D cursor to the world origin"""
    ...

def snap_cursor_to_grid(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Snap 3D cursor to the nearest grid division"""
    ...

def snap_cursor_to_selected(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Snap 3D cursor to the middle of the selected item(s)"""
    ...

def snap_selected_to_active(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Snap selected item(s) to the active item"""
    ...

def snap_selected_to_cursor(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_offset: bool = ..., use_rotation: bool = ...) -> Set[str]:
    """Snap selected item(s) to the 3D cursor"""
    ...

def snap_selected_to_grid(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Snap selected item(s) to their nearest grid division"""
    ...

def toggle_matcap_flip(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Flip MatCap"""
    ...

def toggle_shading(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Toggle shading type in 3D viewport"""
    ...

def toggle_xray(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Transparent scene display. Allow selecting through items"""
    ...

def transform_gizmo_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., type: str = ...) -> Set[str]:
    """Set the current transform gizmo"""
    ...

def view_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_all_regions: bool = ..., center: bool = ...) -> Set[str]:
    """View all objects in scene"""
    ...

def view_axis(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., align_active: bool = ..., relative: bool = ...) -> Set[str]:
    """Use a preset viewpoint"""
    ...

def view_camera(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Toggle the camera view"""
    ...

def view_center_camera(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Center the camera view, resizing the view to fit its bounds"""
    ...

def view_center_cursor(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Center the view so that the cursor is in the middle of the view"""
    ...

def view_center_lock(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Center the view lock offset"""
    ...

def view_center_pick(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Center the view to the Z-depth position under the mouse cursor"""
    ...

def view_lock_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Clear all view locking"""
    ...

def view_lock_to_active(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Lock the view to the active object/bone"""
    ...

def view_orbit(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, angle: float = ..., type: str = ...) -> Set[str]:
    """Orbit the view"""
    ...

def view_pan(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Pan the view in a given direction"""
    ...

def view_persportho(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Switch the current view from perspective/orthographic projection"""
    ...

def view_roll(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, angle: float = ..., type: str = ...) -> Set[str]:
    """Roll the view"""
    ...

def view_selected(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_all_regions: bool = ...) -> Set[str]:
    """Move the view to the selection center"""
    ...

def walk(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Interactively walk around the scene"""
    ...

def zoom(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mx: int = ..., my: int = ..., delta: int = ..., use_cursor_init: bool = ...) -> Set[str]:
    """Zoom in/out in the view"""
    ...

def zoom_border(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., zoom_out: bool = ...) -> Set[str]:
    """Zoom in the view to the nearest object contained in the border"""
    ...

def zoom_camera_1_to_1(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Match the camera to 1:1 to the render output"""
    ...
