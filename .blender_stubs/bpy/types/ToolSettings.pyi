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
    @property
    def use_auto_normalize(self) -> Annotated[bool, "is_animatable=False"]:
        """Ensure all bone-deforming vertex groups add up to 1.0 while weight painting or assigning to vertices"""
        ...
    @use_auto_normalize.setter
    def use_auto_normalize(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_lock_relative(self) -> Annotated[bool, "is_animatable=False"]:
        """Display bone-deforming groups as if all locked deform groups were deleted, and the remaining ones were re-normalized"""
        ...
    @use_lock_relative.setter
    def use_lock_relative(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_multipaint(self) -> Annotated[bool, "is_animatable=False"]:
        """Paint across the weights of all selected bones, maintaining their relative influence"""
        ...
    @use_multipaint.setter
    def use_multipaint(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def vertex_group_user(self) -> Annotated[Literal['NONE', 'ACTIVE', 'ALL'], "is_animatable=False"]:
        """Display unweighted vertices"""
        ...
    @vertex_group_user.setter
    def vertex_group_user(self, value: Annotated[Literal['NONE', 'ACTIVE', 'ALL'], "is_animatable=False"]):
        ...
    @property
    def vertex_group_subset(self) -> Annotated[Literal['ALL', 'BONE_DEFORM', 'OTHER_DEFORM'], "is_animatable=False"]:
        """Filter Vertex groups for Display"""
        ...
    @vertex_group_subset.setter
    def vertex_group_subset(self, value: Annotated[Literal['ALL', 'BONE_DEFORM', 'OTHER_DEFORM'], "is_animatable=False"]):
        ...
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
    @property
    def uv_sculpt_lock_borders(self) -> Annotated[bool, "is_animatable=False"]:
        """Disable editing of boundary edges"""
        ...
    @uv_sculpt_lock_borders.setter
    def uv_sculpt_lock_borders(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def uv_sculpt_all_islands(self) -> Annotated[bool, "is_animatable=False"]:
        """Brush operates on all islands"""
        ...
    @uv_sculpt_all_islands.setter
    def uv_sculpt_all_islands(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def lock_object_mode(self) -> Annotated[bool, "is_animatable=False"]:
        """Restrict selection to objects using the same mode as the active object, to prevent accidental mode switch when selecting"""
        ...
    @lock_object_mode.setter
    def lock_object_mode(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def workspace_tool_type(self) -> Annotated[Literal['DEFAULT', 'FALLBACK'], "is_animatable=False"]:
        """Action when dragging in the viewport"""
        ...
    @workspace_tool_type.setter
    def workspace_tool_type(self, value: Annotated[Literal['DEFAULT', 'FALLBACK'], "is_animatable=False"]):
        ...
    @property
    def use_proportional_edit(self) -> Annotated[bool, "is_animatable=False"]:
        """Proportional edit mode"""
        ...
    @use_proportional_edit.setter
    def use_proportional_edit(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_proportional_edit_objects(self) -> Annotated[bool, "is_animatable=False"]:
        """Proportional editing object mode"""
        ...
    @use_proportional_edit_objects.setter
    def use_proportional_edit_objects(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_proportional_projected(self) -> Annotated[bool, "is_animatable=False"]:
        """Proportional Editing using screen space locations"""
        ...
    @use_proportional_projected.setter
    def use_proportional_projected(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_proportional_connected(self) -> Annotated[bool, "is_animatable=False"]:
        """Proportional Editing using connected geometry only"""
        ...
    @use_proportional_connected.setter
    def use_proportional_connected(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_proportional_edit_mask(self) -> Annotated[bool, "is_animatable=False"]:
        """Proportional editing mask mode"""
        ...
    @use_proportional_edit_mask.setter
    def use_proportional_edit_mask(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_proportional_action(self) -> Annotated[bool, "is_animatable=False"]:
        """Proportional editing in action editor"""
        ...
    @use_proportional_action.setter
    def use_proportional_action(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_proportional_fcurve(self) -> Annotated[bool, "is_animatable=False"]:
        """Proportional editing in F-Curve editor"""
        ...
    @use_proportional_fcurve.setter
    def use_proportional_fcurve(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def lock_markers(self) -> Annotated[bool, "is_animatable=False"]:
        """Prevent marker editing"""
        ...
    @lock_markers.setter
    def lock_markers(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def proportional_edit_falloff(self) -> Annotated[Literal['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], "is_animatable=False"]:
        """Falloff type for proportional editing mode"""
        ...
    @proportional_edit_falloff.setter
    def proportional_edit_falloff(self, value: Annotated[Literal['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], "is_animatable=False"]):
        ...
    @property
    def proportional_size(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Display size for proportional editing circle"""
        ...
    @proportional_size.setter
    def proportional_size(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def proportional_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Display size for proportional editing circle"""
        ...
    @proportional_distance.setter
    def proportional_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def double_threshold(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=6", "is_animatable=False"]:
        """Threshold distance for Auto Merge"""
        ...
    @double_threshold.setter
    def double_threshold(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=6", "is_animatable=False"]):
        ...
    @property
    def transform_pivot_point(self) -> Annotated[Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT', 'ACTIVE_ELEMENT'], "is_animatable=False"]:
        """Pivot center for rotation/scaling"""
        ...
    @transform_pivot_point.setter
    def transform_pivot_point(self, value: Annotated[Literal['BOUNDING_BOX_CENTER', 'CURSOR', 'INDIVIDUAL_ORIGINS', 'MEDIAN_POINT', 'ACTIVE_ELEMENT'], "is_animatable=False"]):
        ...
    @property
    def use_transform_pivot_point_align(self) -> Annotated[bool, "is_animatable=False"]:
        """Only transform object locations, without affecting rotation or scaling"""
        ...
    @use_transform_pivot_point_align.setter
    def use_transform_pivot_point_align(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_transform_data_origin(self) -> Annotated[bool, "is_animatable=False"]:
        """Transform object origins, while leaving the shape in place"""
        ...
    @use_transform_data_origin.setter
    def use_transform_data_origin(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_transform_skip_children(self) -> Annotated[bool, "is_animatable=False"]:
        """Transform the parents, leaving the children in place"""
        ...
    @use_transform_skip_children.setter
    def use_transform_skip_children(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_transform_correct_face_attributes(self) -> Annotated[bool, "is_animatable=False"]:
        """Correct data such as UVs and color attributes when transforming"""
        ...
    @use_transform_correct_face_attributes.setter
    def use_transform_correct_face_attributes(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_transform_correct_keep_connected(self) -> Annotated[bool, "is_animatable=False"]:
        """During the Face Attributes correction, merge attributes connected to the same vertex"""
        ...
    @use_transform_correct_keep_connected.setter
    def use_transform_correct_keep_connected(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_mesh_automerge(self) -> Annotated[bool, "is_animatable=False"]:
        """Automatically merge vertices moved to the same location"""
        ...
    @use_mesh_automerge.setter
    def use_mesh_automerge(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_mesh_automerge_and_split(self) -> Annotated[bool, "is_animatable=False"]:
        """Automatically split edges and faces"""
        ...
    @use_mesh_automerge_and_split.setter
    def use_mesh_automerge_and_split(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap during transform"""
        ...
    @use_snap.setter
    def use_snap(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_node(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap Node during transform"""
        ...
    @use_snap_node.setter
    def use_snap_node(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_sequencer(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap strips during transform"""
        ...
    @use_snap_sequencer.setter
    def use_snap_sequencer(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_uv(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap UV during transform"""
        ...
    @use_snap_uv.setter
    def use_snap_uv(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_align_rotation(self) -> Annotated[bool, "is_animatable=False"]:
        """Align rotation with the snapping target"""
        ...
    @use_snap_align_rotation.setter
    def use_snap_align_rotation(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_grid_absolute(self) -> Annotated[bool, "is_animatable=False"]:
        """Absolute grid alignment while translating (based on the pivot center)"""
        ...
    @use_snap_grid_absolute.setter
    def use_snap_grid_absolute(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def snap_angle_increment_2d(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=100.0", "precision=2", "is_animatable=False"]:
        """Angle used for rotation increments in 2D editors"""
        ...
    @snap_angle_increment_2d.setter
    def snap_angle_increment_2d(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=100.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def snap_angle_increment_2d_precision(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Precision angle used for rotation increments in 2D editors"""
        ...
    @snap_angle_increment_2d_precision.setter
    def snap_angle_increment_2d_precision(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def snap_angle_increment_3d(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=100.0", "precision=2", "is_animatable=False"]:
        """Angle used for rotation increments in 3D editors"""
        ...
    @snap_angle_increment_3d.setter
    def snap_angle_increment_3d(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=100.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def snap_angle_increment_3d_precision(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Precision angle used for rotation increments in 3D editors"""
        ...
    @snap_angle_increment_3d_precision.setter
    def snap_angle_increment_3d_precision(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def snap_elements(self) -> Annotated[set[str], "is_animatable=False"]:
        """Type of element to snap to"""
        ...
    @snap_elements.setter
    def snap_elements(self, value: Annotated[set[str], "is_animatable=False"]):
        ...
    @property
    def snap_elements_base(self) -> Annotated[set[str], "is_animatable=False"]:
        """Type of element for the "Snap Base" to snap to"""
        ...
    @snap_elements_base.setter
    def snap_elements_base(self, value: Annotated[set[str], "is_animatable=False"]):
        ...
    @property
    def snap_elements_individual(self) -> Annotated[set[str], "is_animatable=False"]:
        """Type of element for individual transformed elements to snap to"""
        ...
    @snap_elements_individual.setter
    def snap_elements_individual(self, value: Annotated[set[str], "is_animatable=False"]):
        ...
    @property
    def snap_face_nearest_steps(self) -> Annotated[int, "subtype='FACTOR'", "step=1", "is_animatable=False"]:
        """Number of steps to break transformation into for face nearest snapping"""
        ...
    @snap_face_nearest_steps.setter
    def snap_face_nearest_steps(self, value: Annotated[int, "subtype='FACTOR'", "step=1", "is_animatable=False"]):
        ...
    @property
    def use_snap_to_same_target(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap only to target that source was initially near ("Face Nearest" only)"""
        ...
    @use_snap_to_same_target.setter
    def use_snap_to_same_target(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_anim(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable snapping when transforming keyframes"""
        ...
    @use_snap_anim.setter
    def use_snap_anim(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_driver(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable snapping when transforming keys in the Driver Editor"""
        ...
    @use_snap_driver.setter
    def use_snap_driver(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_time_absolute(self) -> Annotated[bool, "is_animatable=False"]:
        """Absolute time alignment when transforming keyframes"""
        ...
    @use_snap_time_absolute.setter
    def use_snap_time_absolute(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_driver_absolute(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap to full values"""
        ...
    @use_snap_driver_absolute.setter
    def use_snap_driver_absolute(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def snap_anim_element(self) -> Annotated[Literal['FRAME', 'SECOND', 'MARKER'], "is_animatable=False"]:
        """Type of element to snap to"""
        ...
    @snap_anim_element.setter
    def snap_anim_element(self, value: Annotated[Literal['FRAME', 'SECOND', 'MARKER'], "is_animatable=False"]):
        ...
    @property
    def use_snap_playhead(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap playhead when scrubbing"""
        ...
    @use_snap_playhead.setter
    def use_snap_playhead(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def snap_playhead_element(self) -> Annotated[set[str], "is_animatable=False"]:
        """Type of element to snap to"""
        ...
    @snap_playhead_element.setter
    def snap_playhead_element(self, value: Annotated[set[str], "is_animatable=False"]):
        ...
    @property
    def snap_playhead_frame_step(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """At which interval to snap to frames"""
        ...
    @snap_playhead_frame_step.setter
    def snap_playhead_frame_step(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def snap_playhead_second_step(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """At which interval to snap to seconds"""
        ...
    @snap_playhead_second_step.setter
    def snap_playhead_second_step(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def playhead_snap_distance(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Maximum distance for snapping in pixels"""
        ...
    @playhead_snap_distance.setter
    def playhead_snap_distance(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]):
        ...
    @property
    def snap_uv_element(self) -> Annotated[set[str], "is_animatable=False"]:
        """Type of element to snap to"""
        ...
    @snap_uv_element.setter
    def snap_uv_element(self, value: Annotated[set[str], "is_animatable=False"]):
        ...
    @property
    def snap_target(self) -> Annotated[Literal['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], "is_animatable=False"]:
        """Which part to snap onto the target"""
        ...
    @snap_target.setter
    def snap_target(self, value: Annotated[Literal['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], "is_animatable=False"]):
        ...
    @property
    def use_snap_peel_object(self) -> Annotated[bool, "is_animatable=False"]:
        """Consider objects as whole when finding volume center"""
        ...
    @use_snap_peel_object.setter
    def use_snap_peel_object(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_backface_culling(self) -> Annotated[bool, "is_animatable=False"]:
        """Exclude back facing geometry from snapping"""
        ...
    @use_snap_backface_culling.setter
    def use_snap_backface_culling(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_self(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap onto itself only if enabled (edit mode only)"""
        ...
    @use_snap_self.setter
    def use_snap_self(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_edit(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap onto non-active objects in edit mode (edit mode only)"""
        ...
    @use_snap_edit.setter
    def use_snap_edit(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_nonedit(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap onto objects not in edit mode (edit mode only)"""
        ...
    @use_snap_nonedit.setter
    def use_snap_nonedit(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_selectable(self) -> Annotated[bool, "is_animatable=False"]:
        """Snap only onto objects that are selectable"""
        ...
    @use_snap_selectable.setter
    def use_snap_selectable(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_translate(self) -> Annotated[bool, "is_animatable=False"]:
        """Move is affected by snapping settings"""
        ...
    @use_snap_translate.setter
    def use_snap_translate(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_rotate(self) -> Annotated[bool, "is_animatable=False"]:
        """Rotate is affected by the snapping settings"""
        ...
    @use_snap_rotate.setter
    def use_snap_rotate(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_snap_scale(self) -> Annotated[bool, "is_animatable=False"]:
        """Scale is affected by snapping settings"""
        ...
    @use_snap_scale.setter
    def use_snap_scale(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def plane_axis(self) -> Annotated[Literal['X', 'Y', 'Z'], "is_animatable=False"]:
        """The axis used for placing the base region"""
        ...
    @plane_axis.setter
    def plane_axis(self, value: Annotated[Literal['X', 'Y', 'Z'], "is_animatable=False"]):
        ...
    @property
    def plane_axis_auto(self) -> Annotated[bool, "is_animatable=False"]:
        """Select the closest axis when placing objects (surface overrides)"""
        ...
    @plane_axis_auto.setter
    def plane_axis_auto(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def plane_depth(self) -> Annotated[Literal['SURFACE', 'CURSOR_PLANE', 'CURSOR_VIEW'], "is_animatable=False"]:
        """The initial depth used when placing the cursor"""
        ...
    @plane_depth.setter
    def plane_depth(self, value: Annotated[Literal['SURFACE', 'CURSOR_PLANE', 'CURSOR_VIEW'], "is_animatable=False"]):
        ...
    @property
    def plane_orientation(self) -> Annotated[Literal['SURFACE', 'DEFAULT'], "is_animatable=False"]:
        """The initial depth used when placing the cursor"""
        ...
    @plane_orientation.setter
    def plane_orientation(self, value: Annotated[Literal['SURFACE', 'DEFAULT'], "is_animatable=False"]):
        ...
    @property
    def snap_elements_tool(self) -> Annotated[Literal['GEOMETRY', 'DEFAULT'], "is_animatable=False"]:
        """The target to use while snapping"""
        ...
    @snap_elements_tool.setter
    def snap_elements_tool(self, value: Annotated[Literal['GEOMETRY', 'DEFAULT'], "is_animatable=False"]):
        ...
    @property
    def use_gpencil_draw_additive(self) -> Annotated[bool, "is_animatable=False"]:
        """When creating new frames, the strokes from the previous/active frame are included as the basis for the new one"""
        ...
    @use_gpencil_draw_additive.setter
    def use_gpencil_draw_additive(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_gpencil_draw_onback(self) -> Annotated[bool, "is_animatable=False"]:
        """New strokes are drawn below of all strokes in the layer"""
        ...
    @use_gpencil_draw_onback.setter
    def use_gpencil_draw_onback(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_gpencil_thumbnail_list(self) -> Annotated[bool, "is_animatable=False"]:
        """Show compact list of colors instead of thumbnails"""
        ...
    @use_gpencil_thumbnail_list.setter
    def use_gpencil_thumbnail_list(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_gpencil_weight_data_add(self) -> Annotated[bool, "is_animatable=False"]:
        """Weight data for new strokes is added according to the current vertex group and weight. If no vertex group selected, weight is not added."""
        ...
    @use_gpencil_weight_data_add.setter
    def use_gpencil_weight_data_add(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_gpencil_automerge_strokes(self) -> Annotated[bool, "is_animatable=False"]:
        """Join the last drawn stroke with previous strokes in the active layer by distance"""
        ...
    @use_gpencil_automerge_strokes.setter
    def use_gpencil_automerge_strokes(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def gpencil_sculpt(self) -> Annotated[Optional['GPencilSculptSettings'], "is_animatable=False"]:
        """Settings for stroke sculpting tools and brushes"""
        ...
    @property
    def gpencil_interpolate(self) -> Annotated[Optional['GPencilInterpolateSettings'], "is_animatable=False"]:
        """Settings for Grease Pencil interpolation tools"""
        ...
    @property
    def gpencil_stroke_placement_view3d(self) -> Annotated[Literal['ORIGIN', 'CURSOR', 'SURFACE', 'STROKE'], "is_animatable=False"]:

        ...
    @gpencil_stroke_placement_view3d.setter
    def gpencil_stroke_placement_view3d(self, value: Annotated[Literal['ORIGIN', 'CURSOR', 'SURFACE', 'STROKE'], "is_animatable=False"]):
        ...
    @property
    def gpencil_stroke_snap_mode(self) -> Annotated[Literal['NONE', 'ENDS', 'FIRST'], "is_animatable=False"]:

        ...
    @gpencil_stroke_snap_mode.setter
    def gpencil_stroke_snap_mode(self, value: Annotated[Literal['NONE', 'ENDS', 'FIRST'], "is_animatable=False"]):
        ...
    @property
    def gpencil_surface_offset(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """Offset along the normal when drawing on surfaces"""
        ...
    @gpencil_surface_offset.setter
    def gpencil_surface_offset(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]):
        ...
    @property
    def use_gpencil_project_only_selected(self) -> Annotated[bool, "is_animatable=False"]:
        """Project the strokes only onto selected objects"""
        ...
    @use_gpencil_project_only_selected.setter
    def use_gpencil_project_only_selected(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def gpencil_selectmode_edit(self) -> Annotated[Literal['POINT', 'STROKE', 'SEGMENT'], "is_animatable=False"]:

        ...
    @gpencil_selectmode_edit.setter
    def gpencil_selectmode_edit(self, value: Annotated[Literal['POINT', 'STROKE', 'SEGMENT'], "is_animatable=False"]):
        ...
    @property
    def use_gpencil_select_mask_point(self) -> Annotated[bool, "is_animatable=False"]:
        """Only sculpt selected stroke points"""
        ...
    @use_gpencil_select_mask_point.setter
    def use_gpencil_select_mask_point(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_gpencil_select_mask_stroke(self) -> Annotated[bool, "is_animatable=False"]:
        """Only sculpt selected strokes"""
        ...
    @use_gpencil_select_mask_stroke.setter
    def use_gpencil_select_mask_stroke(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_gpencil_select_mask_segment(self) -> Annotated[bool, "is_animatable=False"]:
        """Only sculpt selected stroke points between other strokes"""
        ...
    @use_gpencil_select_mask_segment.setter
    def use_gpencil_select_mask_segment(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_gpencil_vertex_select_mask_point(self) -> Annotated[bool, "is_animatable=False"]:
        """Only paint selected stroke points"""
        ...
    @use_gpencil_vertex_select_mask_point.setter
    def use_gpencil_vertex_select_mask_point(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_gpencil_vertex_select_mask_stroke(self) -> Annotated[bool, "is_animatable=False"]:
        """Only paint selected strokes"""
        ...
    @use_gpencil_vertex_select_mask_stroke.setter
    def use_gpencil_vertex_select_mask_stroke(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_gpencil_vertex_select_mask_segment(self) -> Annotated[bool, "is_animatable=False"]:
        """Only paint selected stroke points between other strokes"""
        ...
    @use_gpencil_vertex_select_mask_segment.setter
    def use_gpencil_vertex_select_mask_segment(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_grease_pencil_multi_frame_editing(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable multi-frame editing"""
        ...
    @use_grease_pencil_multi_frame_editing.setter
    def use_grease_pencil_multi_frame_editing(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def annotation_stroke_placement_view2d(self) -> Annotated[Literal['IMAGE', 'VIEW'], "is_animatable=False"]:

        ...
    @annotation_stroke_placement_view2d.setter
    def annotation_stroke_placement_view2d(self, value: Annotated[Literal['IMAGE', 'VIEW'], "is_animatable=False"]):
        ...
    @property
    def annotation_stroke_placement_view3d(self) -> Annotated[Literal['CURSOR', 'VIEW', 'SURFACE'], "is_animatable=False"]:
        """How annotation strokes are orientated in 3D space"""
        ...
    @annotation_stroke_placement_view3d.setter
    def annotation_stroke_placement_view3d(self, value: Annotated[Literal['CURSOR', 'VIEW', 'SURFACE'], "is_animatable=False"]):
        ...
    @property
    def use_annotation_stroke_endpoints(self) -> Annotated[bool, "is_animatable=False"]:
        """Only use the first and last parts of the stroke for snapping"""
        ...
    @use_annotation_stroke_endpoints.setter
    def use_annotation_stroke_endpoints(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_annotation_project_only_selected(self) -> Annotated[bool, "is_animatable=False"]:
        """Project the strokes only onto selected objects"""
        ...
    @use_annotation_project_only_selected.setter
    def use_annotation_project_only_selected(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def annotation_thickness(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Thickness of annotation strokes"""
        ...
    @annotation_thickness.setter
    def annotation_thickness(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]):
        ...
    @property
    def use_keyframe_insert_auto(self) -> Annotated[bool, "is_animatable=False"]:
        """Automatic keyframe insertion for objects, bones and masks"""
        ...
    @use_keyframe_insert_auto.setter
    def use_keyframe_insert_auto(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def auto_keying_mode(self) -> Annotated[Literal['ADD_REPLACE_KEYS', 'REPLACE_KEYS'], "is_animatable=False"]:
        """Mode of automatic keyframe insertion for objects, bones and masks"""
        ...
    @auto_keying_mode.setter
    def auto_keying_mode(self, value: Annotated[Literal['ADD_REPLACE_KEYS', 'REPLACE_KEYS'], "is_animatable=False"]):
        ...
    @property
    def use_record_with_nla(self) -> Annotated[bool, "is_animatable=False"]:
        """Add a new NLA Track + Strip for every loop/pass made over the animation to allow non-destructive tweaking"""
        ...
    @use_record_with_nla.setter
    def use_record_with_nla(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_keyframe_insert_keyingset(self) -> Annotated[bool, "is_animatable=False"]:
        """Automatic keyframe insertion using active Keying Set only"""
        ...
    @use_keyframe_insert_keyingset.setter
    def use_keyframe_insert_keyingset(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_keyframe_cycle_aware(self) -> Annotated[bool, "is_animatable=False"]:
        """For channels with cyclic extrapolation, keyframe insertion is automatically remapped inside the cycle time range, and keeps ends in sync. Curves newly added to actions with a Manual Frame Range and Cyclic Animation are automatically made cyclic."""
        ...
    @use_keyframe_cycle_aware.setter
    def use_keyframe_cycle_aware(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def keyframe_type(self) -> Annotated[Literal['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER', 'GENERATED'], "is_animatable=False"]:
        """Type of keyframes to create when inserting keyframes"""
        ...
    @keyframe_type.setter
    def keyframe_type(self, value: Annotated[Literal['KEYFRAME', 'BREAKDOWN', 'MOVING_HOLD', 'EXTREME', 'JITTER', 'GENERATED'], "is_animatable=False"]):
        ...
    @property
    def anim_mirror_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to mirror over. Leave empty and name a bone to always mirror over that bone of the active armature"""
        ...
    @anim_mirror_object.setter
    def anim_mirror_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def anim_mirror_bone(self) -> Annotated[str, "is_animatable=False"]:
        """Bone to use for the mirroring"""
        ...
    @anim_mirror_bone.setter
    def anim_mirror_bone(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def anim_relative_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to which matrices are made relative"""
        ...
    @anim_relative_object.setter
    def anim_relative_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def anim_fix_to_cam_use_loc(self) -> Annotated[bool, "is_animatable=False"]:
        """Create location keys when fixing to the scene camera"""
        ...
    @anim_fix_to_cam_use_loc.setter
    def anim_fix_to_cam_use_loc(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def anim_fix_to_cam_use_rot(self) -> Annotated[bool, "is_animatable=False"]:
        """Create rotation keys when fixing to the scene camera"""
        ...
    @anim_fix_to_cam_use_rot.setter
    def anim_fix_to_cam_use_rot(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def anim_fix_to_cam_use_scale(self) -> Annotated[bool, "is_animatable=False"]:
        """Create scale keys when fixing to the scene camera"""
        ...
    @anim_fix_to_cam_use_scale.setter
    def anim_fix_to_cam_use_scale(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def uv_select_mode(self) -> Annotated[Literal['VERTEX', 'EDGE', 'FACE'], "is_animatable=False"]:
        """UV selection and display mode"""
        ...
    @uv_select_mode.setter
    def uv_select_mode(self, value: Annotated[Literal['VERTEX', 'EDGE', 'FACE'], "is_animatable=False"]):
        ...
    @property
    def uv_sticky_select_mode(self) -> Annotated[Literal['DISABLED', 'SHARED_LOCATION', 'SHARED_VERTEX'], "is_animatable=False"]:
        """Method for extending UV vertex selection"""
        ...
    @uv_sticky_select_mode.setter
    def uv_sticky_select_mode(self, value: Annotated[Literal['DISABLED', 'SHARED_LOCATION', 'SHARED_VERTEX'], "is_animatable=False"]):
        ...
    @property
    def use_uv_select_sync(self) -> Annotated[bool, "is_animatable=False"]:
        """Keep UV and edit mode mesh selection in sync"""
        ...
    @use_uv_select_sync.setter
    def use_uv_select_sync(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_uv_select_island(self) -> Annotated[bool, "is_animatable=False"]:
        """Island selection"""
        ...
    @use_uv_select_island.setter
    def use_uv_select_island(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_uv_local_view(self) -> Annotated[bool, "is_animatable=False"]:
        """Display only faces with the currently displayed image assigned"""
        ...
    @show_uv_local_view.setter
    def show_uv_local_view(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_uv_custom_region(self) -> Annotated[bool, "is_animatable=False"]:
        """Custom defined region"""
        ...
    @use_uv_custom_region.setter
    def use_uv_custom_region(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def mesh_select_mode(self) -> Annotated[list[bool], "is_animatable=False"]:
        """Which mesh elements selection works on"""
        ...
    @mesh_select_mode.setter
    def mesh_select_mode(self, value: Annotated[list[bool], "is_animatable=False"]):
        ...
    @property
    def vertex_group_weight(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Weight to assign in vertex groups"""
        ...
    @vertex_group_weight.setter
    def vertex_group_weight(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def use_edge_path_live_unwrap(self) -> Annotated[bool, "is_animatable=False"]:
        """Changing edge seams recalculates UV unwrap"""
        ...
    @use_edge_path_live_unwrap.setter
    def use_edge_path_live_unwrap(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def normal_vector(self) -> Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3", "is_animatable=False"]:
        """Normal vector used to copy, add or multiply"""
        ...
    @normal_vector.setter
    def normal_vector(self, value: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...
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