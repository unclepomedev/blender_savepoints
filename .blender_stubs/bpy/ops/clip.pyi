# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def add_marker(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[float] = ...) -> set[str]:
    """Place new marker at specified location"""
    ...

def add_marker_at_click(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Place new marker at the desired (clicked) position"""
    ...

def add_marker_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, CLIP_OT_add_marker: 'CLIP_OT_add_marker' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Add new marker and move it on movie"""
    ...

def add_marker_slide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, CLIP_OT_add_marker: 'CLIP_OT_add_marker' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Add new marker and slide it with mouse until mouse button release"""
    ...

def apply_solution_scale(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, distance: float = ...) -> set[str]:
    """Apply scale on solution itself to make distance between selected tracks equals to desired"""
    ...

def average_tracks(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, keep_original: bool = ...) -> set[str]:
    """Average selected tracks into active"""
    ...

def bundles_to_mesh(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Create vertex cloud using coordinates of reconstructed tracks"""
    ...

def camera_preset_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ..., use_focal_length: bool = ...) -> set[str]:
    """Add or remove a Tracking Camera Intrinsics Preset"""
    ...

def change_frame(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frame: int = ...) -> set[str]:
    """Interactively change the current frame number"""
    ...

def clean_tracks(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frames: int = ..., error: float = ..., action: str = ...) -> set[str]:
    """Clean tracks with high error values or few frames"""
    ...

def clear_solution(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear all calculated data"""
    ...

def clear_track_path(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ..., clear_active: bool = ...) -> set[str]:
    """Clear tracks after/before current position or clear the whole track"""
    ...

def constraint_to_fcurve(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Create F-Curves for object which will copy object's movement caused by this constraint"""
    ...

def copy_tracks(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy the selected tracks to the internal clipboard"""
    ...

def create_plane_track(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Create new plane track out of selected point tracks"""
    ...

def cursor_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[float] = ...) -> set[str]:
    """Set 2D cursor location"""
    ...

def delete_marker(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, confirm: bool = ...) -> set[str]:
    """Delete marker for current frame from selected tracks"""
    ...

def delete_proxy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Delete movie clip proxy files from the hard drive"""
    ...

def delete_track(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, confirm: bool = ...) -> set[str]:
    """Delete selected tracks"""
    ...

def detect_features(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, placement: str = ..., margin: int = ..., threshold: float = ..., min_distance: int = ...) -> set[str]:
    """Automatically detect features and place markers to track"""
    ...

def disable_markers(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Disable/enable selected markers"""
    ...

def dopesheet_select_channel(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[float] = ..., extend: bool = ...) -> set[str]:
    """Select movie tracking channel"""
    ...

def dopesheet_view_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reset viewable area to show full keyframe range"""
    ...

def filter_tracks(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, track_threshold: float = ...) -> set[str]:
    """Filter tracks which has weirdly looking spikes in motion curves"""
    ...

def frame_jump(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, position: str = ...) -> set[str]:
    """Jump to special frame"""
    ...

def graph_center_current_frame(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Scroll view so current frame would be centered"""
    ...

def graph_delete_curve(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, confirm: bool = ...) -> set[str]:
    """Delete track corresponding to the selected curve"""
    ...

def graph_delete_knot(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Delete curve knots"""
    ...

def graph_disable_markers(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Disable/enable selected markers"""
    ...

def graph_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[float] = ..., extend: bool = ...) -> set[str]:
    """Select graph curves"""
    ...

def graph_select_all_markers(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Change selection of all markers of active track"""
    ...

def graph_select_box(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., deselect: bool = ..., extend: bool = ...) -> set[str]:
    """Select curve points using box selection"""
    ...

def graph_view_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """View all curves in editor"""
    ...

def hide_tracks(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> set[str]:
    """Hide selected tracks"""
    ...

def hide_tracks_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear hide selected tracks"""
    ...

def join_tracks(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Join selected tracks"""
    ...

def keyframe_delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Delete a keyframe from selected tracks at current frame"""
    ...

def keyframe_insert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Insert a keyframe to selected tracks at current frame"""
    ...

def lock_selection_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Toggle Lock Selection option of the current clip editor"""
    ...

def lock_tracks(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Lock/unlock selected tracks"""
    ...

def mode_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ...) -> set[str]:
    """Set the clip interaction mode"""
    ...

def new_image_from_plane_marker(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Create new image from the content of the plane marker"""
    ...

def open(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., show_multiview: bool = ..., use_multiview: bool = ..., display_type: str = ..., sort_method: str = ...) -> set[str]:
    """Load a sequence of frames or a movie file"""
    ...

def paste_tracks(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Paste tracks from the internal clipboard"""
    ...

def prefetch(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Prefetch frames from disk for faster playback/tracking"""
    ...

def rebuild_proxy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Rebuild all selected proxies and timecode indices in the background"""
    ...

def refine_markers(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, backwards: bool = ...) -> set[str]:
    """Refine selected markers positions by running the tracker from track's reference to current frame"""
    ...

def reload(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reload clip"""
    ...

def select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., deselect_all: bool = ..., location: list[float] = ...) -> set[str]:
    """Select tracking markers"""
    ...

def select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Change selection of all tracking markers"""
    ...

def select_box(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., mode: str = ...) -> set[str]:
    """Select markers using box selection"""
    ...

def select_circle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, x: int = ..., y: int = ..., radius: int = ..., wait_for_input: bool = ..., mode: str = ...) -> set[str]:
    """Select markers using circle selection"""
    ...

def select_grouped(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, group: str = ...) -> set[str]:
    """Select all tracks from specified group"""
    ...

def select_lasso(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_smooth_stroke: bool = ..., smooth_stroke_factor: float = ..., smooth_stroke_radius: int = ..., mode: str = ...) -> set[str]:
    """Select markers using lasso selection"""
    ...

def set_active_clip(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(undocumented operator)"""
    ...

def set_axis(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, axis: str = ...) -> set[str]:
    """Set the direction of a scene axis by rotating the camera (or its parent if present). This assumes that the selected track lies on a real axis connecting it to the origin"""
    ...

def set_origin(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_median: bool = ...) -> set[str]:
    """Set active marker as origin by moving camera (or its parent if present) in 3D space"""
    ...

def set_plane(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, plane: str = ...) -> set[str]:
    """Set plane based on 3 selected bundles by moving camera (or its parent if present) in 3D space"""
    ...

def set_scale(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, distance: float = ...) -> set[str]:
    """Set scale of scene by scaling camera (or its parent if present)"""
    ...

def set_scene_frames(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set scene's start and end frame to match clip's start frame and length"""
    ...

def set_solution_scale(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, distance: float = ...) -> set[str]:
    """Set object solution scale using distance between two selected tracks"""
    ...

def set_solver_keyframe(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, keyframe: str = ...) -> set[str]:
    """Set keyframe used by solver"""
    ...

def set_viewport_background(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set current movie clip as a camera background in 3D Viewport (works only when a 3D Viewport is visible)"""
    ...

def setup_tracking_scene(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Prepare scene for compositing 3D objects into this footage"""
    ...

def slide_marker(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, offset: list[float] = ...) -> set[str]:
    """Slide marker areas"""
    ...

def slide_plane_marker(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Slide plane marker areas"""
    ...

def solve_camera(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Solve camera motion from tracks"""
    ...

def stabilize_2d_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add selected tracks to 2D translation stabilization"""
    ...

def stabilize_2d_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove selected track from translation stabilization"""
    ...

def stabilize_2d_rotation_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add selected tracks to 2D rotation stabilization"""
    ...

def stabilize_2d_rotation_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove selected track from rotation stabilization"""
    ...

def stabilize_2d_rotation_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select tracks which are used for rotation stabilization"""
    ...

def stabilize_2d_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select tracks which are used for translation stabilization"""
    ...

def track_color_preset_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> set[str]:
    """Add or remove a Clip Track Color Preset"""
    ...

def track_copy_color(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy color to all selected tracks"""
    ...

def track_markers(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, backwards: bool = ..., sequence: bool = ...) -> set[str]:
    """Track selected markers"""
    ...

def track_settings_as_default(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy tracking settings from active track to default settings"""
    ...

def track_settings_to_track(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy tracking settings from active track to selected tracks"""
    ...

def track_to_empty(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Create an Empty object which will be copying movement of active track"""
    ...

def tracking_object_new(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add new object for tracking"""
    ...

def tracking_object_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove object for tracking"""
    ...

def tracking_settings_preset_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> set[str]:
    """Add or remove a motion tracking settings preset"""
    ...

def update_image_from_plane_marker(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Update current image used by plane marker from the content of the plane marker"""
    ...

def view_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, fit_view: bool = ...) -> set[str]:
    """View whole image with markers"""
    ...

def view_center_cursor(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Center the view so that the cursor is in the middle of the view"""
    ...

def view_ndof(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Use a 3D mouse device to pan/zoom the view"""
    ...

def view_pan(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, offset: list[float] = ...) -> set[str]:
    """Pan the view"""
    ...

def view_selected(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """View all selected elements"""
    ...

def view_zoom(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ..., use_cursor_init: bool = ...) -> set[str]:
    """Zoom in/out the view"""
    ...

def view_zoom_in(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[float] = ...) -> set[str]:
    """Zoom in the view"""
    ...

def view_zoom_out(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[float] = ...) -> set[str]:
    """Zoom out the view"""
    ...

def view_zoom_ratio(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ratio: float = ...) -> set[str]:
    """Set the zoom ratio (based on clip size)"""
    ...
