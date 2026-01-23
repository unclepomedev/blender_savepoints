# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def bake_keys(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add keyframes on every frame between the selected keyframes"""
    ...

def clean(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, threshold: float = ..., channels: bool = ...) -> set[str]:
    """Simplify F-Curves by removing closely spaced keyframes"""
    ...

def clickselect(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, wait_to_deselect_others: bool = ..., use_select_on_click: bool = ..., mouse_x: int = ..., mouse_y: int = ..., extend: bool = ..., deselect_all: bool = ..., column: bool = ..., channel: bool = ...) -> set[str]:
    """Select keyframes by clicking on them"""
    ...

def copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy selected keyframes to the internal clipboard"""
    ...

def delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, confirm: bool = ...) -> set[str]:
    """Remove all selected keyframes"""
    ...

def duplicate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Make a copy of all selected keyframes"""
    ...

def duplicate_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ACTION_OT_duplicate: 'ACTION_OT_duplicate' = ..., TRANSFORM_OT_transform: 'TRANSFORM_OT_transform' = ...) -> set[str]:
    """Make a copy of all selected keyframes and move them"""
    ...

def easing_type(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Set easing type for the F-Curve segments starting from the selected keyframes"""
    ...

def extrapolation_type(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Set extrapolation mode for selected F-Curves"""
    ...

def frame_jump(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set the current frame to the average frame value of selected keyframes"""
    ...

def handle_type(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Set type of handle for selected keyframes"""
    ...

def interpolation_type(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Set interpolation mode for the F-Curve segments starting from the selected keyframes"""
    ...

def keyframe_insert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Insert keyframes for the specified channels"""
    ...

def keyframe_type(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Set type of keyframe for the selected keyframes"""
    ...

def markers_make_local(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Move selected scene markers to the active Action as local 'pose' markers"""
    ...

def mirror(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Flip selected keyframes over the selected mirror line"""
    ...

def new(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Create new action"""
    ...

def paste(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, offset: str = ..., merge: str = ..., flipped: bool = ...) -> set[str]:
    """Paste keyframes from the internal clipboard for the selected channels, starting on the current frame"""
    ...

def previewrange_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set Preview Range based on extents of selected Keyframes"""
    ...

def push_down(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Push action down on to the NLA stack as a new strip"""
    ...

def select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Toggle selection of all keyframes"""
    ...

def select_box(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, axis_range: bool = ..., xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., mode: str = ..., tweak: bool = ...) -> set[str]:
    """Select all keyframes within the specified region"""
    ...

def select_circle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, x: int = ..., y: int = ..., radius: int = ..., wait_for_input: bool = ..., mode: str = ...) -> set[str]:
    """Select keyframe points using circle selection"""
    ...

def select_column(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ...) -> set[str]:
    """Select all keyframes on the specified frame(s)"""
    ...

def select_lasso(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_smooth_stroke: bool = ..., smooth_stroke_factor: float = ..., smooth_stroke_radius: int = ..., mode: str = ...) -> set[str]:
    """Select keyframe points using lasso selection"""
    ...

def select_leftright(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., extend: bool = ...) -> set[str]:
    """Select keyframes to the left or the right of the current frame"""
    ...

def select_less(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Deselect keyframes on ends of selection islands"""
    ...

def select_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select keyframes occurring in the same F-Curves as selected ones"""
    ...

def select_more(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select keyframes beside already selected ones"""
    ...

def snap(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Snap selected keyframes to the times specified"""
    ...

def stash(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, create_new: bool = ...) -> set[str]:
    """Store this action in the NLA stack as a non-contributing strip for later use"""
    ...

def stash_and_create(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Store this action in the NLA stack as a non-contributing strip for later use, and create a new action"""
    ...

def unlink(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, force_delete: bool = ...) -> set[str]:
    """Unlink this action from the active action slot (and/or exit Tweak Mode)"""
    ...

def view_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reset viewable area to show full keyframe range"""
    ...

def view_frame(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Move the view to the current frame"""
    ...

def view_selected(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reset viewable area to show selected keyframes range"""
    ...
