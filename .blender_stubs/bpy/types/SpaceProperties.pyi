# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
from .ID import ID
class SpaceProperties(Space):
    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    show_locked_time: bool
    """Synchronize the visible timeline range with other time-based editors"""
    show_region_header: bool
    context: Literal['TOOL', 'SCENE', 'RENDER', 'OUTPUT', 'VIEW_LAYER', 'WORLD', 'COLLECTION', 'OBJECT', 'CONSTRAINT', 'MODIFIER', 'DATA', 'BONE', 'BONE_CONSTRAINT', 'MATERIAL', 'TEXTURE', 'PARTICLES', 'PHYSICS', 'SHADERFX', 'STRIP', 'STRIP_MODIFIER']
    show_properties_tool: bool
    show_properties_scene: bool
    show_properties_render: bool
    show_properties_output: bool
    show_properties_view_layer: bool
    show_properties_world: bool
    show_properties_collection: bool
    show_properties_object: bool
    show_properties_constraints: bool
    show_properties_modifiers: bool
    show_properties_data: bool
    show_properties_bone: bool
    show_properties_bone_constraints: bool
    show_properties_material: bool
    show_properties_texture: bool
    show_properties_particles: bool
    show_properties_physics: bool
    show_properties_effects: bool
    show_properties_strip: bool
    show_properties_strip_modifier: bool
    pin_id: Annotated[Optional['ID'], "is_animatable=False"]
    use_pin_id: bool
    """Use the pinned context"""
    @property
    def tab_search_results(self) -> list[bool]:
        """Whether or not each visible tab has a search result"""
        ...
    search_filter: Annotated[str, "is_animatable=False"]
    """Live search filtering string"""
    outliner_sync: Literal['ALWAYS', 'NEVER', 'AUTO']
    """Change to the corresponding tab when outliner data icons are clicked"""