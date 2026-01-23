# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
import bpy
from typing import Any, Optional, Union

def add_simple_uvs(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Add cube map UVs on mesh"""
    ...

def add_texture_paint_slot(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., slot_type: str = ..., name: str = ..., color: list[float] = ..., width: int = ..., height: int = ..., alpha: bool = ..., generated_type: str = ..., float: bool = ..., domain: str = ..., data_type: str = ...) -> set[str]:
    """Add a paint slot"""
    ...

def brush_colors_flip(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Swap primary and secondary brush colors"""
    ...

def face_select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Change selection for all faces"""
    ...

def face_select_hide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> set[str]:
    """Hide selected faces"""
    ...

def face_select_less(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, face_step: bool = ...) -> set[str]:
    """Deselect Faces connected to existing selection"""
    ...

def face_select_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select linked faces"""
    ...

def face_select_linked_pick(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, deselect: bool = ...) -> set[str]:
    """Select linked faces under the cursor"""
    ...

def face_select_loop(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ..., extend: bool = ...) -> set[str]:
    """Select face loop under the cursor"""
    ...

def face_select_more(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, face_step: bool = ...) -> set[str]:
    """Select Faces connected to existing selection"""
    ...

def face_vert_reveal(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ...) -> set[str]:
    """Reveal hidden faces and vertices"""
    ...

def grab_clone(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, delta: list[float] = ...) -> set[str]:
    """Move the clone source image"""
    ...

def hide_show(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., action: str = ..., area: str = ..., use_front_faces_only: bool = ...) -> set[str]:
    """Hide/show some vertices"""
    ...

def hide_show_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Hide/show all vertices"""
    ...

def hide_show_lasso_gesture(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_smooth_stroke: bool = ..., smooth_stroke_factor: float = ..., smooth_stroke_radius: int = ..., action: str = ..., area: str = ..., use_front_faces_only: bool = ...) -> set[str]:
    """Hide/show some vertices"""
    ...

def hide_show_line_gesture(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xstart: int = ..., xend: int = ..., ystart: int = ..., yend: int = ..., flip: bool = ..., cursor: int = ..., action: str = ..., area: str = ..., use_front_faces_only: bool = ..., use_limit_to_segment: bool = ...) -> set[str]:
    """Hide/show some vertices"""
    ...

def hide_show_masked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Hide/show all masked vertices above a threshold"""
    ...

def hide_show_polyline_gesture(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., action: str = ..., area: str = ..., use_front_faces_only: bool = ...) -> set[str]:
    """Hide/show some vertices"""
    ...

def image_from_view(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, filepath: str = ...) -> set[str]:
    """Make an image from biggest 3D view for reprojection"""
    ...

def image_paint(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, stroke: bpy_prop_collection['OperatorStrokeElement'] = ..., mode: str = ..., pen_flip: bool = ...) -> set[str]:
    """Paint a stroke into the image"""
    ...

def mask_box_gesture(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xmin: int = ..., xmax: int = ..., ymin: int = ..., ymax: int = ..., wait_for_input: bool = ..., use_front_faces_only: bool = ..., mode: str = ..., value: float = ...) -> set[str]:
    """Mask within a rectangle defined by the cursor"""
    ...

def mask_flood_fill(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, mode: str = ..., value: float = ...) -> set[str]:
    """Fill the whole mask with a given value, or invert its values"""
    ...

def mask_lasso_gesture(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_smooth_stroke: bool = ..., smooth_stroke_factor: float = ..., smooth_stroke_radius: int = ..., use_front_faces_only: bool = ..., mode: str = ..., value: float = ...) -> set[str]:
    """Mask within a shape defined by the cursor"""
    ...

def mask_line_gesture(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, xstart: int = ..., xend: int = ..., ystart: int = ..., yend: int = ..., flip: bool = ..., cursor: int = ..., use_front_faces_only: bool = ..., use_limit_to_segment: bool = ..., mode: str = ..., value: float = ...) -> set[str]:
    """Mask to one side of a line defined by the cursor"""
    ...

def mask_polyline_gesture(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, path: bpy_prop_collection['OperatorMousePath'] = ..., use_front_faces_only: bool = ..., mode: str = ..., value: float = ...) -> set[str]:
    """Mask within a shape defined by the cursor"""
    ...

def project_image(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, image: str = ...) -> set[str]:
    """Project an edited render from the active camera back onto the object"""
    ...

def sample_color(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, location: list[int] = ..., merged: bool = ..., palette: bool = ...) -> set[str]:
    """Use the mouse to sample a color in the image"""
    ...

def texture_paint_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Toggle texture paint mode in 3D view"""
    ...

def vert_select_all(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ...) -> set[str]:
    """Change selection for all vertices"""
    ...

def vert_select_hide(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, unselected: bool = ...) -> set[str]:
    """Hide selected vertices"""
    ...

def vert_select_less(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, face_step: bool = ...) -> set[str]:
    """Deselect Vertices connected to existing selection"""
    ...

def vert_select_linked(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select linked vertices"""
    ...

def vert_select_linked_pick(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ...) -> set[str]:
    """Select linked vertices under the cursor"""
    ...

def vert_select_loop(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, select: bool = ..., extend: bool = ...) -> set[str]:
    """Select vertex loop under the cursor"""
    ...

def vert_select_more(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, face_step: bool = ...) -> set[str]:
    """Select Vertices connected to existing selection"""
    ...

def vert_select_ungrouped(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, extend: bool = ...) -> set[str]:
    """Select vertices without a group"""
    ...

def vertex_color_brightness_contrast(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, brightness: float = ..., contrast: float = ...) -> set[str]:
    """Adjust vertex color brightness/contrast"""
    ...

def vertex_color_dirt(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, blur_strength: float = ..., blur_iterations: int = ..., clean_angle: float = ..., dirt_angle: float = ..., dirt_only: bool = ..., normalize: bool = ...) -> set[str]:
    """Generate a dirt map gradient based on cavity"""
    ...

def vertex_color_from_weight(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Convert active weight into gray scale vertex colors"""
    ...

def vertex_color_hsv(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, h: float = ..., s: float = ..., v: float = ...) -> set[str]:
    """Adjust vertex color Hue/Saturation/Value"""
    ...

def vertex_color_invert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Invert RGB values"""
    ...

def vertex_color_levels(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, offset: float = ..., gain: float = ...) -> set[str]:
    """Adjust levels of vertex colors"""
    ...

def vertex_color_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, use_alpha: bool = ...) -> set[str]:
    """Fill the active vertex color layer with the current paint color"""
    ...

def vertex_color_smooth(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Smooth colors across vertices"""
    ...

def vertex_paint(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, stroke: bpy_prop_collection['OperatorStrokeElement'] = ..., mode: str = ..., pen_flip: bool = ..., override_location: bool = ...) -> set[str]:
    """Paint a stroke in the active color attribute layer"""
    ...

def vertex_paint_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Toggle the vertex paint mode in 3D view"""
    ...

def visibility_filter(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, action: str = ..., iterations: int = ..., auto_iteration_count: bool = ...) -> set[str]:
    """Edit the visibility of the current mesh"""
    ...

def visibility_invert(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Invert the visibility of all vertices"""
    ...

def weight_from_bones(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ...) -> set[str]:
    """Set the weights of the groups matching the attached armature's selected bones, using the distance between the vertices and the bones"""
    ...

def weight_gradient(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, type: str = ..., xstart: int = ..., xend: int = ..., ystart: int = ..., yend: int = ..., flip: bool = ..., cursor: int = ...) -> set[str]:
    """Draw a line to apply a weight gradient to selected vertices"""
    ...

def weight_paint(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None, *, stroke: bpy_prop_collection['OperatorStrokeElement'] = ..., mode: str = ..., pen_flip: bool = ..., override_location: bool = ...) -> set[str]:
    """Paint a stroke in the current vertex group's weights"""
    ...

def weight_paint_toggle(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Toggle weight paint mode in 3D view"""
    ...

def weight_sample(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Use the mouse to sample a weight in the 3D view"""
    ...

def weight_sample_group(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Select one of the vertex groups available under current mouse position"""
    ...

def weight_set(override_context: Optional[Union[dict, 'bpy.types.Context']] = None, execution_context: Optional[str] = None, undo: Optional[bool] = None) -> set[str]:
    """Fill the active vertex group with the current paint weight"""
    ...
