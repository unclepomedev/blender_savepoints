# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, radius: float = ..., type: str = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add an object to the scene"""
    ...

def add_modifier_menu(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(undocumented operator)"""
    ...

def add_named(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, linked: bool = ..., name: str = ..., session_uid: int = ..., matrix: list[float] = ..., drop_x: int = ..., drop_y: int = ...) -> set[str]:
    """Add named object"""
    ...

def align(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, bb_quality: bool = ..., align_mode: str = ..., relative_to: str = ..., align_axis: set[str] = ...) -> set[str]:
    """Align objects"""
    ...

def anim_transforms_to_deltas(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Convert object animation for normal transforms to delta transforms"""
    ...

def armature_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, radius: float = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add an armature object to the scene"""
    ...

def assign_property_defaults(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, process_data: bool = ..., process_bones: bool = ...) -> set[str]:
    """Assign the current values of custom properties as their defaults, for use as part of the rest pose state in NLA track mixing"""
    ...

def bake(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., pass_filter: set[str] = ..., filepath: str = ..., width: int = ..., height: int = ..., margin: int = ..., margin_type: str = ..., use_selected_to_active: bool = ..., max_ray_distance: float = ..., cage_extrusion: float = ..., cage_object: str = ..., normal_space: str = ..., normal_r: str = ..., normal_g: str = ..., normal_b: str = ..., target: str = ..., save_mode: str = ..., use_clear: bool = ..., use_cage: bool = ..., use_split_materials: bool = ..., use_automatic_name: bool = ..., uv_layer: str = ...) -> set[str]:
    """Bake image textures of selected objects"""
    ...

def bake_image(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Bake image textures of selected objects"""
    ...

def camera_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add a camera object to the scene"""
    ...

def camera_custom_update(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Update custom camera with new parameters from the shader"""
    ...

def clear_override_library(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Delete the selected local overrides and relink their usages to the linked data-blocks if possible, else reset them and mark them as non editable"""
    ...

def collection_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add an object to a new collection"""
    ...

def collection_external_asset_drop(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, session_uid: int = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ..., use_instance: bool = ..., drop_x: int = ..., drop_y: int = ..., collection: str = ...) -> set[str]:
    """Add the dragged collection to the scene"""
    ...

def collection_instance_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., collection: str = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ..., session_uid: int = ..., drop_x: int = ..., drop_y: int = ...) -> set[str]:
    """Add a collection instance"""
    ...

def collection_link(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, collection: str = ...) -> set[str]:
    """Add an object to an existing collection"""
    ...

def collection_objects_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select all objects in collection"""
    ...

def collection_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove the active object from this collection"""
    ...

def collection_unlink(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Unlink the collection from all objects"""
    ...

def constraint_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Add a constraint to the active object"""
    ...

def constraint_add_with_targets(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Add a constraint to the active object, with target (where applicable) set to the selected objects/bones"""
    ...

def constraints_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear all constraints from the selected objects"""
    ...

def constraints_copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy constraints to other selected objects"""
    ...

def convert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, target: str = ..., keep_original: bool = ..., merge_customdata: bool = ..., thickness: int = ..., faces: bool = ..., offset: float = ...) -> set[str]:
    """Convert selected objects to another type"""
    ...

def copy_global_transform(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copies the matrix of the currently active object or pose bone to the clipboard. Uses world-space matrices"""
    ...

def copy_relative_transform(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copies the matrix of the currently active object or pose bone to the clipboard. Uses matrices relative to a specific object or the active scene camera"""
    ...

def correctivesmooth_bind(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Bind base pose in Corrective Smooth modifier"""
    ...

def curves_empty_hair_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add an empty curve object to the scene with the selected mesh as surface"""
    ...

def curves_random_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add a curves object with random curves to the scene"""
    ...

def data_instance_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., session_uid: int = ..., type: str = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ..., drop_x: int = ..., drop_y: int = ...) -> set[str]:
    """Add an object data instance"""
    ...

def data_transfer(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_reverse_transfer: bool = ..., use_freeze: bool = ..., data_type: str = ..., use_create: bool = ..., vert_mapping: str = ..., edge_mapping: str = ..., loop_mapping: str = ..., poly_mapping: str = ..., use_auto_transform: bool = ..., use_object_transform: bool = ..., use_max_distance: bool = ..., max_distance: float = ..., ray_radius: float = ..., islands_precision: float = ..., layers_select_src: str = ..., layers_select_dst: str = ..., mix_mode: str = ..., mix_factor: float = ...) -> set[str]:
    """Transfer data layer(s) (weights, edge sharp, etc.) from active to selected meshes"""
    ...

def datalayout_transfer(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ..., data_type: str = ..., use_delete: bool = ..., layers_select_src: str = ..., layers_select_dst: str = ...) -> set[str]:
    """Transfer layout of data layer(s) from active to selected meshes"""
    ...

def delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_global: bool = ..., confirm: bool = ...) -> set[str]:
    """Delete selected objects"""
    ...

def delete_fix_to_camera_keys(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Delete all keys that were generated by the 'Fix to Scene Camera' operator"""
    ...

def drop_geometry_nodes(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, session_uid: int = ..., show_datablock_in_modifier: bool = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def drop_named_material(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., session_uid: int = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def duplicate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, linked: bool = ..., mode: str = ...) -> set[str]:
    """Duplicate selected objects"""
    ...

def duplicate_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, OBJECT_OT_duplicate: 'OBJECT_OT_duplicate' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Duplicate the selected objects and move them"""
    ...

def duplicate_move_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, OBJECT_OT_duplicate: 'OBJECT_OT_duplicate' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Duplicate the selected objects, but not their object data, and move them"""
    ...

def duplicates_make_real(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_base_parent: bool = ..., use_hierarchy: bool = ...) -> set[str]:
    """Make instanced objects attached to this object real"""
    ...

def editmode_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Toggle object's edit mode"""
    ...

def effector_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., radius: float = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add an empty object with a physics effector to the scene"""
    ...

def empty_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., radius: float = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add an empty object to the scene"""
    ...

def empty_image_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., show_multiview: bool = ..., use_multiview: bool = ..., display_type: str = ..., sort_method: str = ..., name: str = ..., session_uid: int = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ..., background: bool = ...) -> set[str]:
    """Add an empty image type to scene with data"""
    ...

def explode_refresh(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Refresh data in the Explode modifier"""
    ...

def fix_to_camera(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_location: bool = ..., use_rotation: bool = ..., use_scale: bool = ...) -> set[str]:
    """Generate new keys to fix the selected object/bone to the camera on unkeyed frames"""
    ...

def forcefield_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Toggle object's force field"""
    ...

def geometry_node_bake_delete_single(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, session_uid: int = ..., modifier_name: str = ..., bake_id: int = ...) -> set[str]:
    """Delete baked data of a single bake node or simulation"""
    ...

def geometry_node_bake_pack_single(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, session_uid: int = ..., modifier_name: str = ..., bake_id: int = ...) -> set[str]:
    """Pack baked data from disk into the .blend file"""
    ...

def geometry_node_bake_single(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, session_uid: int = ..., modifier_name: str = ..., bake_id: int = ...) -> set[str]:
    """Bake a single bake node or simulation"""
    ...

def geometry_node_bake_unpack_single(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, session_uid: int = ..., modifier_name: str = ..., bake_id: int = ..., method: str = ...) -> set[str]:
    """Unpack baked data from the .blend file to disk"""
    ...

def geometry_node_tree_copy_assign(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Duplicate the active geometry node group and assign it to the active modifier"""
    ...

def geometry_nodes_input_attribute_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, input_name: str = ..., modifier_name: str = ...) -> set[str]:
    """Switch between an attribute and a single value to define the data for every element"""
    ...

def geometry_nodes_move_to_nodes(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_selected_objects: bool = ...) -> set[str]:
    """Move inputs and outputs from in the modifier to a new node group"""
    ...

def grease_pencil_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., use_in_front: bool = ..., stroke_depth_offset: float = ..., use_lights: bool = ..., stroke_depth_order: str = ..., radius: float = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add a Grease Pencil object to the scene"""
    ...

def grease_pencil_dash_modifier_segment_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Add a segment to the dash modifier"""
    ...

def grease_pencil_dash_modifier_segment_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ..., type: str = ...) -> set[str]:
    """Move the active dash segment up or down"""
    ...

def grease_pencil_dash_modifier_segment_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ..., index: int = ...) -> set[str]:
    """Remove the active segment from the dash modifier"""
    ...

def grease_pencil_time_modifier_segment_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Add a segment to the time modifier"""
    ...

def grease_pencil_time_modifier_segment_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ..., type: str = ...) -> set[str]:
    """Move the active time segment up or down"""
    ...

def grease_pencil_time_modifier_segment_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ..., index: int = ...) -> set[str]:
    """Remove the active segment from the time modifier"""
    ...

def hide_collection(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, collection_index: int = ..., toggle: bool = ..., extend: bool = ...) -> set[str]:
    """Show only objects in collection (Shift to extend)"""
    ...

def hide_render_clear_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reveal all render objects by setting the hide render flag"""
    ...

def hide_view_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ...) -> set[str]:
    """Reveal temporarily hidden objects"""
    ...

def hide_view_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> set[str]:
    """Temporarily hide objects from the viewport"""
    ...

def hook_add_newob(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Hook selected vertices to a newly created object"""
    ...

def hook_add_selob(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_bone: bool = ...) -> set[str]:
    """Hook selected vertices to the first selected object"""
    ...

def hook_assign(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Assign the selected vertices to a hook"""
    ...

def hook_recenter(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Set hook center to cursor position"""
    ...

def hook_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Remove a hook from the active object"""
    ...

def hook_reset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Recalculate and clear offset transformation"""
    ...

def hook_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Select affected vertices on mesh"""
    ...

def instance_offset_from_cursor(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set offset used for collection instances based on cursor position"""
    ...

def instance_offset_from_object(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set offset used for collection instances based on the active object position"""
    ...

def instance_offset_to_cursor(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set cursor position to the offset used for collection instances"""
    ...

def isolate_type_render(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Hide unselected render objects of same type as active by setting the hide render flag"""
    ...

def join(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Join selected objects into active object"""
    ...

def join_shapes(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_mirror: bool = ...) -> set[str]:
    """Add the vertex positions of selected objects as shape keys or update existing shape keys with matching names"""
    ...

def join_uvs(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Transfer UV Maps from active to selected objects (needs matching geometry)"""
    ...

def laplaciandeform_bind(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Bind mesh to system in laplacian deform modifier"""
    ...

def lattice_add_to_selected(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, fit_to_selected: bool = ..., radius: float = ..., margin: float = ..., add_modifiers: bool = ..., resolution_u: int = ..., resolution_v: int = ..., resolution_w: int = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add a lattice and use it to deform selected objects"""
    ...

def light_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., radius: float = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add a light object to the scene"""
    ...

def light_linking_blocker_collection_new(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Create new light linking collection used by the active emitter"""
    ...

def light_linking_blockers_link(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, link_state: str = ...) -> set[str]:
    """Light link selected blockers to the active emitter object"""
    ...

def light_linking_blockers_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select all objects which block light from this emitter"""
    ...

def light_linking_receiver_collection_new(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Create new light linking collection used by the active emitter"""
    ...

def light_linking_receivers_link(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, link_state: str = ...) -> set[str]:
    """Light link selected receivers to the active emitter object"""
    ...

def light_linking_receivers_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select all objects which receive light from this emitter"""
    ...

def light_linking_unlink_from_collection(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove this object or collection from the light linking collection"""
    ...

def lightprobe_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., radius: float = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add a light probe object"""
    ...

def lightprobe_cache_bake(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, subset: str = ...) -> set[str]:
    """Bake irradiance volume light cache"""
    ...

def lightprobe_cache_free(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, subset: str = ...) -> set[str]:
    """Delete cached indirect lighting"""
    ...

def lineart_bake_strokes(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, bake_all: bool = ...) -> set[str]:
    """Bake Line Art for current Grease Pencil object"""
    ...

def lineart_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, clear_all: bool = ...) -> set[str]:
    """Clear all strokes in current Grease Pencil object"""
    ...

def link_to_collection(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, collection_uid: int = ..., is_new: bool = ..., new_collection_name: str = ...) -> set[str]:
    """Link objects to a collection"""
    ...

def location_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, clear_delta: bool = ...) -> set[str]:
    """Clear the object's location"""
    ...

def make_dupli_face(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Convert objects into instanced faces"""
    ...

def make_links_data(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Transfer data from active object to selected objects"""
    ...

def make_links_scene(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, scene: str = ...) -> set[str]:
    """Link selection to another scene"""
    ...

def make_local(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Make library linked data-blocks local to this file"""
    ...

def make_override_library(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, collection: int = ...) -> set[str]:
    """Create a local override of the selected linked objects, and their hierarchy of dependencies"""
    ...

def make_single_user(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., object: bool = ..., obdata: bool = ..., material: bool = ..., animation: bool = ..., obdata_animation: bool = ...) -> set[str]:
    """Make linked data local to each object"""
    ...

def material_slot_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add a new material slot"""
    ...

def material_slot_assign(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Assign active material slot to selection"""
    ...

def material_slot_copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy material to selected objects"""
    ...

def material_slot_deselect(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Deselect by active material slot"""
    ...

def material_slot_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ...) -> set[str]:
    """Move the active material up/down in the list"""
    ...

def material_slot_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove the selected material slot"""
    ...

def material_slot_remove_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove all materials"""
    ...

def material_slot_remove_unused(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove unused material slots"""
    ...

def material_slot_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select by active material slot"""
    ...

def meshdeform_bind(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Bind mesh to cage in mesh deform modifier"""
    ...

def metaball_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., radius: float = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add an metaball object to the scene"""
    ...

def mode_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., toggle: bool = ...) -> set[str]:
    """Sets the object interaction mode"""
    ...

def mode_set_with_submode(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., toggle: bool = ..., mesh_select_mode: set[str] = ...) -> set[str]:
    """Sets the object interaction mode"""
    ...

def modifier_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., use_selected_objects: bool = ...) -> set[str]:
    """Add a procedural operation/effect to the active object"""
    ...

def modifier_add_node_group(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, asset_library_type: str = ..., asset_library_identifier: str = ..., relative_asset_identifier: str = ..., session_uid: int = ..., use_selected_objects: bool = ...) -> set[str]:
    """Add a procedural operation/effect to the active object"""
    ...

def modifier_apply(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ..., report: bool = ..., merge_customdata: bool = ..., single_user: bool = ..., all_keyframes: bool = ..., use_selected_objects: bool = ...) -> set[str]:
    """Apply modifier and remove from the stack"""
    ...

def modifier_apply_as_shapekey(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, keep_modifier: bool = ..., modifier: str = ..., report: bool = ..., use_selected_objects: bool = ...) -> set[str]:
    """Apply modifier as a new shape key and remove from the stack"""
    ...

def modifier_convert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Convert particles to a mesh object"""
    ...

def modifier_copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ..., use_selected_objects: bool = ...) -> set[str]:
    """Duplicate modifier at the same position in the stack"""
    ...

def modifier_copy_to_selected(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Copy the modifier from the active object to all selected objects"""
    ...

def modifier_move_down(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Move modifier down in the stack"""
    ...

def modifier_move_to_index(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ..., index: int = ..., use_selected_objects: bool = ...) -> set[str]:
    """Change the modifier's index in the stack so it evaluates after the set number of others"""
    ...

def modifier_move_up(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Move modifier up in the stack"""
    ...

def modifier_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ..., report: bool = ..., use_selected_objects: bool = ...) -> set[str]:
    """Remove a modifier from the active object"""
    ...

def modifier_set_active(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Activate the modifier to use as the context"""
    ...

def modifiers_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear all modifiers from the selected objects"""
    ...

def modifiers_copy_to_selected(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy modifiers to other selected objects"""
    ...

def move_to_collection(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, collection_uid: int = ..., is_new: bool = ..., new_collection_name: str = ...) -> set[str]:
    """Move objects to a collection"""
    ...

def multires_base_apply(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ..., apply_heuristic: bool = ...) -> set[str]:
    """Modify the base mesh to conform to the displaced mesh"""
    ...

def multires_external_pack(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Pack displacements from an external file"""
    ...

def multires_external_save(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., display_type: str = ..., sort_method: str = ..., modifier: str = ...) -> set[str]:
    """Save displacements to an external file"""
    ...

def multires_higher_levels_delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Deletes the higher resolution mesh, potential loss of detail"""
    ...

def multires_rebuild_subdiv(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Rebuilds all possible subdivisions levels to generate a lower resolution base mesh"""
    ...

def multires_reshape(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Copy vertex coordinates from other object"""
    ...

def multires_subdivide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ..., mode: str = ...) -> set[str]:
    """Add a new level of subdivision"""
    ...

def multires_unsubdivide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Rebuild a lower subdivision level of the current base mesh"""
    ...

def ocean_bake(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ..., free: bool = ...) -> set[str]:
    """Bake an image sequence of ocean data"""
    ...

def origin_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear the object's origin"""
    ...

def origin_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., center: str = ...) -> set[str]:
    """Set the object's origin, by either moving the data, or set to center of data, or use 3D cursor"""
    ...

def parent_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Clear the object's parenting"""
    ...

def parent_inverse_apply(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Apply the object's parent inverse to its data"""
    ...

def parent_no_inverse_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, keep_transform: bool = ...) -> set[str]:
    """Set the object's parenting without setting the inverse parent correction"""
    ...

def parent_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., xmirror: bool = ..., keep_transform: bool = ...) -> set[str]:
    """Set the object's parenting"""
    ...

def particle_system_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add a particle system"""
    ...

def particle_system_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove the selected particle system"""
    ...

def paste_transform(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, method: str = ..., bake_step: int = ..., use_mirror: bool = ..., mirror_axis_loc: str = ..., mirror_axis_rot: str = ..., use_relative: bool = ...) -> set[str]:
    """Pastes the matrix from the clipboard to the currently active pose bone or object. Uses world-space matrices"""
    ...

def paths_calculate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, display_type: str = ..., range: str = ...) -> set[str]:
    """Generate motion paths for the selected objects"""
    ...

def paths_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, only_selected: bool = ...) -> set[str]:
    """(undocumented operator)"""
    ...

def paths_update(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Recalculate motion paths for selected objects"""
    ...

def paths_update_visible(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Recalculate all visible motion paths for objects and poses"""
    ...

def pointcloud_random_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add a point cloud object to the scene"""
    ...

def posemode_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Enable or disable posing/selecting bones"""
    ...

def quadriflow_remesh(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_mesh_symmetry: bool = ..., use_preserve_sharp: bool = ..., use_preserve_boundary: bool = ..., preserve_attributes: bool = ..., smooth_normals: bool = ..., mode: str = ..., target_ratio: float = ..., target_edge_length: float = ..., target_faces: int = ..., mesh_area: float = ..., seed: int = ...) -> set[str]:
    """Create a new quad based mesh using the surface data of the current mesh. All data layers will be lost"""
    ...

def quick_explode(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, style: str = ..., amount: int = ..., frame_duration: int = ..., frame_start: int = ..., frame_end: int = ..., velocity: float = ..., fade: bool = ...) -> set[str]:
    """Make selected objects explode"""
    ...

def quick_fur(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, density: str = ..., length: float = ..., radius: float = ..., view_percentage: float = ..., apply_hair_guides: bool = ..., use_noise: bool = ..., use_frizz: bool = ...) -> set[str]:
    """Add a fur setup to the selected objects"""
    ...

def quick_liquid(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, show_flows: bool = ...) -> set[str]:
    """Make selected objects liquid"""
    ...

def quick_smoke(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, style: str = ..., show_flows: bool = ...) -> set[str]:
    """Use selected objects as smoke emitters"""
    ...

def randomize_transform(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, random_seed: int = ..., use_delta: bool = ..., use_loc: bool = ..., loc: list[float] = ..., use_rot: bool = ..., rot: list[float] = ..., use_scale: bool = ..., scale_even: bool = ..., scale: list[float] = ...) -> set[str]:
    """Randomize objects location, rotation, and scale"""
    ...

def reset_override_library(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reset the selected local overrides to their linked references values"""
    ...

def rotation_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, clear_delta: bool = ...) -> set[str]:
    """Clear the object's rotation"""
    ...

def scale_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, clear_delta: bool = ...) -> set[str]:
    """Clear the object's scale"""
    ...

def select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Change selection of all visible objects in scene"""
    ...

def select_by_type(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., type: str = ...) -> set[str]:
    """Select all visible objects that are of a type"""
    ...

def select_camera(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ...) -> set[str]:
    """Select the active camera"""
    ...

def select_grouped(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., type: str = ...) -> set[str]:
    """Select all visible objects grouped by various properties"""
    ...

def select_hierarchy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ..., extend: bool = ...) -> set[str]:
    """Select object relative to the active object's position in the hierarchy"""
    ...

def select_less(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Deselect objects at the boundaries of parent/child relationships"""
    ...

def select_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., type: str = ...) -> set[str]:
    """Select all visible objects that are linked"""
    ...

def select_mirror(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ...) -> set[str]:
    """Select the mirror objects of the selected object e.g. "L.sword" and "R.sword" """
    ...

def select_more(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select connected parent/child objects"""
    ...

def select_pattern(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, pattern: str = ..., case_sensitive: bool = ..., extend: bool = ...) -> set[str]:
    """Select objects matching a naming pattern"""
    ...

def select_random(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ratio: float = ..., seed: int = ..., action: str = ...) -> set[str]:
    """Select or deselect random visible objects"""
    ...

def select_same_collection(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, collection: str = ...) -> set[str]:
    """Select object in the same collection"""
    ...

def shade_auto_smooth(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_auto_smooth: bool = ..., angle: float = ...) -> set[str]:
    """Add modifier to automatically set the sharpness of mesh edges based on the angle between the neighboring faces"""
    ...

def shade_flat(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, keep_sharp_edges: bool = ...) -> set[str]:
    """Render and display faces uniform, using face normals"""
    ...

def shade_smooth(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, keep_sharp_edges: bool = ...) -> set[str]:
    """Render and display faces smooth, using interpolated vertex normals"""
    ...

def shade_smooth_by_angle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, angle: float = ..., keep_sharp_edges: bool = ...) -> set[str]:
    """Set the sharpness of mesh edges based on the angle between the neighboring faces"""
    ...

def shaderfx_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Add a visual effect to the active object"""
    ...

def shaderfx_copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, shaderfx: str = ...) -> set[str]:
    """Duplicate effect at the same position in the stack"""
    ...

def shaderfx_move_down(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, shaderfx: str = ...) -> set[str]:
    """Move effect down in the stack"""
    ...

def shaderfx_move_to_index(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, shaderfx: str = ..., index: int = ...) -> set[str]:
    """Change the effect's position in the list so it evaluates after the set number of others"""
    ...

def shaderfx_move_up(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, shaderfx: str = ...) -> set[str]:
    """Move effect up in the stack"""
    ...

def shaderfx_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, shaderfx: str = ..., report: bool = ...) -> set[str]:
    """Remove a effect from the active Grease Pencil object"""
    ...

def shape_key_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, from_mix: bool = ...) -> set[str]:
    """Add shape key to the object"""
    ...

def shape_key_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reset the weights of all shape keys to 0 or to the closest value respecting the limits"""
    ...

def shape_key_copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Duplicate the active shape key"""
    ...

def shape_key_lock(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Change the lock state of all shape keys of active object"""
    ...

def shape_key_make_basis(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Make this shape key the new basis key, effectively applying it to the mesh. Note that this applies the shape key at its 100% value"""
    ...

def shape_key_mirror(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_topology: bool = ...) -> set[str]:
    """Mirror the current shape key along the local X axis"""
    ...

def shape_key_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Move selected shape keys up/down in the list"""
    ...

def shape_key_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ..., apply_mix: bool = ...) -> set[str]:
    """Remove shape key from the object"""
    ...

def shape_key_retime(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Resets the timing for absolute shape keys"""
    ...

def shape_key_transfer(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., use_clamp: bool = ...) -> set[str]:
    """Copy the active shape key of another selected object to this one"""
    ...

def simulation_nodes_cache_bake(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, selected: bool = ...) -> set[str]:
    """Bake simulations in geometry nodes modifiers"""
    ...

def simulation_nodes_cache_calculate_to_frame(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, selected: bool = ...) -> set[str]:
    """Calculate simulations in geometry nodes modifiers from the start to current frame"""
    ...

def simulation_nodes_cache_delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, selected: bool = ...) -> set[str]:
    """Delete cached/baked simulations in geometry nodes modifiers"""
    ...

def skin_armature_create(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Create an armature that parallels the skin layout"""
    ...

def skin_loose_mark_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Mark/clear selected vertices as loose"""
    ...

def skin_radii_equalize(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Make skin radii of selected vertices equal on each axis"""
    ...

def skin_root_mark(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Mark selected vertices as roots"""
    ...

def speaker_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add a speaker object to the scene"""
    ...

def subdivision_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, level: int = ..., relative: bool = ..., ensure_modifier: bool = ...) -> set[str]:
    """Sets a Subdivision Surface level (1 to 5)"""
    ...

def surfacedeform_bind(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, modifier: str = ...) -> set[str]:
    """Bind mesh to target in surface deform modifier"""
    ...

def text_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, radius: float = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add a text object to the scene"""
    ...

def track_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Clear tracking constraint or flag from object"""
    ...

def track_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Make the object track another object, using various methods/constraints"""
    ...

def transfer_mode(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_flash_on_transfer: bool = ...) -> set[str]:
    """Switches the active object and assigns the same mode to a new one under the mouse cursor, leaving the active mode in the current one"""
    ...

def transform_apply(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: bool = ..., rotation: bool = ..., scale: bool = ..., properties: bool = ..., isolate_users: bool = ...) -> set[str]:
    """Apply the object's transformation to its data"""
    ...

def transform_axis_target(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Interactively point cameras and lights to a location (Ctrl translates)"""
    ...

def transform_to_mouse(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., session_uid: int = ..., matrix: list[float] = ..., drop_x: int = ..., drop_y: int = ...) -> set[str]:
    """Snap selected item(s) to the mouse location"""
    ...

def transforms_to_deltas(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., reset_values: bool = ...) -> set[str]:
    """Convert normal object transforms to delta transforms, any existing delta transforms will be included as well"""
    ...

def unlink_data(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(undocumented operator)"""
    ...

def update_shapes(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_mirror: bool = ...) -> set[str]:
    """Update existing shape keys with the vertex positions of selected objects with matching names"""
    ...

def vertex_group_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add a new vertex group to the active object"""
    ...

def vertex_group_assign(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Assign the selected vertices to the active vertex group"""
    ...

def vertex_group_assign_new(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Assign the selected vertices to a new vertex group"""
    ...

def vertex_group_clean(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, group_select_mode: str = ..., limit: float = ..., keep_single: bool = ...) -> set[str]:
    """Remove vertex group assignments which are not required"""
    ...

def vertex_group_copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Make a copy of the active vertex group"""
    ...

def vertex_group_copy_to_selected(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Replace vertex groups of selected objects by vertex groups of active object"""
    ...

def vertex_group_deselect(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Deselect all selected vertices assigned to the active vertex group"""
    ...

def vertex_group_invert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, group_select_mode: str = ..., auto_assign: bool = ..., auto_remove: bool = ...) -> set[str]:
    """Invert active vertex group's weights"""
    ...

def vertex_group_levels(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, group_select_mode: str = ..., offset: float = ..., gain: float = ...) -> set[str]:
    """Add some offset and multiply with some gain the weights of the active vertex group"""
    ...

def vertex_group_limit_total(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, group_select_mode: str = ..., limit: int = ...) -> set[str]:
    """Limit deform weights associated with a vertex to a specified number by removing lowest weights"""
    ...

def vertex_group_lock(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ..., mask: str = ...) -> set[str]:
    """Change the lock state of all or some vertex groups of active object"""
    ...

def vertex_group_mirror(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mirror_weights: bool = ..., flip_group_names: bool = ..., all_groups: bool = ..., use_topology: bool = ...) -> set[str]:
    """Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected"""
    ...

def vertex_group_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ...) -> set[str]:
    """Move the active vertex group up/down in the list"""
    ...

def vertex_group_normalize(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Normalize weights of the active vertex group, so that the highest ones are now 1.0"""
    ...

def vertex_group_normalize_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, group_select_mode: str = ..., lock_active: bool = ...) -> set[str]:
    """Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0"""
    ...

def vertex_group_quantize(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, group_select_mode: str = ..., steps: int = ...) -> set[str]:
    """Set weights to a fixed number of steps"""
    ...

def vertex_group_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, all: bool = ..., all_unlocked: bool = ...) -> set[str]:
    """Delete the active or all vertex groups from the active object"""
    ...

def vertex_group_remove_from(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_all_groups: bool = ..., use_all_verts: bool = ...) -> set[str]:
    """Remove the selected vertices from active or all vertex group(s)"""
    ...

def vertex_group_select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select all the vertices assigned to the active vertex group"""
    ...

def vertex_group_set_active(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, group: str = ...) -> set[str]:
    """Set the active vertex group"""
    ...

def vertex_group_smooth(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, group_select_mode: str = ..., factor: float = ..., repeat: int = ..., expand: float = ...) -> set[str]:
    """Smooth weights for selected vertices"""
    ...

def vertex_group_sort(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, sort_type: str = ...) -> set[str]:
    """Sort vertex groups"""
    ...

def vertex_parent_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Parent selected objects to the selected vertices"""
    ...

def vertex_weight_copy(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy weights from active to selected"""
    ...

def vertex_weight_delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, weight_group: int = ...) -> set[str]:
    """Delete this weight from the vertex (disabled if vertex group is locked)"""
    ...

def vertex_weight_normalize_active_vertex(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Normalize active vertex's weights"""
    ...

def vertex_weight_paste(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, weight_group: int = ...) -> set[str]:
    """Copy this group's weight to other selected vertices (disabled if vertex group is locked)"""
    ...

def vertex_weight_set_active(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, weight_group: int = ...) -> set[str]:
    """Set as active vertex group"""
    ...

def visual_geometry_to_objects(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Convert geometry and instances into editable objects and collections"""
    ...

def visual_transform_apply(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Apply the object's visual transformation to its data"""
    ...

def volume_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add a volume object to the scene"""
    ...

def volume_import(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., display_type: str = ..., sort_method: str = ..., use_sequence_detection: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Import OpenVDB volume file"""
    ...

def voxel_remesh(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Calculates a new manifold mesh based on the volume of the current mesh. All data layers will be lost"""
    ...

def voxel_size_edit(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Modify the mesh voxel size interactively used in the voxel remesher"""
    ...
