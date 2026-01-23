# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def annotate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., arrowstyle_start: str = ..., arrowstyle_end: str = ..., use_stabilizer: bool = ..., stabilizer_factor: float = ..., stabilizer_radius: int = ..., stroke: bpy_prop_collection['OperatorStrokeElement'] = ..., wait_for_input: bool = ...) -> Set[str]:
    """Make annotations on the active data"""
    ...

def annotation_active_frame_delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Delete the active frame for the active Annotation Layer"""
    ...

def annotation_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add new Annotation data-block"""
    ...

def data_unlink(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Unlink active Annotation data-block"""
    ...

def layer_annotation_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add new Annotation layer or note for the active data-block"""
    ...

def layer_annotation_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Move the active Annotation layer up/down in the list"""
    ...

def layer_annotation_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove active Annotation layer"""
    ...
