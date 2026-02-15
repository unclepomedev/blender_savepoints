# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class PreferencesEdit(bpy_struct):
    material_link: Literal['OBDATA', 'OBJECT']
    """Toggle whether the material is linked to object data or the object block"""
    object_align: Literal['WORLD', 'VIEW', 'CURSOR']
    """The default alignment for objects added from a 3D viewport menu"""
    use_enter_edit_mode: bool
    """Enter edit mode automatically after adding a new object"""
    collection_instance_empty_size: Annotated[float, "step=10.0", "precision=3"]
    """Display size of the empty when new collection instances are created"""
    use_text_edit_auto_close: bool
    """Automatically close relevant character pairs when typing in the text editor"""
    undo_steps: Annotated[int, "step=1"]
    """Number of undo steps available (smaller values conserve memory)"""
    undo_memory_limit: Annotated[int, "step=1"]
    """Maximum memory usage in megabytes (0 means unlimited)"""
    use_global_undo: bool
    """Global undo works by keeping a full copy of the file itself in memory, so takes extra memory"""
    use_auto_keying: bool
    """Automatic keyframe insertion for Objects and Bones (default setting used for new Scenes)"""
    auto_keying_mode: Literal['ADD_REPLACE_KEYS', 'REPLACE_KEYS']
    """Mode of automatic keyframe insertion for Objects and Bones (default setting used for new Scenes)"""
    use_keyframe_insert_available: bool
    """Insert Keyframes only for properties that are already animated"""
    use_auto_keying_warning: bool
    """Show warning indicators when transforming objects and bones if auto keying is enabled"""
    key_insert_channels: set[str]
    """Which channels to insert keys at when no keying set is active"""
    use_auto_keyframe_insert_needed: bool
    """Auto-Keying will skip inserting keys that don't affect the animation"""
    use_keyframe_insert_needed: bool
    """When keying manually, skip inserting keys that don't affect the animation"""
    use_visual_keying: bool
    """Use Visual keying automatically for constrained objects"""
    use_insertkey_xyz_to_rgb: bool
    """Color for newly added transformation F-Curves (Location, Rotation, Scale) and also Color is based on the transform axis"""
    use_anim_channel_group_colors: bool
    """Use animation channel group colors; generally this is used to show bone group colors"""
    fcurve_new_auto_smoothing: Literal['NONE', 'CONT_ACCEL']
    """Auto Handle Smoothing mode used for newly added F-Curves"""
    keyframe_new_interpolation_type: Literal['CONSTANT', 'LINEAR', 'BEZIER', 'SINE', 'QUAD', 'CUBIC', 'QUART', 'QUINT', 'EXPO', 'CIRC', 'BACK', 'BOUNCE', 'ELASTIC']
    """Interpolation mode used for first keyframe on newly added F-Curves (subsequent keyframes take interpolation from preceding keyframe)"""
    keyframe_new_handle_type: Literal['FREE', 'ALIGNED', 'VECTOR', 'AUTO', 'AUTO_CLAMPED']
    """Handle type for handles of new keyframes"""
    use_negative_frames: bool
    """Current frame number can be manually set to a negative value"""
    fcurve_unselected_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """The opacity of unselected F-Curves against the background of the Graph Editor"""
    show_only_selected_curve_keyframes: bool
    """Only keyframes of selected F-Curves are visible and editable"""
    use_fcurve_high_quality_drawing: bool
    """Draw F-Curves using Anti-Aliasing (disable for better performance)"""
    grease_pencil_manhattan_distance: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Pixels moved by mouse per axis when drawing stroke"""
    grease_pencil_euclidean_distance: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Distance moved by mouse when drawing stroke to include"""
    grease_pencil_eraser_radius: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Radius of eraser 'brush'"""
    grease_pencil_default_color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of new annotation layers"""
    sculpt_paint_overlay_color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of texture overlay"""
    connect_strips_by_default: bool
    """Connect newly added movie strips by default if they have multiple channels"""
    use_duplicate_mesh: bool
    """Causes mesh data to be duplicated with the object"""
    use_duplicate_surface: bool
    """Causes surface data to be duplicated with the object"""
    use_duplicate_curve: bool
    """Causes curve data to be duplicated with the object"""
    use_duplicate_lattice: bool
    """Causes lattice data to be duplicated with the object"""
    use_duplicate_text: bool
    """Causes text data to be duplicated with the object"""
    use_duplicate_metaball: bool
    """Causes metaball data to be duplicated with the object"""
    use_duplicate_armature: bool
    """Causes armature data to be duplicated with the object"""
    use_duplicate_camera: bool
    """Causes camera data to be duplicated with the object"""
    use_duplicate_speaker: bool
    """Causes speaker data to be duplicated with the object"""
    use_duplicate_light: bool
    """Causes light data to be duplicated with the object"""
    use_duplicate_material: bool
    """Causes material data to be duplicated with the object"""
    use_duplicate_action: bool
    """Causes actions to be duplicated with the data-blocks"""
    use_duplicate_particle: bool
    """Causes particle systems to be duplicated with the object"""
    use_duplicate_lightprobe: bool
    """Causes light probe data to be duplicated with the object"""
    use_duplicate_grease_pencil: bool
    """Causes Grease Pencil data to be duplicated with the object"""
    use_duplicate_curves: bool
    """Causes curves data to be duplicated with the object"""
    use_duplicate_pointcloud: bool
    """Causes point cloud data to be duplicated with the object"""
    use_duplicate_volume: bool
    """Causes volume data to be duplicated with the object"""
    use_duplicate_node_tree: bool
    """Make copies of node groups when duplicating nodes in the node editor"""
    node_use_insert_offset: bool
    """Automatically offset the following or previous nodes in a chain when inserting a new node"""
    node_margin: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Minimum distance between nodes for Auto-offsetting nodes"""
    node_preview_resolution: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Resolution used for Shader node previews (should be changed for performance convenience)"""
    use_cursor_lock_adjust: bool
    """Place the cursor without 'jumping' to the new location (when lock-to-cursor is used)"""
    use_mouse_depth_cursor: bool
    """Use the surface depth for cursor placement"""