# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def asset_activate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, asset_library_type: str = ..., asset_library_identifier: str = ..., relative_asset_identifier: str = ..., use_toggle: bool = ...) -> set[str]:
    """Activate a brush asset as current sculpt and paint tool"""
    ...

def asset_delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Delete the active brush asset"""
    ...

def asset_edit_metadata(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, catalog_path: str = ..., author: str = ..., description: str = ...) -> set[str]:
    """Edit asset information like the catalog, preview image, tags, or author"""
    ...

def asset_load_preview(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., show_multiview: bool = ..., use_multiview: bool = ..., display_type: str = ..., sort_method: str = ...) -> set[str]:
    """Choose a preview image for the brush"""
    ...

def asset_revert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Revert the active brush settings to the default values from the asset library"""
    ...

def asset_save(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Update the active brush asset in the asset library with current settings"""
    ...

def asset_save_as(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., asset_library_reference: str = ..., catalog_path: str = ...) -> set[str]:
    """Save a copy of the active brush asset into the default asset library, and make it the active brush"""
    ...

def scale_size(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, scalar: float = ...) -> set[str]:
    """Change brush size by a scalar"""
    ...

def stencil_control(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., texmode: str = ...) -> set[str]:
    """Control the stencil brush"""
    ...

def stencil_fit_image_aspect(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_repeat: bool = ..., use_scale: bool = ..., mask: bool = ...) -> set[str]:
    """When using an image texture, adjust the stencil size to fit the image aspect ratio"""
    ...

def stencil_reset_transform(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mask: bool = ...) -> set[str]:
    """Reset the stencil transformation to the default"""
    ...
