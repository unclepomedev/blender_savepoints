# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union, Set, Dict

def bbone_resize(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., orient_type: str = ..., orient_matrix: float = ..., orient_matrix_type: str = ..., constraint_axis: bool = ..., mirror: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Scale selected bendy bones display size"""
    ...

def bend(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., gpencil_strokes: bool = ..., center_override: float = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Bend selected items between the 3D cursor and the mouse"""
    ...

def create_orientation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., use_view: bool = ..., use: bool = ..., overwrite: bool = ...) -> Set[str]:
    """Create transformation orientation from selection"""
    ...

def delete_orientation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Delete transformation orientation"""
    ...

def edge_bevelweight(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., snap: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Change the bevel weight of edges"""
    ...

def edge_crease(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., snap: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Change the crease of edges"""
    ...

def edge_slide(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., single_side: bool = ..., use_even: bool = ..., flipped: bool = ..., use_clamp: bool = ..., mirror: bool = ..., snap: bool = ..., snap_elements: str = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: float = ..., correct_uv: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Slide an edge loop along a mesh"""
    ...

def from_gizmo(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> Set[str]:
    """Transform selected items by mode type"""
    ...

def mirror(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, orient_type: str = ..., orient_matrix: float = ..., orient_matrix_type: str = ..., constraint_axis: bool = ..., gpencil_strokes: bool = ..., center_override: float = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Mirror selected items around one or more axes"""
    ...

def push_pull(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., center_override: float = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Push/Pull selected items"""
    ...

def resize(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., mouse_dir_constraint: float = ..., orient_type: str = ..., orient_matrix: float = ..., orient_matrix_type: str = ..., constraint_axis: bool = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., snap_elements: str = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: float = ..., gpencil_strokes: bool = ..., texture_space: bool = ..., remove_on_cancel: bool = ..., use_duplicated_keyframes: bool = ..., center_override: float = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Scale (resize) selected items"""
    ...

def rotate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., orient_axis: str = ..., orient_type: str = ..., orient_matrix: float = ..., orient_matrix_type: str = ..., constraint_axis: bool = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., snap_elements: str = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: float = ..., gpencil_strokes: bool = ..., center_override: float = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Rotate selected items"""
    ...

def rotate_normal(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., orient_axis: str = ..., orient_type: str = ..., orient_matrix: float = ..., orient_matrix_type: str = ..., constraint_axis: bool = ..., mirror: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Rotate custom normal of selected items"""
    ...

def select_orientation(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, orientation: str = ...) -> Set[str]:
    """Select transformation orientation"""
    ...

def seq_slide(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., use_restore_handle_selection: bool = ..., snap: bool = ..., texture_space: bool = ..., remove_on_cancel: bool = ..., use_duplicated_keyframes: bool = ..., view2d_edge_pan: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Slide a sequence strip in time"""
    ...

def shear(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, angle: float = ..., orient_axis: str = ..., orient_axis_ortho: str = ..., orient_type: str = ..., orient_matrix: float = ..., orient_matrix_type: str = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., gpencil_strokes: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Shear selected items along the given axis"""
    ...

def shrink_fatten(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., use_even_offset: bool = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Shrink/fatten selected vertices along normals"""
    ...

def skin_resize(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., orient_type: str = ..., orient_matrix: float = ..., orient_matrix_type: str = ..., constraint_axis: bool = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., snap_elements: str = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: float = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Scale selected vertices' skin radii"""
    ...

def tilt(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Tilt selected control vertices of 3D curve"""
    ...

def tosphere(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., gpencil_strokes: bool = ..., center_override: float = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Move selected items outward in a spherical shape around geometric center"""
    ...

def trackball(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., gpencil_strokes: bool = ..., center_override: float = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Trackball style rotation of selected items"""
    ...

def transform(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., value: float = ..., orient_axis: str = ..., orient_type: str = ..., orient_matrix: float = ..., orient_matrix_type: str = ..., constraint_axis: bool = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., snap_elements: str = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: float = ..., snap_align: bool = ..., snap_normal: float = ..., gpencil_strokes: bool = ..., texture_space: bool = ..., remove_on_cancel: bool = ..., use_duplicated_keyframes: bool = ..., center_override: float = ..., release_confirm: bool = ..., use_accurate: bool = ..., use_automerge_and_split: bool = ...) -> Set[str]:
    """Transform selected items by mode type"""
    ...

def translate(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., orient_type: str = ..., orient_matrix: float = ..., orient_matrix_type: str = ..., constraint_axis: bool = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., snap_elements: str = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: float = ..., snap_align: bool = ..., snap_normal: float = ..., gpencil_strokes: bool = ..., cursor_transform: bool = ..., texture_space: bool = ..., remove_on_cancel: bool = ..., use_duplicated_keyframes: bool = ..., view2d_edge_pan: bool = ..., release_confirm: bool = ..., use_accurate: bool = ..., use_automerge_and_split: bool = ..., translate_origin: bool = ...) -> Set[str]:
    """Move selected items"""
    ...

def vert_crease(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., snap: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Change the crease of vertices"""
    ...

def vert_slide(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., use_even: bool = ..., flipped: bool = ..., use_clamp: bool = ..., direction: float = ..., mirror: bool = ..., snap: bool = ..., snap_elements: str = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: float = ..., correct_uv: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> Set[str]:
    """Slide a vertex along a mesh"""
    ...

def vertex_random(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, offset: float = ..., uniform: float = ..., normal: float = ..., seed: int = ..., wait_for_input: bool = ...) -> Set[str]:
    """Randomize vertices"""
    ...

def vertex_warp(override_context: Optional[Union[Dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, warp_angle: float = ..., offset_angle: float = ..., min: float = ..., max: float = ..., viewmat: float = ..., center: float = ...) -> Set[str]:
    """Warp vertices around the cursor"""
    ...
