# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeUserInterface.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

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
    @property
    def menu_shadow_fac(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Blending factor for panel and menu shadows"""
        ...
    @menu_shadow_fac.setter
    def menu_shadow_fac(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def menu_shadow_width(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Width of panel and menu shadows, set to zero to disable"""
        ...
    @menu_shadow_width.setter
    def menu_shadow_width(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def icon_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Transparency of icons in the interface, to reduce contrast"""
        ...
    @icon_alpha.setter
    def icon_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def icon_saturation(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Saturation of icons in the interface"""
        ...
    @icon_saturation.setter
    def icon_saturation(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def widget_emboss(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of the 1px shadow line underlying widgets"""
        ...
    @widget_emboss.setter
    def widget_emboss(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def editor_border(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of the border between editors"""
        ...
    @editor_border.setter
    def editor_border(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def editor_outline(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of the outline of each editor, except the active one"""
        ...
    @editor_outline.setter
    def editor_outline(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def editor_outline_active(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of the outline of the active editor"""
        ...
    @editor_outline_active.setter
    def editor_outline_active(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def widget_text_cursor(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of the text insertion cursor (caret)"""
        ...
    @widget_text_cursor.setter
    def widget_text_cursor(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def panel_roundness(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Roundness of the corners of panels and sub-panels"""
        ...
    @panel_roundness.setter
    def panel_roundness(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def panel_header(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @panel_header.setter
    def panel_header(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def panel_title(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @panel_title.setter
    def panel_title(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def panel_text(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @panel_text.setter
    def panel_text(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def panel_back(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @panel_back.setter
    def panel_back(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def panel_sub_back(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @panel_sub_back.setter
    def panel_sub_back(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def panel_outline(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of the outline of top-level panels"""
        ...
    @panel_outline.setter
    def panel_outline(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def panel_active(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of the outline of top-level panels that are active"""
        ...
    @panel_active.setter
    def panel_active(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def transparent_checker_primary(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Primary color of checkerboard pattern indicating transparent areas"""
        ...
    @transparent_checker_primary.setter
    def transparent_checker_primary(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def transparent_checker_secondary(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Secondary color of checkerboard pattern indicating transparent areas"""
        ...
    @transparent_checker_secondary.setter
    def transparent_checker_secondary(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def transparent_checker_size(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Size of checkerboard pattern indicating transparent areas"""
        ...
    @transparent_checker_size.setter
    def transparent_checker_size(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def axis_x(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @axis_x.setter
    def axis_x(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def axis_y(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @axis_y.setter
    def axis_y(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def axis_z(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @axis_z.setter
    def axis_z(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def axis_w(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """W-axis for quaternion and axis-angle rotations"""
        ...
    @axis_w.setter
    def axis_w(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def gizmo_hi(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @gizmo_hi.setter
    def gizmo_hi(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def gizmo_primary(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @gizmo_primary.setter
    def gizmo_primary(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def gizmo_secondary(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @gizmo_secondary.setter
    def gizmo_secondary(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def gizmo_view_align(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @gizmo_view_align.setter
    def gizmo_view_align(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def gizmo_a(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @gizmo_a.setter
    def gizmo_a(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def gizmo_b(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @gizmo_b.setter
    def gizmo_b(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def icon_scene(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @icon_scene.setter
    def icon_scene(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def icon_collection(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @icon_collection.setter
    def icon_collection(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def icon_object(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @icon_object.setter
    def icon_object(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def icon_object_data(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @icon_object_data.setter
    def icon_object_data(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def icon_modifier(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @icon_modifier.setter
    def icon_modifier(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def icon_shading(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:

        ...
    @icon_shading.setter
    def icon_shading(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def icon_folder(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of folders in the file browser"""
        ...
    @icon_folder.setter
    def icon_folder(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def icon_autokey(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of Auto Keying indicator when enabled"""
        ...
    @icon_autokey.setter
    def icon_autokey(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def icon_border_intensity(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]:
        """Control the intensity of the border around themes icons"""
        ...
    @icon_border_intensity.setter
    def icon_border_intensity(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=2"]) -> None:
        ...