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
from .ThemeSpaceGeneric import ThemeSpaceGeneric
class ThemeNodeEditor(bpy_struct):
    space: 'ThemeSpaceGeneric'
    grid: list[float]
    node_outline: list[float]
    node_selected: list[float]
    node_active: list[float]
    wire: list[float]
    wire_inner: list[float]
    wire_select: list[float]
    node_backdrop: list[float]
    converter_node: list[float]
    color_node: list[float]
    group_node: list[float]
    group_socket_node: list[float]
    frame_node: list[float]
    matte_node: list[float]
    distor_node: list[float]
    noodle_curving: int
    grid_levels: int
    dash_alpha: float
    input_node: list[float]
    output_node: list[float]
    filter_node: list[float]
    vector_node: list[float]
    texture_node: list[float]
    shader_node: list[float]
    script_node: list[float]
    geometry_node: list[float]
    attribute_node: list[float]
    simulation_zone: list[float]
    repeat_zone: list[float]
    foreach_geometry_element_zone: list[float]
    closure_zone: list[float]