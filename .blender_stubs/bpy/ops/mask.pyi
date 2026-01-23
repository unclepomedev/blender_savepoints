# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def add_feather_vertex(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[float] = ...) -> set[str]:
    """Add vertex to feather"""
    ...

def add_feather_vertex_slide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MASK_OT_add_feather_vertex: 'MASK_OT_add_feather_vertex' = ..., MASK_OT_slide_point: 'MASK_OT_slide_point' = ...) -> set[str]:
    """Add new vertex to feather and slide it"""
    ...

def add_vertex(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[float] = ...) -> set[str]:
    """Add vertex to active spline"""
    ...

def add_vertex_slide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MASK_OT_add_vertex: 'MASK_OT_add_vertex' = ..., MASK_OT_slide_point: 'MASK_OT_slide_point' = ...) -> set[str]:
    """Add new vertex and slide it"""
    ...

def copy_splines(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy the selected splines to the internal clipboard"""
    ...

def cyclic_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Toggle cyclic for selected splines"""
    ...

def delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, confirm: bool = ...) -> set[str]:
    """Delete selected control points or splines"""
    ...

def duplicate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Duplicate selected control points and segments between them"""
    ...

def duplicate_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, MASK_OT_duplicate: 'MASK_OT_duplicate' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Duplicate mask and move"""
    ...

def feather_weight_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reset the feather weight to zero"""
    ...

def handle_type_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Set type of handles for selected control points"""
    ...

def hide_view_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ...) -> set[str]:
    """Reveal temporarily hidden mask layers"""
    ...

def hide_view_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> set[str]:
    """Temporarily hide mask layers"""
    ...

def layer_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ...) -> set[str]:
    """Move the active layer up/down in the list"""
    ...

def layer_new(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> set[str]:
    """Add new mask layer for masking"""
    ...

def layer_remove(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove mask layer"""
    ...

def new(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, name: str = ...) -> set[str]:
    """Create new mask"""
    ...

def normals_make_consistent(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Recalculate the direction of selected handles"""
    ...

def parent_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear the mask's parenting"""
    ...

def parent_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set the mask's parenting"""
    ...

def paste_splines(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Paste splines from the internal clipboard"""
    ...

def primitive_circle_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, size: float = ..., location: list[float] = ...) -> set[str]:
    """Add new circle-shaped spline"""
    ...

def primitive_square_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, size: float = ..., location: list[float] = ...) -> set[str]:
    """Add new square-shaped spline"""
    ...

def select(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., deselect: bool = ..., toggle: bool = ..., deselect_all: bool = ..., select_passthrough: bool = ..., location: list[float] = ...) -> set[str]:
    """Select spline points"""
    ...

def select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Change selection of all curve points"""
    ...

def select_box(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., mode: str = ...) -> set[str]:
    """Select curve points using box selection"""
    ...

def select_circle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, x: int = ..., y: int = ..., radius: int = ..., wait_for_input: bool = ..., mode: str = ...) -> set[str]:
    """Select curve points using circle selection"""
    ...

def select_lasso(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_smooth_stroke: bool = ..., smooth_stroke_factor: float = ..., smooth_stroke_radius: int = ..., mode: str = ...) -> set[str]:
    """Select curve points using lasso selection"""
    ...

def select_less(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Deselect spline points at the boundary of each selection region"""
    ...

def select_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select all curve points linked to already selected ones"""
    ...

def select_linked_pick(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, deselect: bool = ...) -> set[str]:
    """(De)select all points linked to the curve under the mouse cursor"""
    ...

def select_more(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select more spline points connected to initial selection"""
    ...

def shape_key_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove mask shape keyframe for active mask layer at the current frame"""
    ...

def shape_key_feather_reset(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reset feather weights on all selected points animation values"""
    ...

def shape_key_insert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Insert mask shape keyframe for active mask layer at the current frame"""
    ...

def shape_key_rekey(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: bool = ..., feather: bool = ...) -> set[str]:
    """Recalculate animation data on selected points for frames selected in the dopesheet"""
    ...

def slide_point(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, slide_feather: bool = ..., is_new_point: bool = ...) -> set[str]:
    """Slide control points"""
    ...

def slide_spline_curvature(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Slide a point on the spline to define its curvature"""
    ...

def switch_direction(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Switch direction of selected splines"""
    ...
