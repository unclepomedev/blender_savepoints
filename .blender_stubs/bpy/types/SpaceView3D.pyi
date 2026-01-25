# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
from .Object import Object
from .RegionView3D import RegionView3D
from .View3DOverlay import View3DOverlay
from .View3DShading import View3DShading
class SpaceView3D(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    show_region_tool_header: bool
    show_region_toolbar: bool
    show_region_ui: bool
    show_region_hud: bool
    show_region_asset_shelf: bool
    camera: 'Object'
    use_render_border: bool
    render_border_min_x: float
    render_border_min_y: float
    render_border_max_x: float
    render_border_max_y: float
    lock_object: 'Object'
    lock_bone: str
    lock_cursor: bool
    local_view: 'SpaceView3D'
    lens: float
    clip_start: float
    clip_end: float
    lock_camera: bool
    show_gizmo: bool
    show_gizmo_navigate: bool
    show_gizmo_context: bool
    show_gizmo_modifier: bool
    show_gizmo_tool: bool
    show_gizmo_object_translate: bool
    show_gizmo_object_rotate: bool
    show_gizmo_object_scale: bool
    show_gizmo_empty_image: bool
    show_gizmo_empty_force_field: bool
    show_gizmo_light_size: bool
    show_gizmo_light_look_at: bool
    show_gizmo_camera_lens: bool
    show_gizmo_camera_dof_distance: bool
    use_local_camera: bool
    region_3d: 'RegionView3D'
    region_quadviews: bpy_prop_collection['RegionView3D']
    show_reconstruction: bool
    tracks_display_size: float
    tracks_display_type: str
    show_camera_path: bool
    show_bundle_names: bool
    use_local_collections: bool
    stereo_3d_eye: str
    stereo_3d_camera: str
    show_stereo_3d_cameras: bool
    show_stereo_3d_convergence_plane: bool
    stereo_3d_convergence_plane_alpha: float
    show_stereo_3d_volume: bool
    stereo_3d_volume_alpha: float
    mirror_xr_session: bool
    show_object_viewport_mesh: bool
    show_object_viewport_curve: bool
    show_object_viewport_surf: bool
    show_object_viewport_meta: bool
    show_object_viewport_font: bool
    show_object_viewport_curves: bool
    show_object_viewport_pointcloud: bool
    show_object_viewport_volume: bool
    show_object_viewport_armature: bool
    show_object_viewport_lattice: bool
    show_object_viewport_empty: bool
    show_object_viewport_grease_pencil: bool
    show_object_viewport_camera: bool
    show_object_viewport_light: bool
    show_object_viewport_speaker: bool
    show_object_viewport_light_probe: bool
    show_object_select_mesh: bool
    show_object_select_curve: bool
    show_object_select_surf: bool
    show_object_select_meta: bool
    show_object_select_font: bool
    show_object_select_curves: bool
    show_object_select_pointcloud: bool
    show_object_select_volume: bool
    show_object_select_armature: bool
    show_object_select_lattice: bool
    show_object_select_empty: bool
    show_object_select_grease_pencil: bool
    show_object_select_camera: bool
    show_object_select_light: bool
    show_object_select_speaker: bool
    show_object_select_light_probe: bool
    icon_from_show_object_viewport: int
    show_viewer: bool
    shading: 'View3DShading'
    overlay: 'View3DOverlay'
    # --- Injected Methods ---
    @classmethod
    def draw_handler_add(cls, callback: Callable, args: tuple, region_type: str, draw_type: str) -> object: ...
    @classmethod
    def draw_handler_remove(cls, handler: object, region_type: str) -> None: ...