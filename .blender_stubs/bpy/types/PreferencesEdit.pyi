# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PreferencesEdit.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class PreferencesEdit(bpy_struct):

    @property
    def material_link(self) -> Literal['OBDATA', 'OBJECT']:
        """Toggle whether the material is linked to object data or the object block"""
        ...
    @material_link.setter
    def material_link(self, value: Literal['OBDATA', 'OBJECT']) -> None:
        ...
    @property
    def object_align(self) -> Literal['WORLD', 'VIEW', 'CURSOR']:
        """The default alignment for objects added from a 3D viewport menu"""
        ...
    @object_align.setter
    def object_align(self, value: Literal['WORLD', 'VIEW', 'CURSOR']) -> None:
        ...
    @property
    def use_enter_edit_mode(self) -> bool:
        """Enter edit mode automatically after adding a new object"""
        ...
    @use_enter_edit_mode.setter
    def use_enter_edit_mode(self, value: bool) -> None:
        ...
    @property
    def collection_instance_empty_size(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Display size of the empty when new collection instances are created"""
        ...
    @collection_instance_empty_size.setter
    def collection_instance_empty_size(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_text_edit_auto_close(self) -> bool:
        """Automatically close relevant character pairs when typing in the text editor"""
        ...
    @use_text_edit_auto_close.setter
    def use_text_edit_auto_close(self, value: bool) -> None:
        ...
    @property
    def undo_steps(self) -> Annotated[int, "step=1"]:
        """Number of undo steps available (smaller values conserve memory)"""
        ...
    @undo_steps.setter
    def undo_steps(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def undo_memory_limit(self) -> Annotated[int, "step=1"]:
        """Maximum memory usage in megabytes (0 means unlimited)"""
        ...
    @undo_memory_limit.setter
    def undo_memory_limit(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_global_undo(self) -> bool:
        """Global undo works by keeping a full copy of the file itself in memory, so takes extra memory"""
        ...
    @use_global_undo.setter
    def use_global_undo(self, value: bool) -> None:
        ...
    @property
    def use_auto_keying(self) -> bool:
        """Automatic keyframe insertion for Objects and Bones (default setting used for new Scenes)"""
        ...
    @use_auto_keying.setter
    def use_auto_keying(self, value: bool) -> None:
        ...
    @property
    def auto_keying_mode(self) -> Literal['ADD_REPLACE_KEYS', 'REPLACE_KEYS']:
        """Mode of automatic keyframe insertion for Objects and Bones (default setting used for new Scenes)"""
        ...
    @auto_keying_mode.setter
    def auto_keying_mode(self, value: Literal['ADD_REPLACE_KEYS', 'REPLACE_KEYS']) -> None:
        ...
    @property
    def use_keyframe_insert_available(self) -> bool:
        """Insert Keyframes only for properties that are already animated"""
        ...
    @use_keyframe_insert_available.setter
    def use_keyframe_insert_available(self, value: bool) -> None:
        ...
    @property
    def use_auto_keying_warning(self) -> bool:
        """Show warning indicators when transforming objects and bones if auto keying is enabled"""
        ...
    @use_auto_keying_warning.setter
    def use_auto_keying_warning(self, value: bool) -> None:
        ...
    @property
    def key_insert_channels(self) -> set[str]:
        """Which channels to insert keys at when no keying set is active"""
        ...
    @key_insert_channels.setter
    def key_insert_channels(self, value: set[str]) -> None:
        ...
    @property
    def use_auto_keyframe_insert_needed(self) -> bool:
        """Auto-Keying will skip inserting keys that don't affect the animation"""
        ...
    @use_auto_keyframe_insert_needed.setter
    def use_auto_keyframe_insert_needed(self, value: bool) -> None:
        ...
    @property
    def use_keyframe_insert_needed(self) -> bool:
        """When keying manually, skip inserting keys that don't affect the animation"""
        ...
    @use_keyframe_insert_needed.setter
    def use_keyframe_insert_needed(self, value: bool) -> None:
        ...
    @property
    def use_visual_keying(self) -> bool:
        """Use Visual keying automatically for constrained objects"""
        ...
    @use_visual_keying.setter
    def use_visual_keying(self, value: bool) -> None:
        ...
    @property
    def use_insertkey_xyz_to_rgb(self) -> bool:
        """Color for newly added transformation F-Curves (Location, Rotation, Scale) and also Color is based on the transform axis"""
        ...
    @use_insertkey_xyz_to_rgb.setter
    def use_insertkey_xyz_to_rgb(self, value: bool) -> None:
        ...
    @property
    def use_anim_channel_group_colors(self) -> bool:
        """Use animation channel group colors; generally this is used to show bone group colors"""
        ...
    @use_anim_channel_group_colors.setter
    def use_anim_channel_group_colors(self, value: bool) -> None:
        ...
    @property
    def fcurve_new_auto_smoothing(self) -> Literal['NONE', 'CONT_ACCEL']:
        """Auto Handle Smoothing mode used for newly added F-Curves"""
        ...
    @fcurve_new_auto_smoothing.setter
    def fcurve_new_auto_smoothing(self, value: Literal['NONE', 'CONT_ACCEL']) -> None:
        ...
    @property
    def keyframe_new_interpolation_type(self) -> Literal['CONSTANT', 'LINEAR', 'BEZIER', 'SINE', 'QUAD', 'CUBIC', 'QUART', 'QUINT', 'EXPO', 'CIRC', 'BACK', 'BOUNCE', 'ELASTIC']:
        """Interpolation mode used for first keyframe on newly added F-Curves (subsequent keyframes take interpolation from preceding keyframe)"""
        ...
    @keyframe_new_interpolation_type.setter
    def keyframe_new_interpolation_type(self, value: Literal['CONSTANT', 'LINEAR', 'BEZIER', 'SINE', 'QUAD', 'CUBIC', 'QUART', 'QUINT', 'EXPO', 'CIRC', 'BACK', 'BOUNCE', 'ELASTIC']) -> None:
        ...
    @property
    def keyframe_new_handle_type(self) -> Literal['FREE', 'ALIGNED', 'VECTOR', 'AUTO', 'AUTO_CLAMPED']:
        """Handle type for handles of new keyframes"""
        ...
    @keyframe_new_handle_type.setter
    def keyframe_new_handle_type(self, value: Literal['FREE', 'ALIGNED', 'VECTOR', 'AUTO', 'AUTO_CLAMPED']) -> None:
        ...
    @property
    def use_negative_frames(self) -> bool:
        """Current frame number can be manually set to a negative value"""
        ...
    @use_negative_frames.setter
    def use_negative_frames(self, value: bool) -> None:
        ...
    @property
    def fcurve_unselected_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """The opacity of unselected F-Curves against the background of the Graph Editor"""
        ...
    @fcurve_unselected_alpha.setter
    def fcurve_unselected_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def show_only_selected_curve_keyframes(self) -> bool:
        """Only keyframes of selected F-Curves are visible and editable"""
        ...
    @show_only_selected_curve_keyframes.setter
    def show_only_selected_curve_keyframes(self, value: bool) -> None:
        ...
    @property
    def use_fcurve_high_quality_drawing(self) -> bool:
        """Draw F-Curves using Anti-Aliasing (disable for better performance)"""
        ...
    @use_fcurve_high_quality_drawing.setter
    def use_fcurve_high_quality_drawing(self, value: bool) -> None:
        ...
    @property
    def grease_pencil_manhattan_distance(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Pixels moved by mouse per axis when drawing stroke"""
        ...
    @grease_pencil_manhattan_distance.setter
    def grease_pencil_manhattan_distance(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def grease_pencil_euclidean_distance(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Distance moved by mouse when drawing stroke to include"""
        ...
    @grease_pencil_euclidean_distance.setter
    def grease_pencil_euclidean_distance(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def grease_pencil_eraser_radius(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Radius of eraser 'brush'"""
        ...
    @grease_pencil_eraser_radius.setter
    def grease_pencil_eraser_radius(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def grease_pencil_default_color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of new annotation layers"""
        ...
    @grease_pencil_default_color.setter
    def grease_pencil_default_color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def sculpt_paint_overlay_color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of texture overlay"""
        ...
    @sculpt_paint_overlay_color.setter
    def sculpt_paint_overlay_color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def connect_strips_by_default(self) -> bool:
        """Connect newly added movie strips by default if they have multiple channels"""
        ...
    @connect_strips_by_default.setter
    def connect_strips_by_default(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_mesh(self) -> bool:
        """Causes mesh data to be duplicated with the object"""
        ...
    @use_duplicate_mesh.setter
    def use_duplicate_mesh(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_surface(self) -> bool:
        """Causes surface data to be duplicated with the object"""
        ...
    @use_duplicate_surface.setter
    def use_duplicate_surface(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_curve(self) -> bool:
        """Causes curve data to be duplicated with the object"""
        ...
    @use_duplicate_curve.setter
    def use_duplicate_curve(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_lattice(self) -> bool:
        """Causes lattice data to be duplicated with the object"""
        ...
    @use_duplicate_lattice.setter
    def use_duplicate_lattice(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_text(self) -> bool:
        """Causes text data to be duplicated with the object"""
        ...
    @use_duplicate_text.setter
    def use_duplicate_text(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_metaball(self) -> bool:
        """Causes metaball data to be duplicated with the object"""
        ...
    @use_duplicate_metaball.setter
    def use_duplicate_metaball(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_armature(self) -> bool:
        """Causes armature data to be duplicated with the object"""
        ...
    @use_duplicate_armature.setter
    def use_duplicate_armature(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_camera(self) -> bool:
        """Causes camera data to be duplicated with the object"""
        ...
    @use_duplicate_camera.setter
    def use_duplicate_camera(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_speaker(self) -> bool:
        """Causes speaker data to be duplicated with the object"""
        ...
    @use_duplicate_speaker.setter
    def use_duplicate_speaker(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_light(self) -> bool:
        """Causes light data to be duplicated with the object"""
        ...
    @use_duplicate_light.setter
    def use_duplicate_light(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_material(self) -> bool:
        """Causes material data to be duplicated with the object"""
        ...
    @use_duplicate_material.setter
    def use_duplicate_material(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_action(self) -> bool:
        """Causes actions to be duplicated with the data-blocks"""
        ...
    @use_duplicate_action.setter
    def use_duplicate_action(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_particle(self) -> bool:
        """Causes particle systems to be duplicated with the object"""
        ...
    @use_duplicate_particle.setter
    def use_duplicate_particle(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_lightprobe(self) -> bool:
        """Causes light probe data to be duplicated with the object"""
        ...
    @use_duplicate_lightprobe.setter
    def use_duplicate_lightprobe(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_grease_pencil(self) -> bool:
        """Causes Grease Pencil data to be duplicated with the object"""
        ...
    @use_duplicate_grease_pencil.setter
    def use_duplicate_grease_pencil(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_curves(self) -> bool:
        """Causes curves data to be duplicated with the object"""
        ...
    @use_duplicate_curves.setter
    def use_duplicate_curves(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_pointcloud(self) -> bool:
        """Causes point cloud data to be duplicated with the object"""
        ...
    @use_duplicate_pointcloud.setter
    def use_duplicate_pointcloud(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_volume(self) -> bool:
        """Causes volume data to be duplicated with the object"""
        ...
    @use_duplicate_volume.setter
    def use_duplicate_volume(self, value: bool) -> None:
        ...
    @property
    def use_duplicate_node_tree(self) -> bool:
        """Make copies of node groups when duplicating nodes in the node editor"""
        ...
    @use_duplicate_node_tree.setter
    def use_duplicate_node_tree(self, value: bool) -> None:
        ...
    @property
    def node_use_insert_offset(self) -> bool:
        """Automatically offset the following or previous nodes in a chain when inserting a new node"""
        ...
    @node_use_insert_offset.setter
    def node_use_insert_offset(self, value: bool) -> None:
        ...
    @property
    def node_margin(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Minimum distance between nodes for Auto-offsetting nodes"""
        ...
    @node_margin.setter
    def node_margin(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def node_preview_resolution(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Resolution used for Shader node previews (should be changed for performance convenience)"""
        ...
    @node_preview_resolution.setter
    def node_preview_resolution(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def use_cursor_lock_adjust(self) -> bool:
        """Place the cursor without 'jumping' to the new location (when lock-to-cursor is used)"""
        ...
    @use_cursor_lock_adjust.setter
    def use_cursor_lock_adjust(self, value: bool) -> None:
        ...
    @property
    def use_mouse_depth_cursor(self) -> bool:
        """Use the surface depth for cursor placement"""
        ...
    @use_mouse_depth_cursor.setter
    def use_mouse_depth_cursor(self, value: bool) -> None:
        ...