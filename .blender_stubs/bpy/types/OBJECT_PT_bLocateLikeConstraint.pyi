# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.OBJECT_PT_bLocateLikeConstraint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ObjectConstraintPanel import ObjectConstraintPanel
from .ConstraintButtonsPanel import ConstraintButtonsPanel
from .Panel import Panel
from .Constraint import Constraint
from .UILayout import UILayout

class OBJECT_PT_bLocateLikeConstraint(ObjectConstraintPanel, ConstraintButtonsPanel, Panel):

    @property
    def layout(self) -> Annotated[Optional['UILayout'], "is_animatable=False"]:
        """Defines the structure of the panel in the UI"""
        ...
    @property
    def text(self) -> Annotated[str, "is_animatable=False"]:
        """XXX todo"""
        ...
    @text.setter
    def text(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def custom_data(self) -> Annotated[Optional['Constraint'], "is_animatable=False"]:
        """Panel data"""
        ...
    @property
    def bl_idname(self) -> Annotated[str, "is_animatable=False"]:
        """If this is set, the panel gets a custom ID, otherwise it takes the name of the class used to define the panel. For example, if the class name is "OBJECT_PT_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_PT_hello"."""
        ...
    @bl_idname.setter
    def bl_idname(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_label(self) -> Annotated[str, "is_animatable=False"]:
        """The panel label, shows up in the panel header at the right of the triangle used to collapse the panel"""
        ...
    @bl_label.setter
    def bl_label(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_translation_context(self) -> Annotated[str, "is_animatable=False"]:
        """Specific translation context, only define when the label needs to be disambiguated from others using the exact same label"""
        ...
    @bl_translation_context.setter
    def bl_translation_context(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_description(self) -> Annotated[str, "is_animatable=False"]:
        """The panel tooltip"""
        ...
    @bl_description.setter
    def bl_description(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_category(self) -> Annotated[str, "is_animatable=False"]:
        """The category (tab) in which the panel will be displayed, when applicable"""
        ...
    @bl_category.setter
    def bl_category(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_owner_id(self) -> Annotated[str, "is_animatable=False"]:
        """The ID owning the data displayed in the panel, if any"""
        ...
    @bl_owner_id.setter
    def bl_owner_id(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_space_type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """The space where the panel is going to be used in"""
        ...
    @bl_space_type.setter
    def bl_space_type(self, value: Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']):
        ...
    @property
    def bl_region_type(self) -> Literal['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'ASSET_SHELF', 'ASSET_SHELF_HEADER', 'PREVIEW', 'HUD', 'NAVIGATION_BAR', 'EXECUTE', 'FOOTER', 'TOOL_HEADER', 'XR']:
        """The region where the panel is going to be used in"""
        ...
    @bl_region_type.setter
    def bl_region_type(self, value: Literal['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'ASSET_SHELF', 'ASSET_SHELF_HEADER', 'PREVIEW', 'HUD', 'NAVIGATION_BAR', 'EXECUTE', 'FOOTER', 'TOOL_HEADER', 'XR']):
        ...
    @property
    def bl_context(self) -> Annotated[str, "is_animatable=False"]:
        """The context in which the panel belongs to. (TODO: explain the possible combinations bl_context/bl_region_type/bl_space_type)"""
        ...
    @bl_context.setter
    def bl_context(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_options(self) -> set[str]:
        """Options for this panel type"""
        ...
    @bl_options.setter
    def bl_options(self, value: set[str]):
        ...
    @property
    def bl_parent_id(self) -> Annotated[str, "is_animatable=False"]:
        """If this is set, the panel becomes a sub-panel"""
        ...
    @bl_parent_id.setter
    def bl_parent_id(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def bl_ui_units_x(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """When set, defines popup panel width"""
        ...
    @bl_ui_units_x.setter
    def bl_ui_units_x(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def bl_order(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Panels with lower numbers are default ordered before panels with higher numbers"""
        ...
    @bl_order.setter
    def bl_order(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def use_pin(self) -> bool:
        """Show the panel on all tabs"""
        ...
    @use_pin.setter
    def use_pin(self, value: bool):
        ...
    @property
    def is_popover(self) -> bool:

        ...
    def poll(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def draw_header(self, *args, **kwargs) -> Any: ...
    def draw_header_preset(self, *args, **kwargs) -> Any: ...