# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .Space import Space
from .ID import ID
class SpaceProperties(Space):
    type: str
    show_locked_time: bool
    show_region_header: bool
    context: str
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
    pin_id: 'ID'
    use_pin_id: bool
    tab_search_results: list[bool]
    search_filter: str
    outliner_sync: str