# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def activate_viewer(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Activate selected viewer node in compositor and geometry nodes"""
    ...

def add_closure_zone(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, settings: bpy_prop_collection['NodeSetting'] = ..., use_transform: bool = ..., offset: float = ...) -> Set[str]:
    """Add a Closure zone"""
    ...

def add_collection(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., session_uid: int = ...) -> Set[str]:
    """Add a collection info node to the current node editor"""
    ...

def add_color(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, color: float = ..., gamma: bool = ..., has_alpha: bool = ...) -> Set[str]:
    """Add a color node to the current node editor"""
    ...

def add_empty_group(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, settings: bpy_prop_collection['NodeSetting'] = ..., use_transform: bool = ...) -> Set[str]:
    """Add a group node with an empty group"""
    ...

def add_foreach_geometry_element_zone(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, settings: bpy_prop_collection['NodeSetting'] = ..., use_transform: bool = ..., offset: float = ...) -> Set[str]:
    """Add a For Each Geometry Element zone that allows executing nodes e.g. for each vertex separately"""
    ...

def add_group(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., session_uid: int = ..., show_datablock_in_node: bool = ...) -> Set[str]:
    """Add an existing node group to the current node editor"""
    ...

def add_group_asset(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, asset_library_type: str = ..., asset_library_identifier: str = ..., relative_asset_identifier: str = ...) -> Set[str]:
    """Add a node group asset to the active node tree"""
    ...

def add_group_input_node(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, socket_identifier: str = ..., panel_identifier: int = ...) -> Set[str]:
    """Add a Group Input node with selected sockets to the current node editor"""
    ...

def add_image(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., show_multiview: bool = ..., use_multiview: bool = ..., display_type: str = ..., sort_method: str = ..., name: str = ..., session_uid: int = ...) -> Set[str]:
    """Add a image/movie file as node to the current node editor"""
    ...

def add_import_node(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ...) -> Set[str]:
    """Add an import node to the node tree"""
    ...

def add_mask(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., session_uid: int = ...) -> Set[str]:
    """Add a mask node to the current node editor"""
    ...

def add_material(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., session_uid: int = ...) -> Set[str]:
    """Add a material node to the current node editor"""
    ...

def add_node(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, settings: bpy_prop_collection['NodeSetting'] = ..., use_transform: bool = ..., type: str = ..., visible_output: str = ...) -> Set[str]:
    """Add a node to the active tree"""
    ...

def add_object(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., session_uid: int = ...) -> Set[str]:
    """Add an object info node to the current node editor"""
    ...

def add_repeat_zone(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, settings: bpy_prop_collection['NodeSetting'] = ..., use_transform: bool = ..., offset: float = ...) -> Set[str]:
    """Add a repeat zone that allows executing nodes a dynamic number of times"""
    ...

def add_reroute(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., cursor: int = ...) -> Set[str]:
    """Add a reroute node"""
    ...

def add_simulation_zone(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, settings: bpy_prop_collection['NodeSetting'] = ..., use_transform: bool = ..., offset: float = ...) -> Set[str]:
    """Add simulation zone input and output nodes to the active tree"""
    ...

def add_zone(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, settings: bpy_prop_collection['NodeSetting'] = ..., use_transform: bool = ..., offset: float = ..., input_node_type: str = ..., output_node_type: str = ..., add_default_geometry_link: bool = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def attach(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Attach active node to a frame"""
    ...

def backimage_fit(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Fit the background image to the view"""
    ...

def backimage_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Move node backdrop"""
    ...

def backimage_sample(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Use mouse to sample background image"""
    ...

def backimage_zoom(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, factor: float = ...) -> Set[str]:
    """Zoom in/out the background image"""
    ...

def bake_node_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def bake_node_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def bake_node_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def capture_attribute_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def capture_attribute_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def capture_attribute_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def clear_viewer_border(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Clear the boundaries for viewer operations"""
    ...

def clipboard_copy(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy the selected nodes to the internal clipboard"""
    ...

def clipboard_paste(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, offset: float = ...) -> Set[str]:
    """Paste nodes from the internal clipboard to the active node tree"""
    ...

def closure_input_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def closure_input_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def closure_input_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def closure_output_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def closure_output_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def closure_output_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def collapse_hide_unused_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Toggle collapsed nodes and hide unused sockets"""
    ...

def combine_bundle_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def combine_bundle_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def combine_bundle_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def connect_to_output(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, run_in_geometry_nodes: bool = ...) -> Set[str]:
    """Connect active node to the active output node of the node tree"""
    ...

def cryptomatte_layer_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a new input layer to a Cryptomatte node"""
    ...

def cryptomatte_layer_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove layer from a Cryptomatte node"""
    ...

def deactivate_viewer(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Deactivate selected viewer node in geometry nodes"""
    ...

def default_group_width_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Set the width based on the parent group node in the current context"""
    ...

def delete(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove selected nodes"""
    ...

def delete_reconnect(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove nodes and reconnect nodes as if deletion was muted"""
    ...

def detach(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Detach selected nodes from parents"""
    ...

def detach_translate_attach(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, NODE_OT_detach: 'NODE_OT_detach' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ..., NODE_OT_attach: 'NODE_OT_attach' = ...) -> Set[str]:
    """Detach nodes, move and attach to frame"""
    ...

def duplicate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, keep_inputs: bool = ..., linked: bool = ...) -> Set[str]:
    """Duplicate selected nodes"""
    ...

def duplicate_compositing_node_group(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Duplicate the currently assigned compositing node group."""
    ...

def duplicate_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, NODE_OT_duplicate: 'NODE_OT_duplicate' = ..., NODE_OT_translate_attach: 'NODE_OT_translate_attach' = ...) -> Set[str]:
    """Duplicate selected nodes and move them"""
    ...

def duplicate_move_keep_inputs(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, NODE_OT_duplicate: 'NODE_OT_duplicate' = ..., NODE_OT_translate_attach: 'NODE_OT_translate_attach' = ...) -> Set[str]:
    """Duplicate selected nodes keeping input links and move them"""
    ...

def duplicate_move_linked(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, NODE_OT_duplicate: 'NODE_OT_duplicate' = ..., NODE_OT_translate_attach: 'NODE_OT_translate_attach' = ...) -> Set[str]:
    """Duplicate selected nodes, but not their node trees, and move them"""
    ...

def enum_definition_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def enum_definition_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def enum_definition_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def evaluate_closure_input_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def evaluate_closure_input_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def evaluate_closure_input_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def evaluate_closure_output_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def evaluate_closure_output_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def evaluate_closure_output_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def field_to_grid_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def field_to_grid_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def field_to_grid_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def file_output_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def file_output_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def file_output_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def find_node(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Search for a node by name and focus and select it"""
    ...

def foreach_geometry_element_zone_generation_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def foreach_geometry_element_zone_generation_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def foreach_geometry_element_zone_generation_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def foreach_geometry_element_zone_input_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def foreach_geometry_element_zone_input_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def foreach_geometry_element_zone_input_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def foreach_geometry_element_zone_main_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def foreach_geometry_element_zone_main_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def foreach_geometry_element_zone_main_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def format_string_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def format_string_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def format_string_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def geometry_nodes_viewer_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def geometry_nodes_viewer_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def geometry_nodes_viewer_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def gltf_settings_node_operator(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a node to the active tree for glTF export"""
    ...

def group_edit(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, exit: bool = ...) -> Set[str]:
    """Edit node group"""
    ...

def group_enter_exit(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Enter or exit node group based on cursor location"""
    ...

def group_insert(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Insert selected nodes into a node group"""
    ...

def group_make(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Make group from selected nodes"""
    ...

def group_separate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Separate selected nodes from the node group"""
    ...

def group_ungroup(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Ungroup selected nodes"""
    ...

def hide_socket_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Toggle unused node socket display"""
    ...

def hide_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Toggle collapsing of selected nodes"""
    ...

def index_switch_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add an item to the index switch"""
    ...

def index_switch_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, index: int = ...) -> Set[str]:
    """Remove an item from the index switch"""
    ...

def insert_offset(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Automatically offset nodes on insertion"""
    ...

def interface_item_duplicate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a copy of the active item to the interface"""
    ...

def interface_item_make_panel_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Make the active boolean socket a toggle for its parent panel"""
    ...

def interface_item_new(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, item_type: str = ...) -> Set[str]:
    """Add a new item to the interface"""
    ...

def interface_item_new_panel_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Add a checkbox to the currently selected panel"""
    ...

def interface_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove active item from the interface"""
    ...

def interface_item_unlink_panel_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Make the panel toggle a stand-alone socket"""
    ...

def join(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Attach selected nodes to a new common frame"""
    ...

def join_named(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, NODE_OT_join: 'NODE_OT_join' = ..., WM_OT_call_panel: 'WM_OT_call_panel' = ...) -> Set[str]:
    """Create a new frame node around the selected nodes and name it immediately"""
    ...

def join_nodes(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Merge selected group input nodes into one if possible"""
    ...

def link(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, detach: bool = ..., drag_start: float = ..., inside_padding: float = ..., outside_padding: float = ..., speed_ramp: float = ..., max_speed: float = ..., delay: float = ..., zoom_influence: float = ...) -> Set[str]:
    """Use the mouse to create a link between two nodes"""
    ...

def link_make(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, replace: bool = ...) -> Set[str]:
    """Make a link between selected output and input sockets"""
    ...

def link_viewer(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Link to viewer node"""
    ...

def links_cut(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., cursor: int = ...) -> Set[str]:
    """Use the mouse to cut (remove) some links"""
    ...

def links_detach(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Remove all links to selected nodes, and try to connect neighbor nodes together"""
    ...

def links_mute(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., cursor: int = ...) -> Set[str]:
    """Use the mouse to mute links"""
    ...

def move_detach_links(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, NODE_OT_links_detach: 'NODE_OT_links_detach' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> Set[str]:
    """Move a node to detach links"""
    ...

def move_detach_links_release(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, NODE_OT_links_detach: 'NODE_OT_links_detach' = ..., NODE_OT_translate_attach: 'NODE_OT_translate_attach' = ...) -> Set[str]:
    """Move a node to detach links"""
    ...

def mute_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Toggle muting of selected nodes"""
    ...

def new_compositing_node_group(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> Set[str]:
    """Create a new compositing node group and initialize it with default nodes"""
    ...

def new_compositor_sequencer_node_group(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> Set[str]:
    """Create a new compositor node group for sequencer"""
    ...

def new_geometry_node_group_assign(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Create a new geometry node group and assign it to the active modifier"""
    ...

def new_geometry_node_group_tool(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Create a new geometry node group for a tool"""
    ...

def new_geometry_nodes_modifier(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Create a new modifier with a new geometry node group"""
    ...

def new_node_tree(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., name: str = ...) -> Set[str]:
    """Create a new node tree"""
    ...

def node_color_preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Add or remove a Node Color Preset"""
    ...

def node_copy_color(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Copy color to all selected nodes"""
    ...

def options_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Toggle option buttons display for selected nodes"""
    ...

def parent_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Attach selected nodes"""
    ...

def preview_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Toggle preview display for selected nodes"""
    ...

def read_viewlayers(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Read all render layers of all used scenes"""
    ...

def render_changed(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Render current scene, when input node's layer has been changed"""
    ...

def repeat_zone_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def repeat_zone_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def repeat_zone_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def resize(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Resize a node"""
    ...

def select(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., deselect: bool = ..., toggle: bool = ..., deselect_all: bool = ..., select_passthrough: bool = ..., location: int = ..., socket_select: bool = ..., clear_viewer: bool = ...) -> Set[str]:
    """Select the node under the cursor"""
    ...

def select_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> Set[str]:
    """(De)select all nodes"""
    ...

def select_box(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, tweak: bool = ..., xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., mode: str = ...) -> Set[str]:
    """Use box selection to select nodes"""
    ...

def select_circle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, x: int = ..., y: int = ..., radius: int = ..., wait_for_input: bool = ..., mode: str = ...) -> Set[str]:
    """Use circle selection to select nodes"""
    ...

def select_grouped(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., type: str = ...) -> Set[str]:
    """Select nodes with similar properties"""
    ...

def select_lasso(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, tweak: bool = ..., path: bpy_prop_collection['OperatorMousePath'] = ..., use_smooth_stroke: bool = ..., smooth_stroke_factor: float = ..., smooth_stroke_radius: int = ..., mode: str = ...) -> Set[str]:
    """Select nodes using lasso selection"""
    ...

def select_link_viewer(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, NODE_OT_select: 'NODE_OT_select' = ..., NODE_OT_link_viewer: 'NODE_OT_link_viewer' = ...) -> Set[str]:
    """Select node and link it to a viewer node"""
    ...

def select_linked_from(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Select nodes linked from the selected ones"""
    ...

def select_linked_to(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Select nodes linked to the selected ones"""
    ...

def select_same_type_step(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, prev: bool = ...) -> Set[str]:
    """Activate and view same node type, step by step"""
    ...

def separate_bundle_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def separate_bundle_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def separate_bundle_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def shader_script_update(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Update shader script node with new sockets and options from the script"""
    ...

def simulation_zone_item_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Add item below active item"""
    ...

def simulation_zone_item_move(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., node_identifier: int = ...) -> Set[str]:
    """Move active item"""
    ...

def simulation_zone_item_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_identifier: int = ...) -> Set[str]:
    """Remove active item"""
    ...

def sockets_sync(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, node_name: str = ...) -> Set[str]:
    """Update sockets to match what is actually used"""
    ...

def swap_empty_group(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, settings: bpy_prop_collection['NodeSetting'] = ...) -> Set[str]:
    """Replace active node with an empty group"""
    ...

def swap_group_asset(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, asset_library_type: str = ..., asset_library_identifier: str = ..., relative_asset_identifier: str = ...) -> Set[str]:
    """Swap selected nodes with the specified node group asset"""
    ...

def swap_node(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, settings: bpy_prop_collection['NodeSetting'] = ..., type: str = ..., visible_output: str = ...) -> Set[str]:
    """Replace the selected nodes with the specified type"""
    ...

def swap_zone(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, settings: bpy_prop_collection['NodeSetting'] = ..., offset: float = ..., input_node_type: str = ..., output_node_type: str = ..., add_default_geometry_link: bool = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def test_inlining_shader_nodes(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Create a new inlined shader node tree as is consumed by renderers"""
    ...

def toggle_viewer(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Toggle selected viewer node in compositor and geometry nodes"""
    ...

def translate_attach(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ..., NODE_OT_attach: 'NODE_OT_attach' = ...) -> Set[str]:
    """Move nodes and attach to frame"""
    ...

def translate_attach_remove_on_cancel(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ..., NODE_OT_attach: 'NODE_OT_attach' = ...) -> Set[str]:
    """Move nodes and attach to frame"""
    ...

def tree_path_parent(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, parent_tree_index: int = ...) -> Set[str]:
    """Go to parent node tree"""
    ...

def view_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Resize view so you can see all nodes"""
    ...

def view_selected(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Resize view so you can see selected nodes"""
    ...

def viewer_border(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ...) -> Set[str]:
    """Set the boundaries for viewer operations"""
    ...

def viewer_shortcut_get(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, viewer_index: int = ...) -> Set[str]:
    """Toggle a specific viewer node using 1,2,..,9 keys"""
    ...

def viewer_shortcut_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, viewer_index: int = ...) -> Set[str]:
    """Create a viewer shortcut for the selected node by pressing ctrl+1,2,..9"""
    ...
