# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def entry_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, list_path: str = ..., active_index_path: str = ...) -> Set[str]:
    """Add an entry to the list after the current active item"""
    ...

def entry_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, list_path: str = ..., active_index_path: str = ..., direction: str = ...) -> Set[str]:
    """Move an entry in the list up or down"""
    ...

def entry_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, list_path: str = ..., active_index_path: str = ...) -> Set[str]:
    """Remove the selected entry from the list"""
    ...
