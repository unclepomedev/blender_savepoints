# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def actionzone(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: int = ...) -> set[str]:
    """Handle area action zones for mouse actions/gestures"""
    ...

def animation_cancel(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, restore_frame: bool = ...) -> set[str]:
    """Cancel animation, returning to the original frame"""
    ...

def animation_play(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, reverse: bool = ..., sync: bool = ...) -> set[str]:
    """Play animation"""
    ...

def animation_step(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Step through animation by position"""
    ...

def area_close(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Close selected area"""
    ...

def area_dupli(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Duplicate selected area into new window"""
    ...

def area_join(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, source_xy: list[int] = ..., target_xy: list[int] = ...) -> set[str]:
    """Join selected areas into new window"""
    ...

def area_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, x: int = ..., y: int = ..., delta: int = ..., snap: bool = ...) -> set[str]:
    """Move selected area edges"""
    ...

def area_options(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Operations for splitting and merging"""
    ...

def area_split(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., factor: float = ..., cursor: list[int] = ...) -> set[str]:
    """Split selected area into new windows"""
    ...

def area_swap(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, cursor: list[int] = ...) -> set[str]:
    """Swap selected areas screen positions"""
    ...

def back_to_previous(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Revert back to the original screen layout, before fullscreen area overlay"""
    ...

def delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Delete active screen"""
    ...

def drivers_editor_show(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Show drivers editor in a separate window"""
    ...

def frame_jump(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, end: bool = ...) -> set[str]:
    """Jump to first/last frame in frame range"""
    ...

def frame_offset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, delta: int = ...) -> set[str]:
    """Move current frame forward/backward by a given number"""
    ...

def header_toggle_menus(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Expand or collapse the header pull-down menus"""
    ...

def info_log_show(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Show info log in a separate window"""
    ...

def keyframe_jump(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, next: bool = ...) -> set[str]:
    """Jump to previous/next keyframe"""
    ...

def marker_jump(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, next: bool = ...) -> set[str]:
    """Jump to previous/next marker"""
    ...

def new(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add a new screen"""
    ...

def quadview_size(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Resize Quad View areas"""
    ...

def redo_last(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Display parameters for last action performed"""
    ...

def region_blend(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Blend in and out overlapping region"""
    ...

def region_context_menu(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Display region context menu"""
    ...

def region_flip(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Toggle the region's alignment (left/right or top/bottom)"""
    ...

def region_quadview(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Split selected area into camera, front, right, and top views"""
    ...

def region_scale(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Scale selected area"""
    ...

def region_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, region_type: str = ...) -> set[str]:
    """Hide or unhide the region"""
    ...

def repeat_history(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, index: int = ...) -> set[str]:
    """Display menu for previous actions performed"""
    ...

def repeat_last(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Repeat last action"""
    ...

def screen_full_area(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_hide_panels: bool = ...) -> set[str]:
    """Toggle display selected area as fullscreen/maximized"""
    ...

def screen_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, delta: int = ...) -> set[str]:
    """Cycle through available screens"""
    ...

def screenshot(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., show_multiview: bool = ..., use_multiview: bool = ..., display_type: str = ..., sort_method: str = ...) -> set[str]:
    """Capture a picture of the whole Blender window"""
    ...

def screenshot_area(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., show_multiview: bool = ..., use_multiview: bool = ..., display_type: str = ..., sort_method: str = ...) -> set[str]:
    """Capture a picture of an editor"""
    ...

def space_context_cycle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ...) -> set[str]:
    """Cycle through the editor context by activating the next/previous one"""
    ...

def space_type_set_or_cycle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, space_type: str = ...) -> set[str]:
    """Set the space type or cycle subtype"""
    ...

def spacedata_cleanup(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove unused settings for invisible editors"""
    ...

def time_jump(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, backward: bool = ...) -> set[str]:
    """Jump forward/backward by a given number of frames or seconds"""
    ...

def userpref_show(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, section: str = ...) -> set[str]:
    """Edit user preferences and system settings"""
    ...

def workspace_cycle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ...) -> set[str]:
    """Cycle through workspaces"""
    ...
