# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def cyclic_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, direction: str = ...) -> set[str]:
    """Make active spline closed/opened loop"""
    ...

def de_select_first(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(De)select first of visible part of each NURBS"""
    ...

def de_select_last(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """(De)select last of visible part of each NURBS"""
    ...

def decimate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ratio: float = ...) -> set[str]:
    """Simplify selected curves"""
    ...

def delete(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Delete selected control points or segments"""
    ...

def dissolve_verts(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Delete selected control points, correcting surrounding handles"""
    ...

def draw(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, error_threshold: float = ..., fit_method: str = ..., corner_angle: float = ..., use_cyclic: bool = ..., stroke: bpy_prop_collection['OperatorStrokeElement'] = ..., wait_for_input: bool = ...) -> set[str]:
    """Draw a freehand spline"""
    ...

def duplicate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Duplicate selected control points"""
    ...

def duplicate_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, CURVE_OT_duplicate: 'CURVE_OT_duplicate' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Duplicate curve and move"""
    ...

def extrude(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ...) -> set[str]:
    """Extrude selected control point(s)"""
    ...

def extrude_move(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, CURVE_OT_extrude: 'CURVE_OT_extrude' = ..., TRANSFORM_OT_translate: 'TRANSFORM_OT_translate' = ...) -> set[str]:
    """Extrude curve and move result"""
    ...

def handle_type_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Set type of handles for selected control points"""
    ...

def hide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> set[str]:
    """Hide (un)selected control points"""
    ...

def make_segment(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Join two curves by their selected ends"""
    ...

def match_texture_space(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Match texture space to object's bounding box"""
    ...

def normals_make_consistent(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, calc_length: bool = ...) -> set[str]:
    """Recalculate the direction of selected handles"""
    ...

def pen(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ..., deselect: bool = ..., toggle: bool = ..., deselect_all: bool = ..., select_passthrough: bool = ..., extrude_point: bool = ..., extrude_handle: str = ..., delete_point: bool = ..., insert_point: bool = ..., move_segment: bool = ..., select_point: bool = ..., move_point: bool = ..., close_spline: bool = ..., close_spline_method: str = ..., toggle_vector: bool = ..., cycle_handle_type: bool = ...) -> set[str]:
    """Construct and edit splines"""
    ...

def primitive_bezier_circle_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, radius: float = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a Bézier Circle"""
    ...

def primitive_bezier_curve_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, radius: float = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a Bézier Curve"""
    ...

def primitive_nurbs_circle_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, radius: float = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a Nurbs Circle"""
    ...

def primitive_nurbs_curve_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, radius: float = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a Nurbs Curve"""
    ...

def primitive_nurbs_path_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, radius: float = ..., enter_editmode: bool = ..., align: str = ..., location: list[float] = ..., rotation: list[float] = ..., scale: list[float] = ...) -> set[str]:
    """Construct a Path"""
    ...

def radius_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, radius: float = ...) -> set[str]:
    """Set per-point radius which is used for bevel tapering"""
    ...

def reveal(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ...) -> set[str]:
    """Reveal hidden control points"""
    ...

def select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """(De)select all control points"""
    ...

def select_less(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Deselect control points at the boundary of each selection region"""
    ...

def select_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select all control points linked to the current selection"""
    ...

def select_linked_pick(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, deselect: bool = ...) -> set[str]:
    """Select all control points linked to already selected ones"""
    ...

def select_more(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select control points at the boundary of each selection region"""
    ...

def select_next(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select control points following already selected ones along the curves"""
    ...

def select_nth(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, skip: int = ..., nth: int = ..., offset: int = ...) -> set[str]:
    """Deselect every Nth point starting from the active one"""
    ...

def select_previous(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select control points preceding already selected ones along the curves"""
    ...

def select_random(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, ratio: float = ..., seed: int = ..., action: str = ...) -> set[str]:
    """Randomly select some control points"""
    ...

def select_row(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select a row of control points including active one. Successive use on the same point switches between U/V directions"""
    ...

def select_similar(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., compare: str = ..., threshold: float = ...) -> set[str]:
    """Select similar curve points by property type"""
    ...

def separate(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Separate selected points from connected unselected points into a new object"""
    ...

def shade_flat(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set shading to flat"""
    ...

def shade_smooth(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Set shading to smooth"""
    ...

def shortest_path_pick(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select shortest path between two selections"""
    ...

def smooth(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Flatten angles of selected points"""
    ...

def smooth_radius(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Interpolate radii of selected points"""
    ...

def smooth_tilt(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Interpolate tilt of selected points"""
    ...

def smooth_weight(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Interpolate weight of selected points"""
    ...

def spin(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, center: list[float] = ..., axis: list[float] = ...) -> set[str]:
    """Extrude selected boundary row around pivot point and current view axis"""
    ...

def spline_type_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., use_handles: bool = ...) -> set[str]:
    """Set type of active spline"""
    ...

def spline_weight_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, weight: float = ...) -> set[str]:
    """Set softbody goal weight for selected points"""
    ...

def split(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Split off selected points from connected unselected points"""
    ...

def subdivide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, number_cuts: int = ...) -> set[str]:
    """Subdivide selected segments"""
    ...

def switch_direction(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Switch direction of selected splines"""
    ...

def tilt_clear(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Clear the tilt of selected control points"""
    ...

def vertex_add(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[float] = ...) -> set[str]:
    """Add a new control point (linked to only selected end-curve one, if any)"""
    ...
