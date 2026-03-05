# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.CurvesSculpt.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Paint import Paint
from .AssetWeakReference import AssetWeakReference
from .Brush import Brush
from .CurveMapping import CurveMapping
from .Palette import Palette
from .UnifiedPaintSettings import UnifiedPaintSettings

class CurvesSculpt(Paint):

    @property
    def brush(self) -> Annotated[Optional['Brush'], "is_animatable=False"]:
        """Active brush"""
        ...
    @property
    def brush_asset_reference(self) -> Annotated[Optional['AssetWeakReference'], "is_animatable=False"]:
        """A weak reference to the matching brush asset, used e.g. to restore the last used brush on file load"""
        ...
    @property
    def eraser_brush(self) -> Annotated[Optional['Brush'], "is_animatable=False"]:
        """Default eraser brush for quickly alternating with the main brush"""
        ...
    @eraser_brush.setter
    def eraser_brush(self, value: Annotated[Optional['Brush'], "is_animatable=False"]) -> None:
        ...
    @property
    def eraser_brush_asset_reference(self) -> Annotated[Optional['AssetWeakReference'], "is_animatable=False"]:
        """A weak reference to the matching brush asset, used e.g. to restore the last used brush on file load"""
        ...
    @property
    def palette(self) -> Annotated[Optional['Palette'], "is_animatable=False"]:
        """Active Palette"""
        ...
    @palette.setter
    def palette(self, value: Annotated[Optional['Palette'], "is_animatable=False"]) -> None:
        ...
    @property
    def show_brush(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @show_brush.setter
    def show_brush(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_brush_on_surface(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @show_brush_on_surface.setter
    def show_brush_on_surface(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_low_resolution(self) -> Annotated[bool, "is_animatable=False"]:
        """For multires, show low resolution while navigating the view"""
        ...
    @show_low_resolution.setter
    def show_low_resolution(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_sculpt_delay_updates(self) -> Annotated[bool, "is_animatable=False"]:
        """Update the geometry when it enters the view, providing faster view navigation"""
        ...
    @use_sculpt_delay_updates.setter
    def use_sculpt_delay_updates(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_symmetry_x(self) -> Annotated[bool, "is_animatable=False"]:
        """Mirror brush across the X axis"""
        ...
    @use_symmetry_x.setter
    def use_symmetry_x(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_symmetry_y(self) -> Annotated[bool, "is_animatable=False"]:
        """Mirror brush across the Y axis"""
        ...
    @use_symmetry_y.setter
    def use_symmetry_y(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_symmetry_z(self) -> Annotated[bool, "is_animatable=False"]:
        """Mirror brush across the Z axis"""
        ...
    @use_symmetry_z.setter
    def use_symmetry_z(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_symmetry_feather(self) -> Annotated[bool, "is_animatable=False"]:
        """Reduce the strength of the brush where it overlaps symmetrical daubs"""
        ...
    @use_symmetry_feather.setter
    def use_symmetry_feather(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def cavity_curve(self) -> Annotated['CurveMapping', "is_animatable=False"]:
        """Editable cavity curve"""
        ...
    @property
    def use_cavity(self) -> Annotated[bool, "is_animatable=False"]:
        """Mask painting according to mesh geometry cavity"""
        ...
    @use_cavity.setter
    def use_cavity(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def tile_offset(self) -> Annotated[list[float], "subtype='XYZ_LENGTH'", "unit='LENGTH'", "step=100.0", "precision=2", "is_animatable=False"]:
        """Stride at which tiled strokes are copied"""
        ...
    @tile_offset.setter
    def tile_offset(self, value: Annotated[list[float], "subtype='XYZ_LENGTH'", "unit='LENGTH'", "step=100.0", "precision=2", "is_animatable=False"]) -> None:
        ...
    @property
    def tile_x(self) -> Annotated[bool, "is_animatable=False"]:
        """Tile along X axis"""
        ...
    @tile_x.setter
    def tile_x(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def tile_y(self) -> Annotated[bool, "is_animatable=False"]:
        """Tile along Y axis"""
        ...
    @tile_y.setter
    def tile_y(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def tile_z(self) -> Annotated[bool, "is_animatable=False"]:
        """Tile along Z axis"""
        ...
    @tile_z.setter
    def tile_z(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_strength_curve(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @show_strength_curve.setter
    def show_strength_curve(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_size_curve(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @show_size_curve.setter
    def show_size_curve(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_jitter_curve(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @show_jitter_curve.setter
    def show_jitter_curve(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def unified_paint_settings(self) -> Annotated['UnifiedPaintSettings', "is_animatable=False"]:

        ...