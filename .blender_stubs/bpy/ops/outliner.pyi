# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def action_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> Set[str]:
    """Change the active action used"""
    ...

def animdata_operation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def clear_filter(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Clear the search filter"""
    ...

def collection_color_tag_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, color: str = ...) -> Set[str]:
    """Set a color tag for the selected collections"""
    ...

def collection_disable(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Disable viewport display in the view layers"""
    ...

def collection_disable_render(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Do not render this collection"""
    ...

def collection_drop(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Drag to move to collection in Outliner"""
    ...

def collection_duplicate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Recursively duplicate the collection, all its children, objects and object data"""
    ...

def collection_duplicate_linked(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Recursively duplicate the collection, all its children and objects, with linked object data"""
    ...

def collection_enable(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Enable viewport display in the view layers"""
    ...

def collection_enable_render(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Render the collection"""
    ...

def collection_exclude_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Include collection in the active view layer"""
    ...

def collection_exclude_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Exclude collection from the active view layer"""
    ...

def collection_hide(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Hide the collection in this view layer"""
    ...

def collection_hide_inside(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Hide all the objects and collections inside the collection"""
    ...

def collection_hierarchy_delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Delete selected collection hierarchies"""
    ...

def collection_holdout_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Clear masking of collection in the active view layer"""
    ...

def collection_holdout_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Mask collection in the active view layer"""
    ...

def collection_indirect_only_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Clear collection contributing only indirectly in the view layer"""
    ...

def collection_indirect_only_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Set collection to only contribute indirectly (through shadows and reflections) in the view layer"""
    ...

def collection_instance(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Instance selected collections to active scene"""
    ...

def collection_isolate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ...) -> Set[str]:
    """Hide all but this collection and its parents"""
    ...

def collection_link(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Link selected collections to active scene"""
    ...

def collection_new(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, nested: bool = ...) -> Set[str]:
    """Add a new collection inside selected collection"""
    ...

def collection_objects_deselect(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Deselect objects in collection"""
    ...

def collection_objects_select(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Select objects in collection"""
    ...

def collection_show(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Show the collection in this view layer"""
    ...

def collection_show_inside(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Show all the objects and collections inside the collection"""
    ...

def constraint_operation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def data_operation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def datastack_drop(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy or reorder modifiers, constraints, and effects"""
    ...

def delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, hierarchy: bool = ...) -> Set[str]:
    """Delete selected objects and collections"""
    ...

def drivers_add_selected(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add drivers to selected items"""
    ...

def drivers_delete_selected(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Delete drivers assigned to selected items"""
    ...

def expanded_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Expand/Collapse all items"""
    ...

def hide(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Hide selected objects and collections"""
    ...

def highlight_update(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Update the item highlight based on the current mouse position"""
    ...

def id_copy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy the selected data-blocks to the internal clipboard"""
    ...

def id_delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Delete the ID under cursor"""
    ...

def id_linked_relocate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Replace the active linked ID (and its dependencies if any) by another one, from the same or a different library"""
    ...

def id_operation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """General data-block management operations"""
    ...

def id_paste(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Paste data-blocks from the internal clipboard"""
    ...

def id_remap(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, id_type: str = ..., old_id: str = ..., new_id: str = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def item_activate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., extend_range: bool = ..., deselect_all: bool = ..., recurse: bool = ...) -> Set[str]:
    """Handle mouse clicks to select and activate items"""
    ...

def item_drag_drop(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Drag and drop element to another place"""
    ...

def item_openclose(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> Set[str]:
    """Toggle whether item under cursor is enabled or closed"""
    ...

def item_rename(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_active: bool = ...) -> Set[str]:
    """Rename the active element"""
    ...

def keyingset_add_selected(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add selected items (blue-gray rows) to active Keying Set"""
    ...

def keyingset_remove_selected(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove selected items (blue-gray rows) from active Keying Set"""
    ...

def lib_operation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def lib_relocate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Relocate the library under cursor"""
    ...

def liboverride_operation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., selection_set: str = ...) -> Set[str]:
    """Create, reset or clear library override hierarchies"""
    ...

def liboverride_troubleshoot_operation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., selection_set: str = ...) -> Set[str]:
    """Advanced operations over library override to help fix broken hierarchies"""
    ...

def material_drop(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Drag material to object in Outliner"""
    ...

def modifier_operation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def object_operation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def operation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Context menu for item operations"""
    ...

def orphans_manage(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Open a window to manage unused data"""
    ...

def orphans_purge(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, do_local_ids: bool = ..., do_linked_ids: bool = ..., do_recursive: bool = ...) -> Set[str]:
    """Clear all orphaned data-blocks without any users from the file"""
    ...

def parent_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Drag to clear parent in Outliner"""
    ...

def parent_drop(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Drag to parent in Outliner"""
    ...

def scene_drop(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Drag object to scene in Outliner"""
    ...

def scene_operation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Context menu for scene operations"""
    ...

def scroll_page(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, up: bool = ...) -> Set[str]:
    """Scroll page up or down"""
    ...

def select_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> Set[str]:
    """Toggle the Outliner selection of items"""
    ...

def select_box(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, tweak: bool = ..., xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., mode: str = ...) -> Set[str]:
    """Use box selection to select tree elements"""
    ...

def select_walk(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., extend: bool = ..., toggle_all: bool = ...) -> Set[str]:
    """Use walk navigation to select tree elements"""
    ...

def show_active(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Open up the tree and adjust the view so that the active object is shown centered"""
    ...

def show_hierarchy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Open all object entries and close all others"""
    ...

def show_one_level(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, open: bool = ...) -> Set[str]:
    """Expand/collapse all entries by one level"""
    ...

def start_filter(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Start entering filter text"""
    ...

def unhide_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Unhide all objects and collections"""
    ...
