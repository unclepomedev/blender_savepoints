# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def alembic_export(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., filter_glob: str = ..., start: int = ..., end: int = ..., xsamples: int = ..., gsamples: int = ..., sh_open: float = ..., sh_close: float = ..., selected: bool = ..., flatten: bool = ..., collection: str = ..., uvs: bool = ..., packuv: bool = ..., normals: bool = ..., vcolors: bool = ..., orcos: bool = ..., face_sets: bool = ..., subdiv_schema: bool = ..., apply_subdiv: bool = ..., curves_as_mesh: bool = ..., use_instancing: bool = ..., global_scale: float = ..., triangulate: bool = ..., quad_method: str = ..., ngon_method: str = ..., export_hair: bool = ..., export_particles: bool = ..., export_custom_properties: bool = ..., as_background_job: bool = ..., evaluation_mode: str = ..., init_scene_frame_range: bool = ...) -> Set[str]:
    """Export current scene in an Alembic archive"""
    ...

def alembic_import(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., display_type: str = ..., sort_method: str = ..., filter_glob: str = ..., scale: float = ..., set_frame_range: bool = ..., validate_meshes: bool = ..., always_add_cache_reader: bool = ..., is_sequence: bool = ..., as_background_job: bool = ...) -> Set[str]:
    """Load an Alembic archive"""
    ...

def append(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., filename: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., link: bool = ..., do_reuse_local_id: bool = ..., clear_asset_data: bool = ..., autoselect: bool = ..., active_collection: bool = ..., instance_collections: bool = ..., instance_object_data: bool = ..., set_fake: bool = ..., use_recursive: bool = ...) -> Set[str]:
    """Append from a Library .blend file"""
    ...

def batch_rename(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_type: str = ..., data_source: str = ..., actions: bpy_prop_collection['BatchRenameAction'] = ...) -> Set[str]:
    """Rename multiple items at once"""
    ...

def blend_strings_utf8_validate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Check and fix all strings in current .blend file to be valid UTF-8 Unicode (needed for some old, 2.4x area files)"""
    ...

def call_asset_shelf_popover(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> Set[str]:
    """Open a predefined asset shelf in a popup"""
    ...

def call_menu(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> Set[str]:
    """Open a predefined menu"""
    ...

def call_menu_pie(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> Set[str]:
    """Open a predefined pie menu"""
    ...

def call_panel(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., keep_open: bool = ...) -> Set[str]:
    """Open a predefined panel"""
    ...

def clear_recent_files(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, remove: str = ...) -> Set[str]:
    """Clear the recent files list"""
    ...

def collection_export_all(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Invoke all configured exporters for all collections"""
    ...

def context_collection_boolean_set(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path_iter: str = ..., data_path_item: str = ..., type: str = ...) -> Set[str]:
    """Set boolean values for a collection of items"""
    ...

def context_cycle_array(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., reverse: bool = ...) -> Set[str]:
    """Set a context array value (useful for cycling the active mesh edit mode)"""
    ...

def context_cycle_enum(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., reverse: bool = ..., wrap: bool = ...) -> Set[str]:
    """Toggle a context value"""
    ...

def context_cycle_int(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., reverse: bool = ..., wrap: bool = ...) -> Set[str]:
    """Set a context value (useful for cycling active material, shape keys, groups, etc.)"""
    ...

def context_menu_enum(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def context_modal_mouse(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path_iter: str = ..., data_path_item: str = ..., header_text: str = ..., input_scale: float = ..., invert: bool = ..., initial_x: int = ...) -> Set[str]:
    """Adjust arbitrary values with mouse input"""
    ...

def context_pie_enum(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def context_scale_float(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., value: float = ...) -> Set[str]:
    """Scale a float context value"""
    ...

def context_scale_int(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., value: float = ..., always_step: bool = ...) -> Set[str]:
    """Scale an int context value"""
    ...

def context_set_boolean(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., value: bool = ...) -> Set[str]:
    """Set a context value"""
    ...

def context_set_enum(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., value: str = ...) -> Set[str]:
    """Set a context value"""
    ...

def context_set_float(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., value: float = ..., relative: bool = ...) -> Set[str]:
    """Set a context value"""
    ...

def context_set_id(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., value: str = ...) -> Set[str]:
    """Set a context value to an ID data-block"""
    ...

def context_set_int(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., value: int = ..., relative: bool = ...) -> Set[str]:
    """Set a context value"""
    ...

def context_set_string(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., value: str = ...) -> Set[str]:
    """Set a context value"""
    ...

def context_set_value(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., value: str = ...) -> Set[str]:
    """Set a context value"""
    ...

def context_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., module: str = ...) -> Set[str]:
    """Toggle a context value"""
    ...

def context_toggle_enum(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., value_1: str = ..., value_2: str = ...) -> Set[str]:
    """Toggle a context value"""
    ...

def debug_menu(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, debug_value: int = ...) -> Set[str]:
    """Open a popup to set the debug level"""
    ...

def doc_view(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, doc_id: str = ...) -> Set[str]:
    """Open online reference docs in a web browser"""
    ...

def doc_view_manual(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, doc_id: str = ...) -> Set[str]:
    """Load online manual"""
    ...

def doc_view_manual_ui_context(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """View a context based online manual in a web browser"""
    ...

def drop_blend_file(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def drop_import_file(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ...) -> Set[str]:
    """Operator that allows file handlers to receive file drops"""
    ...

def fbx_import(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., global_scale: float = ..., mtl_name_collision_mode: str = ..., import_colors: str = ..., use_custom_normals: bool = ..., use_custom_props: bool = ..., use_custom_props_enum_as_string: bool = ..., import_subdivision: bool = ..., ignore_leaf_bones: bool = ..., validate_meshes: bool = ..., use_anim: bool = ..., anim_offset: float = ..., filter_glob: str = ...) -> Set[str]:
    """Import FBX file into current scene"""
    ...

def grease_pencil_export_pdf(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., use_fill: bool = ..., selected_object_type: str = ..., frame_mode: str = ..., stroke_sample: float = ..., use_uniform_width: bool = ...) -> Set[str]:
    """Export Grease Pencil to PDF"""
    ...

def grease_pencil_export_svg(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., use_fill: bool = ..., selected_object_type: str = ..., frame_mode: str = ..., stroke_sample: float = ..., use_uniform_width: bool = ..., use_clip_camera: bool = ...) -> Set[str]:
    """Export Grease Pencil to SVG"""
    ...

def grease_pencil_import_svg(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., display_type: str = ..., sort_method: str = ..., resolution: int = ..., scale: float = ..., use_scene_unit: bool = ...) -> Set[str]:
    """Import SVG into Grease Pencil"""
    ...

def id_linked_relocate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, id_session_uid: int = ..., filepath: str = ..., directory: str = ..., filename: str = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., display_type: str = ..., sort_method: str = ..., link: bool = ..., do_reuse_local_id: bool = ..., clear_asset_data: bool = ..., autoselect: bool = ..., active_collection: bool = ..., instance_collections: bool = ..., instance_object_data: bool = ...) -> Set[str]:
    """Relocate a linked ID, i.e. select another ID to link, and remap its local usages to that newly linked data-block). Currently only designed as an internal operator, not directly exposed to the user"""
    ...

def interface_theme_preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Add a custom theme to the preset list"""
    ...

def interface_theme_preset_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Remove a custom theme from the preset list"""
    ...

def interface_theme_preset_save(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Save a custom theme in the preset list"""
    ...

def keyconfig_preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Add a custom keymap configuration to the preset list"""
    ...

def keyconfig_preset_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ...) -> Set[str]:
    """Remove a custom keymap configuration from the preset list"""
    ...

def lib_reload(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, library: str = ..., filepath: str = ..., directory: str = ..., filename: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., display_type: str = ..., sort_method: str = ...) -> Set[str]:
    """Reload the given library"""
    ...

def lib_relocate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, library: str = ..., filepath: str = ..., directory: str = ..., filename: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., display_type: str = ..., sort_method: str = ...) -> Set[str]:
    """Relocate the given library to one or several others"""
    ...

def link(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., filename: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., display_type: str = ..., sort_method: str = ..., link: bool = ..., do_reuse_local_id: bool = ..., clear_asset_data: bool = ..., autoselect: bool = ..., active_collection: bool = ..., instance_collections: bool = ..., instance_object_data: bool = ...) -> Set[str]:
    """Link from a Library .blend file"""
    ...

def memory_statistics(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Print memory statistics to the console"""
    ...

def obj_export(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., export_animation: bool = ..., start_frame: int = ..., end_frame: int = ..., forward_axis: str = ..., up_axis: str = ..., global_scale: float = ..., apply_modifiers: bool = ..., apply_transform: bool = ..., export_eval_mode: str = ..., export_selected_objects: bool = ..., export_uv: bool = ..., export_normals: bool = ..., export_colors: bool = ..., export_materials: bool = ..., export_pbr_extensions: bool = ..., path_mode: str = ..., export_triangulated_mesh: bool = ..., export_curves_as_nurbs: bool = ..., export_object_groups: bool = ..., export_material_groups: bool = ..., export_vertex_groups: bool = ..., export_smooth_groups: bool = ..., smooth_group_bitflags: bool = ..., filter_glob: str = ..., collection: str = ...) -> Set[str]:
    """Save the scene to a Wavefront OBJ file"""
    ...

def obj_import(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., global_scale: float = ..., clamp_size: float = ..., forward_axis: str = ..., up_axis: str = ..., use_split_objects: bool = ..., use_split_groups: bool = ..., import_vertex_groups: bool = ..., validate_meshes: bool = ..., close_spline_loops: bool = ..., collection_separator: str = ..., mtl_name_collision_mode: str = ..., filter_glob: str = ...) -> Set[str]:
    """Load a Wavefront OBJ scene"""
    ...

def open_mainfile(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., load_ui: bool = ..., use_scripts: bool = ..., display_file_selector: bool = ..., state: int = ...) -> Set[str]:
    """Open a Blender file"""
    ...

def operator_cheat_sheet(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """List all the operators in a text-block, useful for scripting"""
    ...

def operator_defaults(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Set the active operator to its default values"""
    ...

def operator_pie_enum(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., prop_string: str = ...) -> Set[str]:
    """(undocumented operator)"""
    ...

def operator_preset_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., remove_name: bool = ..., remove_active: bool = ..., operator: str = ...) -> Set[str]:
    """Add or remove an Operator Preset"""
    ...

def operator_presets_cleanup(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, operator: str = ..., properties: bpy_prop_collection['OperatorFileListElement'] = ...) -> Set[str]:
    """Remove outdated operator properties from presets that may cause problems"""
    ...

def owner_disable(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, owner_id: str = ...) -> Set[str]:
    """Disable add-on for workspace"""
    ...

def owner_enable(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, owner_id: str = ...) -> Set[str]:
    """Enable add-on for workspace"""
    ...

def path_open(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ...) -> Set[str]:
    """Open a path in a file browser"""
    ...

def ply_export(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., forward_axis: str = ..., up_axis: str = ..., global_scale: float = ..., apply_modifiers: bool = ..., export_selected_objects: bool = ..., collection: str = ..., export_uv: bool = ..., export_normals: bool = ..., export_colors: str = ..., export_attributes: bool = ..., export_triangulated_mesh: bool = ..., ascii_format: bool = ..., filter_glob: str = ...) -> Set[str]:
    """Save the scene to a PLY file"""
    ...

def ply_import(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., global_scale: float = ..., use_scene_unit: bool = ..., forward_axis: str = ..., up_axis: str = ..., merge_verts: bool = ..., import_colors: str = ..., import_attributes: bool = ..., filter_glob: str = ...) -> Set[str]:
    """Import an PLY file as an object"""
    ...

def previews_batch_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, files: bpy_prop_collection['OperatorFileListElement'] = ..., directory: str = ..., filter_blender: bool = ..., filter_folder: bool = ..., use_scenes: bool = ..., use_collections: bool = ..., use_objects: bool = ..., use_intern_data: bool = ..., use_trusted: bool = ..., use_backups: bool = ...) -> Set[str]:
    """Clear selected .blend file's previews"""
    ...

def previews_batch_generate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, files: bpy_prop_collection['OperatorFileListElement'] = ..., directory: str = ..., filter_blender: bool = ..., filter_folder: bool = ..., use_scenes: bool = ..., use_collections: bool = ..., use_objects: bool = ..., use_intern_data: bool = ..., use_trusted: bool = ..., use_backups: bool = ...) -> Set[str]:
    """Generate selected .blend file's previews"""
    ...

def previews_clear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, id_type: str = ...) -> Set[str]:
    """Clear data-block previews (only for some types like objects, materials, textures, etc.)"""
    ...

def previews_ensure(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Ensure data-block previews are available and up-to-date (to be saved in .blend file, only for some types like materials, textures, etc.)"""
    ...

def properties_add(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ...) -> Set[str]:
    """Add your own property to the data-block"""
    ...

def properties_context_change(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, context: str = ...) -> Set[str]:
    """Jump to a different tab inside the properties editor"""
    ...

def properties_edit(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., property_name: str = ..., property_type: str = ..., is_overridable_library: bool = ..., description: str = ..., use_soft_limits: bool = ..., array_length: int = ..., default_int: int = ..., min_int: int = ..., max_int: int = ..., soft_min_int: int = ..., soft_max_int: int = ..., step_int: int = ..., default_bool: bool = ..., default_float: float = ..., min_float: float = ..., max_float: float = ..., soft_min_float: float = ..., soft_max_float: float = ..., precision: int = ..., step_float: float = ..., subtype: str = ..., default_string: str = ..., id_type: str = ..., eval_string: str = ...) -> Set[str]:
    """Change a custom property's type, or adjust how it is displayed in the interface"""
    ...

def properties_edit_value(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., property_name: str = ..., eval_string: str = ...) -> Set[str]:
    """Edit the value of a custom property"""
    ...

def properties_remove(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path: str = ..., property_name: str = ...) -> Set[str]:
    """Internal use (edit a property data_path)"""
    ...

def quit_blender(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Quit Blender"""
    ...

def radial_control(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, data_path_primary: str = ..., data_path_secondary: str = ..., use_secondary: str = ..., rotation_path: str = ..., color_path: str = ..., fill_color_path: str = ..., fill_color_override_path: str = ..., fill_color_override_test_path: str = ..., zoom_path: str = ..., image_id: str = ..., secondary_tex: bool = ..., release_confirm: bool = ...) -> Set[str]:
    """Set some size property (e.g. brush size) with mouse wheel"""
    ...

def read_factory_settings(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_factory_startup_app_template_only: bool = ..., app_template: str = ..., use_empty: bool = ...) -> Set[str]:
    """Load factory default startup file and preferences. To make changes permanent, use "Save Startup File" and "Save Preferences" """
    ...

def read_factory_userpref(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_factory_startup_app_template_only: bool = ...) -> Set[str]:
    """Load factory default preferences. To make changes to preferences permanent, use "Save Preferences" """
    ...

def read_history(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Reloads history and bookmarks"""
    ...

def read_homefile(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., load_ui: bool = ..., use_splash: bool = ..., use_factory_startup: bool = ..., use_factory_startup_app_template_only: bool = ..., app_template: str = ..., use_empty: bool = ...) -> Set[str]:
    """Open the default file"""
    ...

def read_userpref(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Load last saved preferences"""
    ...

def recover_auto_save(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., use_scripts: bool = ...) -> Set[str]:
    """Open an automatically saved file to recover it"""
    ...

def recover_last_session(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_scripts: bool = ...) -> Set[str]:
    """Open the last closed file ("quit.blend")"""
    ...

def redraw_timer(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., iterations: int = ..., time_limit: float = ...) -> Set[str]:
    """Simple redraw timer to test the speed of updating the interface"""
    ...

def revert_mainfile(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_scripts: bool = ...) -> Set[str]:
    """Reload the saved file"""
    ...

def save_as_mainfile(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., compress: bool = ..., relative_remap: bool = ..., copy: bool = ...) -> Set[str]:
    """Save the current file in the desired location"""
    ...

def save_homefile(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Make the current file the default startup file"""
    ...

def save_mainfile(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., hide_props_region: bool = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., compress: bool = ..., relative_remap: bool = ..., exit: bool = ..., incremental: bool = ...) -> Set[str]:
    """Save the current Blender file"""
    ...

def save_userpref(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Make the current preferences default"""
    ...

def search_menu(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Pop-up a search over all menus in the current context"""
    ...

def search_operator(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Pop-up a search over all available operators in current context"""
    ...

def search_single_menu(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, menu_idname: str = ..., initial_query: str = ...) -> Set[str]:
    """Pop-up a search for a menu in current context"""
    ...

def set_stereo_3d(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, display_mode: str = ..., anaglyph_type: str = ..., interlace_type: str = ..., use_interlace_swap: bool = ..., use_sidebyside_crosseyed: bool = ...) -> Set[str]:
    """Toggle 3D stereo support for current window (or change the display mode)"""
    ...

def set_working_color_space(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, convert_colors: bool = ..., working_space: str = ...) -> Set[str]:
    """Change the working color space of all colors in this blend file"""
    ...

def splash(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Open the splash screen with release info"""
    ...

def splash_about(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Open a window with information about Blender"""
    ...

def stl_export(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., ascii_format: bool = ..., use_batch: bool = ..., export_selected_objects: bool = ..., collection: str = ..., global_scale: float = ..., use_scene_unit: bool = ..., forward_axis: str = ..., up_axis: str = ..., apply_modifiers: bool = ..., filter_glob: str = ...) -> Set[str]:
    """Save the scene to an STL file"""
    ...

def stl_import(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., global_scale: float = ..., use_scene_unit: bool = ..., use_facet_normal: bool = ..., forward_axis: str = ..., up_axis: str = ..., use_mesh_validate: bool = ..., filter_glob: str = ...) -> Set[str]:
    """Import an STL file as an object"""
    ...

def sysinfo(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ...) -> Set[str]:
    """Generate system information, saved into a text file"""
    ...

def tool_set_by_brush_type(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, brush_type: str = ..., space_type: str = ...) -> Set[str]:
    """Look up the most appropriate tool for the given brush type and activate that"""
    ...

def tool_set_by_id(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., cycle: bool = ..., as_fallback: bool = ..., space_type: str = ...) -> Set[str]:
    """Set the tool by name (for key-maps)"""
    ...

def tool_set_by_index(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, index: int = ..., cycle: bool = ..., expand: bool = ..., as_fallback: bool = ..., space_type: str = ...) -> Set[str]:
    """Set the tool by index (for key-maps)"""
    ...

def toolbar(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """(undocumented operator)"""
    ...

def toolbar_fallback_pie(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """(undocumented operator)"""
    ...

def toolbar_prompt(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Leader key like functionality for accessing tools"""
    ...

def url_open(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, url: str = ...) -> Set[str]:
    """Open a website in the web browser"""
    ...

def url_open_preset(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> Set[str]:
    """Open a preset website in the web browser"""
    ...

def usd_export(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., display_type: str = ..., sort_method: str = ..., filter_glob: str = ..., selected_objects_only: bool = ..., collection: str = ..., export_animation: bool = ..., export_hair: bool = ..., export_uvmaps: bool = ..., rename_uvmaps: bool = ..., export_mesh_colors: bool = ..., export_normals: bool = ..., export_materials: bool = ..., export_subdivision: str = ..., export_armatures: bool = ..., only_deform_bones: bool = ..., export_shapekeys: bool = ..., use_instancing: bool = ..., evaluation_mode: str = ..., generate_preview_surface: bool = ..., generate_materialx_network: bool = ..., convert_orientation: bool = ..., export_global_forward_selection: str = ..., export_global_up_selection: str = ..., export_textures_mode: str = ..., overwrite_textures: bool = ..., relative_paths: bool = ..., xform_op_mode: str = ..., root_prim_path: str = ..., export_custom_properties: bool = ..., custom_properties_namespace: str = ..., accessibility_label: str = ..., accessibility_description: str = ..., author_blender_name: bool = ..., convert_world_material: bool = ..., allow_unicode: bool = ..., export_meshes: bool = ..., export_lights: bool = ..., export_cameras: bool = ..., export_curves: bool = ..., export_points: bool = ..., export_volumes: bool = ..., triangulate_meshes: bool = ..., quad_method: str = ..., ngon_method: str = ..., usdz_downscale_size: str = ..., usdz_downscale_custom_size: int = ..., merge_parent_xform: bool = ..., convert_scene_units: str = ..., meters_per_unit: float = ...) -> Set[str]:
    """Export current scene in a USD archive"""
    ...

def usd_import(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., check_existing: bool = ..., filter_blender: bool = ..., filter_backup: bool = ..., filter_image: bool = ..., filter_movie: bool = ..., filter_python: bool = ..., filter_font: bool = ..., filter_sound: bool = ..., filter_text: bool = ..., filter_archive: bool = ..., filter_btx: bool = ..., filter_alembic: bool = ..., filter_usd: bool = ..., filter_obj: bool = ..., filter_volume: bool = ..., filter_folder: bool = ..., filter_blenlib: bool = ..., filemode: int = ..., relative_path: bool = ..., display_type: str = ..., sort_method: str = ..., filter_glob: str = ..., scale: float = ..., set_frame_range: bool = ..., import_cameras: bool = ..., import_curves: bool = ..., import_lights: bool = ..., import_materials: bool = ..., import_meshes: bool = ..., import_volumes: bool = ..., import_shapes: bool = ..., import_skeletons: bool = ..., import_blendshapes: bool = ..., import_points: bool = ..., import_subdivision: bool = ..., support_scene_instancing: bool = ..., import_visible_only: bool = ..., create_collection: bool = ..., read_mesh_uvs: bool = ..., read_mesh_colors: bool = ..., read_mesh_attributes: bool = ..., prim_path_mask: str = ..., import_guide: bool = ..., import_proxy: bool = ..., import_render: bool = ..., import_all_materials: bool = ..., import_usd_preview: bool = ..., set_material_blend: bool = ..., light_intensity_scale: float = ..., mtl_purpose: str = ..., mtl_name_collision_mode: str = ..., import_textures_mode: str = ..., import_textures_dir: str = ..., tex_name_collision_mode: str = ..., property_import_mode: str = ..., validate_meshes: bool = ..., create_world_material: bool = ..., import_defined_only: bool = ..., merge_parent_xform: bool = ..., apply_unit_conversion_scale: bool = ...) -> Set[str]:
    """Import USD stage into current scene"""
    ...

def window_close(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Close the current window"""
    ...

def window_fullscreen_toggle(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Toggle the current window full-screen"""
    ...

def window_new(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Create a new window"""
    ...

def window_new_main(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Create a new main window with its own workspace and scene selection"""
    ...
