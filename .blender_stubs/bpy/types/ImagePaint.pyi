# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ImagePaint.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Paint import Paint
from .AssetWeakReference import AssetWeakReference
from .Brush import Brush
from .CurveMapping import CurveMapping
from .Image import Image
from .Palette import Palette
from .UnifiedPaintSettings import UnifiedPaintSettings

class ImagePaint(Paint):

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
    @property
    def use_occlude(self) -> Annotated[bool, "is_animatable=False"]:
        """Only paint onto the faces directly under the brush (slower)"""
        ...
    @use_occlude.setter
    def use_occlude(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_backface_culling(self) -> Annotated[bool, "is_animatable=False"]:
        """Ignore faces pointing away from the view (faster)"""
        ...
    @use_backface_culling.setter
    def use_backface_culling(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_normal_falloff(self) -> Annotated[bool, "is_animatable=False"]:
        """Paint most on faces pointing towards the view"""
        ...
    @use_normal_falloff.setter
    def use_normal_falloff(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_stencil_layer(self) -> Annotated[bool, "is_animatable=False"]:
        """Set the mask layer from the UV map buttons"""
        ...
    @use_stencil_layer.setter
    def use_stencil_layer(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def invert_stencil(self) -> Annotated[bool, "is_animatable=False"]:
        """Invert the stencil layer"""
        ...
    @invert_stencil.setter
    def invert_stencil(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def stencil_image(self) -> Annotated[Optional['Image'], "is_animatable=False"]:
        """Image used as stencil"""
        ...
    @stencil_image.setter
    def stencil_image(self, value: Annotated[Optional['Image'], "is_animatable=False"]) -> None:
        ...
    @property
    def canvas(self) -> Annotated[Optional['Image'], "is_animatable=False"]:
        """Image used as canvas"""
        ...
    @canvas.setter
    def canvas(self, value: Annotated[Optional['Image'], "is_animatable=False"]) -> None:
        ...
    @property
    def clone_image(self) -> Annotated[Optional['Image'], "is_animatable=False"]:
        """Image used as clone source"""
        ...
    @clone_image.setter
    def clone_image(self, value: Annotated[Optional['Image'], "is_animatable=False"]) -> None:
        ...
    @property
    def stencil_color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Stencil color in the viewport"""
        ...
    @stencil_color.setter
    def stencil_color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def dither(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Amount of dithering when painting on byte images"""
        ...
    @dither.setter
    def dither(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def use_clone_layer(self) -> Annotated[bool, "is_animatable=False"]:
        """Use another UV map as clone source, otherwise use the 3D cursor as the source"""
        ...
    @use_clone_layer.setter
    def use_clone_layer(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def seam_bleed(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Extend paint beyond the faces' UVs to reduce seams (in pixels, slower)"""
        ...
    @seam_bleed.setter
    def seam_bleed(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def normal_angle(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Paint most on faces pointing towards the view according to this angle"""
        ...
    @normal_angle.setter
    def normal_angle(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def screen_grab_size(self) -> Annotated[list[int], "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Size to capture the image for re-projecting"""
        ...
    @screen_grab_size.setter
    def screen_grab_size(self, value: Annotated[list[int], "subtype='PIXEL'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def mode(self) -> Annotated[Literal['MATERIAL', 'IMAGE'], "is_animatable=False"]:
        """Mode of operation for projection painting"""
        ...
    @mode.setter
    def mode(self, value: Annotated[Literal['MATERIAL', 'IMAGE'], "is_animatable=False"]) -> None:
        ...
    @property
    def interpolation(self) -> Annotated[Literal['LINEAR', 'CLOSEST'], "is_animatable=False"]:
        """Texture filtering type"""
        ...
    @interpolation.setter
    def interpolation(self, value: Annotated[Literal['LINEAR', 'CLOSEST'], "is_animatable=False"]) -> None:
        ...
    @property
    def missing_uvs(self) -> Annotated[bool, "is_animatable=False"]:
        """A UV layer is missing on the mesh"""
        ...
    @property
    def missing_materials(self) -> Annotated[bool, "is_animatable=False"]:
        """The mesh is missing materials"""
        ...
    @property
    def missing_stencil(self) -> Annotated[bool, "is_animatable=False"]:
        """Image Painting does not have a stencil"""
        ...
    @property
    def missing_texture(self) -> Annotated[bool, "is_animatable=False"]:
        """Image Painting does not have a texture to paint on"""
        ...
    @property
    def clone_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Opacity of clone image display"""
        ...
    @clone_alpha.setter
    def clone_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def clone_offset(self) -> Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]:

        ...
    @clone_offset.setter
    def clone_offset(self, value: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    def detect_data(self, *args, **kwargs) -> Any: ...