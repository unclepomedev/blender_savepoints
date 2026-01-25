# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a new workspace by duplicating the current one or appending one from the user configuration"""
    ...

def append_activate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, idname: str = ..., filepath: str = ...) -> Set[str]:
    """Append a workspace and make it the active one in the current window"""
    ...

def delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Delete the active workspace"""
    ...

def delete_all_others(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Delete all workspaces except this one"""
    ...

def duplicate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a new workspace"""
    ...

def reorder_to_back(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reorder workspace to be last in the list"""
    ...

def reorder_to_front(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reorder workspace to be first in the list"""
    ...

def scene_pin_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remember the last used scene for the current workspace and switch to it whenever this workspace is activated again"""
    ...
