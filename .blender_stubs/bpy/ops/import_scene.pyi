# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def fbx(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., directory: str = ..., filter_glob: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., ui_tab: str = ..., use_manual_orientation: bool = ..., global_scale: float = ..., bake_space_transform: bool = ..., use_custom_normals: bool = ..., colors_type: str = ..., use_image_search: bool = ..., use_alpha_decals: bool = ..., decal_offset: float = ..., use_anim: bool = ..., anim_offset: float = ..., use_subsurf: bool = ..., use_custom_props: bool = ..., use_custom_props_enum_as_string: bool = ..., ignore_leaf_bones: bool = ..., force_connect_children: bool = ..., automatic_bone_orientation: bool = ..., primary_bone_axis: str = ..., secondary_bone_axis: str = ..., use_prepost_rot: bool = ..., mtl_name_collision_mode: str = ..., axis_forward: str = ..., axis_up: str = ...) -> Set[str]:
    """Load a FBX file"""
    ...

def gltf(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ..., export_import_convert_lighting_mode: str = ..., filter_glob: str = ..., directory: str = ..., files: bpy_prop_collection['OperatorFileListElement'] = ..., loglevel: int = ..., import_pack_images: bool = ..., merge_vertices: bool = ..., import_shading: str = ..., bone_heuristic: str = ..., disable_bone_shape: bool = ..., bone_shape_scale_factor: float = ..., guess_original_bind_pose: bool = ..., import_webp_texture: bool = ..., import_unused_materials: bool = ..., import_select_created_objects: bool = ..., import_scene_extras: bool = ..., import_scene_as_collection: bool = ..., import_merge_material_slots: bool = ...) -> Set[str]:
    """Load a glTF 2.0 file"""
    ...
