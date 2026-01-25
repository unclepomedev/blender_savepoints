# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def assign_action(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Set this pose Action as active Action on the active Object"""
    ...

def bundle_install(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, asset_library_reference: str = ..., filepath: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ...) -> Set[str]:
    """Copy the current .blend file into an Asset Library. Only works on standalone .blend files (i.e. when no other files are referenced)"""
    ...

def catalog_delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, catalog_id: str = ...) -> Set[str]:
    """Remove an asset catalog from the asset library (contained assets will not be affected and show up as unassigned)"""
    ...

def catalog_new(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, parent_path: str = ...) -> Set[str]:
    """Create a new catalog to put assets in"""
    ...

def catalog_redo(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Redo the last undone edit to the asset catalogs"""
    ...

def catalog_undo(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Undo the last edit to the asset catalogs"""
    ...

def catalog_undo_push(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Store the current state of the asset catalogs in the undo buffer"""
    ...

def catalogs_save(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Make any edits to any catalogs permanent by writing the current set up to the asset library"""
    ...

def clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, set_fake_user: bool = ...) -> Set[str]:
    """Delete all asset metadata and turn the selected asset data-blocks back into normal data-blocks"""
    ...

def clear_single(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, set_fake_user: bool = ...) -> Set[str]:
    """Delete all asset metadata and turn the asset data-block back into a normal data-block"""
    ...

def library_refresh(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reread assets and asset catalogs from the asset library on disk"""
    ...

def mark(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Enable easier reuse of selected data-blocks through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)"""
    ...

def mark_single(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Enable easier reuse of a data-block through the Asset Browser, with the help of customizable metadata (like previews, descriptions and tags)"""
    ...

def open_containing_blend_file(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Open the blend file that contains the active asset"""
    ...

def screenshot_preview(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, p1: int = ..., p2: int = ..., force_square: bool = ...) -> Set[str]:
    """Capture a screenshot to use as a preview for the selected asset"""
    ...

def tag_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a new keyword tag to the active asset"""
    ...

def tag_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove an existing keyword tag from the active asset"""
    ...
