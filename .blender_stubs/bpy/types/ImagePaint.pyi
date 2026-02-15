# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

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
    use_occlude: Annotated[bool, "is_animatable=False"]
    """Only paint onto the faces directly under the brush (slower)"""
    use_backface_culling: Annotated[bool, "is_animatable=False"]
    """Ignore faces pointing away from the view (faster)"""
    use_normal_falloff: Annotated[bool, "is_animatable=False"]
    """Paint most on faces pointing towards the view"""
    use_stencil_layer: Annotated[bool, "is_animatable=False"]
    """Set the mask layer from the UV map buttons"""
    invert_stencil: Annotated[bool, "is_animatable=False"]
    """Invert the stencil layer"""
    stencil_image: Annotated[Optional['Image'], "is_animatable=False"]
    """Image used as stencil"""
    canvas: Annotated[Optional['Image'], "is_animatable=False"]
    """Image used as canvas"""
    clone_image: Annotated[Optional['Image'], "is_animatable=False"]
    """Image used as clone source"""
    stencil_color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]
    """Stencil color in the viewport"""
    dither: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Amount of dithering when painting on byte images"""
    use_clone_layer: Annotated[bool, "is_animatable=False"]
    """Use another UV map as clone source, otherwise use the 3D cursor as the source"""
    seam_bleed: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Extend paint beyond the faces' UVs to reduce seams (in pixels, slower)"""
    normal_angle: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Paint most on faces pointing towards the view according to this angle"""
    screen_grab_size: Annotated[list[int], "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Size to capture the image for re-projecting"""
    mode: Annotated[Literal['MATERIAL', 'IMAGE'], "is_animatable=False"]
    """Mode of operation for projection painting"""
    interpolation: Annotated[Literal['LINEAR', 'CLOSEST'], "is_animatable=False"]
    """Texture filtering type"""
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
    clone_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Opacity of clone image display"""
    clone_offset: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3", "is_animatable=False"]
    def detect_data(self, *args, **kwargs) -> Any: ...