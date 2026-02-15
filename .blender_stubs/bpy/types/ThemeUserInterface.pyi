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
from .ThemeWidgetColors import ThemeWidgetColors
from .ThemeWidgetStateColors import ThemeWidgetStateColors
class ThemeUserInterface(bpy_struct):
    @property
    def wcol_regular(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_tool(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_toolbar_item(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_radio(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_text(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_option(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_toggle(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_num(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_numslider(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_box(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_curve(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_menu(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_pulldown(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_menu_back(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_pie_menu(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_tooltip(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_menu_item(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_scroll(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_progress(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_list_item(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    @property
    def wcol_state(self) -> Annotated['ThemeWidgetStateColors', "is_animatable=False"]:
        ...
    @property
    def wcol_tab(self) -> Annotated['ThemeWidgetColors', "is_animatable=False"]:
        ...
    menu_shadow_fac: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Blending factor for panel and menu shadows"""
    menu_shadow_width: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Width of panel and menu shadows, set to zero to disable"""
    icon_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Transparency of icons in the interface, to reduce contrast"""
    icon_saturation: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Saturation of icons in the interface"""
    widget_emboss: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of the 1px shadow line underlying widgets"""
    editor_border: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of the border between editors"""
    editor_outline: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of the outline of each editor, except the active one"""
    editor_outline_active: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of the outline of the active editor"""
    widget_text_cursor: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of the text insertion cursor (caret)"""
    panel_roundness: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Roundness of the corners of panels and sub-panels"""
    panel_header: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    panel_title: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    panel_text: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    panel_back: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    panel_sub_back: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    panel_outline: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of the outline of top-level panels"""
    panel_active: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of the outline of top-level panels that are active"""
    transparent_checker_primary: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Primary color of checkerboard pattern indicating transparent areas"""
    transparent_checker_secondary: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Secondary color of checkerboard pattern indicating transparent areas"""
    transparent_checker_size: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Size of checkerboard pattern indicating transparent areas"""
    axis_x: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    axis_y: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    axis_z: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    axis_w: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """W-axis for quaternion and axis-angle rotations"""
    gizmo_hi: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    gizmo_primary: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    gizmo_secondary: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    gizmo_view_align: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    gizmo_a: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    gizmo_b: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    icon_scene: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    icon_collection: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    icon_object: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    icon_object_data: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    icon_modifier: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    icon_shading: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    icon_folder: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of folders in the file browser"""
    icon_autokey: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color of Auto Keying indicator when enabled"""
    icon_border_intensity: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]
    """Control the intensity of the border around themes icons"""