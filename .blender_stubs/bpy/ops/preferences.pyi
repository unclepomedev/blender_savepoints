# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def addon_disable(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, module: str = ...) -> set[str]:
    """Turn off this add-on"""
    ...

def addon_enable(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, module: str = ...) -> set[str]:
    """Turn on this add-on"""
    ...

def addon_expand(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, module: str = ...) -> set[str]:
    """Display information and preferences for this add-on"""
    ...

def addon_install(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, overwrite: bool = ..., enable_on_install: bool = ..., target: str = ..., filepath: str = ..., filter_folder: bool = ..., filter_python: bool = ..., filter_glob: str = ...) -> set[str]:
    """Install an add-on"""
    ...

def addon_refresh(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Scan add-on directories for new modules"""
    ...

def addon_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, module: str = ...) -> set[str]:
    """Delete the add-on from the file system"""
    ...

def addon_show(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, module: str = ...) -> set[str]:
    """Show add-on preferences"""
    ...

def app_template_install(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, overwrite: bool = ..., filepath: str = ..., filter_folder: bool = ..., filter_glob: str = ...) -> set[str]:
    """Install an application template"""
    ...

def asset_library_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, directory: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ...) -> set[str]:
    """Add a directory to be used by the Asset Browser as source of assets"""
    ...

def asset_library_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, index: int = ...) -> set[str]:
    """Remove a path to a .blend file, so the Asset Browser will not attempt to show it anymore"""
    ...

def associate_blend(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Use this installation for .blend files and to display thumbnails"""
    ...

def autoexec_path_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add path to exclude from auto-execution"""
    ...

def autoexec_path_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, index: int = ...) -> set[str]:
    """Remove path to exclude from auto-execution"""
    ...

def clear_filter(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear the search filter"""
    ...

def copy_prev(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy settings from previous version"""
    ...

def extension_repo_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remote_url: str = ..., use_access_token: bool = ..., access_token: str = ..., use_sync_on_startup: bool = ..., use_custom_directory: bool = ..., custom_directory: str = ..., type: str = ...) -> set[str]:
    """Add a new repository used to store extensions"""
    ...

def extension_repo_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, index: int = ..., remove_files: bool = ...) -> set[str]:
    """Remove an extension repository"""
    ...

def extension_url_drop(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, url: str = ...) -> set[str]:
    """Handle dropping an extension URL"""
    ...

def keyconfig_activate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def keyconfig_export(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ..., filepath: str = ..., filter_folder: bool = ..., filter_text: bool = ..., filter_python: bool = ...) -> set[str]:
    """Export key configuration to a Python script"""
    ...

def keyconfig_import(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., filter_folder: bool = ..., filter_text: bool = ..., filter_python: bool = ..., keep_original: bool = ...) -> set[str]:
    """Import key configuration from a Python script"""
    ...

def keyconfig_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove key config"""
    ...

def keyconfig_test(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Test key configuration for conflicts"""
    ...

def keyitem_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add key map item"""
    ...

def keyitem_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, item_id: int = ...) -> set[str]:
    """Remove key map item"""
    ...

def keyitem_restore(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, item_id: int = ...) -> set[str]:
    """Restore key map item"""
    ...

def keymap_restore(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> set[str]:
    """Restore key map(s)"""
    ...

def reset_default_theme(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reset to the default theme colors"""
    ...

def script_directory_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, directory: str = ..., filter_folder: bool = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def script_directory_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, index: int = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def start_filter(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Start entering filter text"""
    ...

def studiolight_copy_settings(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, index: int = ...) -> set[str]:
    """Copy Studio Light settings to the Studio Light editor"""
    ...

def studiolight_install(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, files: bpy_prop_collection['OperatorFileListElement'] = ..., directory: str = ..., filter_folder: bool = ..., filter_glob: str = ..., type: str = ...) -> set[str]:
    """Install a user defined light"""
    ...

def studiolight_new(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filename: str = ...) -> set[str]:
    """Save custom studio light from the studio light editor settings"""
    ...

def studiolight_uninstall(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, index: int = ...) -> set[str]:
    """Delete Studio Light"""
    ...

def theme_install(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, overwrite: bool = ..., filepath: str = ..., filter_folder: bool = ..., filter_glob: str = ...) -> set[str]:
    """Load and apply a Blender XML theme file"""
    ...

def unassociate_blend(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove this installation's associations with .blend files"""
    ...
