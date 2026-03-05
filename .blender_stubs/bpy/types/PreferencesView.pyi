# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PreferencesView.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ColorRamp import ColorRamp

class PreferencesView(bpy_struct):

    @property
    def ui_scale(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Changes the size of the fonts and widgets in the interface"""
        ...
    @ui_scale.setter
    def ui_scale(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def border_width(self) -> Annotated[int, "step=1"]:
        """Size of the padding around each editor."""
        ...
    @border_width.setter
    def border_width(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def ui_line_width(self) -> Literal['THIN', 'AUTO', 'THICK']:
        """Changes the thickness of widget outlines, lines and dots in the interface"""
        ...
    @ui_line_width.setter
    def ui_line_width(self, value: Literal['THIN', 'AUTO', 'THICK']) -> None:
        ...
    @property
    def show_tooltips(self) -> bool:
        """Display tooltips (when disabled, hold Alt then hover to force display)"""
        ...
    @show_tooltips.setter
    def show_tooltips(self, value: bool) -> None:
        ...
    @property
    def show_tooltips_python(self) -> bool:
        """Show Python references in tooltips"""
        ...
    @show_tooltips_python.setter
    def show_tooltips_python(self, value: bool) -> None:
        ...
    @property
    def show_developer_ui(self) -> bool:
        """Display advanced settings and tools for developers"""
        ...
    @show_developer_ui.setter
    def show_developer_ui(self, value: bool) -> None:
        ...
    @property
    def show_area_handle(self) -> bool:
        """Show visible area maintenance corner handles"""
        ...
    @show_area_handle.setter
    def show_area_handle(self, value: bool) -> None:
        ...
    @property
    def show_number_arrows(self) -> bool:
        """Display arrows in numeric input fields for increasing or decreasing values"""
        ...
    @show_number_arrows.setter
    def show_number_arrows(self, value: bool) -> None:
        ...
    @property
    def show_object_info(self) -> bool:
        """Include the name of the active object and the current frame number in the text info overlay"""
        ...
    @show_object_info.setter
    def show_object_info(self, value: bool) -> None:
        ...
    @property
    def show_view_name(self) -> bool:
        """Include the name of the view orientation in the text info overlay"""
        ...
    @show_view_name.setter
    def show_view_name(self, value: bool) -> None:
        ...
    @property
    def show_splash(self) -> bool:
        """Display splash screen on startup"""
        ...
    @show_splash.setter
    def show_splash(self, value: bool) -> None:
        ...
    @property
    def show_playback_fps(self) -> bool:
        """Include the number of frames displayed per second in the text info overlay while animation is played back"""
        ...
    @show_playback_fps.setter
    def show_playback_fps(self, value: bool) -> None:
        ...
    @property
    def playback_fps_samples(self) -> Annotated[int, "step=1"]:
        """The number of frames to use for calculating FPS average. Zero to calculate this automatically, where the number of samples matches the target FPS."""
        ...
    @playback_fps_samples.setter
    def playback_fps_samples(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_fresnel_edit(self) -> bool:
        """Enable a fresnel effect on edit mesh overlays.
It improves shape readability of very dense meshes, but increases eye fatigue when modeling lower poly"""
        ...
    @use_fresnel_edit.setter
    def use_fresnel_edit(self, value: bool) -> None:
        ...
    @property
    def show_addons_enabled_only(self) -> bool:
        """Only show enabled add-ons. Un-check to see all installed add-ons."""
        ...
    @show_addons_enabled_only.setter
    def show_addons_enabled_only(self, value: bool) -> None:
        ...
    @property
    def factor_display_type(self) -> Literal['FACTOR', 'PERCENTAGE']:
        """How factor values are displayed"""
        ...
    @factor_display_type.setter
    def factor_display_type(self, value: Literal['FACTOR', 'PERCENTAGE']) -> None:
        ...
    @property
    def use_weight_color_range(self) -> bool:
        """Enable color range used for weight visualization in weight painting mode"""
        ...
    @use_weight_color_range.setter
    def use_weight_color_range(self, value: bool) -> None:
        ...
    @property
    def weight_color_range(self) -> Annotated['ColorRamp', "is_animatable=False"]:
        """Color range used for weight visualization in weight painting mode"""
        ...
    @property
    def show_navigate_ui(self) -> bool:
        """Show navigation controls in 2D and 3D views which do not have scroll bars"""
        ...
    @show_navigate_ui.setter
    def show_navigate_ui(self, value: bool) -> None:
        ...
    @property
    def use_mouse_over_open(self) -> bool:
        """Open menu buttons and pull-downs automatically when the mouse is hovering"""
        ...
    @use_mouse_over_open.setter
    def use_mouse_over_open(self, value: bool) -> None:
        ...
    @property
    def menu_close_leave(self) -> bool:
        """Close menus when the mouse is moved out of the region."""
        ...
    @menu_close_leave.setter
    def menu_close_leave(self, value: bool) -> None:
        ...
    @property
    def open_toplevel_delay(self) -> Annotated[int, "step=1"]:
        """Time delay in 1/10 seconds before automatically opening top level menus"""
        ...
    @open_toplevel_delay.setter
    def open_toplevel_delay(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def open_sublevel_delay(self) -> Annotated[int, "step=1"]:
        """Time delay in 1/10 seconds before automatically opening sub level menus"""
        ...
    @open_sublevel_delay.setter
    def open_sublevel_delay(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def color_picker_type(self) -> Literal['CIRCLE_HSV', 'CIRCLE_HSL', 'SQUARE_SV', 'SQUARE_HS', 'SQUARE_HV']:
        """Different styles of displaying the color picker widget"""
        ...
    @color_picker_type.setter
    def color_picker_type(self, value: Literal['CIRCLE_HSV', 'CIRCLE_HSL', 'SQUARE_SV', 'SQUARE_HS', 'SQUARE_HV']) -> None:
        ...
    @property
    def pie_initial_timeout(self) -> Annotated[int, "step=1"]:
        """Pie menus will use the initial mouse position as center for this amount of time (in 1/100ths of sec)"""
        ...
    @pie_initial_timeout.setter
    def pie_initial_timeout(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def pie_tap_timeout(self) -> Annotated[int, "step=1"]:
        """Pie menu button held longer than this will dismiss menu on release (in 1/100ths of sec)"""
        ...
    @pie_tap_timeout.setter
    def pie_tap_timeout(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def pie_animation_timeout(self) -> Annotated[int, "step=1"]:
        """Time needed to fully animate the pie to unfolded state (in 1/100ths of sec)"""
        ...
    @pie_animation_timeout.setter
    def pie_animation_timeout(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def pie_menu_radius(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Pie menu size in pixels"""
        ...
    @pie_menu_radius.setter
    def pie_menu_radius(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def pie_menu_threshold(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Distance from center needed before a selection can be made"""
        ...
    @pie_menu_threshold.setter
    def pie_menu_threshold(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def pie_menu_confirm(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Distance threshold after which selection is made (zero to disable)"""
        ...
    @pie_menu_confirm.setter
    def pie_menu_confirm(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def use_save_prompt(self) -> bool:
        """Ask for confirmation when quitting with unsaved changes"""
        ...
    @use_save_prompt.setter
    def use_save_prompt(self, value: bool) -> None:
        ...
    @property
    def show_column_layout(self) -> bool:
        """Use a column layout for toolbox"""
        ...
    @show_column_layout.setter
    def show_column_layout(self, value: bool) -> None:
        ...
    @property
    def use_filter_brushes_by_tool(self) -> bool:
        """Only show brushes applicable for the currently active tool in the asset shelf. Stored in the Preferences, which may have to be saved manually if Auto-Save Preferences is disabled"""
        ...
    @use_filter_brushes_by_tool.setter
    def use_filter_brushes_by_tool(self, value: bool) -> None:
        ...
    @property
    def header_align(self) -> Literal['NONE', 'TOP', 'BOTTOM']:
        """Default header position for new space-types"""
        ...
    @header_align.setter
    def header_align(self, value: Literal['NONE', 'TOP', 'BOTTOM']) -> None:
        ...
    @property
    def render_display_type(self) -> Literal['NONE', 'SCREEN', 'AREA', 'WINDOW']:
        """Default location where rendered images will be displayed in"""
        ...
    @render_display_type.setter
    def render_display_type(self, value: Literal['NONE', 'SCREEN', 'AREA', 'WINDOW']) -> None:
        ...
    @property
    def filebrowser_display_type(self) -> Literal['SCREEN', 'WINDOW']:
        """Default location where the File Editor will be displayed in"""
        ...
    @filebrowser_display_type.setter
    def filebrowser_display_type(self, value: Literal['SCREEN', 'WINDOW']) -> None:
        ...
    @property
    def preferences_display_type(self) -> Literal['SCREEN', 'WINDOW']:
        """Default location where the Preferences will be displayed in"""
        ...
    @preferences_display_type.setter
    def preferences_display_type(self, value: Literal['SCREEN', 'WINDOW']) -> None:
        ...
    @property
    def mini_axis_type(self) -> Literal['NONE', 'MINIMAL', 'GIZMO']:
        """Show small rotating 3D axes in the top right corner of the 3D viewport"""
        ...
    @mini_axis_type.setter
    def mini_axis_type(self, value: Literal['NONE', 'MINIMAL', 'GIZMO']) -> None:
        ...
    @property
    def mini_axis_size(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """The axes icon's size"""
        ...
    @mini_axis_size.setter
    def mini_axis_size(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def mini_axis_brightness(self) -> Annotated[int, "step=1"]:
        """Brightness of the icon"""
        ...
    @mini_axis_brightness.setter
    def mini_axis_brightness(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def smooth_view(self) -> Annotated[int, "step=1"]:
        """Time to animate the view in milliseconds, zero to disable"""
        ...
    @smooth_view.setter
    def smooth_view(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def rotation_angle(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Rotation step for numerical pad keys (2 4 6 8)"""
        ...
    @rotation_angle.setter
    def rotation_angle(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def show_gizmo(self) -> bool:
        """Use transform gizmos by default"""
        ...
    @show_gizmo.setter
    def show_gizmo(self, value: bool) -> None:
        ...
    @property
    def gizmo_size(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Diameter of the gizmo"""
        ...
    @gizmo_size.setter
    def gizmo_size(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def gizmo_size_navigate_v3d(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """The Navigate Gizmo size"""
        ...
    @gizmo_size_navigate_v3d.setter
    def gizmo_size_navigate_v3d(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def lookdev_sphere_size(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Diameter of the HDRI reference spheres"""
        ...
    @lookdev_sphere_size.setter
    def lookdev_sphere_size(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def view2d_grid_spacing_min(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Minimum number of pixels between each gridline in 2D Viewports"""
        ...
    @view2d_grid_spacing_min.setter
    def view2d_grid_spacing_min(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def timecode_style(self) -> Literal['MINIMAL', 'SMPTE', 'SMPTE_COMPACT', 'MILLISECONDS', 'SECONDS_ONLY']:
        """Format of timecode displayed when not displaying timing in terms of frames"""
        ...
    @timecode_style.setter
    def timecode_style(self, value: Literal['MINIMAL', 'SMPTE', 'SMPTE_COMPACT', 'MILLISECONDS', 'SECONDS_ONLY']) -> None:
        ...
    @property
    def view_frame_type(self) -> Literal['KEEP_RANGE', 'SECONDS', 'KEYFRAMES']:
        """How zooming to frame focuses around current frame"""
        ...
    @view_frame_type.setter
    def view_frame_type(self, value: Literal['KEEP_RANGE', 'SECONDS', 'KEYFRAMES']) -> None:
        ...
    @property
    def view_frame_keyframes(self) -> Annotated[int, "step=1"]:
        """Keyframes around cursor that we zoom around"""
        ...
    @view_frame_keyframes.setter
    def view_frame_keyframes(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def view_frame_seconds(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]:
        """Seconds around cursor that we zoom around"""
        ...
    @view_frame_seconds.setter
    def view_frame_seconds(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_text_antialiasing(self) -> bool:
        """Smooth jagged edges of user interface text"""
        ...
    @use_text_antialiasing.setter
    def use_text_antialiasing(self, value: bool) -> None:
        ...
    @property
    def use_text_render_subpixelaa(self) -> bool:
        """Render text for optimal horizontal placement"""
        ...
    @use_text_render_subpixelaa.setter
    def use_text_render_subpixelaa(self, value: bool) -> None:
        ...
    @property
    def text_hinting(self) -> Literal['AUTO', 'NONE', 'SLIGHT', 'FULL']:
        """Method for making user interface text render sharp"""
        ...
    @text_hinting.setter
    def text_hinting(self, value: Literal['AUTO', 'NONE', 'SLIGHT', 'FULL']) -> None:
        ...
    @property
    def font_path_ui(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Path to interface font"""
        ...
    @font_path_ui.setter
    def font_path_ui(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def font_path_ui_mono(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Path to interface monospaced Font"""
        ...
    @font_path_ui_mono.setter
    def font_path_ui_mono(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def language(self) -> Literal['DEFAULT', 'ab', 'ar_EG', 'eu_EU', 'be', 'bg_BG', 'ca_AD', 'zh_HANS', 'zh_HANT', 'hr_HR', 'cs_CZ', 'da', 'nl_NL', 'en_GB', 'en_US', 'eo', 'fi_FI', 'fr_FR', 'ka', 'de_DE', 'el_GR', 'ha', 'he_IL', 'hi_IN', 'hu_HU', 'id_ID', 'it_IT', 'ja_JP', 'km', 'ko_KR', 'ky_KG', 'lt', 'ml', 'ne_NP', 'fa_IR', 'pl_PL', 'pt_BR', 'pt_PT', 'ro_RO', 'ru_RU', 'sr_RS', 'sr_RS@latin', 'sk_SK', 'sl', 'es', 'sw', 'sv_SE', 'ta', 'th_TH', 'tr_TR', 'uk_UA', 'ur', 'vi_VN']:
        """Language used for translation"""
        ...
    @language.setter
    def language(self, value: Literal['DEFAULT', 'ab', 'ar_EG', 'eu_EU', 'be', 'bg_BG', 'ca_AD', 'zh_HANS', 'zh_HANT', 'hr_HR', 'cs_CZ', 'da', 'nl_NL', 'en_GB', 'en_US', 'eo', 'fi_FI', 'fr_FR', 'ka', 'de_DE', 'el_GR', 'ha', 'he_IL', 'hi_IN', 'hu_HU', 'id_ID', 'it_IT', 'ja_JP', 'km', 'ko_KR', 'ky_KG', 'lt', 'ml', 'ne_NP', 'fa_IR', 'pl_PL', 'pt_BR', 'pt_PT', 'ro_RO', 'ru_RU', 'sr_RS', 'sr_RS@latin', 'sk_SK', 'sl', 'es', 'sw', 'sv_SE', 'ta', 'th_TH', 'tr_TR', 'uk_UA', 'ur', 'vi_VN']) -> None:
        ...
    @property
    def use_translate_tooltips(self) -> bool:
        """Translate the descriptions when hovering UI elements (recommended)"""
        ...
    @use_translate_tooltips.setter
    def use_translate_tooltips(self, value: bool) -> None:
        ...
    @property
    def use_translate_interface(self) -> bool:
        """Translate all labels in menus, buttons and panels (note that this might make it hard to follow tutorials or the manual)"""
        ...
    @use_translate_interface.setter
    def use_translate_interface(self, value: bool) -> None:
        ...
    @property
    def use_translate_reports(self) -> bool:
        """Translate additional information, such as error messages"""
        ...
    @use_translate_reports.setter
    def use_translate_reports(self, value: bool) -> None:
        ...
    @property
    def use_translate_new_dataname(self) -> bool:
        """Translate the names of new data-blocks (objects, materials...)"""
        ...
    @use_translate_new_dataname.setter
    def use_translate_new_dataname(self, value: bool) -> None:
        ...
    @property
    def show_statusbar_memory(self) -> bool:
        """Show Blender memory usage"""
        ...
    @show_statusbar_memory.setter
    def show_statusbar_memory(self, value: bool) -> None:
        ...
    @property
    def show_statusbar_vram(self) -> bool:
        """Show GPU video memory usage"""
        ...
    @show_statusbar_vram.setter
    def show_statusbar_vram(self, value: bool) -> None:
        ...
    @property
    def show_statusbar_version(self) -> bool:
        """Show Blender version string"""
        ...
    @show_statusbar_version.setter
    def show_statusbar_version(self, value: bool) -> None:
        ...
    @property
    def show_statusbar_stats(self) -> bool:
        """Show scene statistics"""
        ...
    @show_statusbar_stats.setter
    def show_statusbar_stats(self, value: bool) -> None:
        ...
    @property
    def show_statusbar_scene_duration(self) -> bool:
        """Show scene duration"""
        ...
    @show_statusbar_scene_duration.setter
    def show_statusbar_scene_duration(self, value: bool) -> None:
        ...
    @property
    def show_extensions_updates(self) -> bool:
        """Show Extensions Update Count"""
        ...
    @show_extensions_updates.setter
    def show_extensions_updates(self, value: bool) -> None:
        ...
    @property
    def use_reduce_motion(self) -> bool:
        """Avoid animations and other motion effects in the interface"""
        ...
    @use_reduce_motion.setter
    def use_reduce_motion(self, value: bool) -> None:
        ...