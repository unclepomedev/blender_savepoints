# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def apply_pose_asset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, asset_library_type: str = ..., asset_library_identifier: str = ..., relative_asset_identifier: str = ..., blend_factor: float = ..., flipped: bool = ...) -> set[str]:
    """Apply the given Pose Action to the rig"""
    ...

def asset_delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Delete the selected Pose Asset"""
    ...

def asset_modify(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ...) -> set[str]:
    """Update the selected pose asset in the asset library from the currently selected bones. The mode defines how the asset is updated"""
    ...

def blend_pose_asset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, asset_library_type: str = ..., asset_library_identifier: str = ..., relative_asset_identifier: str = ..., blend_factor: float = ..., flipped: bool = ..., release_confirm: bool = ...) -> set[str]:
    """Blend the given Pose Action to the rig"""
    ...

def copy_as_asset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Create a new pose asset on the clipboard, to be pasted into an Asset Browser"""
    ...

def create_pose_asset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, pose_name: str = ..., asset_library_reference: str = ..., catalog_path: str = ...) -> set[str]:
    """Create a new asset from the selected bones in the scene"""
    ...

def paste_asset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Paste the Asset that was previously copied using Copy As Asset"""
    ...

def pose_asset_select_bones(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ..., flipped: bool = ...) -> set[str]:
    """Select those bones that are used in this pose"""
    ...

def restore_previous_action(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Switch back to the previous Action, after creating a pose asset"""
    ...
