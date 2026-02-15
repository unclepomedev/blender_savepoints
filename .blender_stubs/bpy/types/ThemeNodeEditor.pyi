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
from .ThemeSpaceGeneric import ThemeSpaceGeneric
class ThemeNodeEditor(bpy_struct):
    @property
    def space(self) -> Annotated['ThemeSpaceGeneric', "is_animatable=False"]:
        """Settings for space"""
        ...
    grid: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    node_outline: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    node_selected: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    node_active: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    wire: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    wire_inner: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    wire_select: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    node_backdrop: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    converter_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    color_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    group_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    group_socket_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    frame_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    matte_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    distor_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    noodle_curving: Annotated[int, "step=1"]
    """Curving of the noodle"""
    grid_levels: Annotated[int, "step=1"]
    """Number of subdivisions for the dot grid displayed in the background"""
    dash_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Opacity for the dashed lines in wires"""
    input_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    output_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    filter_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    vector_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    texture_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    shader_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    script_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    geometry_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    attribute_node: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    simulation_zone: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    repeat_zone: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    foreach_geometry_element_zone: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    closure_zone: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]