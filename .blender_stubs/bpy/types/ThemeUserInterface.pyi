# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ThemeWidgetColors import ThemeWidgetColors
from .ThemeWidgetStateColors import ThemeWidgetStateColors
class ThemeUserInterface(bpy_struct):
    wcol_regular: 'ThemeWidgetColors'
    wcol_tool: 'ThemeWidgetColors'
    wcol_toolbar_item: 'ThemeWidgetColors'
    wcol_radio: 'ThemeWidgetColors'
    wcol_text: 'ThemeWidgetColors'
    wcol_option: 'ThemeWidgetColors'
    wcol_toggle: 'ThemeWidgetColors'
    wcol_num: 'ThemeWidgetColors'
    wcol_numslider: 'ThemeWidgetColors'
    wcol_box: 'ThemeWidgetColors'
    wcol_curve: 'ThemeWidgetColors'
    wcol_menu: 'ThemeWidgetColors'
    wcol_pulldown: 'ThemeWidgetColors'
    wcol_menu_back: 'ThemeWidgetColors'
    wcol_pie_menu: 'ThemeWidgetColors'
    wcol_tooltip: 'ThemeWidgetColors'
    wcol_menu_item: 'ThemeWidgetColors'
    wcol_scroll: 'ThemeWidgetColors'
    wcol_progress: 'ThemeWidgetColors'
    wcol_list_item: 'ThemeWidgetColors'
    wcol_state: 'ThemeWidgetStateColors'
    wcol_tab: 'ThemeWidgetColors'
    menu_shadow_fac: float
    menu_shadow_width: int
    icon_alpha: float
    icon_saturation: float
    widget_emboss: float
    editor_border: float
    editor_outline: float
    editor_outline_active: float
    widget_text_cursor: float
    panel_roundness: float
    panel_header: float
    panel_title: float
    panel_text: float
    panel_back: float
    panel_sub_back: float
    panel_outline: float
    panel_active: float
    transparent_checker_primary: float
    transparent_checker_secondary: float
    transparent_checker_size: int
    axis_x: float
    axis_y: float
    axis_z: float
    axis_w: float
    gizmo_hi: float
    gizmo_primary: float
    gizmo_secondary: float
    gizmo_view_align: float
    gizmo_a: float
    gizmo_b: float
    icon_scene: float
    icon_collection: float
    icon_object: float
    icon_object_data: float
    icon_modifier: float
    icon_shading: float
    icon_folder: float
    icon_autokey: float
    icon_border_intensity: float