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
from .ThemeSpaceGeneric import ThemeSpaceGeneric
class ThemeNodeEditor(bpy_struct):
    space: 'ThemeSpaceGeneric'
    grid: float
    node_outline: float
    node_selected: float
    node_active: float
    wire: float
    wire_inner: float
    wire_select: float
    node_backdrop: float
    converter_node: float
    color_node: float
    group_node: float
    group_socket_node: float
    frame_node: float
    matte_node: float
    distor_node: float
    noodle_curving: int
    grid_levels: int
    dash_alpha: float
    input_node: float
    output_node: float
    filter_node: float
    vector_node: float
    texture_node: float
    shader_node: float
    script_node: float
    geometry_node: float
    attribute_node: float
    simulation_zone: float
    repeat_zone: float
    foreach_geometry_element_zone: float
    closure_zone: float