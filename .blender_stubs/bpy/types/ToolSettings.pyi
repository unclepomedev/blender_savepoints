# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ToolSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .CurvePaintSettings import CurvePaintSettings
from .CurveProfile import CurveProfile
from .CurvesSculpt import CurvesSculpt
from .GPencilInterpolateSettings import GPencilInterpolateSettings
from .GPencilSculptSettings import GPencilSculptSettings
from .GpPaint import GpPaint
from .GpSculptPaint import GpSculptPaint
from .GpVertexPaint import GpVertexPaint
from .GpWeightPaint import GpWeightPaint
from .ImagePaint import ImagePaint
from .MeshStatVis import MeshStatVis
from .Object import Object
from .PaintModeSettings import PaintModeSettings
from .ParticleEdit import ParticleEdit
from .Sculpt import Sculpt
from .SequencerToolSettings import SequencerToolSettings
from .UvSculpt import UvSculpt
from .VertexPaint import VertexPaint

class ToolSettings(bpy_struct):

    @property
    def sculpt(self) -> Annotated[Optional['Sculpt'], "is_animatable=False"]:

        ...
    @property
    def curves_sculpt(self) -> Annotated[Optional['CurvesSculpt'], "is_animatable=False"]:

        ...
    use_auto_normalize: Annotated[bool, "is_animatable=False"]
    """Ensure all bone-deforming vertex groups add up to 1.0 while weight painting or assigning to vertices"""
    use_lock_relative: Annotated[bool, "is_animatable=False"]
    """Display bone-deforming groups as if all locked deform groups were deleted, and the remaining ones were re-normalized"""
    use_multipaint: Annotated[bool, "is_animatable=False"]
    """Paint across the weights of all selected bones, maintaining their relative influence"""
    vertex_group_user: Annotated[Literal['NONE', 'ACTIVE', 'ALL'], "is_animatable=False"]
    """Display unweighted vertices"""
    vertex_group_subset: Annotated[Literal['ALL', 'BONE_DEFORM', 'OTHER_DEFORM'], "is_animatable=False"]
    """Filter Vertex groups for Display"""
    @property
    def vertex_paint(self) -> Annotated[Optional['VertexPaint'], "is_animatable=False"]:

        ...
    @property
    def weight_paint(self) -> Annotated[Optional['VertexPaint'], "is_animatable=False"]:

        ...
    @property
    def image_paint(self) -> Annotated[Optional['ImagePaint'], "is_animatable=False"]:

        ...
    @property
    def paint_mode(self) -> Annotated[Optional['PaintModeSettings'], "is_animatable=False"]:

        ...
    @property
    def uv_sculpt(self) -> Annotated[Optional['UvSculpt'], "is_animatable=False"]:

        ...
    @property
    def gpencil_paint(self) -> Annotated[Optional['GpPaint'], "is_animatable=False"]:

        ...
    @property
    def gpencil_vertex_paint(self) -> Annotated[Optional['GpVertexPaint'], "is_animatable=False"]:

        ...
    @property
    def gpencil_sculpt_paint(self) -> Annotated[Optional['GpSculptPaint'], "is_animatable=False"]:

        ...
    @property
    def gpencil_weight_paint(self) -> Annotated[Optional['GpWeightPaint'], "is_animatable=False"]:

        ...
    @property
    def particle_edit(self) -> Annotated[Optional['ParticleEdit'], "is_animatable=False"]:

        ...
    uv_sculpt_lock_borders: Annotated[bool, "is_animatable=False"]
    """Disable editing of boundary edges"""
    uv_sculpt_all_islands: Annotated[bool, "is_animatable=False"]
    """Brush operates on all islands"""
    lock_object_mode: Annotated[bool, "is_animatable=False"]
    """Restrict selection to objects using the same mode as the active object, to prevent accidental mode switch when selecting"""
    workspace_tool_type: Annotated[Literal['DEFAULT', 'FALLBACK'], "is_animatable=False"]
    """Action when dragging in the viewport"""
    use_proportional_edit: Annotated[bool, "is_animatable=False"]
    """Proportional edit mode"""
    use_proportional_edit_objects: Annotated[bool, "is_animatable=False"]
    """Proportional editing object mode"""
    use_proportional_projected: Annotated[bool, "is_animatable=False"]
    """Proportional Editing using screen space locations"""
    use_proportional_connected: Annotated[bool, "is_animatable=False"]
    """Proportional Editing using connected geometry only"""
    use_proportional_edit_mask: Annotated[bool, "is_animatable=False"]
    """Proportional editing mask mode"""
    use_proportional_action: Annotated[bool, "is_animatable=False"]
    """Proportional editing in action editor"""
    use_proportional_fcurve: Annotated[bool, "is_animatable=False"]
    """Proportional editing in F-Curve editor"""
    lock_markers: Annotated[bool, "is_animatable=False"]
    """Prevent marker editing"""
    proportional_edit_falloff: Annotated[Literal['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], "is_animatable=False"]
    """Falloff type for proportional editing mode"""
    proportional_size: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Display size for proportional editing circle"""
    proportional_distance: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]
    """Display size for proportional editing circle"""
    double_threshold: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=6", "is_animatable=False"]
    """Threshold distance for Auto Merge"""
    transform_pivot_point: Annotated[Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT', 'ACTIVE_ELEMENT'], "is_animatable=False"]
    """Pivot center for rotation/scaling"""
    use_transform_pivot_point_align: Annotated[bool, "is_animatable=False"]
    """Only transform object locations, without affecting rotation or scaling"""
    use_transform_data_origin: Annotated[bool, "is_animatable=False"]
    """Transform object origins, while leaving the shape in place"""
    use_transform_skip_children: Annotated[bool, "is_animatable=False"]
    """Transform the parents, leaving the children in place"""
    use_transform_correct_face_attributes: Annotated[bool, "is_animatable=False"]
    """Correct data such as UVs and color attributes when transforming"""
    use_transform_correct_keep_connected: Annotated[bool, "is_animatable=False"]
    """During the Face Attributes correction, merge attributes connected to the same vertex"""
    use_mesh_automerge: Annotated[bool, "is_animatable=False"]
    """Automatically merge vertices moved to the same location"""
    use_mesh_automerge_and_split: Annotated[bool, "is_animatable=False"]
    """Automatically split edges and faces"""
    use_snap: Annotated[bool, "is_animatable=False"]
    """Snap during transform"""
    use_snap_node: Annotated[bool, "is_animatable=False"]
    """Snap Node during transform"""
    use_snap_sequencer: Annotated[bool, "is_animatable=False"]
    """Snap strips during transform"""
    use_snap_uv: Annotated[bool, "is_animatable=False"]
    """Snap UV during transform"""
    use_snap_align_rotation: Annotated[bool, "is_animatable=False"]
    """Align rotation with the snapping target"""
    use_snap_grid_absolute: Annotated[bool, "is_animatable=False"]
    """Absolute grid alignment while translating (based on the pivot center)"""
    snap_angle_increment_2d: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=100.0", "precision=2", "is_animatable=False"]
    """Angle used for rotation increments in 2D editors"""
    snap_angle_increment_2d_precision: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Precision angle used for rotation increments in 2D editors"""
    snap_angle_increment_3d: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=100.0", "precision=2", "is_animatable=False"]
    """Angle used for rotation increments in 3D editors"""
    snap_angle_increment_3d_precision: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Precision angle used for rotation increments in 3D editors"""
    snap_elements: Annotated[set[str], "is_animatable=False"]
    """Type of element to snap to"""
    snap_elements_base: Annotated[set[str], "is_animatable=False"]
    """Type of element for the "Snap Base" to snap to"""
    snap_elements_individual: Annotated[set[str], "is_animatable=False"]
    """Type of element for individual transformed elements to snap to"""
    snap_face_nearest_steps: Annotated[int, "subtype='FACTOR'", "step=1", "is_animatable=False"]
    """Number of steps to break transformation into for face nearest snapping"""
    use_snap_to_same_target: Annotated[bool, "is_animatable=False"]
    """Snap only to target that source was initially near ("Face Nearest" only)"""
    use_snap_anim: Annotated[bool, "is_animatable=False"]
    """Enable snapping when transforming keyframes"""
    use_snap_driver: Annotated[bool, "is_animatable=False"]
    """Enable snapping when transforming keys in the Driver Editor"""
    use_snap_time_absolute: Annotated[bool, "is_animatable=False"]
    """Absolute time alignment when transforming keyframes"""
    use_snap_driver_absolute: Annotated[bool, "is_animatable=False"]
    """Snap to full values"""
    snap_anim_element: Annotated[Literal['FRAME', 'SECOND', 'MARKER'], "is_animatable=False"]
    """Type of element to snap to"""
    use_snap_playhead: Annotated[bool, "is_animatable=False"]
    """Snap playhead when scrubbing"""
    snap_playhead_element: Annotated[set[str], "is_animatable=False"]
    """Type of element to snap to"""
    snap_playhead_frame_step: Annotated[int, "step=1", "is_animatable=False"]
    """At which interval to snap to frames"""
    snap_playhead_second_step: Annotated[int, "step=1", "is_animatable=False"]
    """At which interval to snap to seconds"""
    playhead_snap_distance: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Maximum distance for snapping in pixels"""
    snap_uv_element: Annotated[set[str], "is_animatable=False"]
    """Type of element to snap to"""
    snap_target: Annotated[Literal['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], "is_animatable=False"]
    """Which part to snap onto the target"""
    use_snap_peel_object: Annotated[bool, "is_animatable=False"]
    """Consider objects as whole when finding volume center"""
    use_snap_backface_culling: Annotated[bool, "is_animatable=False"]
    """Exclude back facing geometry from snapping"""
    use_snap_self: Annotated[bool, "is_animatable=False"]
    """Snap onto itself only if enabled (edit mode only)"""
    use_snap_edit: Annotated[bool, "is_animatable=False"]
    """Snap onto non-active objects in edit mode (edit mode only)"""
    use_snap_nonedit: Annotated[bool, "is_animatable=False"]
    """Snap onto objects not in edit mode (edit mode only)"""
    use_snap_selectable: Annotated[bool, "is_animatable=False"]
    """Snap only onto objects that are selectable"""
    use_snap_translate: Annotated[bool, "is_animatable=False"]
    """Move is affected by snapping settings"""
    use_snap_rotate: Annotated[bool, "is_animatable=False"]
    """Rotate is affected by the snapping settings"""
    use_snap_scale: Annotated[bool, "is_animatable=False"]
    """Scale is affected by snapping settings"""
    plane_axis: Annotated[Literal['X', 'Y', 'Z'], "is_animatable=False"]
    """The axis used for placing the base region"""
    plane_axis_auto: Annotated[bool, "is_animatable=False"]
    """Select the closest axis when placing objects (surface overrides)"""
    plane_depth: Annotated[Literal['SURFACE', 'CURSOR_PLANE', 'CURSOR_VIEW'], "is_animatable=False"]
    """The initial depth used when placing the cursor"""
    plane_orientation: Annotated[Literal['SURFACE', 'DEFAULT'], "is_animatable=False"]
    """The initial depth used when placing the cursor"""
    snap_elements_tool: Annotated[Literal['GEOMETRY', 'DEFAULT'], "is_animatable=False"]
    """The target to use while snapping"""
    use_gpencil_draw_additive: Annotated[bool, "is_animatable=False"]
    """When creating new frames, the strokes from the previous/active frame are included as the basis for the new one"""
    use_gpencil_draw_onback: Annotated[bool, "is_animatable=False"]
    """New strokes are drawn below of all strokes in the layer"""
    use_gpencil_thumbnail_list: Annotated[bool, "is_animatable=False"]
    """Show compact list of colors instead of thumbnails"""
    use_gpencil_weight_data_add: Annotated[bool, "is_animatable=False"]
    """Weight data for new strokes is added according to the current vertex group and weight. If no vertex group selected, weight is not added."""
    use_gpencil_automerge_strokes: Annotated[bool, "is_animatable=False"]
    """Join the last drawn stroke with previous strokes in the active layer by distance"""
    @property
    def gpencil_sculpt(self) -> Annotated[Optional['GPencilSculptSettings'], "is_animatable=False"]:
        """Settings for stroke sculpting tools and brushes"""
        ...
    @property
    def gpencil_interpolate(self) -> Annotated[Optional['GPencilInterpolateSettings'], "is_animatable=False"]:
        """Settings for Grease Pencil interpolation tools"""
        ...
    gpencil_stroke_placement_view3d: Annotated[Literal['ORIGIN', 'CURSOR', 'SURFACE', 'STROKE'], "is_animatable=False"]

    gpencil_stroke_snap_mode: Annotated[Literal['NONE', 'ENDS', 'FIRST'], "is_animatable=False"]

    gpencil_surface_offset: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """Offset along the normal when drawing on surfaces"""
    use_gpencil_project_only_selected: Annotated[bool, "is_animatable=False"]
    """Project the strokes only onto selected objects"""
    gpencil_selectmode_edit: Annotated[Literal['POINT', 'STROKE', 'SEGMENT'], "is_animatable=False"]

    use_gpencil_select_mask_point: Annotated[bool, "is_animatable=False"]
    """Only sculpt selected stroke points"""
    use_gpencil_select_mask_stroke: Annotated[bool, "is_animatable=False"]
    """Only sculpt selected strokes"""
    use_gpencil_select_mask_segment: Annotated[bool, "is_animatable=False"]
    """Only sculpt selected stroke points between other strokes"""
    use_gpencil_vertex_select_mask_point: Annotated[bool, "is_animatable=False"]
    """Only paint selected stroke points"""
    use_gpencil_vertex_select_mask_stroke: Annotated[bool, "is_animatable=False"]
    """Only paint selected strokes"""
    use_gpencil_vertex_select_mask_segment: Annotated[bool, "is_animatable=False"]
    """Only paint selected stroke points between other strokes"""
    use_grease_pencil_multi_frame_editing: Annotated[bool, "is_animatable=False"]
    """Enable multi-frame editing"""
    annotation_stroke_placement_view2d: Annotated[Literal['IMAGE', 'VIEW'], "is_animatable=False"]

    annotation_stroke_placement_view3d: Annotated[Literal['CURSOR', 'VIEW', 'SURFACE'], "is_animatable=False"]
    """How annotation strokes are orientated in 3D space"""
    use_annotation_stroke_endpoints: Annotated[bool, "is_animatable=False"]
    """Only use the first and last parts of the stroke for snapping"""
    use_annotation_project_only_selected: Annotated[bool, "is_animatable=False"]
    """Project the strokes only onto selected objects"""
    annotation_thickness: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Thickness of annotation strokes"""
    use_keyframe_insert_auto: Annotated[bool, "is_animatable=False"]
    """Automatic keyframe insertion for objects, bones and masks"""
    auto_keying_mode: Annotated[Literal['ADD_REPLACE_KEYS', 'REPLACE_KEYS'], "is_animatable=False"]
    """Mode of automatic keyframe insertion for objects, bones and masks"""
    use_record_with_nla: Annotated[bool, "is_animatable=False"]
    """Add a new NLA Track + Strip for every loop/pass made over the animation to allow non-destructive tweaking"""
    use_keyframe_insert_keyingset: Annotated[bool, "is_animatable=False"]
    """Automatic keyframe insertion using active Keying Set only"""
    use_keyframe_cycle_aware: Annotated[bool, "is_animatable=False"]
    """For channels with cyclic extrapolation, keyframe insertion is automatically remapped inside the cycle time range, and keeps ends in sync. Curves newly added to actions with a Manual Frame Range and Cyclic Animation are automatically made cyclic."""
    keyframe_type: Annotated[Literal['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER', 'GENERATED'], "is_animatable=False"]
    """Type of keyframes to create when inserting keyframes"""
    anim_mirror_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Object to mirror over. Leave empty and name a bone to always mirror over that bone of the active armature"""
    anim_mirror_bone: Annotated[str, "is_animatable=False"]
    """Bone to use for the mirroring"""
    anim_relative_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Object to which matrices are made relative"""
    anim_fix_to_cam_use_loc: Annotated[bool, "is_animatable=False"]
    """Create location keys when fixing to the scene camera"""
    anim_fix_to_cam_use_rot: Annotated[bool, "is_animatable=False"]
    """Create rotation keys when fixing to the scene camera"""
    anim_fix_to_cam_use_scale: Annotated[bool, "is_animatable=False"]
    """Create scale keys when fixing to the scene camera"""
    uv_select_mode: Annotated[Literal['VERTEX', 'EDGE', 'FACE'], "is_animatable=False"]
    """UV selection and display mode"""
    uv_sticky_select_mode: Annotated[Literal['DISABLED', 'SHARED_LOCATION', 'SHARED_VERTEX'], "is_animatable=False"]
    """Method for extending UV vertex selection"""
    use_uv_select_sync: Annotated[bool, "is_animatable=False"]
    """Keep UV and edit mode mesh selection in sync"""
    use_uv_select_island: Annotated[bool, "is_animatable=False"]
    """Island selection"""
    show_uv_local_view: Annotated[bool, "is_animatable=False"]
    """Display only faces with the currently displayed image assigned"""
    use_uv_custom_region: Annotated[bool, "is_animatable=False"]
    """Custom defined region"""
    mesh_select_mode: Annotated[list[bool], "is_animatable=False"]
    """Which mesh elements selection works on"""
    vertex_group_weight: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Weight to assign in vertex groups"""
    use_edge_path_live_unwrap: Annotated[bool, "is_animatable=False"]
    """Changing edge seams recalculates UV unwrap"""
    normal_vector: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3", "is_animatable=False"]
    """Normal vector used to copy, add or multiply"""
    @property
    def curve_paint_settings(self) -> Annotated['CurvePaintSettings', "is_animatable=False"]:

        ...
    @property
    def statvis(self) -> Annotated['MeshStatVis', "is_animatable=False"]:

        ...
    @property
    def custom_bevel_profile_preset(self) -> Annotated[Optional['CurveProfile'], "is_animatable=False"]:
        """Used for defining a profile's path"""
        ...
    @property
    def sequencer_tool_settings(self) -> Annotated['SequencerToolSettings', "is_animatable=False"]:

        ...