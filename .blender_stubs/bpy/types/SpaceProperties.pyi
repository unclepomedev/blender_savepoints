# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceProperties.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space
from .ID import ID

class SpaceProperties(Space):

    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    @property
    def show_locked_time(self) -> bool:
        """Synchronize the visible timeline range with other time-based editors"""
        ...
    @show_locked_time.setter
    def show_locked_time(self, value: bool):
        ...
    @property
    def show_region_header(self) -> bool:

        ...
    @show_region_header.setter
    def show_region_header(self, value: bool):
        ...
    @property
    def context(self) -> Literal['TOOL', 'SCENE', 'RENDER', 'OUTPUT', 'VIEW_LAYER', 'WORLD', 'COLLECTION', 'OBJECT', 'CONSTRAINT', 'MODIFIER', 'DATA', 'BONE', 'BONE_CONSTRAINT', 'MATERIAL', 'TEXTURE', 'PARTICLES', 'PHYSICS', 'SHADERFX', 'STRIP', 'STRIP_MODIFIER']:

        ...
    @context.setter
    def context(self, value: Literal['TOOL', 'SCENE', 'RENDER', 'OUTPUT', 'VIEW_LAYER', 'WORLD', 'COLLECTION', 'OBJECT', 'CONSTRAINT', 'MODIFIER', 'DATA', 'BONE', 'BONE_CONSTRAINT', 'MATERIAL', 'TEXTURE', 'PARTICLES', 'PHYSICS', 'SHADERFX', 'STRIP', 'STRIP_MODIFIER']):
        ...
    @property
    def show_properties_tool(self) -> bool:

        ...
    @show_properties_tool.setter
    def show_properties_tool(self, value: bool):
        ...
    @property
    def show_properties_scene(self) -> bool:

        ...
    @show_properties_scene.setter
    def show_properties_scene(self, value: bool):
        ...
    @property
    def show_properties_render(self) -> bool:

        ...
    @show_properties_render.setter
    def show_properties_render(self, value: bool):
        ...
    @property
    def show_properties_output(self) -> bool:

        ...
    @show_properties_output.setter
    def show_properties_output(self, value: bool):
        ...
    @property
    def show_properties_view_layer(self) -> bool:

        ...
    @show_properties_view_layer.setter
    def show_properties_view_layer(self, value: bool):
        ...
    @property
    def show_properties_world(self) -> bool:

        ...
    @show_properties_world.setter
    def show_properties_world(self, value: bool):
        ...
    @property
    def show_properties_collection(self) -> bool:

        ...
    @show_properties_collection.setter
    def show_properties_collection(self, value: bool):
        ...
    @property
    def show_properties_object(self) -> bool:

        ...
    @show_properties_object.setter
    def show_properties_object(self, value: bool):
        ...
    @property
    def show_properties_constraints(self) -> bool:

        ...
    @show_properties_constraints.setter
    def show_properties_constraints(self, value: bool):
        ...
    @property
    def show_properties_modifiers(self) -> bool:

        ...
    @show_properties_modifiers.setter
    def show_properties_modifiers(self, value: bool):
        ...
    @property
    def show_properties_data(self) -> bool:

        ...
    @show_properties_data.setter
    def show_properties_data(self, value: bool):
        ...
    @property
    def show_properties_bone(self) -> bool:

        ...
    @show_properties_bone.setter
    def show_properties_bone(self, value: bool):
        ...
    @property
    def show_properties_bone_constraints(self) -> bool:

        ...
    @show_properties_bone_constraints.setter
    def show_properties_bone_constraints(self, value: bool):
        ...
    @property
    def show_properties_material(self) -> bool:

        ...
    @show_properties_material.setter
    def show_properties_material(self, value: bool):
        ...
    @property
    def show_properties_texture(self) -> bool:

        ...
    @show_properties_texture.setter
    def show_properties_texture(self, value: bool):
        ...
    @property
    def show_properties_particles(self) -> bool:

        ...
    @show_properties_particles.setter
    def show_properties_particles(self, value: bool):
        ...
    @property
    def show_properties_physics(self) -> bool:

        ...
    @show_properties_physics.setter
    def show_properties_physics(self, value: bool):
        ...
    @property
    def show_properties_effects(self) -> bool:

        ...
    @show_properties_effects.setter
    def show_properties_effects(self, value: bool):
        ...
    @property
    def show_properties_strip(self) -> bool:

        ...
    @show_properties_strip.setter
    def show_properties_strip(self, value: bool):
        ...
    @property
    def show_properties_strip_modifier(self) -> bool:

        ...
    @show_properties_strip_modifier.setter
    def show_properties_strip_modifier(self, value: bool):
        ...
    @property
    def pin_id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:

        ...
    @pin_id.setter
    def pin_id(self, value: Annotated[Optional['ID'], "is_animatable=False"]):
        ...
    @property
    def use_pin_id(self) -> bool:
        """Use the pinned context"""
        ...
    @use_pin_id.setter
    def use_pin_id(self, value: bool):
        ...
    @property
    def tab_search_results(self) -> list[bool]:
        """Whether or not each visible tab has a search result"""
        ...
    @property
    def search_filter(self) -> Annotated[str, "is_animatable=False"]:
        """Live search filtering string"""
        ...
    @search_filter.setter
    def search_filter(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def outliner_sync(self) -> Literal['ALWAYS', 'NEVER', 'AUTO']:
        """Change to the corresponding tab when outliner data icons are clicked"""
        ...
    @outliner_sync.setter
    def outliner_sync(self, value: Literal['ALWAYS', 'NEVER', 'AUTO']):
        ...