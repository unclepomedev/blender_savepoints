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
    widget_emboss: list[float]
    editor_border: list[float]
    editor_outline: list[float]
    editor_outline_active: list[float]
    widget_text_cursor: list[float]
    panel_roundness: float
    panel_header: list[float]
    panel_title: list[float]
    panel_text: list[float]
    panel_back: list[float]
    panel_sub_back: list[float]
    panel_outline: list[float]
    panel_active: list[float]
    transparent_checker_primary: list[float]
    transparent_checker_secondary: list[float]
    transparent_checker_size: int
    axis_x: list[float]
    axis_y: list[float]
    axis_z: list[float]
    axis_w: list[float]
    gizmo_hi: list[float]
    gizmo_primary: list[float]
    gizmo_secondary: list[float]
    gizmo_view_align: list[float]
    gizmo_a: list[float]
    gizmo_b: list[float]
    icon_scene: list[float]
    icon_collection: list[float]
    icon_object: list[float]
    icon_object_data: list[float]
    icon_modifier: list[float]
    icon_shading: list[float]
    icon_folder: list[float]
    icon_autokey: list[float]
    icon_border_intensity: float