# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def assign_default_button(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set this property's current value as the new default"""
    ...

def button_execute(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, skip_depressed: bool = ...) -> set[str]:
    """Presses active button"""
    ...

def button_string_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Unsets the text of the active button"""
    ...

def copy_as_driver_button(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Create a new driver with this property as input, and copy it to the internal clipboard. Use Paste Driver to add it to the target property, or Paste Driver Variables to extend an existing driver"""
    ...

def copy_data_path_button(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, full_path: bool = ...) -> set[str]:
    """Copy the RNA data path for this property to the clipboard"""
    ...

def copy_driver_to_selected_button(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> set[str]:
    """Copy the property's driver from the active item to the same property of all selected items, if the same property exists"""
    ...

def copy_python_command_button(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy the Python command matching this button"""
    ...

def copy_to_selected_button(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> set[str]:
    """Copy the property's value from the active item to the same property of all selected items if the same property exists"""
    ...

def drop_color(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, color: list[float] = ..., gamma: bool = ..., has_alpha: bool = ...) -> set[str]:
    """Drop colors to buttons"""
    ...

def drop_material(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, session_uid: int = ...) -> set[str]:
    """Drag material to Material slots in Properties"""
    ...

def drop_name(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, string: str = ...) -> set[str]:
    """Drop name to button"""
    ...

def editsource(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Edit UI source code of the active button"""
    ...

def eyedropper_bone(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Sample a bone from the 3D View or the Outliner to store in a property"""
    ...

def eyedropper_color(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, prop_data_path: str = ...) -> set[str]:
    """Sample a color from the Blender window to store in a property"""
    ...

def eyedropper_colorramp(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Sample a color band"""
    ...

def eyedropper_colorramp_point(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Point-sample a color band"""
    ...

def eyedropper_depth(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, prop_data_path: str = ...) -> set[str]:
    """Sample depth from the 3D view"""
    ...

def eyedropper_driver(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mapping_type: str = ...) -> set[str]:
    """Pick a property to use as a driver target"""
    ...

def eyedropper_grease_pencil_color(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., material_mode: str = ...) -> set[str]:
    """Sample a color from the Blender Window and create Grease Pencil material"""
    ...

def eyedropper_id(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Sample a data-block from the 3D View to store in a property"""
    ...

def jump_to_target_button(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Switch to the target object or bone"""
    ...

def list_start_filter(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Start entering filter text for the list in focus"""
    ...

def override_add_button(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> set[str]:
    """Create an override operation"""
    ...

def override_idtemplate_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Delete the selected local override and relink its usages to the linked data-block if possible, else reset it and mark it as non editable"""
    ...

def override_idtemplate_make(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Create a local override of the selected linked data-block, and its hierarchy of dependencies"""
    ...

def override_idtemplate_reset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reset the selected local override to its linked reference values"""
    ...

def override_remove_button(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> set[str]:
    """Remove an override operation"""
    ...

def reloadtranslation(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Force a full reload of UI translation"""
    ...

def reset_default_button(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ...) -> set[str]:
    """Reset this property's value to its default value"""
    ...

def unset_property_button(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear the property and use default or generated value in operators"""
    ...

def view_drop(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Drag and drop onto a data-set or item within the data-set"""
    ...

def view_item_delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Delete selected list item"""
    ...

def view_item_rename(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Rename the active item in the data-set view"""
    ...

def view_item_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, wait_to_deselect_others: bool = ..., use_select_on_click: bool = ..., mouse_x: int = ..., mouse_y: int = ..., extend: bool = ..., range_select: bool = ...) -> set[str]:
    """Activate selected view item"""
    ...

def view_scroll(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(undocumented operator)"""
    ...

def view_start_filter(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Start entering filter text for the data-set in focus"""
    ...
