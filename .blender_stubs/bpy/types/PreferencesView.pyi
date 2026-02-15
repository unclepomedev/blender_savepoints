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
from .ColorRamp import ColorRamp
class PreferencesView(bpy_struct):
    ui_scale: Annotated[float, "step=1.0", "precision=2"]
    """Changes the size of the fonts and widgets in the interface"""
    border_width: Annotated[int, "step=1"]
    """Size of the padding around each editor."""
    ui_line_width: Literal['THIN', 'AUTO', 'THICK']
    """Changes the thickness of widget outlines, lines and dots in the interface"""
    show_tooltips: bool
    """Display tooltips (when disabled, hold Alt then hover to force display)"""
    show_tooltips_python: bool
    """Show Python references in tooltips"""
    show_developer_ui: bool
    """Display advanced settings and tools for developers"""
    show_area_handle: bool
    """Show visible area maintenance corner handles"""
    show_number_arrows: bool
    """Display arrows in numeric input fields for increasing or decreasing values"""
    show_object_info: bool
    """Include the name of the active object and the current frame number in the text info overlay"""
    show_view_name: bool
    """Include the name of the view orientation in the text info overlay"""
    show_splash: bool
    """Display splash screen on startup"""
    show_playback_fps: bool
    """Include the number of frames displayed per second in the text info overlay while animation is played back"""
    playback_fps_samples: Annotated[int, "step=1"]
    """The number of frames to use for calculating FPS average. Zero to calculate this automatically, where the number of samples matches the target FPS."""
    use_fresnel_edit: bool
    """Enable a fresnel effect on edit mesh overlays.
It improves shape readability of very dense meshes, but increases eye fatigue when modeling lower poly"""
    show_addons_enabled_only: bool
    """Only show enabled add-ons. Un-check to see all installed add-ons."""
    factor_display_type: Literal['FACTOR', 'PERCENTAGE']
    """How factor values are displayed"""
    use_weight_color_range: bool
    """Enable color range used for weight visualization in weight painting mode"""
    @property
    def weight_color_range(self) -> Annotated['ColorRamp', "is_animatable=False"]:
        """Color range used for weight visualization in weight painting mode"""
        ...
    show_navigate_ui: bool
    """Show navigation controls in 2D and 3D views which do not have scroll bars"""
    use_mouse_over_open: bool
    """Open menu buttons and pull-downs automatically when the mouse is hovering"""
    menu_close_leave: bool
    """Close menus when the mouse is moved out of the region."""
    open_toplevel_delay: Annotated[int, "step=1"]
    """Time delay in 1/10 seconds before automatically opening top level menus"""
    open_sublevel_delay: Annotated[int, "step=1"]
    """Time delay in 1/10 seconds before automatically opening sub level menus"""
    color_picker_type: Literal['CIRCLE_HSV', 'CIRCLE_HSL', 'SQUARE_SV', 'SQUARE_HS', 'SQUARE_HV']
    """Different styles of displaying the color picker widget"""
    pie_initial_timeout: Annotated[int, "step=1"]
    """Pie menus will use the initial mouse position as center for this amount of time (in 1/100ths of sec)"""
    pie_tap_timeout: Annotated[int, "step=1"]
    """Pie menu button held longer than this will dismiss menu on release (in 1/100ths of sec)"""
    pie_animation_timeout: Annotated[int, "step=1"]
    """Time needed to fully animate the pie to unfolded state (in 1/100ths of sec)"""
    pie_menu_radius: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Pie menu size in pixels"""
    pie_menu_threshold: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Distance from center needed before a selection can be made"""
    pie_menu_confirm: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Distance threshold after which selection is made (zero to disable)"""
    use_save_prompt: bool
    """Ask for confirmation when quitting with unsaved changes"""
    show_column_layout: bool
    """Use a column layout for toolbox"""
    use_filter_brushes_by_tool: bool
    """Only show brushes applicable for the currently active tool in the asset shelf. Stored in the Preferences, which may have to be saved manually if Auto-Save Preferences is disabled"""
    header_align: Literal['NONE', 'TOP', 'BOTTOM']
    """Default header position for new space-types"""
    render_display_type: Literal['NONE', 'SCREEN', 'AREA', 'WINDOW']
    """Default location where rendered images will be displayed in"""
    filebrowser_display_type: Literal['SCREEN', 'WINDOW']
    """Default location where the File Editor will be displayed in"""
    preferences_display_type: Literal['SCREEN', 'WINDOW']
    """Default location where the Preferences will be displayed in"""
    mini_axis_type: Literal['NONE', 'MINIMAL', 'GIZMO']
    """Show small rotating 3D axes in the top right corner of the 3D viewport"""
    mini_axis_size: Annotated[int, "subtype='PIXEL'", "step=1"]
    """The axes icon's size"""
    mini_axis_brightness: Annotated[int, "step=1"]
    """Brightness of the icon"""
    smooth_view: Annotated[int, "step=1"]
    """Time to animate the view in milliseconds, zero to disable"""
    rotation_angle: Annotated[float, "step=10.0", "precision=3"]
    """Rotation step for numerical pad keys (2 4 6 8)"""
    show_gizmo: bool
    """Use transform gizmos by default"""
    gizmo_size: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Diameter of the gizmo"""
    gizmo_size_navigate_v3d: Annotated[int, "subtype='PIXEL'", "step=1"]
    """The Navigate Gizmo size"""
    lookdev_sphere_size: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Diameter of the HDRI reference spheres"""
    view2d_grid_spacing_min: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Minimum number of pixels between each gridline in 2D Viewports"""
    timecode_style: Literal['MINIMAL', 'SMPTE', 'SMPTE_COMPACT', 'MILLISECONDS', 'SECONDS_ONLY']
    """Format of timecode displayed when not displaying timing in terms of frames"""
    view_frame_type: Literal['KEEP_RANGE', 'SECONDS', 'KEYFRAMES']
    """How zooming to frame focuses around current frame"""
    view_frame_keyframes: Annotated[int, "step=1"]
    """Keyframes around cursor that we zoom around"""
    view_frame_seconds: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]
    """Seconds around cursor that we zoom around"""
    use_text_antialiasing: bool
    """Smooth jagged edges of user interface text"""
    use_text_render_subpixelaa: bool
    """Render text for optimal horizontal placement"""
    text_hinting: Literal['AUTO', 'NONE', 'SLIGHT', 'FULL']
    """Method for making user interface text render sharp"""
    font_path_ui: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """Path to interface font"""
    font_path_ui_mono: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """Path to interface monospaced Font"""
    language: Literal['DEFAULT', 'ab', 'ar_EG', 'eu_EU', 'be', 'bg_BG', 'ca_AD', 'zh_HANS', 'zh_HANT', 'hr_HR', 'cs_CZ', 'da', 'nl_NL', 'en_GB', 'en_US', 'eo', 'fi_FI', 'fr_FR', 'ka', 'de_DE', 'el_GR', 'ha', 'he_IL', 'hi_IN', 'hu_HU', 'id_ID', 'it_IT', 'ja_JP', 'km', 'ko_KR', 'ky_KG', 'lt', 'ml', 'ne_NP', 'fa_IR', 'pl_PL', 'pt_BR', 'pt_PT', 'ro_RO', 'ru_RU', 'sr_RS', 'sr_RS@latin', 'sk_SK', 'sl', 'es', 'sw', 'sv_SE', 'ta', 'th_TH', 'tr_TR', 'uk_UA', 'ur', 'vi_VN']
    """Language used for translation"""
    use_translate_tooltips: bool
    """Translate the descriptions when hovering UI elements (recommended)"""
    use_translate_interface: bool
    """Translate all labels in menus, buttons and panels (note that this might make it hard to follow tutorials or the manual)"""
    use_translate_reports: bool
    """Translate additional information, such as error messages"""
    use_translate_new_dataname: bool
    """Translate the names of new data-blocks (objects, materials...)"""
    show_statusbar_memory: bool
    """Show Blender memory usage"""
    show_statusbar_vram: bool
    """Show GPU video memory usage"""
    show_statusbar_version: bool
    """Show Blender version string"""
    show_statusbar_stats: bool
    """Show scene statistics"""
    show_statusbar_scene_duration: bool
    """Show scene duration"""
    show_extensions_updates: bool
    """Show Extensions Update Count"""
    use_reduce_motion: bool
    """Avoid animations and other motion effects in the interface"""