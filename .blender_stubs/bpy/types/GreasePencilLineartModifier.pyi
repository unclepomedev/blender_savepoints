# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GreasePencilLineartModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier
from .Collection import Collection
from .Material import Material
from .Object import Object

class GreasePencilLineartModifier(Modifier):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Modifier name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Literal['GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY', 'DATA_TRANSFER', 'MESH_CACHE', 'MESH_SEQUENCE_CACHE', 'NORMAL_EDIT', 'WEIGHTED_NORMAL', 'UV_PROJECT', 'UV_WARP', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_PROXIMITY', 'GREASE_PENCIL_COLOR', 'GREASE_PENCIL_TINT', 'GREASE_PENCIL_OPACITY', 'GREASE_PENCIL_VERTEX_WEIGHT_ANGLE', 'GREASE_PENCIL_TIME', 'GREASE_PENCIL_TEXTURE', 'ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 'EDGE_SPLIT', 'NODES', 'MASK', 'MIRROR', 'MESH_TO_VOLUME', 'MULTIRES', 'REMESH', 'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'VOLUME_TO_MESH', 'WELD', 'WIREFRAME', 'GREASE_PENCIL_ARRAY', 'GREASE_PENCIL_BUILD', 'GREASE_PENCIL_LENGTH', 'LINEART', 'GREASE_PENCIL_MIRROR', 'GREASE_PENCIL_MULTIPLY', 'GREASE_PENCIL_SIMPLIFY', 'GREASE_PENCIL_SUBDIV', 'GREASE_PENCIL_ENVELOPE', 'GREASE_PENCIL_OUTLINE', 'ARMATURE', 'CAST', 'CURVE', 'DISPLACE', 'HOOK', 'LAPLACIANDEFORM', 'LATTICE', 'MESH_DEFORM', 'SHRINKWRAP', 'SIMPLE_DEFORM', 'SMOOTH', 'CORRECTIVE_SMOOTH', 'LAPLACIANSMOOTH', 'SURFACE_DEFORM', 'WARP', 'WAVE', 'VOLUME_DISPLACE', 'GREASE_PENCIL_HOOK', 'GREASE_PENCIL_NOISE', 'GREASE_PENCIL_OFFSET', 'GREASE_PENCIL_SMOOTH', 'GREASE_PENCIL_THICKNESS', 'GREASE_PENCIL_LATTICE', 'GREASE_PENCIL_DASH', 'GREASE_PENCIL_ARMATURE', 'GREASE_PENCIL_SHRINKWRAP', 'CLOTH', 'COLLISION', 'DYNAMIC_PAINT', 'EXPLODE', 'FLUID', 'OCEAN', 'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM', 'SOFT_BODY', 'SURFACE']:

        ...
    @property
    def show_viewport(self) -> bool:
        """Display modifier in viewport"""
        ...
    @show_viewport.setter
    def show_viewport(self, value: bool):
        ...
    @property
    def show_render(self) -> bool:
        """Use modifier during render"""
        ...
    @show_render.setter
    def show_render(self, value: bool):
        ...
    @property
    def show_in_editmode(self) -> bool:
        """Display modifier in Edit mode"""
        ...
    @show_in_editmode.setter
    def show_in_editmode(self, value: bool):
        ...
    @property
    def show_on_cage(self) -> bool:
        """Adjust edit cage to modifier result"""
        ...
    @show_on_cage.setter
    def show_on_cage(self, value: bool):
        ...
    @property
    def show_expanded(self) -> bool:
        """Set modifier expanded in the user interface"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool):
        ...
    @property
    def is_active(self) -> Annotated[bool, "is_animatable=False"]:
        """The active modifier in the list"""
        ...
    @is_active.setter
    def is_active(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pin_to_last(self) -> Annotated[bool, "is_animatable=False"]:
        """Keep the modifier at the end of the list"""
        ...
    @use_pin_to_last.setter
    def use_pin_to_last(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def is_override_data(self) -> bool:
        """In a local override object, whether this modifier comes from the linked reference object, or is local to the override"""
        ...
    @property
    def use_apply_on_spline(self) -> bool:
        """Apply this and all preceding deformation modifiers on splines' points rather than on filled curve/surface"""
        ...
    @use_apply_on_spline.setter
    def use_apply_on_spline(self, value: bool):
        ...
    @property
    def execution_time(self) -> Annotated[float, "subtype='TIME_ABSOLUTE'", "unit='TIME_ABSOLUTE'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Time in seconds that the modifier took to evaluate. This is only set on evaluated objects. If multiple modifiers run in parallel, execution time is not a reliable metric."""
        ...
    @property
    def persistent_uid(self) -> Annotated[int, "step=1"]:
        """Uniquely identifies the modifier within the modifier stack that it is part of"""
        ...
    @property
    def use_custom_camera(self) -> bool:
        """Use custom camera instead of the active camera"""
        ...
    @use_custom_camera.setter
    def use_custom_camera(self, value: bool):
        ...
    @property
    def use_fuzzy_intersections(self) -> bool:
        """Treat intersection and contour lines as if they were the same type so they can be chained together"""
        ...
    @use_fuzzy_intersections.setter
    def use_fuzzy_intersections(self, value: bool):
        ...
    @property
    def use_fuzzy_all(self) -> bool:
        """Treat all lines as the same line type so they can be chained together"""
        ...
    @use_fuzzy_all.setter
    def use_fuzzy_all(self, value: bool):
        ...
    @property
    def use_object_instances(self) -> bool:
        """Allow particle objects and face/vertex instances to show in Line Art"""
        ...
    @use_object_instances.setter
    def use_object_instances(self, value: bool):
        ...
    @property
    def use_edge_overlap(self) -> bool:
        """Allow edges in the same location (i.e. from edge split) to show properly. May run slower."""
        ...
    @use_edge_overlap.setter
    def use_edge_overlap(self, value: bool):
        ...
    @property
    def use_clip_plane_boundaries(self) -> bool:
        """Allow lines generated by the near/far clipping plane to be shown"""
        ...
    @use_clip_plane_boundaries.setter
    def use_clip_plane_boundaries(self, value: bool):
        ...
    @property
    def crease_threshold(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.009999999776482582", "precision=1"]:
        """Angles smaller than this will be treated as creases. Crease angle priority: object Line Art crease override > mesh auto smooth angle > Line Art default crease."""
        ...
    @crease_threshold.setter
    def crease_threshold(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.009999999776482582", "precision=1"]):
        ...
    @property
    def split_angle(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.009999999776482582", "precision=1"]:
        """Angle in screen space below which a stroke is split in two"""
        ...
    @split_angle.setter
    def split_angle(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=0.009999999776482582", "precision=1"]):
        ...
    @property
    def smooth_tolerance(self) -> Annotated[float, "step=0.05000000074505806", "precision=4"]:
        """Strength of smoothing applied on jagged chains"""
        ...
    @smooth_tolerance.setter
    def smooth_tolerance(self, value: Annotated[float, "step=0.05000000074505806", "precision=4"]):
        ...
    @property
    def use_loose_as_contour(self) -> bool:
        """Loose edges will have contour type"""
        ...
    @use_loose_as_contour.setter
    def use_loose_as_contour(self, value: bool):
        ...
    @property
    def invert_source_vertex_group(self) -> bool:
        """Invert source vertex group values"""
        ...
    @invert_source_vertex_group.setter
    def invert_source_vertex_group(self, value: bool):
        ...
    @property
    def use_output_vertex_group_match_by_name(self) -> bool:
        """Match output vertex group based on name"""
        ...
    @use_output_vertex_group_match_by_name.setter
    def use_output_vertex_group_match_by_name(self, value: bool):
        ...
    @property
    def use_face_mark(self) -> bool:
        """Filter feature lines using Freestyle face marks"""
        ...
    @use_face_mark.setter
    def use_face_mark(self, value: bool):
        ...
    @property
    def use_face_mark_invert(self) -> bool:
        """Invert face mark filtering"""
        ...
    @use_face_mark_invert.setter
    def use_face_mark_invert(self, value: bool):
        ...
    @property
    def use_face_mark_boundaries(self) -> bool:
        """Filter feature lines based on face mark boundaries"""
        ...
    @use_face_mark_boundaries.setter
    def use_face_mark_boundaries(self, value: bool):
        ...
    @property
    def use_face_mark_keep_contour(self) -> bool:
        """Preserve contour lines while filtering"""
        ...
    @use_face_mark_keep_contour.setter
    def use_face_mark_keep_contour(self, value: bool):
        ...
    @property
    def chaining_image_threshold(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=4"]:
        """Segments with an image distance smaller than this will be chained together"""
        ...
    @chaining_image_threshold.setter
    def chaining_image_threshold(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=4"]):
        ...
    @property
    def use_loose_edge_chain(self) -> bool:
        """Allow loose edges to be chained together"""
        ...
    @use_loose_edge_chain.setter
    def use_loose_edge_chain(self, value: bool):
        ...
    @property
    def use_geometry_space_chain(self) -> bool:
        """Use geometry distance for chaining instead of image space"""
        ...
    @use_geometry_space_chain.setter
    def use_geometry_space_chain(self, value: bool):
        ...
    @property
    def use_detail_preserve(self) -> bool:
        """Keep the zig-zag "noise" in initial chaining"""
        ...
    @use_detail_preserve.setter
    def use_detail_preserve(self, value: bool):
        ...
    @property
    def use_overlap_edge_type_support(self) -> bool:
        """Allow an edge to have multiple overlapping types. This will create a separate stroke for each overlapping type."""
        ...
    @use_overlap_edge_type_support.setter
    def use_overlap_edge_type_support(self, value: bool):
        ...
    @property
    def stroke_depth_offset(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=4"]:
        """Move strokes slightly towards the camera to avoid clipping while preserve depth for the viewport"""
        ...
    @stroke_depth_offset.setter
    def stroke_depth_offset(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.0010000000474974513", "precision=4"]):
        ...
    @property
    def use_offset_towards_custom_camera(self) -> bool:
        """Offset strokes towards selected camera instead of the active camera"""
        ...
    @use_offset_towards_custom_camera.setter
    def use_offset_towards_custom_camera(self, value: bool):
        ...
    @property
    def source_camera(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Use specified camera object for generating Line Art strokes"""
        ...
    @source_camera.setter
    def source_camera(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def light_contour_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Use this light object to generate light contour"""
        ...
    @light_contour_object.setter
    def light_contour_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def source_type(self) -> Literal['COLLECTION', 'OBJECT', 'SCENE']:
        """Line Art stroke source type"""
        ...
    @source_type.setter
    def source_type(self, value: Literal['COLLECTION', 'OBJECT', 'SCENE']):
        ...
    @property
    def source_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Generate strokes from this object"""
        ...
    @source_object.setter
    def source_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def source_collection(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Generate strokes from the objects in this collection"""
        ...
    @source_collection.setter
    def source_collection(self, value: Annotated[Optional['Collection'], "is_animatable=False"]):
        ...
    @property
    def use_contour(self) -> bool:
        """Generate strokes from contours lines"""
        ...
    @use_contour.setter
    def use_contour(self, value: bool):
        ...
    @property
    def use_loose(self) -> bool:
        """Generate strokes from loose edges"""
        ...
    @use_loose.setter
    def use_loose(self, value: bool):
        ...
    @property
    def use_crease(self) -> bool:
        """Generate strokes from creased edges"""
        ...
    @use_crease.setter
    def use_crease(self, value: bool):
        ...
    @property
    def use_material(self) -> bool:
        """Generate strokes from borders between materials"""
        ...
    @use_material.setter
    def use_material(self, value: bool):
        ...
    @property
    def use_edge_mark(self) -> bool:
        """Generate strokes from Freestyle marked edges"""
        ...
    @use_edge_mark.setter
    def use_edge_mark(self, value: bool):
        ...
    @property
    def use_intersection(self) -> bool:
        """Generate strokes from intersections"""
        ...
    @use_intersection.setter
    def use_intersection(self, value: bool):
        ...
    @property
    def use_light_contour(self) -> bool:
        """Generate light/shadow separation lines from a reference light object"""
        ...
    @use_light_contour.setter
    def use_light_contour(self, value: bool):
        ...
    @property
    def use_shadow(self) -> bool:
        """Project contour lines using a light source object"""
        ...
    @use_shadow.setter
    def use_shadow(self, value: bool):
        ...
    @property
    def shadow_region_filtering(self) -> Literal['NONE', 'ILLUMINATED', 'SHADED', 'ILLUMINATED_ENCLOSED']:
        """Select feature lines that comes from lit or shaded regions. Will not affect cast shadow and light contour since they are at the border."""
        ...
    @shadow_region_filtering.setter
    def shadow_region_filtering(self, value: Literal['NONE', 'ILLUMINATED', 'SHADED', 'ILLUMINATED_ENCLOSED']):
        ...
    @property
    def silhouette_filtering(self) -> Literal['NONE', 'GROUP', 'INDIVIDUAL']:
        """Select contour or silhouette"""
        ...
    @silhouette_filtering.setter
    def silhouette_filtering(self, value: Literal['NONE', 'GROUP', 'INDIVIDUAL']):
        ...
    @property
    def use_multiple_levels(self) -> bool:
        """Generate strokes from a range of occlusion levels"""
        ...
    @use_multiple_levels.setter
    def use_multiple_levels(self, value: bool):
        ...
    @property
    def level_start(self) -> Annotated[int, "step=1"]:
        """Minimum number of occlusions for the generated strokes"""
        ...
    @level_start.setter
    def level_start(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def level_end(self) -> Annotated[int, "step=1"]:
        """Maximum number of occlusions for the generated strokes"""
        ...
    @level_end.setter
    def level_end(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def target_layer(self) -> Annotated[str, "is_animatable=False"]:
        """Grease Pencil layer to which assign the generated strokes"""
        ...
    @target_layer.setter
    def target_layer(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def target_material(self) -> Annotated[Optional['Material'], "is_animatable=False"]:
        """Grease Pencil material assigned to the generated strokes"""
        ...
    @target_material.setter
    def target_material(self, value: Annotated[Optional['Material'], "is_animatable=False"]):
        ...
    @property
    def source_vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Match the beginning of vertex group names from mesh objects, match all when left empty"""
        ...
    @source_vertex_group.setter
    def source_vertex_group(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def vertex_group(self) -> Annotated[str, "is_animatable=False"]:
        """Vertex group name for selected strokes"""
        ...
    @vertex_group.setter
    def vertex_group(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def is_baked(self) -> bool:
        """This modifier has baked data"""
        ...
    @is_baked.setter
    def is_baked(self, value: bool):
        ...
    @property
    def use_cache(self) -> bool:
        """Use cached scene data from the first Line Art modifier in the stack. Certain settings will be unavailable."""
        ...
    @use_cache.setter
    def use_cache(self, value: bool):
        ...
    @property
    def overscan(self) -> Annotated[float, "step=0.009999999776482582", "precision=3"]:
        """A margin to prevent strokes from ending abruptly at the edge of the image"""
        ...
    @overscan.setter
    def overscan(self, value: Annotated[float, "step=0.009999999776482582", "precision=3"]):
        ...
    @property
    def radius(self) -> Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]:
        """The radius for the generated strokes"""
        ...
    @radius.setter
    def radius(self, value: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]):
        ...
    @property
    def opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]:
        """The strength value for the generate strokes"""
        ...
    @opacity.setter
    def opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=0.009999999776482582", "precision=2"]):
        ...
    @property
    def use_material_mask(self) -> bool:
        """Use material masks to filter out occluded strokes"""
        ...
    @use_material_mask.setter
    def use_material_mask(self, value: bool):
        ...
    @property
    def use_material_mask_match(self) -> bool:
        """Require matching all material masks instead of just one"""
        ...
    @use_material_mask_match.setter
    def use_material_mask_match(self, value: bool):
        ...
    @property
    def use_material_mask_bits(self) -> list[bool]:
        """Mask bits to match from Material Line Art settings"""
        ...
    @use_material_mask_bits.setter
    def use_material_mask_bits(self, value: list[bool]):
        ...
    @property
    def use_intersection_match(self) -> bool:
        """Require matching all intersection masks instead of just one"""
        ...
    @use_intersection_match.setter
    def use_intersection_match(self, value: bool):
        ...
    @property
    def use_intersection_mask(self) -> list[bool]:
        """Mask bits to match from Collection Line Art settings"""
        ...
    @use_intersection_mask.setter
    def use_intersection_mask(self, value: list[bool]):
        ...
    @property
    def use_crease_on_smooth(self) -> bool:
        """Allow crease edges to show inside smooth surfaces"""
        ...
    @use_crease_on_smooth.setter
    def use_crease_on_smooth(self, value: bool):
        ...
    @property
    def use_crease_on_sharp(self) -> bool:
        """Allow crease to show on sharp edges"""
        ...
    @use_crease_on_sharp.setter
    def use_crease_on_sharp(self, value: bool):
        ...
    @property
    def use_image_boundary_trimming(self) -> bool:
        """Trim all edges right at the boundary of image (including overscan region)"""
        ...
    @use_image_boundary_trimming.setter
    def use_image_boundary_trimming(self, value: bool):
        ...
    @property
    def use_back_face_culling(self) -> bool:
        """Remove all back faces to speed up calculation, this will create edges in different occlusion levels than when disabled"""
        ...
    @use_back_face_culling.setter
    def use_back_face_culling(self, value: bool):
        ...
    @property
    def shadow_camera_near(self) -> Annotated[float, "step=0.10000000149011612", "precision=2"]:
        """Near clipping distance of shadow camera"""
        ...
    @shadow_camera_near.setter
    def shadow_camera_near(self, value: Annotated[float, "step=0.10000000149011612", "precision=2"]):
        ...
    @property
    def shadow_camera_far(self) -> Annotated[float, "step=0.10000000149011612", "precision=2"]:
        """Far clipping distance of shadow camera"""
        ...
    @shadow_camera_far.setter
    def shadow_camera_far(self, value: Annotated[float, "step=0.10000000149011612", "precision=2"]):
        ...
    @property
    def shadow_camera_size(self) -> Annotated[float, "step=0.10000000149011612", "precision=2"]:
        """Represents the "Orthographic Scale" of an orthographic camera. If the camera is positioned at the light's location with this scale, it will represent the coverage of the shadow "camera"."""
        ...
    @shadow_camera_size.setter
    def shadow_camera_size(self, value: Annotated[float, "step=0.10000000149011612", "precision=2"]):
        ...
    @property
    def use_invert_collection(self) -> bool:
        """Select everything except lines from specified collection"""
        ...
    @use_invert_collection.setter
    def use_invert_collection(self, value: bool):
        ...
    @property
    def use_invert_silhouette(self) -> bool:
        """Select anti-silhouette lines"""
        ...
    @use_invert_silhouette.setter
    def use_invert_silhouette(self, value: bool):
        ...