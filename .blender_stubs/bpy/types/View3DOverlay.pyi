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

    show_overlays: bool
    """Display overlays like gizmos and outlines"""
    show_ortho_grid: bool
    """Show grid in orthographic side view"""
    show_floor: bool
    """Show the ground plane grid"""
    show_axis_x: bool
    """Show the X axis line"""
    show_axis_y: bool
    """Show the Y axis line"""
    show_axis_z: bool
    """Show the Z axis line"""
    grid_scale: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """Multiplier for the distance between 3D View grid lines"""
    grid_lines: Annotated[int, "step=1"]
    """Number of grid lines to display in perspective view"""
    grid_subdivisions: Annotated[int, "step=1"]
    """Number of subdivisions between grid lines"""
    @property
    def grid_scale_unit(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Grid cell size scaled by scene unit system settings"""
        ...
    show_outline_selected: bool
    """Show an outline highlight around selected objects"""
    show_object_origins: bool
    """Show object center dots"""
    show_object_origins_all: bool
    """Show the object origin center dot for all (selected and unselected) objects"""
    show_relationship_lines: bool
    """Show dashed lines indicating parent or constraint relationships"""
    show_cursor: bool
    """Display 3D Cursor Overlay"""
    show_text: bool
    """Display overlay text"""
    show_stats: bool
    """Display scene statistics overlay text"""
    show_camera_guides: bool
    """Show camera composition guides"""
    show_camera_passepartout: bool
    """Show camera passepartout"""
    show_extras: bool
    """Object details, including empty wire, cameras and other visual guides"""
    show_light_colors: bool
    """Show light colors"""
    show_bones: bool
    """Display bones (disable to show motion paths only)"""
    show_face_orientation: Annotated[bool, "is_animatable=False"]
    """Show the Face Orientation Overlay"""
    show_fade_inactive: Annotated[bool, "is_animatable=False"]
    """Fade inactive geometry using the viewport background color"""
    fade_inactive_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Strength of the fade effect"""
    show_xray_bone: Annotated[bool, "is_animatable=False"]
    """Show the bone selection overlay"""
    xray_alpha_bone: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Opacity to use for bone selection"""
    bone_wire_alpha: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2", "is_animatable=False"]
    """Maximum opacity of bones in wireframe display mode"""
    show_motion_paths: Annotated[bool, "is_animatable=False"]
    """Show the Motion Paths Overlay"""
    show_onion_skins: Annotated[bool, "is_animatable=False"]
    """Show the Onion Skinning Overlay"""
    show_look_dev: Annotated[bool, "is_animatable=False"]
    """Show reference spheres with neutral shading that react to lighting to assist in look development"""
    show_wireframes: Annotated[bool, "is_animatable=False"]
    """Show face edges wires"""
    wireframe_threshold: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Adjust the angle threshold for displaying edges (1.0 for all)"""
    wireframe_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Opacity of the displayed edges (1.0 for opaque)"""
    show_viewer_attribute: Annotated[bool, "is_animatable=False"]
    """Show attribute overlay for active viewer node"""
    viewer_attribute_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Opacity of the attribute that is currently visualized"""
    show_viewer_text: Annotated[bool, "is_animatable=False"]
    """Show attribute values as text in viewport"""
    show_paint_wire: bool
    """Use wireframe display in painting modes"""
    show_wpaint_contours: bool
    """Show contour lines formed by points with the same interpolated weight"""
    show_weight: bool
    """Display weights in editmode"""
    show_retopology: bool
    """Hide the solid mesh and offset the overlay towards the view. Selection is occluded by inactive geometry, unless X-Ray is enabled"""
    retopology_offset: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """Offset used to draw edit mesh in front of other geometry"""
    show_face_normals: bool
    """Display face normals as lines"""
    show_vertex_normals: bool
    """Display vertex normals as lines"""
    show_split_normals: bool
    """Display vertex-per-face normals as lines"""
    show_faces: bool
    """Display a face selection overlay"""
    show_face_center: bool
    """Display face center when face selection is enabled in solid shading modes"""
    show_edge_crease: bool
    """Display creases created for Subdivision Surface modifier"""
    show_edge_bevel_weight: bool
    """Display weights created for the Bevel modifier"""
    show_edge_seams: bool
    """Display UV unwrapping seams"""
    show_edge_sharp: bool
    """Display sharp edges, used with the Edge Split modifier"""
    show_freestyle_edge_marks: bool
    """Display Freestyle edge marks, used with the Freestyle renderer"""
    show_freestyle_face_marks: bool
    """Display Freestyle face marks, used with the Freestyle renderer"""
    show_statvis: bool
    """Display statistical information about the mesh"""
    show_extra_edge_length: bool
    """Display selected edge lengths, using global values when set in the transform panel"""
    show_extra_edge_angle: bool
    """Display selected edge angle, using global values when set in the transform panel"""
    show_extra_face_angle: bool
    """Display the angles in the selected edges, using global values when set in the transform panel"""
    show_extra_face_area: bool
    """Display the area of selected faces, using global values when set in the transform panel"""
    show_extra_indices: bool
    """Display the index numbers of selected vertices, edges, and faces"""
    display_handle: Literal['NONE', 'SELECTED', 'ALL']
    """Limit the display of curve handles in edit mode"""
    show_curve_normals: bool
    """Display 3D curve normals in editmode"""
    normals_length: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]
    """Display size for normals in the 3D view"""
    normals_constant_screen_size: Annotated[float, "subtype='PIXEL'", "step=50.0", "precision=0"]
    """Screen size for normals in the 3D view"""
    use_normals_constant_screen_size: bool
    """Keep size of normals constant in relation to 3D view"""
    texture_paint_mode_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Opacity of the texture paint mode stencil mask overlay"""
    vertex_paint_mode_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Opacity of the texture paint mode stencil mask overlay"""
    weight_paint_mode_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Opacity of the weight paint mode overlay"""
    sculpt_mode_mask_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]

    show_sculpt_curves_cage: bool
    """Show original curves that are currently being edited"""
    sculpt_curves_cage_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Opacity of the cage overlay in curves sculpt mode"""
    sculpt_mode_face_sets_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]

    show_sculpt_mask: bool

    show_sculpt_face_sets: bool

    show_annotation: bool
    """Show annotations for this view"""
    use_gpencil_fade_objects: bool
    """Fade all viewport objects with a full color layer to improve visibility"""
    use_gpencil_grid: bool
    """Display a grid over Grease Pencil paper"""
    use_gpencil_fade_layers: bool
    """Toggle fading of Grease Pencil layers except the active one"""
    use_gpencil_fade_gp_objects: bool
    """Fade Grease Pencil Objects, except the active one"""
    use_gpencil_canvas_xray: bool
    """Show Canvas grid in front"""
    use_gpencil_show_directions: bool
    """Show stroke drawing direction with a bigger green dot (start) and smaller red dot (end) points"""
    use_gpencil_show_material_name: bool
    """Show material name assigned to each stroke"""
    gpencil_grid_opacity: Annotated[float, "step=10.0", "precision=3"]
    """Canvas grid opacity"""
    gpencil_grid_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Canvas grid color"""
    gpencil_grid_scale: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Canvas grid scale"""
    gpencil_grid_offset: Annotated[list[float], "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Canvas grid offset"""
    gpencil_grid_subdivisions: Annotated[int, "step=1"]
    """Canvas grid subdivisions"""
    gpencil_fade_objects: Annotated[float, "step=10.0", "precision=3"]
    """Fade factor"""
    gpencil_fade_layer: Annotated[float, "step=10.0", "precision=3"]
    """Fade layer opacity for Grease Pencil layers except the active one"""
    use_gpencil_edit_lines: bool
    """Show Edit Lines when editing strokes"""
    use_gpencil_multiedit_line_only: bool
    """Show Edit Lines only in multiframe"""
    use_gpencil_onion_skin: bool
    """Show ghosts of the keyframes before and after the current frame"""
    use_gpencil_onion_skin_active_object: bool
    """Show only the onion skins of the active object"""
    vertex_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Opacity for edit vertices"""
    gpencil_vertex_paint_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Vertex Paint mix factor"""
    use_debug_freeze_view_culling: bool
    """Freeze view culling bounds"""