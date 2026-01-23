# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def package_disable(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Turn off this extension"""
    ...

def package_install(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, repo_directory: str = ..., repo_index: int = ..., pkg_id: str = ..., enable_on_install: bool = ..., url: str = ..., do_legacy_replace: bool = ...) -> set[str]:
    """Download and install the extension"""
    ...

def package_install_files(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filter_glob: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., filepath: str = ..., repo: str = ..., enable_on_install: bool = ..., target: str = ..., overwrite: bool = ..., url: str = ...) -> set[str]:
    """Install extensions from files into a locally managed repository"""
    ...

def package_install_marked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, enable_on_install: bool = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def package_mark_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, pkg_id: str = ..., repo_index: int = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def package_mark_clear_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(undocumented operator)"""
    ...

def package_mark_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, pkg_id: str = ..., repo_index: int = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def package_mark_set_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(undocumented operator)"""
    ...

def package_obsolete_marked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Zeroes package versions, useful for development - to test upgrading"""
    ...

def package_show_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, pkg_id: str = ..., repo_index: int = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def package_show_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, pkg_id: str = ..., repo_index: int = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def package_show_settings(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, pkg_id: str = ..., repo_index: int = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def package_theme_disable(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, pkg_id: str = ..., repo_index: int = ...) -> set[str]:
    """Turn off this theme"""
    ...

def package_theme_enable(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, pkg_id: str = ..., repo_index: int = ...) -> set[str]:
    """Turn off this theme"""
    ...

def package_uninstall(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, repo_directory: str = ..., repo_index: int = ..., pkg_id: str = ...) -> set[str]:
    """Disable and uninstall the extension"""
    ...

def package_uninstall_marked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(undocumented operator)"""
    ...

def package_uninstall_system(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(undocumented operator)"""
    ...

def package_upgrade_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_active_only: bool = ...) -> set[str]:
    """Upgrade all the extensions to their latest version for all the remote repositories"""
    ...

def repo_enable_from_drop(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, repo_index: int = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def repo_lock_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Lock repositories - to test locking"""
    ...

def repo_refresh_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_active_only: bool = ...) -> set[str]:
    """Scan extension & legacy add-ons for changes to modules & meta-data (similar to restarting). Any issues are reported as warnings"""
    ...

def repo_sync(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, repo_directory: str = ..., repo_index: int = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def repo_sync_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_active_only: bool = ...) -> set[str]:
    """Refresh the list of extensions for all the remote repositories"""
    ...

def repo_unlock(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove the repository file-system lock"""
    ...

def repo_unlock_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Unlock repositories - to test unlocking"""
    ...

def status_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(undocumented operator)"""
    ...

def status_clear_errors(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(undocumented operator)"""
    ...

def userpref_allow_online(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Allow internet access. Blender may access configured online extension repositories. Installed third party add-ons may access the internet for their own functionality"""
    ...

def userpref_allow_online_popup(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Allow internet access. Blender may access configured online extension repositories. Installed third party add-ons may access the internet for their own functionality"""
    ...

def userpref_show_for_update(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Open extensions preferences"""
    ...

def userpref_show_online(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Show system preferences "Network" panel to allow online access"""
    ...

def userpref_tags_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: bool = ..., data_path: str = ...) -> set[str]:
    """Set the value of all tags"""
    ...
