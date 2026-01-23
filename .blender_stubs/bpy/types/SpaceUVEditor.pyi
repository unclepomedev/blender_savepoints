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
class SpaceUVEditor(bpy_struct):
    edge_display_type: str
    show_stretch: bool
    display_stretch_type: str
    show_modified_edges: bool
    show_metadata: bool
    show_uv: bool
    show_pixel_coords: bool
    show_faces: bool
    tile_grid_shape: list[int]
    show_grid_over_image: bool
    grid_shape_source: str
    custom_grid_subdivisions: list[int]
    uv_opacity: float
    uv_face_opacity: float
    uv_edge_opacity: float
    stretch_opacity: float
    pixel_round_mode: str
    lock_bounds: bool
    use_live_unwrap: bool