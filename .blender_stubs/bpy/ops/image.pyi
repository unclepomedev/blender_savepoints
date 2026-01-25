# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def add_render_slot(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add a new render slot"""
    ...

def change_frame(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, frame: int = ...) -> set[str]:
    """Interactively change the current frame number"""
    ...

def clear_render_border(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear the boundaries of the render region and disable render region"""
    ...

def clear_render_slot(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear the currently selected render slot"""
    ...

def clipboard_copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy the image to the clipboard"""
    ...

def clipboard_paste(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Paste new image from the clipboard"""
    ...

def convert_to_mesh_plane(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, interpolation: str = ..., extension: str = ..., use_auto_refresh: bool = ..., relative: bool = ..., shader: str = ..., emit_strength: float = ..., use_transparency: bool = ..., render_method: str = ..., use_backface_culling: bool = ..., show_transparent_back: bool = ..., overwrite_material: bool = ..., name_from: str = ..., delete_ref: bool = ...) -> set[str]:
    """Convert selected reference images to textured mesh plane"""
    ...

def curves_point_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, point: str = ..., size: int = ...) -> set[str]:
    """Set black point or white point for curves"""
    ...

def cycle_render_slot(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, reverse: bool = ...) -> set[str]:
    """Cycle through all non-void render slots"""
    ...

def external_edit(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ...) -> set[str]:
    """Edit image in an external application"""
    ...

def file_browse(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., show_multiview: bool = ..., use_multiview: bool = ..., display_type: str = ..., sort_method: str = ...) -> set[str]:
    """Open an image file browser, hold Shift to open the file, Alt to browse containing directory"""
    ...

def flip(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_flip_x: bool = ..., use_flip_y: bool = ...) -> set[str]:
    """Flip the image"""
    ...

def import_as_mesh_planes(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, interpolation: str = ..., extension: str = ..., use_auto_refresh: bool = ..., relative: bool = ..., shader: str = ..., emit_strength: float = ..., use_transparency: bool = ..., render_method: str = ..., use_backface_culling: bool = ..., show_transparent_back: bool = ..., overwrite_material: bool = ..., filepath: str = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., directory: str = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_folder: bool = ..., force_reload: bool = ..., image_sequence: bool = ..., offset: bool = ..., offset_axis: str = ..., offset_amount: float = ..., align_axis: str = ..., prev_align_axis: str = ..., align_track: bool = ..., size_mode: str = ..., fill_mode: str = ..., height: float = ..., factor: float = ...) -> set[str]:
    """Create mesh plane(s) from image files with the appropriate aspect ratio"""
    ...

def invert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, invert_r: bool = ..., invert_g: bool = ..., invert_b: bool = ..., invert_a: bool = ...) -> set[str]:
    """Invert image's channels"""
    ...

def match_movie_length(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set image's user's length to the one of this video"""
    ...

def new(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., width: int = ..., height: int = ..., color: list[float] = ..., alpha: bool = ..., generated_type: str = ..., float: bool = ..., use_stereo_3d: bool = ..., tiled: bool = ...) -> set[str]:
    """Create a new image"""
    ...

def open(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, allow_path_tokens: bool = ..., filepath: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., show_multiview: bool = ..., use_multiview: bool = ..., display_type: str = ..., sort_method: str = ..., use_sequence_detection: bool = ..., use_udim_detecting: bool = ...) -> set[str]:
    """Open image"""
    ...

def open_images(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., relative_path: bool = ..., use_sequence_detection: bool = ..., use_udim_detection: bool = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def pack(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Pack an image as embedded data into the .blend file"""
    ...

def project_apply(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Project edited image back onto the object"""
    ...

def project_edit(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Edit a snapshot of the 3D Viewport in an external image editor"""
    ...

def read_viewlayers(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Read all the current scene's view layers from cache, as needed"""
    ...

def reload(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reload current image from disk"""
    ...

def remove_render_slot(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove the current render slot"""
    ...

def render_border(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ...) -> set[str]:
    """Set the boundaries of the render region and enable render region"""
    ...

def replace(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., show_multiview: bool = ..., use_multiview: bool = ..., display_type: str = ..., sort_method: str = ...) -> set[str]:
    """Replace current image by another one from disk"""
    ...

def resize(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, size: list[int] = ..., all_udims: bool = ...) -> set[str]:
    """Resize the image"""
    ...

def rotate_orthogonal(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, degrees: str = ...) -> set[str]:
    """Rotate the image"""
    ...

def sample(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, size: int = ...) -> set[str]:
    """Use mouse to sample a color in current image"""
    ...

def sample_line(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xstart: int = ..., xend: int = ..., ystart: int = ..., yend: int = ..., flip: bool = ..., cursor: int = ...) -> set[str]:
    """Sample a line and show it in Scope panels"""
    ...

def save(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Save the image with current name and settings"""
    ...

def save_all_modified(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Save all modified images"""
    ...

def save_as(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, save_as_render: bool = ..., copy: bool = ..., allow_path_tokens: bool = ..., filepath: str = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., show_multiview: bool = ..., use_multiview: bool = ..., display_type: str = ..., sort_method: str = ...) -> set[str]:
    """Save the image with another name and/or settings"""
    ...

def save_sequence(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Save a sequence of images"""
    ...

def tile_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, number: int = ..., count: int = ..., label: str = ..., fill: bool = ..., color: list[float] = ..., generated_type: str = ..., width: int = ..., height: int = ..., float: bool = ..., alpha: bool = ...) -> set[str]:
    """Adds a tile to the image"""
    ...

def tile_fill(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, color: list[float] = ..., generated_type: str = ..., width: int = ..., height: int = ..., float: bool = ..., alpha: bool = ...) -> set[str]:
    """Fill the current tile with a generated image"""
    ...

def tile_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Removes a tile from the image"""
    ...

def unpack(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, method: str = ..., id: str = ...) -> set[str]:
    """Save an image packed in the .blend file to disk"""
    ...

def view_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, fit_view: bool = ...) -> set[str]:
    """View the entire image"""
    ...

def view_center_cursor(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Center the view so that the cursor is in the middle of the view"""
    ...

def view_cursor_center(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, fit_view: bool = ...) -> set[str]:
    """Set 2D Cursor To Center View location"""
    ...

def view_ndof(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Use a 3D mouse device to pan/zoom the view"""
    ...

def view_pan(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, offset: list[float] = ...) -> set[str]:
    """Pan the view"""
    ...

def view_selected(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """View all selected UVs"""
    ...

def view_zoom(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ..., use_cursor_init: bool = ...) -> set[str]:
    """Zoom in/out the image"""
    ...

def view_zoom_border(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., zoom_out: bool = ...) -> set[str]:
    """Zoom in the view to the nearest item contained in the border"""
    ...

def view_zoom_in(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[float] = ...) -> set[str]:
    """Zoom in the image (centered around 2D cursor)"""
    ...

def view_zoom_out(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[float] = ...) -> set[str]:
    """Zoom out the image (centered around 2D cursor)"""
    ...

def view_zoom_ratio(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ratio: float = ...) -> set[str]:
    """Set zoom ratio of the view"""
    ...
