# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def execute_preset(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., menu_idname: str = ...) -> Set[str]:
    """Load a preset"""
    ...

def python_file_run(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ...) -> Set[str]:
    """Run Python file"""
    ...

def reload(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reload scripts"""
    ...
