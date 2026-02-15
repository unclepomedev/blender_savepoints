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
class SpaceUVEditor(bpy_struct):
    edge_display_type: Literal['OUTLINE', 'DASH', 'BLACK', 'WHITE']
    """Display style for UV edges"""
    show_stretch: bool
    """Display faces colored according to the difference in shape between UVs and their 3D coordinates (blue for low distortion, red for high distortion)"""
    display_stretch_type: Literal['ANGLE', 'AREA']
    """Type of stretch to display"""
    show_modified_edges: bool
    """Display edges after modifiers are applied"""
    show_metadata: bool
    """Display metadata properties of the image"""
    show_uv: bool
    """Display overlay of UV layer"""
    show_pixel_coords: bool
    """Display UV coordinates in pixels rather than from 0.0 to 1.0"""
    show_faces: bool
    """Display faces over the image"""
    tile_grid_shape: Annotated[list[int], "subtype='XYZ'", "step=1"]
    """How many tiles will be shown in the background"""
    show_grid_over_image: bool
    """Show the grid over the image"""
    grid_shape_source: Literal['DYNAMIC', 'FIXED', 'PIXEL']
    """Specify source for the grid shape"""
    custom_grid_subdivisions: Annotated[list[int], "subtype='XYZ'", "step=1"]
    """Number of grid units in UV space that make one UV Unit"""
    uv_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Opacity of UV overlays"""
    uv_face_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Opacity of faces in UV overlays"""
    stretch_opacity: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Opacity of the UV Stretch overlay"""
    pixel_round_mode: Literal['DISABLED', 'CORNER', 'CENTER']
    """Round UVs to pixels while editing"""
    lock_bounds: bool
    """Constraint to stay within the image bounds while editing"""
    use_live_unwrap: bool
    """Continuously unwrap the selected UV island while transforming pinned vertices"""