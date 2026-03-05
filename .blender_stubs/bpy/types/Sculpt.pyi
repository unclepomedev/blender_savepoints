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
    @property
    def eraser_brush(self) -> Annotated[Optional['Brush'], "is_animatable=False"]:
        """Default eraser brush for quickly alternating with the main brush"""
        ...
    @eraser_brush.setter
    def eraser_brush(self, value: Annotated[Optional['Brush'], "is_animatable=False"]):
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
    def palette(self, value: Annotated[Optional['Palette'], "is_animatable=False"]):
        ...
    @property
    def show_brush(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @show_brush.setter
    def show_brush(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_brush_on_surface(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @show_brush_on_surface.setter
    def show_brush_on_surface(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_low_resolution(self) -> Annotated[bool, "is_animatable=False"]:
        """For multires, show low resolution while navigating the view"""
        ...
    @show_low_resolution.setter
    def show_low_resolution(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_sculpt_delay_updates(self) -> Annotated[bool, "is_animatable=False"]:
        """Update the geometry when it enters the view, providing faster view navigation"""
        ...
    @use_sculpt_delay_updates.setter
    def use_sculpt_delay_updates(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_symmetry_x(self) -> Annotated[bool, "is_animatable=False"]:
        """Mirror brush across the X axis"""
        ...
    @use_symmetry_x.setter
    def use_symmetry_x(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_symmetry_y(self) -> Annotated[bool, "is_animatable=False"]:
        """Mirror brush across the Y axis"""
        ...
    @use_symmetry_y.setter
    def use_symmetry_y(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_symmetry_z(self) -> Annotated[bool, "is_animatable=False"]:
        """Mirror brush across the Z axis"""
        ...
    @use_symmetry_z.setter
    def use_symmetry_z(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_symmetry_feather(self) -> Annotated[bool, "is_animatable=False"]:
        """Reduce the strength of the brush where it overlaps symmetrical daubs"""
        ...
    @use_symmetry_feather.setter
    def use_symmetry_feather(self, value: Annotated[bool, "is_animatable=False"]):
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
    def use_cavity(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def tile_offset(self) -> Annotated[list[float], "subtype='XYZ_LENGTH'", "unit='LENGTH'", "step=100.0", "precision=2", "is_animatable=False"]:
        """Stride at which tiled strokes are copied"""
        ...
    @tile_offset.setter
    def tile_offset(self, value: Annotated[list[float], "subtype='XYZ_LENGTH'", "unit='LENGTH'", "step=100.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def tile_x(self) -> Annotated[bool, "is_animatable=False"]:
        """Tile along X axis"""
        ...
    @tile_x.setter
    def tile_x(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def tile_y(self) -> Annotated[bool, "is_animatable=False"]:
        """Tile along Y axis"""
        ...
    @tile_y.setter
    def tile_y(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def tile_z(self) -> Annotated[bool, "is_animatable=False"]:
        """Tile along Z axis"""
        ...
    @tile_z.setter
    def tile_z(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_strength_curve(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @show_strength_curve.setter
    def show_strength_curve(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_size_curve(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @show_size_curve.setter
    def show_size_curve(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_jitter_curve(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    @show_jitter_curve.setter
    def show_jitter_curve(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def unified_paint_settings(self) -> Annotated['UnifiedPaintSettings', "is_animatable=False"]:

        ...
    @property
    def lock_x(self) -> Annotated[bool, "is_animatable=False"]:
        """Disallow changes to the X axis of vertices"""
        ...
    @lock_x.setter
    def lock_x(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def lock_y(self) -> Annotated[bool, "is_animatable=False"]:
        """Disallow changes to the Y axis of vertices"""
        ...
    @lock_y.setter
    def lock_y(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def lock_z(self) -> Annotated[bool, "is_animatable=False"]:
        """Disallow changes to the Z axis of vertices"""
        ...
    @lock_z.setter
    def lock_z(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_deform_only(self) -> Annotated[bool, "is_animatable=False"]:
        """Use only deformation modifiers (temporary disable all constructive modifiers except multi-resolution)"""
        ...
    @use_deform_only.setter
    def use_deform_only(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def detail_size(self) -> Annotated[float, "subtype='PIXEL'", "step=0.10000000149011612", "precision=2", "is_animatable=False"]:
        """Maximum edge length for dynamic topology sculpting (in pixels)"""
        ...
    @detail_size.setter
    def detail_size(self, value: Annotated[float, "subtype='PIXEL'", "step=0.10000000149011612", "precision=2", "is_animatable=False"]):
        ...
    @property
    def detail_percent(self) -> Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=2", "is_animatable=False"]:
        """Maximum edge length for dynamic topology sculpting (in brush percentage)"""
        ...
    @detail_percent.setter
    def detail_percent(self, value: Annotated[float, "subtype='PERCENTAGE'", "step=10.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def constant_detail_resolution(self) -> Annotated[float, "step=10.0", "precision=2", "is_animatable=False"]:
        """Maximum edge length for dynamic topology sculpting (as divisor of Blender unit - higher value means smaller edge length)"""
        ...
    @constant_detail_resolution.setter
    def constant_detail_resolution(self, value: Annotated[float, "step=10.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def use_automasking_topology(self) -> Annotated[bool, "is_animatable=False"]:
        """Affect only vertices connected to the active vertex under the brush"""
        ...
    @use_automasking_topology.setter
    def use_automasking_topology(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_automasking_face_sets(self) -> Annotated[bool, "is_animatable=False"]:
        """Affect only vertices that share Face Sets with the active vertex"""
        ...
    @use_automasking_face_sets.setter
    def use_automasking_face_sets(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_automasking_boundary_edges(self) -> Annotated[bool, "is_animatable=False"]:
        """Do not affect non manifold boundary edges"""
        ...
    @use_automasking_boundary_edges.setter
    def use_automasking_boundary_edges(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_automasking_boundary_face_sets(self) -> Annotated[bool, "is_animatable=False"]:
        """Do not affect vertices that belong to a Face Set boundary"""
        ...
    @use_automasking_boundary_face_sets.setter
    def use_automasking_boundary_face_sets(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_automasking_cavity(self) -> Annotated[bool, "is_animatable=False"]:
        """Do not affect vertices on peaks, based on the surface curvature"""
        ...
    @use_automasking_cavity.setter
    def use_automasking_cavity(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_automasking_cavity_inverted(self) -> Annotated[bool, "is_animatable=False"]:
        """Do not affect vertices within crevices, based on the surface curvature"""
        ...
    @use_automasking_cavity_inverted.setter
    def use_automasking_cavity_inverted(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_automasking_custom_cavity_curve(self) -> Annotated[bool, "is_animatable=False"]:
        """Use custom curve"""
        ...
    @use_automasking_custom_cavity_curve.setter
    def use_automasking_custom_cavity_curve(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def automasking_boundary_edges_propagation_steps(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Distance where boundary edge automasking is going to protect vertices from the fully masked edge"""
        ...
    @automasking_boundary_edges_propagation_steps.setter
    def automasking_boundary_edges_propagation_steps(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def automasking_cavity_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """The contrast of the cavity mask"""
        ...
    @automasking_cavity_factor.setter
    def automasking_cavity_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]):
        ...
    @property
    def automasking_cavity_blur_steps(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """The number of times the cavity mask is blurred"""
        ...
    @automasking_cavity_blur_steps.setter
    def automasking_cavity_blur_steps(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def automasking_cavity_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for the sensitivity"""
        ...
    @property
    def automasking_cavity_curve_op(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve used for the sensitivity"""
        ...
    @property
    def use_automasking_start_normal(self) -> Annotated[bool, "is_animatable=False"]:
        """Affect only vertices with a similar normal to where the stroke starts"""
        ...
    @use_automasking_start_normal.setter
    def use_automasking_start_normal(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_automasking_view_normal(self) -> Annotated[bool, "is_animatable=False"]:
        """Affect only vertices with a normal that faces the viewer"""
        ...
    @use_automasking_view_normal.setter
    def use_automasking_view_normal(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_automasking_view_occlusion(self) -> Annotated[bool, "is_animatable=False"]:
        """Only affect vertices that are not occluded by other faces (slower performance)"""
        ...
    @use_automasking_view_occlusion.setter
    def use_automasking_view_occlusion(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def automasking_start_normal_limit(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """The range of angles that will be affected"""
        ...
    @automasking_start_normal_limit.setter
    def automasking_start_normal_limit(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def automasking_start_normal_falloff(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Extend the angular range with a falloff gradient"""
        ...
    @automasking_start_normal_falloff.setter
    def automasking_start_normal_falloff(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def automasking_view_normal_limit(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """The range of angles that will be affected"""
        ...
    @automasking_view_normal_limit.setter
    def automasking_view_normal_limit(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def automasking_view_normal_falloff(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Extend the angular range with a falloff gradient"""
        ...
    @automasking_view_normal_falloff.setter
    def automasking_view_normal_falloff(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def symmetrize_direction(self) -> Annotated[Literal['NEGATIVE_X', 'POSITIVE_X', 'NEGATIVE_Y', 'POSITIVE_Y', 'NEGATIVE_Z', 'POSITIVE_Z'], "is_animatable=False"]:
        """Source and destination for symmetrize operator"""
        ...
    @symmetrize_direction.setter
    def symmetrize_direction(self, value: Annotated[Literal['NEGATIVE_X', 'POSITIVE_X', 'NEGATIVE_Y', 'POSITIVE_Y', 'NEGATIVE_Z', 'POSITIVE_Z'], "is_animatable=False"]):
        ...
    @property
    def detail_refine_method(self) -> Annotated[Literal['SUBDIVIDE', 'COLLAPSE', 'SUBDIVIDE_COLLAPSE'], "is_animatable=False"]:
        """In dynamic-topology mode, how to add or remove mesh detail"""
        ...
    @detail_refine_method.setter
    def detail_refine_method(self, value: Annotated[Literal['SUBDIVIDE', 'COLLAPSE', 'SUBDIVIDE_COLLAPSE'], "is_animatable=False"]):
        ...
    @property
    def detail_type_method(self) -> Annotated[Literal['RELATIVE', 'CONSTANT', 'BRUSH', 'MANUAL'], "is_animatable=False"]:
        """In dynamic-topology mode, how mesh detail size is calculated"""
        ...
    @detail_type_method.setter
    def detail_type_method(self, value: Annotated[Literal['RELATIVE', 'CONSTANT', 'BRUSH', 'MANUAL'], "is_animatable=False"]):
        ...
    @property
    def gravity(self) -> Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """Amount of gravity after each dab"""
        ...
    @gravity.setter
    def gravity(self, value: Annotated[float, "subtype='FACTOR'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]):
        ...
    @property
    def transform_mode(self) -> Annotated[Literal['ALL_VERTICES', 'RADIUS_ELASTIC'], "is_animatable=False"]:
        """How the transformation is going to be applied to the target"""
        ...
    @transform_mode.setter
    def transform_mode(self, value: Annotated[Literal['ALL_VERTICES', 'RADIUS_ELASTIC'], "is_animatable=False"]):
        ...
    @property
    def gravity_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object whose Z axis defines orientation of gravity"""
        ...
    @gravity_object.setter
    def gravity_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...