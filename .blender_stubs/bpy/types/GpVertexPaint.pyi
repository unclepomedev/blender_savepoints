# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.GpVertexPaint.html
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

class GpVertexPaint(Paint):

    @property
    def brush(self) -> Annotated[Optional['Brush'], "is_animatable=False"]:
        """Active brush"""
        ...
    @property
    def brush_asset_reference(self) -> Annotated[Optional['AssetWeakReference'], "is_animatable=False"]:
        """A weak reference to the matching brush asset, used e.g. to restore the last used brush on file load"""
        ...
    eraser_brush: Annotated[Optional['Brush'], "is_animatable=False"]
    """Default eraser brush for quickly alternating with the main brush"""
    @property
    def eraser_brush_asset_reference(self) -> Annotated[Optional['AssetWeakReference'], "is_animatable=False"]:
        """A weak reference to the matching brush asset, used e.g. to restore the last used brush on file load"""
        ...
    palette: Annotated[Optional['Palette'], "is_animatable=False"]
    """Active Palette"""
    show_brush: Annotated[bool, "is_animatable=False"]

    show_brush_on_surface: Annotated[bool, "is_animatable=False"]

    show_low_resolution: Annotated[bool, "is_animatable=False"]
    """For multires, show low resolution while navigating the view"""
    use_sculpt_delay_updates: Annotated[bool, "is_animatable=False"]
    """Update the geometry when it enters the view, providing faster view navigation"""
    use_symmetry_x: Annotated[bool, "is_animatable=False"]
    """Mirror brush across the X axis"""
    use_symmetry_y: Annotated[bool, "is_animatable=False"]
    """Mirror brush across the Y axis"""
    use_symmetry_z: Annotated[bool, "is_animatable=False"]
    """Mirror brush across the Z axis"""
    use_symmetry_feather: Annotated[bool, "is_animatable=False"]
    """Reduce the strength of the brush where it overlaps symmetrical daubs"""
    @property
    def cavity_curve(self) -> Annotated['CurveMapping', "is_animatable=False"]:
        """Editable cavity curve"""
        ...
    use_cavity: Annotated[bool, "is_animatable=False"]
    """Mask painting according to mesh geometry cavity"""
    tile_offset: Annotated[list[float], "subtype='XYZ_LENGTH'", "unit='LENGTH'", "step=100.0", "precision=2", "is_animatable=False"]
    """Stride at which tiled strokes are copied"""
    tile_x: Annotated[bool, "is_animatable=False"]
    """Tile along X axis"""
    tile_y: Annotated[bool, "is_animatable=False"]
    """Tile along Y axis"""
    tile_z: Annotated[bool, "is_animatable=False"]
    """Tile along Z axis"""
    show_strength_curve: Annotated[bool, "is_animatable=False"]

    show_size_curve: Annotated[bool, "is_animatable=False"]

    show_jitter_curve: Annotated[bool, "is_animatable=False"]

    @property
    def unified_paint_settings(self) -> Annotated['UnifiedPaintSettings', "is_animatable=False"]:

        ...