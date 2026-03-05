# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.View3DOverlay.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class View3DOverlay(bpy_struct):

    @property
    def show_overlays(self) -> bool:
        """Display overlays like gizmos and outlines"""
        ...
    @show_overlays.setter
    def show_overlays(self, value: bool):
        ...
    @property
    def show_ortho_grid(self) -> bool:
        """Show grid in orthographic side view"""
        ...
    @show_ortho_grid.setter
    def show_ortho_grid(self, value: bool):
        ...
    @property
    def show_floor(self) -> bool:
        """Show the ground plane grid"""
        ...
    @show_floor.setter
    def show_floor(self, value: bool):
        ...
    @property
    def show_axis_x(self) -> bool:
        """Show the X axis line"""
        ...
    @show_axis_x.setter
    def show_axis_x(self, value: bool):
        ...
    @property
    def show_axis_y(self) -> bool:
        """Show the Y axis line"""
        ...
    @show_axis_y.setter
    def show_axis_y(self, value: bool):
        ...
    @property
    def show_axis_z(self) -> bool:
        """Show the Z axis line"""
        ...
    @show_axis_z.setter
    def show_axis_z(self, value: bool):
        ...
    @property
    def grid_scale(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Multiplier for the distance between 3D View grid lines"""
        ...
    @grid_scale.setter
    def grid_scale(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]):
        ...
    @property
    def grid_lines(self) -> Annotated[int, "step=1"]:
        """Number of grid lines to display in perspective view"""
        ...
    @grid_lines.setter
    def grid_lines(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def grid_subdivisions(self) -> Annotated[int, "step=1"]:
        """Number of subdivisions between grid lines"""
        ...
    @grid_subdivisions.setter
    def grid_subdivisions(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def grid_scale_unit(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Grid cell size scaled by scene unit system settings"""
        ...
    @property
    def show_outline_selected(self) -> bool:
        """Show an outline highlight around selected objects"""
        ...
    @show_outline_selected.setter
    def show_outline_selected(self, value: bool):
        ...
    @property
    def show_object_origins(self) -> bool:
        """Show object center dots"""
        ...
    @show_object_origins.setter
    def show_object_origins(self, value: bool):
        ...
    @property
    def show_object_origins_all(self) -> bool:
        """Show the object origin center dot for all (selected and unselected) objects"""
        ...
    @show_object_origins_all.setter
    def show_object_origins_all(self, value: bool):
        ...
    @property
    def show_relationship_lines(self) -> bool:
        """Show dashed lines indicating parent or constraint relationships"""
        ...
    @show_relationship_lines.setter
    def show_relationship_lines(self, value: bool):
        ...
    @property
    def show_cursor(self) -> bool:
        """Display 3D Cursor Overlay"""
        ...
    @show_cursor.setter
    def show_cursor(self, value: bool):
        ...
    @property
    def show_text(self) -> bool:
        """Display overlay text"""
        ...
    @show_text.setter
    def show_text(self, value: bool):
        ...
    @property
    def show_stats(self) -> bool:
        """Display scene statistics overlay text"""
        ...
    @show_stats.setter
    def show_stats(self, value: bool):
        ...
    @property
    def show_camera_guides(self) -> bool:
        """Show camera composition guides"""
        ...
    @show_camera_guides.setter
    def show_camera_guides(self, value: bool):
        ...
    @property
    def show_camera_passepartout(self) -> bool:
        """Show camera passepartout"""
        ...
    @show_camera_passepartout.setter
    def show_camera_passepartout(self, value: bool):
        ...
    @property
    def show_extras(self) -> bool:
        """Object details, including empty wire, cameras and other visual guides"""
        ...
    @show_extras.setter
    def show_extras(self, value: bool):
        ...
    @property
    def show_light_colors(self) -> bool:
        """Show light colors"""
        ...
    @show_light_colors.setter
    def show_light_colors(self, value: bool):
        ...
    @property
    def show_bones(self) -> bool:
        """Display bones (disable to show motion paths only)"""
        ...
    @show_bones.setter
    def show_bones(self, value: bool):
        ...
    @property
    def show_face_orientation(self) -> Annotated[bool, "is_animatable=False"]:
        """Show the Face Orientation Overlay"""
        ...
    @show_face_orientation.setter
    def show_face_orientation(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_fade_inactive(self) -> Annotated[bool, "is_animatable=False"]:
        """Fade inactive geometry using the viewport background color"""
        ...
    @show_fade_inactive.setter
    def show_fade_inactive(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def fade_inactive_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Strength of the fade effect"""
        ...
    @fade_inactive_alpha.setter
    def fade_inactive_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def show_xray_bone(self) -> Annotated[bool, "is_animatable=False"]:
        """Show the bone selection overlay"""
        ...
    @show_xray_bone.setter
    def show_xray_bone(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def xray_alpha_bone(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Opacity to use for bone selection"""
        ...
    @xray_alpha_bone.setter
    def xray_alpha_bone(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def bone_wire_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2", "is_animatable=False"]:
        """Maximum opacity of bones in wireframe display mode"""
        ...
    @bone_wire_alpha.setter
    def bone_wire_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def show_motion_paths(self) -> Annotated[bool, "is_animatable=False"]:
        """Show the Motion Paths Overlay"""
        ...
    @show_motion_paths.setter
    def show_motion_paths(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_onion_skins(self) -> Annotated[bool, "is_animatable=False"]:
        """Show the Onion Skinning Overlay"""
        ...
    @show_onion_skins.setter
    def show_onion_skins(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_look_dev(self) -> Annotated[bool, "is_animatable=False"]:
        """Show reference spheres with neutral shading that react to lighting to assist in look development"""
        ...
    @show_look_dev.setter
    def show_look_dev(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_wireframes(self) -> Annotated[bool, "is_animatable=False"]:
        """Show face edges wires"""
        ...
    @show_wireframes.setter
    def show_wireframes(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def wireframe_threshold(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Adjust the angle threshold for displaying edges (1.0 for all)"""
        ...
    @wireframe_threshold.setter
    def wireframe_threshold(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def wireframe_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Opacity of the displayed edges (1.0 for opaque)"""
        ...
    @wireframe_opacity.setter
    def wireframe_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def show_viewer_attribute(self) -> Annotated[bool, "is_animatable=False"]:
        """Show attribute overlay for active viewer node"""
        ...
    @show_viewer_attribute.setter
    def show_viewer_attribute(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def viewer_attribute_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Opacity of the attribute that is currently visualized"""
        ...
    @viewer_attribute_opacity.setter
    def viewer_attribute_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def show_viewer_text(self) -> Annotated[bool, "is_animatable=False"]:
        """Show attribute values as text in viewport"""
        ...
    @show_viewer_text.setter
    def show_viewer_text(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_paint_wire(self) -> bool:
        """Use wireframe display in painting modes"""
        ...
    @show_paint_wire.setter
    def show_paint_wire(self, value: bool):
        ...
    @property
    def show_wpaint_contours(self) -> bool:
        """Show contour lines formed by points with the same interpolated weight"""
        ...
    @show_wpaint_contours.setter
    def show_wpaint_contours(self, value: bool):
        ...
    @property
    def show_weight(self) -> bool:
        """Display weights in editmode"""
        ...
    @show_weight.setter
    def show_weight(self, value: bool):
        ...
    @property
    def show_retopology(self) -> bool:
        """Hide the solid mesh and offset the overlay towards the view. Selection is occluded by inactive geometry, unless X-Ray is enabled"""
        ...
    @show_retopology.setter
    def show_retopology(self, value: bool):
        ...
    @property
    def retopology_offset(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """Offset used to draw edit mesh in front of other geometry"""
        ...
    @retopology_offset.setter
    def retopology_offset(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]):
        ...
    @property
    def show_face_normals(self) -> bool:
        """Display face normals as lines"""
        ...
    @show_face_normals.setter
    def show_face_normals(self, value: bool):
        ...
    @property
    def show_vertex_normals(self) -> bool:
        """Display vertex normals as lines"""
        ...
    @show_vertex_normals.setter
    def show_vertex_normals(self, value: bool):
        ...
    @property
    def show_split_normals(self) -> bool:
        """Display vertex-per-face normals as lines"""
        ...
    @show_split_normals.setter
    def show_split_normals(self, value: bool):
        ...
    @property
    def show_faces(self) -> bool:
        """Display a face selection overlay"""
        ...
    @show_faces.setter
    def show_faces(self, value: bool):
        ...
    @property
    def show_face_center(self) -> bool:
        """Display face center when face selection is enabled in solid shading modes"""
        ...
    @show_face_center.setter
    def show_face_center(self, value: bool):
        ...
    @property
    def show_edge_crease(self) -> bool:
        """Display creases created for Subdivision Surface modifier"""
        ...
    @show_edge_crease.setter
    def show_edge_crease(self, value: bool):
        ...
    @property
    def show_edge_bevel_weight(self) -> bool:
        """Display weights created for the Bevel modifier"""
        ...
    @show_edge_bevel_weight.setter
    def show_edge_bevel_weight(self, value: bool):
        ...
    @property
    def show_edge_seams(self) -> bool:
        """Display UV unwrapping seams"""
        ...
    @show_edge_seams.setter
    def show_edge_seams(self, value: bool):
        ...
    @property
    def show_edge_sharp(self) -> bool:
        """Display sharp edges, used with the Edge Split modifier"""
        ...
    @show_edge_sharp.setter
    def show_edge_sharp(self, value: bool):
        ...
    @property
    def show_freestyle_edge_marks(self) -> bool:
        """Display Freestyle edge marks, used with the Freestyle renderer"""
        ...
    @show_freestyle_edge_marks.setter
    def show_freestyle_edge_marks(self, value: bool):
        ...
    @property
    def show_freestyle_face_marks(self) -> bool:
        """Display Freestyle face marks, used with the Freestyle renderer"""
        ...
    @show_freestyle_face_marks.setter
    def show_freestyle_face_marks(self, value: bool):
        ...
    @property
    def show_statvis(self) -> bool:
        """Display statistical information about the mesh"""
        ...
    @show_statvis.setter
    def show_statvis(self, value: bool):
        ...
    @property
    def show_extra_edge_length(self) -> bool:
        """Display selected edge lengths, using global values when set in the transform panel"""
        ...
    @show_extra_edge_length.setter
    def show_extra_edge_length(self, value: bool):
        ...
    @property
    def show_extra_edge_angle(self) -> bool:
        """Display selected edge angle, using global values when set in the transform panel"""
        ...
    @show_extra_edge_angle.setter
    def show_extra_edge_angle(self, value: bool):
        ...
    @property
    def show_extra_face_angle(self) -> bool:
        """Display the angles in the selected edges, using global values when set in the transform panel"""
        ...
    @show_extra_face_angle.setter
    def show_extra_face_angle(self, value: bool):
        ...
    @property
    def show_extra_face_area(self) -> bool:
        """Display the area of selected faces, using global values when set in the transform panel"""
        ...
    @show_extra_face_area.setter
    def show_extra_face_area(self, value: bool):
        ...
    @property
    def show_extra_indices(self) -> bool:
        """Display the index numbers of selected vertices, edges, and faces"""
        ...
    @show_extra_indices.setter
    def show_extra_indices(self, value: bool):
        ...
    @property
    def display_handle(self) -> Literal['NONE', 'SELECTED', 'ALL']:
        """Limit the display of curve handles in edit mode"""
        ...
    @display_handle.setter
    def display_handle(self, value: Literal['NONE', 'SELECTED', 'ALL']):
        ...
    @property
    def show_curve_normals(self) -> bool:
        """Display 3D curve normals in editmode"""
        ...
    @show_curve_normals.setter
    def show_curve_normals(self, value: bool):
        ...
    @property
    def normals_length(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]:
        """Display size for normals in the 3D view"""
        ...
    @normals_length.setter
    def normals_length(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]):
        ...
    @property
    def normals_constant_screen_size(self) -> Annotated[float, "subtype='PIXEL'", "step=50.0", "precision=0"]:
        """Screen size for normals in the 3D view"""
        ...
    @normals_constant_screen_size.setter
    def normals_constant_screen_size(self, value: Annotated[float, "subtype='PIXEL'", "step=50.0", "precision=0"]):
        ...
    @property
    def use_normals_constant_screen_size(self) -> bool:
        """Keep size of normals constant in relation to 3D view"""
        ...
    @use_normals_constant_screen_size.setter
    def use_normals_constant_screen_size(self, value: bool):
        ...
    @property
    def texture_paint_mode_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Opacity of the texture paint mode stencil mask overlay"""
        ...
    @texture_paint_mode_opacity.setter
    def texture_paint_mode_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def vertex_paint_mode_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Opacity of the texture paint mode stencil mask overlay"""
        ...
    @vertex_paint_mode_opacity.setter
    def vertex_paint_mode_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def weight_paint_mode_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Opacity of the weight paint mode overlay"""
        ...
    @weight_paint_mode_opacity.setter
    def weight_paint_mode_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def sculpt_mode_mask_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:

        ...
    @sculpt_mode_mask_opacity.setter
    def sculpt_mode_mask_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def show_sculpt_curves_cage(self) -> bool:
        """Show original curves that are currently being edited"""
        ...
    @show_sculpt_curves_cage.setter
    def show_sculpt_curves_cage(self, value: bool):
        ...
    @property
    def sculpt_curves_cage_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Opacity of the cage overlay in curves sculpt mode"""
        ...
    @sculpt_curves_cage_opacity.setter
    def sculpt_curves_cage_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def sculpt_mode_face_sets_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:

        ...
    @sculpt_mode_face_sets_opacity.setter
    def sculpt_mode_face_sets_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def show_sculpt_mask(self) -> bool:

        ...
    @show_sculpt_mask.setter
    def show_sculpt_mask(self, value: bool):
        ...
    @property
    def show_sculpt_face_sets(self) -> bool:

        ...
    @show_sculpt_face_sets.setter
    def show_sculpt_face_sets(self, value: bool):
        ...
    @property
    def show_annotation(self) -> bool:
        """Show annotations for this view"""
        ...
    @show_annotation.setter
    def show_annotation(self, value: bool):
        ...
    @property
    def use_gpencil_fade_objects(self) -> bool:
        """Fade all viewport objects with a full color layer to improve visibility"""
        ...
    @use_gpencil_fade_objects.setter
    def use_gpencil_fade_objects(self, value: bool):
        ...
    @property
    def use_gpencil_grid(self) -> bool:
        """Display a grid over Grease Pencil paper"""
        ...
    @use_gpencil_grid.setter
    def use_gpencil_grid(self, value: bool):
        ...
    @property
    def use_gpencil_fade_layers(self) -> bool:
        """Toggle fading of Grease Pencil layers except the active one"""
        ...
    @use_gpencil_fade_layers.setter
    def use_gpencil_fade_layers(self, value: bool):
        ...
    @property
    def use_gpencil_fade_gp_objects(self) -> bool:
        """Fade Grease Pencil Objects, except the active one"""
        ...
    @use_gpencil_fade_gp_objects.setter
    def use_gpencil_fade_gp_objects(self, value: bool):
        ...
    @property
    def use_gpencil_canvas_xray(self) -> bool:
        """Show Canvas grid in front"""
        ...
    @use_gpencil_canvas_xray.setter
    def use_gpencil_canvas_xray(self, value: bool):
        ...
    @property
    def use_gpencil_show_directions(self) -> bool:
        """Show stroke drawing direction with a bigger green dot (start) and smaller red dot (end) points"""
        ...
    @use_gpencil_show_directions.setter
    def use_gpencil_show_directions(self, value: bool):
        ...
    @property
    def use_gpencil_show_material_name(self) -> bool:
        """Show material name assigned to each stroke"""
        ...
    @use_gpencil_show_material_name.setter
    def use_gpencil_show_material_name(self, value: bool):
        ...
    @property
    def gpencil_grid_opacity(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Canvas grid opacity"""
        ...
    @gpencil_grid_opacity.setter
    def gpencil_grid_opacity(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def gpencil_grid_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Canvas grid color"""
        ...
    @gpencil_grid_color.setter
    def gpencil_grid_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def gpencil_grid_scale(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]:
        """Canvas grid scale"""
        ...
    @gpencil_grid_scale.setter
    def gpencil_grid_scale(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]):
        ...
    @property
    def gpencil_grid_offset(self) -> Annotated[list[float], "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """Canvas grid offset"""
        ...
    @gpencil_grid_offset.setter
    def gpencil_grid_offset(self, value: Annotated[list[float], "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]):
        ...
    @property
    def gpencil_grid_subdivisions(self) -> Annotated[int, "step=1"]:
        """Canvas grid subdivisions"""
        ...
    @gpencil_grid_subdivisions.setter
    def gpencil_grid_subdivisions(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def gpencil_fade_objects(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Fade factor"""
        ...
    @gpencil_fade_objects.setter
    def gpencil_fade_objects(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def gpencil_fade_layer(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Fade layer opacity for Grease Pencil layers except the active one"""
        ...
    @gpencil_fade_layer.setter
    def gpencil_fade_layer(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def use_gpencil_edit_lines(self) -> bool:
        """Show Edit Lines when editing strokes"""
        ...
    @use_gpencil_edit_lines.setter
    def use_gpencil_edit_lines(self, value: bool):
        ...
    @property
    def use_gpencil_multiedit_line_only(self) -> bool:
        """Show Edit Lines only in multiframe"""
        ...
    @use_gpencil_multiedit_line_only.setter
    def use_gpencil_multiedit_line_only(self, value: bool):
        ...
    @property
    def use_gpencil_onion_skin(self) -> bool:
        """Show ghosts of the keyframes before and after the current frame"""
        ...
    @use_gpencil_onion_skin.setter
    def use_gpencil_onion_skin(self, value: bool):
        ...
    @property
    def use_gpencil_onion_skin_active_object(self) -> bool:
        """Show only the onion skins of the active object"""
        ...
    @use_gpencil_onion_skin_active_object.setter
    def use_gpencil_onion_skin_active_object(self, value: bool):
        ...
    @property
    def vertex_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Opacity for edit vertices"""
        ...
    @vertex_opacity.setter
    def vertex_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def gpencil_vertex_paint_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Vertex Paint mix factor"""
        ...
    @gpencil_vertex_paint_opacity.setter
    def gpencil_vertex_paint_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def use_debug_freeze_view_culling(self) -> bool:
        """Freeze view culling bounds"""
        ...
    @use_debug_freeze_view_culling.setter
    def use_debug_freeze_view_culling(self, value: bool):
        ...