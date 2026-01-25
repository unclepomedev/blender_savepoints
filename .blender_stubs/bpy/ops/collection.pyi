# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def create(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> Set[str]:
    """Create an object collection from selected objects"""
    ...

def export_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Invoke all configured exporters on this collection"""
    ...

def exporter_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> Set[str]:
    """Add exporter to the exporter list"""
    ...

def exporter_export(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, index: int = ...) -> Set[str]:
    """Invoke the export operation"""
    ...

def exporter_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ...) -> Set[str]:
    """Move exporter up or down in the exporter list"""
    ...

def exporter_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, index: int = ...) -> Set[str]:
    """Remove exporter from the exporter list"""
    ...

def objects_add_active(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, collection: str = ...) -> Set[str]:
    """Add selected objects to one of the collections the active-object is part of. Optionally add to "All Collections" to ensure selected objects are included in the same collections as the active object"""
    ...

def objects_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, collection: str = ...) -> Set[str]:
    """Remove selected objects from a collection"""
    ...

def objects_remove_active(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, collection: str = ...) -> Set[str]:
    """Remove the object from an object collection that contains the active object"""
    ...

def objects_remove_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove selected objects from all collections"""
    ...
