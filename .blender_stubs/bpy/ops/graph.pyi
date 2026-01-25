# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def bake_keys(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add keyframes on every frame between the selected keyframes"""
    ...

def blend_offset(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ...) -> Set[str]:
    """Shift selected keys to the value of the neighboring keys as a block"""
    ...

def blend_to_default(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ...) -> Set[str]:
    """Blend selected keys to their default value from their current position"""
    ...

def blend_to_ease(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ...) -> Set[str]:
    """Blends keyframes from current state to an ease-in or ease-out curve"""
    ...

def blend_to_neighbor(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ...) -> Set[str]:
    """Blend selected keyframes to their left or right neighbor"""
    ...

def breakdown(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ...) -> Set[str]:
    """Move selected keyframes to an inbetween position relative to adjacent keys"""
    ...

def butterworth_smooth(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, cutoff_frequency: float = ..., filter_order: int = ..., samples_per_frame: int = ..., blend: float = ..., blend_in_out: int = ...) -> Set[str]:
    """Smooth an F-Curve while maintaining the general shape of the curve"""
    ...

def clean(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, threshold: float = ..., channels: bool = ...) -> Set[str]:
    """Simplify F-Curves by removing closely spaced keyframes"""
    ...

def click_insert(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frame: float = ..., value: float = ..., extend: bool = ...) -> Set[str]:
    """Insert new keyframe at the cursor position for the active F-Curve"""
    ...

def clickselect(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, wait_to_deselect_others: bool = ..., use_select_on_click: bool = ..., mouse_x: int = ..., mouse_y: int = ..., extend: bool = ..., deselect_all: bool = ..., column: bool = ..., curves: bool = ...) -> Set[str]:
    """Select keyframes by clicking on them"""
    ...

def copy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy selected keyframes to the internal clipboard"""
    ...

def cursor_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frame: float = ..., value: float = ...) -> Set[str]:
    """Interactively set the current frame and value cursor"""
    ...

def decimate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., factor: float = ..., remove_error_margin: float = ...) -> Set[str]:
    """Decimate F-Curves by removing keyframes that influence the curve shape the least"""
    ...

def delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, confirm: bool = ...) -> Set[str]:
    """Remove all selected keyframes"""
    ...

def driver_delete_invalid(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Delete all visible drivers considered invalid"""
    ...

def driver_variables_copy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy the driver variables of the active driver"""
    ...

def driver_variables_paste(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, replace: bool = ...) -> Set[str]:
    """Add copied driver variables to the active driver"""
    ...

def duplicate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ...) -> Set[str]:
    """Make a copy of all selected keyframes"""
    ...

def duplicate_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, GRAPH_OT_duplicate: 'GRAPH_OT_duplicate' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> Set[str]:
    """Make a copy of all selected keyframes and move them"""
    ...

def ease(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ..., sharpness: float = ...) -> Set[str]:
    """Align keyframes on a ease-in or ease-out curve"""
    ...

def easing_type(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Set easing type for the F-Curve segments starting from the selected keyframes"""
    ...

def equalize_handles(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, side: str = ..., handle_length: float = ..., flatten: bool = ...) -> Set[str]:
    """Ensure selected keyframes' handles have equal length, optionally making them horizontal. Automatic, Automatic Clamped, or Vector handle types will be converted to Aligned"""
    ...

def euler_filter(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Fix large jumps and flips in the selected Euler Rotation F-Curves arising from rotation values being clipped when baking physics"""
    ...

def extrapolation_type(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Set extrapolation mode for selected F-Curves"""
    ...

def fmodifier_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., only_active: bool = ...) -> Set[str]:
    """Add F-Modifier to the active/selected F-Curves"""
    ...

def fmodifier_copy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy the F-Modifier(s) of the active F-Curve"""
    ...

def fmodifier_paste(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, only_active: bool = ..., replace: bool = ...) -> Set[str]:
    """Add copied F-Modifiers to the selected F-Curves"""
    ...

def frame_jump(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Place the cursor on the midpoint of selected keyframes"""
    ...

def gaussian_smooth(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ..., sigma: float = ..., filter_width: int = ...) -> Set[str]:
    """Smooth the curve using a Gaussian filter"""
    ...

def ghost_curves_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Clear F-Curve snapshots (Ghosts) for active Graph Editor"""
    ...

def ghost_curves_create(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Create snapshot (Ghosts) of selected F-Curves as background aid for active Graph Editor"""
    ...

def handle_type(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Set type of handle for selected keyframes"""
    ...

def hide(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> Set[str]:
    """Hide selected curves from Graph Editor view"""
    ...

def interpolation_type(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Set interpolation mode for the F-Curve segments starting from the selected keyframes"""
    ...

def keyframe_insert(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Insert keyframes for the specified channels"""
    ...

def keyframe_jump(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, next: bool = ...) -> Set[str]:
    """Jump to previous/next keyframe"""
    ...

def keys_to_samples(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Convert selected channels to an uneditable set of samples to save storage space"""
    ...

def match_slope(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ...) -> Set[str]:
    """Blend selected keys to the slope of neighboring ones"""
    ...

def mirror(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Flip selected keyframes over the selected mirror line"""
    ...

def paste(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, offset: str = ..., value_offset: str = ..., merge: str = ..., flipped: bool = ...) -> Set[str]:
    """Paste keyframes from the internal clipboard for the selected channels, starting on the current frame"""
    ...

def previewrange_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Set Preview Range based on range of selected keyframes"""
    ...

def push_pull(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ...) -> Set[str]:
    """Exaggerate or minimize the value of the selected keys"""
    ...

def reveal(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ...) -> Set[str]:
    """Make previously hidden curves visible again in Graph Editor view"""
    ...

def samples_to_keys(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Convert selected channels from samples to keyframes"""
    ...

def scale_average(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ...) -> Set[str]:
    """Scale selected key values by their combined average"""
    ...

def scale_from_neighbor(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ..., anchor: str = ...) -> Set[str]:
    """Increase or decrease the value of selected keys in relationship to the neighboring one"""
    ...

def select_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> Set[str]:
    """Toggle selection of all keyframes"""
    ...

def select_box(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, axis_range: bool = ..., include_handles: bool = ..., tweak: bool = ..., use_curve_selection: bool = ..., xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., mode: str = ...) -> Set[str]:
    """Select all keyframes within the specified region"""
    ...

def select_circle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, x: int = ..., y: int = ..., radius: int = ..., wait_for_input: bool = ..., mode: str = ..., include_handles: bool = ..., use_curve_selection: bool = ...) -> Set[str]:
    """Select keyframe points using circle selection"""
    ...

def select_column(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ...) -> Set[str]:
    """Select all keyframes on the specified frame(s)"""
    ...

def select_key_handles(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, left_handle_action: str = ..., right_handle_action: str = ..., key_action: str = ...) -> Set[str]:
    """For selected keyframes, select/deselect any combination of the key itself and its handles"""
    ...

def select_lasso(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_smooth_stroke: bool = ..., smooth_stroke_factor: float = ..., smooth_stroke_radius: int = ..., mode: str = ..., include_handles: bool = ..., use_curve_selection: bool = ...) -> Set[str]:
    """Select keyframe points using lasso selection"""
    ...

def select_leftright(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., extend: bool = ...) -> Set[str]:
    """Select keyframes to the left or the right of the current frame"""
    ...

def select_less(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Deselect keyframes on ends of selection islands"""
    ...

def select_linked(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Select keyframes occurring in the same F-Curves as selected ones"""
    ...

def select_more(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Select keyframes beside already selected ones"""
    ...

def shear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ..., direction: str = ...) -> Set[str]:
    """Affect the value of the keys linearly, keeping the same relationship between them using either the left or the right key as reference"""
    ...

def smooth(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Apply weighted moving means to make selected F-Curves less bumpy"""
    ...

def snap(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Snap selected keyframes to the chosen times/values"""
    ...

def snap_cursor_value(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Place the cursor value on the average value of selected keyframes"""
    ...

def sound_to_samples(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., show_multiview: bool = ..., use_multiview: bool = ..., display_type: str = ..., sort_method: str = ..., low: float = ..., high: float = ..., attack: float = ..., release: float = ..., threshold: float = ..., use_accumulate: bool = ..., use_additive: bool = ..., use_square: bool = ..., sthreshold: float = ...) -> Set[str]:
    """Bakes a sound wave to samples on selected channels"""
    ...

def time_offset(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frame_offset: float = ...) -> Set[str]:
    """Shifts the value of selected keys in time"""
    ...

def view_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, include_handles: bool = ...) -> Set[str]:
    """Reset viewable area to show full keyframe range"""
    ...

def view_frame(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Move the view to the current frame"""
    ...

def view_selected(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, include_handles: bool = ...) -> Set[str]:
    """Reset viewable area to show selected keyframe range"""
    ...
