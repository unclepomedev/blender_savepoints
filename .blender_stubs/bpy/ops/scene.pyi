# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Delete active scene"""
    ...

def drop_scene_asset(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, session_uid: int = ...) -> Set[str]:
    """Import scene and set it as the active one in the window"""
    ...

def freestyle_add_edge_marks_to_keying_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add the data paths to the Freestyle Edge Mark property of selected edges to the active keying set"""
    ...

def freestyle_add_face_marks_to_keying_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add the data paths to the Freestyle Face Mark property of selected polygons to the active keying set"""
    ...

def freestyle_alpha_modifier_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Add an alpha transparency modifier to the line style associated with the active lineset"""
    ...

def freestyle_color_modifier_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Add a line color modifier to the line style associated with the active lineset"""
    ...

def freestyle_fill_range_by_selection(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., name: str = ...) -> Set[str]:
    """Fill the Range Min/Max entries by the min/max distance between selected mesh objects and the source object (either a user-specified object or the active camera)"""
    ...

def freestyle_geometry_modifier_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Add a stroke geometry modifier to the line style associated with the active lineset"""
    ...

def freestyle_lineset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a line set into the list of line sets"""
    ...

def freestyle_lineset_copy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy the active line set to the internal clipboard"""
    ...

def freestyle_lineset_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ...) -> Set[str]:
    """Change the position of the active line set within the list of line sets"""
    ...

def freestyle_lineset_paste(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Paste the internal clipboard content to the active line set"""
    ...

def freestyle_lineset_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove the active line set from the list of line sets"""
    ...

def freestyle_linestyle_new(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Create a new line style, reusable by multiple line sets"""
    ...

def freestyle_modifier_copy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Duplicate the modifier within the list of modifiers"""
    ...

def freestyle_modifier_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ...) -> Set[str]:
    """Move the modifier within the list of modifiers"""
    ...

def freestyle_modifier_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove the modifier from the list of modifiers"""
    ...

def freestyle_module_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a style module into the list of modules"""
    ...

def freestyle_module_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ...) -> Set[str]:
    """Change the position of the style module within in the list of style modules"""
    ...

def freestyle_module_open(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., make_internal: bool = ...) -> Set[str]:
    """Open a style module file"""
    ...

def freestyle_module_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove the style module from the stack"""
    ...

def freestyle_stroke_material_create(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Create Freestyle stroke material for testing"""
    ...

def freestyle_thickness_modifier_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Add a line thickness modifier to the line style associated with the active lineset"""
    ...

def gltf2_action_filter_refresh(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Refresh list of actions"""
    ...

def gpencil_brush_preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Add or remove Grease Pencil brush preset"""
    ...

def gpencil_material_preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Add or remove Grease Pencil material preset"""
    ...

def new(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Add new scene by type"""
    ...

def new_sequencer(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Add new scene by type in the sequence editor and assign to active strip"""
    ...

def new_sequencer_scene(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Add new scene to be used by the sequencer"""
    ...

def render_view_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a render view"""
    ...

def render_view_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove the selected render view"""
    ...

def view_layer_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Add a view layer"""
    ...

def view_layer_add_aov(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a Shader AOV"""
    ...

def view_layer_add_lightgroup(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> Set[str]:
    """Add a Light Group"""
    ...

def view_layer_add_used_lightgroups(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add all used Light Groups"""
    ...

def view_layer_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove the selected view layer"""
    ...

def view_layer_remove_aov(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove Active AOV"""
    ...

def view_layer_remove_lightgroup(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove Active Lightgroup"""
    ...

def view_layer_remove_unused_lightgroups(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove all unused Light Groups"""
    ...
