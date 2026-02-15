# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.VIEW3D_AST_brush_sculpt_curves.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .View3DAssetShelf import View3DAssetShelf
from .AssetShelf import AssetShelf

class VIEW3D_AST_brush_sculpt_curves(View3DAssetShelf, AssetShelf):

    bl_idname: Annotated[str, "is_animatable=False"]
    """If this is set, the asset gets a custom ID, otherwise it takes the name of the class used to define the asset (for example, if the class name is "OBJECT_AST_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_AST_hello")"""
    bl_space_type: Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']
    """The space where the asset shelf will show up in. Ignored for popup asset shelves which can be displayed in any space."""
    bl_options: set[str]
    """Options for this asset shelf type"""
    bl_activate_operator: Annotated[str, "is_animatable=False"]
    """Operator to call when activating an item with asset reference properties"""
    bl_drag_operator: Annotated[str, "is_animatable=False"]
    """Operator to call when dragging an item with asset reference properties"""
    bl_default_preview_size: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Default size of the asset preview thumbnails in pixels"""
    filter_action: bool
    """Show Action data-blocks"""
    filter_armature: bool
    """Show Armature data-blocks"""
    filter_brush: bool
    """Show Brushes data-blocks"""
    filter_camera: bool
    """Show Camera data-blocks"""
    filter_cachefile: bool
    """Show Cache File data-blocks"""
    filter_curve: bool
    """Show Curve data-blocks"""
    filter_annotations: bool
    """Show Annotation data-blocks"""
    filter_grease_pencil: bool
    """Show Grease Pencil data-blocks"""
    filter_group: bool
    """Show Collection data-blocks"""
    filter_curves: bool
    """Show/hide Curves data-blocks"""
    filter_image: bool
    """Show Image data-blocks"""
    filter_light: bool
    """Show Light data-blocks"""
    filter_light_probe: bool
    """Show Light Probe data-blocks"""
    filter_linestyle: bool
    """Show Freestyle's Line Style data-blocks"""
    filter_lattice: bool
    """Show Lattice data-blocks"""
    filter_material: bool
    """Show Material data-blocks"""
    filter_metaball: bool
    """Show Metaball data-blocks"""
    filter_movie_clip: bool
    """Show Movie Clip data-blocks"""
    filter_mesh: bool
    """Show Mesh data-blocks"""
    filter_mask: bool
    """Show Mask data-blocks"""
    filter_node_tree: bool
    """Show Node Tree data-blocks"""
    filter_object: bool
    """Show Object data-blocks"""
    filter_particle_settings: bool
    """Show Particle Settings data-blocks"""
    filter_palette: bool
    """Show Palette data-blocks"""
    filter_paint_curve: bool
    """Show Paint Curve data-blocks"""
    filter_pointcloud: bool
    """Show/hide Point Cloud data-blocks"""
    filter_scene: bool
    """Show Scene data-blocks"""
    filter_speaker: bool
    """Show Speaker data-blocks"""
    filter_sound: bool
    """Show Sound data-blocks"""
    filter_texture: bool
    """Show Texture data-blocks"""
    filter_text: bool
    """Show Text data-blocks"""
    filter_font: bool
    """Show Font data-blocks"""
    filter_volume: bool
    """Show/hide Volume data-blocks"""
    filter_world: bool
    """Show World data-blocks"""
    filter_work_space: bool
    """Show workspace data-blocks"""
    asset_library_reference: Literal['ALL', 'LOCAL', 'ESSENTIALS', 'CUSTOM']
    """Choose the asset library to display assets from"""
    show_names: bool
    """Show the asset name together with the preview. Otherwise only the preview will be visible."""
    preview_size: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Size of the asset preview thumbnails in pixels"""
    search_filter: Annotated[str, "is_animatable=False"]
    """Filter assets by name"""
    def poll(self, *args, **kwargs) -> Any: ...
    def asset_poll(self, *args, **kwargs) -> Any: ...
    def get_active_asset(self, *args, **kwargs) -> Any: ...
    def draw_context_menu(self, *args, **kwargs) -> Any: ...