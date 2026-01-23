# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def add_scene_strip_from_scene_asset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, move_strips: bool = ..., frame_start: int = ..., channel: int = ..., replace_sel: bool = ..., overlap: bool = ..., overlap_shuffle_override: bool = ..., skip_locked_or_muted_channels: bool = ..., asset_library_type: str = ..., asset_library_identifier: str = ..., relative_asset_identifier: str = ...) -> set[str]:
    """Add a strip using a duplicate of this scene asset as the source"""
    ...

def box_blade(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., mode: str = ..., type: str = ..., ignore_selection: bool = ..., ignore_connections: bool = ..., remove_gaps: bool = ...) -> set[str]:
    """Draw a box around the parts of strips you want to cut away"""
    ...

def change_effect_type(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Replace effect strip with another that takes the same number of inputs"""
    ...

def change_path(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., display_type: str = ..., sort_method: str = ..., use_placeholders: bool = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def change_scene(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, scene: str = ...) -> set[str]:
    """Change Scene assigned to Strip"""
    ...

def connect(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, toggle: bool = ...) -> set[str]:
    """Link selected strips together for simplified group selection"""
    ...

def copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy the selected strips to the internal clipboard"""
    ...

def crossfade_sounds(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Do cross-fading volume animation of two selected sound strips"""
    ...

def cursor_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[float] = ...) -> set[str]:
    """Set 2D cursor location"""
    ...

def deinterlace_selected_movies(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Deinterlace all selected movie sources"""
    ...

def delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, delete_data: bool = ...) -> set[str]:
    """Delete selected strips from the sequencer"""
    ...

def disconnect(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Unlink selected strips so that they can be selected individually"""
    ...

def duplicate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, linked: bool = ...) -> set[str]:
    """Duplicate the selected strips"""
    ...

def duplicate_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, SEQUENCER_OT_duplicate: 'SEQUENCER_OT_duplicate' = ..., TRANSFORM_OT_seq_slide: 'TRANSFORM_OT_seq_slide' = ...) -> set[str]:
    """Duplicate selected strips and move them"""
    ...

def duplicate_move_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, SEQUENCER_OT_duplicate: 'SEQUENCER_OT_duplicate' = ..., TRANSFORM_OT_seq_slide: 'TRANSFORM_OT_seq_slide' = ...) -> set[str]:
    """Duplicate selected strips, but not their data, and move them"""
    ...

def effect_strip_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., move_strips: bool = ..., frame_start: int = ..., length: int = ..., channel: int = ..., replace_sel: bool = ..., overlap: bool = ..., overlap_shuffle_override: bool = ..., skip_locked_or_muted_channels: bool = ..., color: list[float] = ...) -> set[str]:
    """Add an effect to the sequencer, most are applied on top of existing strips"""
    ...

def enable_proxies(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, proxy_25: bool = ..., proxy_50: bool = ..., proxy_75: bool = ..., proxy_100: bool = ..., overwrite: bool = ...) -> set[str]:
    """Enable selected proxies on all selected Movie and Image strips"""
    ...

def export_subtitles(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ...) -> set[str]:
    """Export .srt file containing text strips"""
    ...

def fades_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, duration_seconds: float = ..., type: str = ...) -> set[str]:
    """Adds or updates a fade animation for either visual or audio strips"""
    ...

def fades_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Removes fade animation from selected strips"""
    ...

def gap_insert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frames: int = ...) -> set[str]:
    """Insert gap at current frame to first strips at the right, independent of selection or locked state of strips"""
    ...

def gap_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> set[str]:
    """Remove gap at current frame to first strip at the right, independent of selection or locked state of strips"""
    ...

def image_strip_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., show_multiview: bool = ..., use_multiview: bool = ..., display_type: str = ..., sort_method: str = ..., move_strips: bool = ..., frame_start: int = ..., length: int = ..., channel: int = ..., replace_sel: bool = ..., overlap: bool = ..., overlap_shuffle_override: bool = ..., skip_locked_or_muted_channels: bool = ..., fit_method: str = ..., set_view_transform: bool = ..., image_import_type: str = ..., use_sequence_detection: bool = ..., use_placeholders: bool = ...) -> set[str]:
    """Add an image or image sequence to the sequencer"""
    ...

def images_separate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, length: int = ...) -> set[str]:
    """On image sequence strips, it returns a strip for each image"""
    ...

def lock(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Lock strips so they cannot be transformed"""
    ...

def mask_strip_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, move_strips: bool = ..., frame_start: int = ..., channel: int = ..., replace_sel: bool = ..., overlap: bool = ..., overlap_shuffle_override: bool = ..., skip_locked_or_muted_channels: bool = ..., mask: str = ...) -> set[str]:
    """Add a mask strip to the sequencer"""
    ...

def meta_make(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Group selected strips into a meta-strip"""
    ...

def meta_separate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Put the contents of a meta-strip back in the sequencer"""
    ...

def meta_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Toggle a meta-strip (to edit enclosed strips)"""
    ...

def movie_strip_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., show_multiview: bool = ..., use_multiview: bool = ..., display_type: str = ..., sort_method: str = ..., move_strips: bool = ..., frame_start: int = ..., channel: int = ..., replace_sel: bool = ..., overlap: bool = ..., overlap_shuffle_override: bool = ..., skip_locked_or_muted_channels: bool = ..., fit_method: str = ..., set_view_transform: bool = ..., adjust_playback_rate: bool = ..., sound: bool = ..., use_framerate: bool = ...) -> set[str]:
    """Add a movie strip to the sequencer"""
    ...

def movieclip_strip_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, move_strips: bool = ..., frame_start: int = ..., channel: int = ..., replace_sel: bool = ..., overlap: bool = ..., overlap_shuffle_override: bool = ..., skip_locked_or_muted_channels: bool = ..., clip: str = ...) -> set[str]:
    """Add a movieclip strip to the sequencer"""
    ...

def mute(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> set[str]:
    """Mute (un)selected strips"""
    ...

def offset_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear strip in/out offsets from the start and end of content"""
    ...

def paste(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, keep_offset: bool = ..., x: int = ..., y: int = ...) -> set[str]:
    """Paste strips from the internal clipboard"""
    ...

def preview_duplicate_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, SEQUENCER_OT_duplicate: 'SEQUENCER_OT_duplicate' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Duplicate selected strips and move them"""
    ...

def preview_duplicate_move_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, SEQUENCER_OT_duplicate: 'SEQUENCER_OT_duplicate' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Duplicate selected strips, but not their data, and move them"""
    ...

def reassign_inputs(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reassign the inputs for the effect strip"""
    ...

def rebuild_proxy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Rebuild all selected proxies and timecode indices"""
    ...

def refresh_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Refresh the sequencer editor"""
    ...

def reload(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, adjust_length: bool = ...) -> set[str]:
    """Reload strips in the sequencer"""
    ...

def rename_channel(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(undocumented operator)"""
    ...

def rendersize(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set render size and aspect from active strip"""
    ...

def retiming_add_freeze_frame_slide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, SEQUENCER_OT_retiming_freeze_frame_add: 'SEQUENCER_OT_retiming_freeze_frame_add' = ..., TRANSFORM_OT_seq_slide: 'TRANSFORM_OT_seq_slide' = ...) -> set[str]:
    """Add freeze frame and move it"""
    ...

def retiming_add_transition_slide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, SEQUENCER_OT_retiming_transition_add: 'SEQUENCER_OT_retiming_transition_add' = ..., TRANSFORM_OT_seq_slide: 'TRANSFORM_OT_seq_slide' = ...) -> set[str]:
    """Add smooth transition between 2 retimed segments and change its duration"""
    ...

def retiming_freeze_frame_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, duration: int = ...) -> set[str]:
    """Add freeze frame"""
    ...

def retiming_key_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, timeline_frame: int = ...) -> set[str]:
    """Add retiming Key"""
    ...

def retiming_key_delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Delete selected retiming keys from the sequencer"""
    ...

def retiming_reset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reset strip retiming"""
    ...

def retiming_segment_speed_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, speed: float = ..., keep_retiming: bool = ...) -> set[str]:
    """Set speed of retimed segment"""
    ...

def retiming_show(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Show retiming keys in selected strips"""
    ...

def retiming_transition_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, duration: int = ...) -> set[str]:
    """Add smooth transition between 2 retimed segments"""
    ...

def sample(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, size: int = ...) -> set[str]:
    """Use mouse to sample color in current frame"""
    ...

def scene_frame_range_update(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Update frame range of scene strip"""
    ...

def scene_strip_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, move_strips: bool = ..., frame_start: int = ..., channel: int = ..., replace_sel: bool = ..., overlap: bool = ..., overlap_shuffle_override: bool = ..., skip_locked_or_muted_channels: bool = ..., scene: str = ...) -> set[str]:
    """Add a strip re-using this scene as the source"""
    ...

def scene_strip_add_new(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, move_strips: bool = ..., frame_start: int = ..., channel: int = ..., replace_sel: bool = ..., overlap: bool = ..., overlap_shuffle_override: bool = ..., skip_locked_or_muted_channels: bool = ..., type: str = ...) -> set[str]:
    """Add a strip using a new scene as the source"""
    ...

def select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, wait_to_deselect_others: bool = ..., use_select_on_click: bool = ..., mouse_x: int = ..., mouse_y: int = ..., extend: bool = ..., deselect: bool = ..., toggle: bool = ..., deselect_all: bool = ..., select_passthrough: bool = ..., center: bool = ..., linked_handle: bool = ..., linked_time: bool = ..., side_of_frame: bool = ..., ignore_connections: bool = ...) -> set[str]:
    """Select a strip (last selected becomes the "active strip")"""
    ...

def select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Select or deselect all strips"""
    ...

def select_box(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., mode: str = ..., tweak: bool = ..., include_handles: bool = ..., ignore_connections: bool = ...) -> set[str]:
    """Select strips using box selection"""
    ...

def select_circle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, x: int = ..., y: int = ..., radius: int = ..., wait_for_input: bool = ..., mode: str = ..., ignore_connections: bool = ...) -> set[str]:
    """Select strips using circle selection"""
    ...

def select_grouped(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., extend: bool = ..., use_active_channel: bool = ...) -> set[str]:
    """Select all strips grouped by various properties"""
    ...

def select_handle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, wait_to_deselect_others: bool = ..., use_select_on_click: bool = ..., mouse_x: int = ..., mouse_y: int = ..., ignore_connections: bool = ...) -> set[str]:
    """Select strip handle"""
    ...

def select_handles(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, side: str = ...) -> set[str]:
    """Select gizmo handles on the sides of the selected strip"""
    ...

def select_lasso(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_smooth_stroke: bool = ..., smooth_stroke_factor: float = ..., smooth_stroke_radius: int = ..., mode: str = ...) -> set[str]:
    """Select strips using lasso selection"""
    ...

def select_less(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Shrink the current selection of adjacent selected strips"""
    ...

def select_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select all strips adjacent to the current selection"""
    ...

def select_linked_pick(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ...) -> set[str]:
    """Select a chain of linked strips nearest to the mouse pointer"""
    ...

def select_more(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select more strips adjacent to the current selection"""
    ...

def select_side(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, side: str = ...) -> set[str]:
    """Select strips on the nominated side of the selected strips"""
    ...

def select_side_of_frame(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., side: str = ...) -> set[str]:
    """Select strips relative to the current frame"""
    ...

def set_range_to_strips(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, preview: bool = ...) -> set[str]:
    """Set the frame range to the selected strips start and end"""
    ...

def slip(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, offset: float = ..., slip_keyframes: bool = ..., use_cursor_position: bool = ..., ignore_connections: bool = ...) -> set[str]:
    """Slip the contents of selected strips"""
    ...

def snap(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frame: int = ...) -> set[str]:
    """Frame where selected strips will be snapped"""
    ...

def sound_strip_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., display_type: str = ..., sort_method: str = ..., move_strips: bool = ..., frame_start: int = ..., channel: int = ..., replace_sel: bool = ..., overlap: bool = ..., overlap_shuffle_override: bool = ..., skip_locked_or_muted_channels: bool = ..., cache: bool = ..., mono: bool = ...) -> set[str]:
    """Add a sound strip to the sequencer"""
    ...

def split(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frame: int = ..., channel: int = ..., type: str = ..., use_cursor_position: bool = ..., side: str = ..., ignore_selection: bool = ..., ignore_connections: bool = ...) -> set[str]:
    """Split the selected strips in two"""
    ...

def split_multicam(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, camera: int = ...) -> set[str]:
    """Split multicam strip and select camera"""
    ...

def strip_color_tag_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, color: str = ...) -> set[str]:
    """Set a color tag for the selected strips"""
    ...

def strip_jump(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, next: bool = ..., center: bool = ...) -> set[str]:
    """Move frame to previous edit point"""
    ...

def strip_modifier_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Add a modifier to the strip"""
    ...

def strip_modifier_copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Copy modifiers of the active strip to all selected strips"""
    ...

def strip_modifier_equalizer_redefine(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, graphs: str = ..., name: str = ...) -> set[str]:
    """Redefine equalizer graphs"""
    ...

def strip_modifier_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., direction: str = ...) -> set[str]:
    """Move modifier up and down in the stack"""
    ...

def strip_modifier_move_to_index(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ..., index: int = ...) -> set[str]:
    """Change the strip modifier's index in the stack so it evaluates after the set number of others"""
    ...

def strip_modifier_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> set[str]:
    """Remove a modifier from the strip"""
    ...

def strip_modifier_set_active(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Activate the strip modifier to use as the context"""
    ...

def strip_transform_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, property: str = ...) -> set[str]:
    """Reset image transformation to default value"""
    ...

def strip_transform_fit(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, fit_method: str = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def swap(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, side: str = ...) -> set[str]:
    """Swap active strip with strip to the right or left"""
    ...

def swap_data(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Swap 2 sequencer strips"""
    ...

def swap_inputs(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Swap the two inputs of the effect strip"""
    ...

def text_cursor_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., select_text: bool = ...) -> set[str]:
    """Move cursor in text"""
    ...

def text_cursor_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select_text: bool = ...) -> set[str]:
    """Set cursor position in text"""
    ...

def text_delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Delete text at cursor position"""
    ...

def text_deselect_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Deselect all characters"""
    ...

def text_edit_copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy text to clipboard"""
    ...

def text_edit_cut(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Cut text to clipboard"""
    ...

def text_edit_mode_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Toggle text editing"""
    ...

def text_edit_paste(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Paste text from clipboard"""
    ...

def text_insert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, string: str = ...) -> set[str]:
    """Insert text at cursor position"""
    ...

def text_line_break(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Insert line break at cursor position"""
    ...

def text_select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select all characters"""
    ...

def unlock(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Unlock strips so they can be transformed"""
    ...

def unmute(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> set[str]:
    """Unmute (un)selected strips"""
    ...

def view_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """View all the strips in the sequencer"""
    ...

def view_all_preview(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Zoom preview to fit in the area"""
    ...

def view_frame(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Move the view to the current frame"""
    ...

def view_ghost_border(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ...) -> set[str]:
    """Set the boundaries of the border used for offset view"""
    ...

def view_selected(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Zoom the sequencer on the selected strips"""
    ...

def view_zoom_ratio(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ratio: float = ...) -> set[str]:
    """Change zoom ratio of sequencer preview"""
    ...
