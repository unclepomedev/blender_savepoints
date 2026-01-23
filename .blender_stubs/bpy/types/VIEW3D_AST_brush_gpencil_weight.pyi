# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .AssetShelfHiddenByDefault import AssetShelfHiddenByDefault
from .View3DAssetShelf import View3DAssetShelf
from .AssetShelf import AssetShelf
class VIEW3D_AST_brush_gpencil_weight(AssetShelfHiddenByDefault, View3DAssetShelf, AssetShelf):
    bl_idname: str
    bl_space_type: str
    bl_options: set[str]
    bl_activate_operator: str
    bl_drag_operator: str
    bl_default_preview_size: int
    filter_action: bool
    filter_armature: bool
    filter_brush: bool
    filter_camera: bool
    filter_cachefile: bool
    filter_curve: bool
    filter_annotations: bool
    filter_grease_pencil: bool
    filter_group: bool
    filter_curves: bool
    filter_image: bool
    filter_light: bool
    filter_light_probe: bool
    filter_linestyle: bool
    filter_lattice: bool
    filter_material: bool
    filter_metaball: bool
    filter_movie_clip: bool
    filter_mesh: bool
    filter_mask: bool
    filter_node_tree: bool
    filter_object: bool
    filter_particle_settings: bool
    filter_palette: bool
    filter_paint_curve: bool
    filter_pointcloud: bool
    filter_scene: bool
    filter_speaker: bool
    filter_sound: bool
    filter_texture: bool
    filter_text: bool
    filter_font: bool
    filter_volume: bool
    filter_world: bool
    filter_work_space: bool
    asset_library_reference: str
    show_names: bool
    preview_size: int
    search_filter: str
    def poll(self, *args, **kwargs) -> Any: ...
    def asset_poll(self, *args, **kwargs) -> Any: ...
    def get_active_asset(self, *args, **kwargs) -> Any: ...
    def draw_context_menu(self, *args, **kwargs) -> Any: ...