# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def brush_edit(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, stroke: bpy_prop_collection['OperatorStrokeElement'] = ..., pen_flip: bool = ...) -> Set[str]:
    """Apply a stroke of brush to the particles"""
    ...

def connect_hair(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> Set[str]:
    """Connect hair to the emitter mesh"""
    ...

def copy_particle_systems(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, space: str = ..., remove_target_particles: bool = ..., use_active: bool = ...) -> Set[str]:
    """Copy particle systems from the active object to selected objects"""
    ...

def delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Delete selected particles or keys"""
    ...

def disconnect_hair(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> Set[str]:
    """Disconnect hair from the emitter mesh"""
    ...

def duplicate_particle_system(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_duplicate_settings: bool = ...) -> Set[str]:
    """Duplicate particle system within the active object"""
    ...

def dupliob_copy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Duplicate the current instance object"""
    ...

def dupliob_move_down(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Move instance object down in the list"""
    ...

def dupliob_move_up(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Move instance object up in the list"""
    ...

def dupliob_refresh(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Refresh list of instance objects and their weights"""
    ...

def dupliob_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove the selected instance object"""
    ...

def edited_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Undo all edition performed on the particle system"""
    ...

def hair_dynamics_preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Add or remove a Hair Dynamics Preset"""
    ...

def hide(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> Set[str]:
    """Hide selected particles"""
    ...

def mirror(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Duplicate and mirror the selected particles along the local X axis"""
    ...

def new(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add new particle settings"""
    ...

def new_target(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a new particle target"""
    ...

def particle_edit_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Toggle particle edit mode"""
    ...

def particle_system_remove_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove all particle system within the active object"""
    ...

def rekey(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, keys_number: int = ...) -> Set[str]:
    """Change the number of keys of selected particles (root and tip keys included)"""
    ...

def remove_doubles(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, threshold: float = ...) -> Set[str]:
    """Remove selected particles close enough of others"""
    ...

def reveal(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ...) -> Set[str]:
    """Show hidden particles"""
    ...

def select_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> Set[str]:
    """(De)select all particles' keys"""
    ...

def select_less(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Deselect boundary selected keys of each particle"""
    ...

def select_linked(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Select all keys linked to already selected ones"""
    ...

def select_linked_pick(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, deselect: bool = ..., location: int = ...) -> Set[str]:
    """Select nearest particle from mouse pointer"""
    ...

def select_more(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Select keys linked to boundary selected keys of each particle"""
    ...

def select_random(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ratio: float = ..., seed: int = ..., action: str = ..., type: str = ...) -> Set[str]:
    """Select a randomly distributed set of hair or points"""
    ...

def select_roots(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> Set[str]:
    """Select roots of all visible particles"""
    ...

def select_tips(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> Set[str]:
    """Select tips of all visible particles"""
    ...

def shape_cut(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Cut hair to conform to the set shape object"""
    ...

def subdivide(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Subdivide selected particles segments (adds keys)"""
    ...

def target_move_down(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Move particle target down in the list"""
    ...

def target_move_up(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Move particle target up in the list"""
    ...

def target_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove the selected particle target"""
    ...

def unify_length(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Make selected hair the same length"""
    ...

def weight_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ...) -> Set[str]:
    """Set the weight of selected keys"""
    ...
