# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceUVEditor.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class SpaceUVEditor(bpy_struct):

    @property
    def edge_display_type(self) -> Literal['OUTLINE', 'DASH', 'BLACK', 'WHITE']:
        """Display style for UV edges"""
        ...
    @edge_display_type.setter
    def edge_display_type(self, value: Literal['OUTLINE', 'DASH', 'BLACK', 'WHITE']):
        ...
    @property
    def show_stretch(self) -> bool:
        """Display faces colored according to the difference in shape between UVs and their 3D coordinates (blue for low distortion, red for high distortion)"""
        ...
    @show_stretch.setter
    def show_stretch(self, value: bool):
        ...
    @property
    def display_stretch_type(self) -> Literal['ANGLE', 'AREA']:
        """Type of stretch to display"""
        ...
    @display_stretch_type.setter
    def display_stretch_type(self, value: Literal['ANGLE', 'AREA']):
        ...
    @property
    def show_modified_edges(self) -> bool:
        """Display edges after modifiers are applied"""
        ...
    @show_modified_edges.setter
    def show_modified_edges(self, value: bool):
        ...
    @property
    def show_metadata(self) -> bool:
        """Display metadata properties of the image"""
        ...
    @show_metadata.setter
    def show_metadata(self, value: bool):
        ...
    @property
    def show_uv(self) -> bool:
        """Display overlay of UV layer"""
        ...
    @show_uv.setter
    def show_uv(self, value: bool):
        ...
    @property
    def show_pixel_coords(self) -> bool:
        """Display UV coordinates in pixels rather than from 0.0 to 1.0"""
        ...
    @show_pixel_coords.setter
    def show_pixel_coords(self, value: bool):
        ...
    @property
    def show_faces(self) -> bool:
        """Display faces over the image"""
        ...
    @show_faces.setter
    def show_faces(self, value: bool):
        ...
    @property
    def tile_grid_shape(self) -> Annotated[list[int], "subtype='XYZ'", "step=1"]:
        """How many tiles will be shown in the background"""
        ...
    @tile_grid_shape.setter
    def tile_grid_shape(self, value: Annotated[list[int], "subtype='XYZ'", "step=1"]):
        ...
    @property
    def show_grid_over_image(self) -> bool:
        """Show the grid over the image"""
        ...
    @show_grid_over_image.setter
    def show_grid_over_image(self, value: bool):
        ...
    @property
    def grid_shape_source(self) -> Literal['DYNAMIC', 'FIXED', 'PIXEL']:
        """Specify source for the grid shape"""
        ...
    @grid_shape_source.setter
    def grid_shape_source(self, value: Literal['DYNAMIC', 'FIXED', 'PIXEL']):
        ...
    @property
    def custom_grid_subdivisions(self) -> Annotated[list[int], "subtype='XYZ'", "step=1"]:
        """Number of grid units in UV space that make one UV Unit"""
        ...
    @custom_grid_subdivisions.setter
    def custom_grid_subdivisions(self, value: Annotated[list[int], "subtype='XYZ'", "step=1"]):
        ...
    @property
    def uv_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Opacity of UV overlays"""
        ...
    @uv_opacity.setter
    def uv_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def uv_face_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Opacity of faces in UV overlays"""
        ...
    @uv_face_opacity.setter
    def uv_face_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def stretch_opacity(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Opacity of the UV Stretch overlay"""
        ...
    @stretch_opacity.setter
    def stretch_opacity(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def pixel_round_mode(self) -> Literal['DISABLED', 'CORNER', 'CENTER']:
        """Round UVs to pixels while editing"""
        ...
    @pixel_round_mode.setter
    def pixel_round_mode(self, value: Literal['DISABLED', 'CORNER', 'CENTER']):
        ...
    @property
    def lock_bounds(self) -> bool:
        """Constraint to stay within the image bounds while editing"""
        ...
    @lock_bounds.setter
    def lock_bounds(self, value: bool):
        ...
    @property
    def use_live_unwrap(self) -> bool:
        """Continuously unwrap the selected UV island while transforming pinned vertices"""
        ...
    @use_live_unwrap.setter
    def use_live_unwrap(self, value: bool):
        ...