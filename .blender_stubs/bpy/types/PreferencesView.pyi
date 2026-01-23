# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ColorRamp import ColorRamp
class PreferencesView(bpy_struct):
    ui_scale: float
    border_width: int
    ui_line_width: str
    show_tooltips: bool
    show_tooltips_python: bool
    show_developer_ui: bool
    show_area_handle: bool
    show_number_arrows: bool
    show_object_info: bool
    show_view_name: bool
    show_splash: bool
    show_playback_fps: bool
    playback_fps_samples: int
    use_fresnel_edit: bool
    show_addons_enabled_only: bool
    factor_display_type: str
    use_weight_color_range: bool
    weight_color_range: 'ColorRamp'
    show_navigate_ui: bool
    use_mouse_over_open: bool
    menu_close_leave: bool
    open_toplevel_delay: int
    open_sublevel_delay: int
    color_picker_type: str
    pie_initial_timeout: int
    pie_tap_timeout: int
    pie_animation_timeout: int
    pie_menu_radius: int
    pie_menu_threshold: int
    pie_menu_confirm: int
    use_save_prompt: bool
    show_column_layout: bool
    use_filter_brushes_by_tool: bool
    header_align: str
    render_display_type: str
    filebrowser_display_type: str
    preferences_display_type: str
    mini_axis_type: str
    mini_axis_size: int
    mini_axis_brightness: int
    smooth_view: int
    rotation_angle: float
    show_gizmo: bool
    gizmo_size: int
    gizmo_size_navigate_v3d: int
    lookdev_sphere_size: int
    view2d_grid_spacing_min: int
    timecode_style: str
    view_frame_type: str
    view_frame_keyframes: int
    view_frame_seconds: float
    use_text_antialiasing: bool
    use_text_render_subpixelaa: bool
    text_hinting: str
    font_path_ui: str
    font_path_ui_mono: str
    language: str
    use_translate_tooltips: bool
    use_translate_interface: bool
    use_translate_reports: bool
    use_translate_new_dataname: bool
    show_statusbar_memory: bool
    show_statusbar_vram: bool
    show_statusbar_version: bool
    show_statusbar_stats: bool
    show_statusbar_scene_duration: bool
    show_extensions_updates: bool
    use_reduce_motion: bool