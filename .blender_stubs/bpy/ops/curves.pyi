# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def add_bezier(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, radius: float = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add new Bézier curve"""
    ...

def add_circle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, radius: float = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Add new circle curve"""
    ...

def attribute_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, value_float: float = ..., value_float_vector_2d: list[float] = ..., value_float_vector_3d: list[float] = ..., value_int: int = ..., value_int_vector_2d: list[int] = ..., value_color: list[float] = ..., value_bool: bool = ...) -> set[str]:
    """Set values of the active attribute for selected elements"""
    ...

def convert_from_particle_system(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add a new curves object based on the current state of the particle system"""
    ...

def convert_to_particle_system(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add a new or update an existing hair particle system on the surface object"""
    ...

def curve_type_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., use_handles: bool = ...) -> set[str]:
    """Set type of selected curves"""
    ...

def cyclic_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Make active curve closed/opened loop"""
    ...

def delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Remove selected control points or curves"""
    ...

def draw(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, error_threshold: float = ..., fit_method: str = ..., corner_angle: float = ..., use_cyclic: bool = ..., stroke: bpy_prop_collection['OperatorStrokeElement'] = ..., wait_for_input: bool = ..., is_curve_2d: bool = ..., bezier_as_nurbs: bool = ...) -> set[str]:
    """Draw a freehand curve"""
    ...

def duplicate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Copy selected points or curves"""
    ...

def duplicate_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, CURVES_OT_duplicate: 'CURVES_OT_duplicate' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Make copies of selected elements and move them"""
    ...

def extrude(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Extrude selected control point(s)"""
    ...

def extrude_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, CURVES_OT_extrude: 'CURVES_OT_extrude' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Extrude curve and move result"""
    ...

def handle_type_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Set the handle type for bezier curves"""
    ...

def pen(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., deselect: bool = ..., toggle: bool = ..., deselect_all: bool = ..., select_passthrough: bool = ..., extrude_point: bool = ..., extrude_handle: str = ..., delete_point: bool = ..., insert_point: bool = ..., move_segment: bool = ..., select_point: bool = ..., move_point: bool = ..., cycle_handle_type: bool = ..., size: float = ...) -> set[str]:
    """Construct and edit Bézier curves"""
    ...

def sculptmode_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Enter/Exit sculpt mode for curves"""
    ...

def select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """(De)select all control points"""
    ...

def select_ends(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, amount_start: int = ..., amount_end: int = ...) -> set[str]:
    """Select end points of curves"""
    ...

def select_less(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Shrink the selection by one point"""
    ...

def select_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select all points in curves with any point selection"""
    ...

def select_linked_pick(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, deselect: bool = ...) -> set[str]:
    """Select all points in the curve under the cursor"""
    ...

def select_more(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Grow the selection by one point"""
    ...

def select_random(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, seed: int = ..., probability: float = ...) -> set[str]:
    """Randomizes existing selection or create new random selection"""
    ...

def separate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Separate selected geometry into a new object"""
    ...

def set_selection_domain(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, domain: str = ...) -> set[str]:
    """Change the mode used for selection masking in curves sculpt mode"""
    ...

def snap_curves_to_surface(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, attach_mode: str = ...) -> set[str]:
    """Move curves so that the first point is exactly on the surface mesh"""
    ...

def split(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Split selected points"""
    ...

def subdivide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, number_cuts: int = ...) -> set[str]:
    """Subdivide selected curve segments"""
    ...

def surface_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Use the active object as surface for selected curves objects and set it as the parent"""
    ...

def switch_direction(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Reverse the direction of the selected curves"""
    ...

def tilt_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear the tilt of selected control points"""
    ...
