# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def bbone_resize(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: list[float] = ..., orient_type: str = ..., orient_matrix: list[float] = ..., orient_matrix_type: str = ..., constraint_axis: list[bool] = ..., mirror: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Scale selected bendy bones display size"""
    ...

def bend(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: list[float] = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., gpencil_strokes: bool = ..., center_override: list[float] = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Bend selected items between the 3D cursor and the mouse"""
    ...

def create_orientation(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ..., use_view: bool = ..., use: bool = ..., overwrite: bool = ...) -> set[str]:
    """Create transformation orientation from selection"""
    ...

def delete_orientation(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Delete transformation orientation"""
    ...

def edge_bevelweight(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., snap: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Change the bevel weight of edges"""
    ...

def edge_crease(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., snap: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Change the crease of edges"""
    ...

def edge_slide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., single_side: bool = ..., use_even: bool = ..., flipped: bool = ..., use_clamp: bool = ..., mirror: bool = ..., snap: bool = ..., snap_elements: set[str] = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: list[float] = ..., correct_uv: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Slide an edge loop along a mesh"""
    ...

def from_gizmo(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Transform selected items by mode type"""
    ...

def mirror(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, orient_type: str = ..., orient_matrix: list[float] = ..., orient_matrix_type: str = ..., constraint_axis: list[bool] = ..., gpencil_strokes: bool = ..., center_override: list[float] = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Mirror selected items around one or more axes"""
    ...

def push_pull(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., center_override: list[float] = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Push/Pull selected items"""
    ...

def resize(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: list[float] = ..., mouse_dir_constraint: list[float] = ..., orient_type: str = ..., orient_matrix: list[float] = ..., orient_matrix_type: str = ..., constraint_axis: list[bool] = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., snap_elements: set[str] = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: list[float] = ..., gpencil_strokes: bool = ..., texture_space: bool = ..., remove_on_cancel: bool = ..., use_duplicated_keyframes: bool = ..., center_override: list[float] = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Scale (resize) selected items"""
    ...

def rotate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., orient_axis: str = ..., orient_type: str = ..., orient_matrix: list[float] = ..., orient_matrix_type: str = ..., constraint_axis: list[bool] = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., snap_elements: set[str] = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: list[float] = ..., gpencil_strokes: bool = ..., center_override: list[float] = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Rotate selected items"""
    ...

def rotate_normal(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., orient_axis: str = ..., orient_type: str = ..., orient_matrix: list[float] = ..., orient_matrix_type: str = ..., constraint_axis: list[bool] = ..., mirror: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Rotate custom normal of selected items"""
    ...

def select_orientation(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, orientation: str = ...) -> set[str]:
    """Select transformation orientation"""
    ...

def seq_slide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: list[float] = ..., use_restore_handle_selection: bool = ..., snap: bool = ..., texture_space: bool = ..., remove_on_cancel: bool = ..., use_duplicated_keyframes: bool = ..., view2d_edge_pan: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Slide a sequence strip in time"""
    ...

def shear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., orient_axis: str = ..., orient_axis_ortho: str = ..., orient_type: str = ..., orient_matrix: list[float] = ..., orient_matrix_type: str = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., gpencil_strokes: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Shear selected items along the given axis"""
    ...

def shrink_fatten(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., use_even_offset: bool = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Shrink/fatten selected vertices along normals"""
    ...

def skin_resize(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: list[float] = ..., orient_type: str = ..., orient_matrix: list[float] = ..., orient_matrix_type: str = ..., constraint_axis: list[bool] = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., snap_elements: set[str] = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: list[float] = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Scale selected vertices' skin radii"""
    ...

def tilt(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Tilt selected control vertices of 3D curve"""
    ...

def tosphere(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., gpencil_strokes: bool = ..., center_override: list[float] = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Move selected items outward in a spherical shape around geometric center"""
    ...

def trackball(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: list[float] = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., gpencil_strokes: bool = ..., center_override: list[float] = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Trackball style rotation of selected items"""
    ...

def transform(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., value: list[float] = ..., orient_axis: str = ..., orient_type: str = ..., orient_matrix: list[float] = ..., orient_matrix_type: str = ..., constraint_axis: list[bool] = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., snap_elements: set[str] = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: list[float] = ..., snap_align: bool = ..., snap_normal: list[float] = ..., gpencil_strokes: bool = ..., texture_space: bool = ..., remove_on_cancel: bool = ..., use_duplicated_keyframes: bool = ..., center_override: list[float] = ..., release_confirm: bool = ..., use_accurate: bool = ..., use_automerge_and_split: bool = ...) -> set[str]:
    """Transform selected items by mode type"""
    ...

def translate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: list[float] = ..., orient_type: str = ..., orient_matrix: list[float] = ..., orient_matrix_type: str = ..., constraint_axis: list[bool] = ..., mirror: bool = ..., use_proportional_edit: bool = ..., proportional_edit_falloff: str = ..., proportional_size: float = ..., use_proportional_connected: bool = ..., use_proportional_projected: bool = ..., snap: bool = ..., snap_elements: set[str] = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: list[float] = ..., snap_align: bool = ..., snap_normal: list[float] = ..., gpencil_strokes: bool = ..., cursor_transform: bool = ..., texture_space: bool = ..., remove_on_cancel: bool = ..., use_duplicated_keyframes: bool = ..., view2d_edge_pan: bool = ..., release_confirm: bool = ..., use_accurate: bool = ..., use_automerge_and_split: bool = ..., translate_origin: bool = ...) -> set[str]:
    """Move selected items"""
    ...

def vert_crease(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., snap: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Change the crease of vertices"""
    ...

def vert_slide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value: float = ..., use_even: bool = ..., flipped: bool = ..., use_clamp: bool = ..., mirror: bool = ..., snap: bool = ..., snap_elements: set[str] = ..., use_snap_project: bool = ..., snap_target: str = ..., use_snap_self: bool = ..., use_snap_edit: bool = ..., use_snap_nonedit: bool = ..., use_snap_selectable: bool = ..., snap_point: list[float] = ..., correct_uv: bool = ..., release_confirm: bool = ..., use_accurate: bool = ...) -> set[str]:
    """Slide a vertex along a mesh"""
    ...

def vertex_random(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, offset: float = ..., uniform: float = ..., normal: float = ..., seed: int = ..., wait_for_input: bool = ...) -> set[str]:
    """Randomize vertices"""
    ...

def vertex_warp(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, warp_angle: float = ..., offset_angle: float = ..., min: float = ..., max: float = ..., viewmat: list[float] = ..., center: list[float] = ...) -> set[str]:
    """Warp vertices around the cursor"""
    ...
