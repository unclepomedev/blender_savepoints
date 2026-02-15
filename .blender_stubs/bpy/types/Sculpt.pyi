# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Sculpt.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Paint import Paint
from .AssetWeakReference import AssetWeakReference
from .Brush import Brush
from .CurveMapping import CurveMapping
from .Object import Object
from .Palette import Palette
from .UnifiedPaintSettings import UnifiedPaintSettings

class Sculpt(Paint):

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
    lock_x: Annotated[bool, "is_animatable=False"]
    """Disallow changes to the X axis of vertices"""
    lock_y: Annotated[bool, "is_animatable=False"]
    """Disallow changes to the Y axis of vertices"""
    lock_z: Annotated[bool, "is_animatable=False"]
    """Disallow changes to the Z axis of vertices"""
    use_deform_only: Annotated[bool, "is_animatable=False"]
    """Use only deformation modifiers (temporary disable all constructive modifiers except multi-resolution)"""
    detail_size: Annotated[float, "subtype='PIXEL'", "step=0.10000000149011612", "precision=2", "is_animatable=False"]
    """Maximum edge length for dynamic topology sculpting (in pixels)"""
    detail_percent: Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=2", "is_animatable=False"]
    """Maximum edge length for dynamic topology sculpting (in brush percentage)"""
    constant_detail_resolution: Annotated[float, "step=10.0", "precision=2", "is_animatable=False"]
    """Maximum edge length for dynamic topology sculpting (as divisor of Blender unit - higher value means smaller edge length)"""
    use_automasking_topology: Annotated[bool, "is_animatable=False"]
    """Affect only vertices connected to the active vertex under the brush"""
    use_automasking_face_sets: Annotated[bool, "is_animatable=False"]
    """Affect only vertices that share Face Sets with the active vertex"""
    use_automasking_boundary_edges: Annotated[bool, "is_animatable=False"]
    """Do not affect non manifold boundary edges"""
    use_automasking_boundary_face_sets: Annotated[bool, "is_animatable=False"]
    """Do not affect vertices that belong to a Face Set boundary"""
    use_automasking_cavity: Annotated[bool, "is_animatable=False"]
    """Do not affect vertices on peaks, based on the surface curvature"""
    use_automasking_cavity_inverted: Annotated[bool, "is_animatable=False"]
    """Do not affect vertices within crevices, based on the surface curvature"""
    use_automasking_custom_cavity_curve: Annotated[bool, "is_animatable=False"]
    """Use custom curve"""
    automasking_boundary_edges_propagation_steps: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Distance where boundary edge automasking is going to protect vertices from the fully masked edge"""
    automasking_cavity_factor: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """The contrast of the cavity mask"""
    automasking_cavity_blur_steps: Annotated[int, "step=1", "is_animatable=False"]
    """The number of times the cavity mask is blurred"""
    @property
    def automasking_cavity_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for the sensitivity"""
        ...
    @property
    def automasking_cavity_curve_op(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for the sensitivity"""
        ...
    use_automasking_start_normal: Annotated[bool, "is_animatable=False"]
    """Affect only vertices with a similar normal to where the stroke starts"""
    use_automasking_view_normal: Annotated[bool, "is_animatable=False"]
    """Affect only vertices with a normal that faces the viewer"""
    use_automasking_view_occlusion: Annotated[bool, "is_animatable=False"]
    """Only affect vertices that are not occluded by other faces (slower performance)"""
    automasking_start_normal_limit: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """The range of angles that will be affected"""
    automasking_start_normal_falloff: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Extend the angular range with a falloff gradient"""
    automasking_view_normal_limit: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """The range of angles that will be affected"""
    automasking_view_normal_falloff: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Extend the angular range with a falloff gradient"""
    symmetrize_direction: Annotated[Literal['NEGATIVE_X', 'POSITIVE_X', 'NEGATIVE_Y', 'POSITIVE_Y', 'NEGATIVE_Z', 'POSITIVE_Z'], "is_animatable=False"]
    """Source and destination for symmetrize operator"""
    detail_refine_method: Annotated[Literal['SUBDIVIDE', 'COLLAPSE', 'SUBDIVIDE_COLLAPSE'], "is_animatable=False"]
    """In dynamic-topology mode, how to add or remove mesh detail"""
    detail_type_method: Annotated[Literal['RELATIVE', 'CONSTANT', 'BRUSH', 'MANUAL'], "is_animatable=False"]
    """In dynamic-topology mode, how mesh detail size is calculated"""
    gravity: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """Amount of gravity after each dab"""
    transform_mode: Annotated[Literal['ALL_VERTICES', 'RADIUS_ELASTIC'], "is_animatable=False"]
    """How the transformation is going to be applied to the target"""
    gravity_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Object whose Z axis defines orientation of gravity"""