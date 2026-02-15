# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .Panel import Panel
from .ToolActivePanelHelper import ToolActivePanelHelper
from .Constraint import Constraint
from .UILayout import UILayout
class IMAGE_PT_active_tool(Panel, ToolActivePanelHelper):
    @property
    def layout(self) -> Annotated[Optional['UILayout'], "is_animatable=False"]:
        """Defines the structure of the panel in the UI"""
        ...
    text: Annotated[str, "is_animatable=False"]
    """XXX todo"""
    @property
    def custom_data(self) -> Annotated[Optional['Constraint'], "is_animatable=False"]:
        """Panel data"""
        ...
    bl_idname: Annotated[str, "is_animatable=False"]
    """If this is set, the panel gets a custom ID, otherwise it takes the name of the class used to define the panel. For example, if the class name is "OBJECT_PT_hello", and bl_idname is not set by the script, then bl_idname = "OBJECT_PT_hello"."""
    bl_label: Annotated[str, "is_animatable=False"]
    """The panel label, shows up in the panel header at the right of the triangle used to collapse the panel"""
    bl_translation_context: Annotated[str, "is_animatable=False"]
    """Specific translation context, only define when the label needs to be disambiguated from others using the exact same label"""
    bl_description: Annotated[str, "is_animatable=False"]
    """The panel tooltip"""
    bl_category: Annotated[str, "is_animatable=False"]
    """The category (tab) in which the panel will be displayed, when applicable"""
    bl_owner_id: Annotated[str, "is_animatable=False"]
    """The ID owning the data displayed in the panel, if any"""
    bl_space_type: Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']
    """The space where the panel is going to be used in"""
    bl_region_type: Literal['WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'ASSET_SHELF', 'ASSET_SHELF_HEADER', 'PREVIEW', 'HUD', 'NAVIGATION_BAR', 'EXECUTE', 'FOOTER', 'TOOL_HEADER', 'XR']
    """The region where the panel is going to be used in"""
    bl_context: Annotated[str, "is_animatable=False"]
    """The context in which the panel belongs to. (TODO: explain the possible combinations bl_context/bl_region_type/bl_space_type)"""
    bl_options: set[str]
    """Options for this panel type"""
    bl_parent_id: Annotated[str, "is_animatable=False"]
    """If this is set, the panel becomes a sub-panel"""
    bl_ui_units_x: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """When set, defines popup panel width"""
    bl_order: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Panels with lower numbers are default ordered before panels with higher numbers"""
    use_pin: bool
    """Show the panel on all tabs"""
    @property
    def is_popover(self) -> bool:
        ...
    def poll(self, *args, **kwargs) -> Any: ...
    def draw(self, *args, **kwargs) -> Any: ...
    def draw_header(self, *args, **kwargs) -> Any: ...
    def draw_header_preset(self, *args, **kwargs) -> Any: ...