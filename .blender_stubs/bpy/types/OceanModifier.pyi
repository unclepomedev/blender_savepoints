# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.OceanModifier.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Modifier import Modifier

class OceanModifier(Modifier):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Modifier name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Literal['GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY', 'DATA_TRANSFER', 'MESH_CACHE', 'MESH_SEQUENCE_CACHE', 'NORMAL_EDIT', 'WEIGHTED_NORMAL', 'UV_PROJECT', 'UV_WARP', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_PROXIMITY', 'GREASE_PENCIL_COLOR', 'GREASE_PENCIL_TINT', 'GREASE_PENCIL_OPACITY', 'GREASE_PENCIL_VERTEX_WEIGHT_ANGLE', 'GREASE_PENCIL_TIME', 'GREASE_PENCIL_TEXTURE', 'ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 'EDGE_SPLIT', 'NODES', 'MASK', 'MIRROR', 'MESH_TO_VOLUME', 'MULTIRES', 'REMESH', 'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'VOLUME_TO_MESH', 'WELD', 'WIREFRAME', 'GREASE_PENCIL_ARRAY', 'GREASE_PENCIL_BUILD', 'GREASE_PENCIL_LENGTH', 'LINEART', 'GREASE_PENCIL_MIRROR', 'GREASE_PENCIL_MULTIPLY', 'GREASE_PENCIL_SIMPLIFY', 'GREASE_PENCIL_SUBDIV', 'GREASE_PENCIL_ENVELOPE', 'GREASE_PENCIL_OUTLINE', 'ARMATURE', 'CAST', 'CURVE', 'DISPLACE', 'HOOK', 'LAPLACIANDEFORM', 'LATTICE', 'MESH_DEFORM', 'SHRINKWRAP', 'SIMPLE_DEFORM', 'SMOOTH', 'CORRECTIVE_SMOOTH', 'LAPLACIANSMOOTH', 'SURFACE_DEFORM', 'WARP', 'WAVE', 'VOLUME_DISPLACE', 'GREASE_PENCIL_HOOK', 'GREASE_PENCIL_NOISE', 'GREASE_PENCIL_OFFSET', 'GREASE_PENCIL_SMOOTH', 'GREASE_PENCIL_THICKNESS', 'GREASE_PENCIL_LATTICE', 'GREASE_PENCIL_DASH', 'GREASE_PENCIL_ARMATURE', 'GREASE_PENCIL_SHRINKWRAP', 'CLOTH', 'COLLISION', 'DYNAMIC_PAINT', 'EXPLODE', 'FLUID', 'OCEAN', 'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM', 'SOFT_BODY', 'SURFACE']:

        ...
    @property
    def show_viewport(self) -> bool:
        """Display modifier in viewport"""
        ...
    @show_viewport.setter
    def show_viewport(self, value: bool):
        ...
    @property
    def show_render(self) -> bool:
        """Use modifier during render"""
        ...
    @show_render.setter
    def show_render(self, value: bool):
        ...
    @property
    def show_in_editmode(self) -> bool:
        """Display modifier in Edit mode"""
        ...
    @show_in_editmode.setter
    def show_in_editmode(self, value: bool):
        ...
    @property
    def show_on_cage(self) -> bool:
        """Adjust edit cage to modifier result"""
        ...
    @show_on_cage.setter
    def show_on_cage(self, value: bool):
        ...
    @property
    def show_expanded(self) -> bool:
        """Set modifier expanded in the user interface"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool):
        ...
    @property
    def is_active(self) -> Annotated[bool, "is_animatable=False"]:
        """The active modifier in the list"""
        ...
    @is_active.setter
    def is_active(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_pin_to_last(self) -> Annotated[bool, "is_animatable=False"]:
        """Keep the modifier at the end of the list"""
        ...
    @use_pin_to_last.setter
    def use_pin_to_last(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def is_override_data(self) -> bool:
        """In a local override object, whether this modifier comes from the linked reference object, or is local to the override"""
        ...
    @property
    def use_apply_on_spline(self) -> bool:
        """Apply this and all preceding deformation modifiers on splines' points rather than on filled curve/surface"""
        ...
    @use_apply_on_spline.setter
    def use_apply_on_spline(self, value: bool):
        ...
    @property
    def execution_time(self) -> Annotated[float, "subtype='TIME_ABSOLUTE'", "unit='TIME_ABSOLUTE'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Time in seconds that the modifier took to evaluate. This is only set on evaluated objects. If multiple modifiers run in parallel, execution time is not a reliable metric."""
        ...
    @property
    def persistent_uid(self) -> Annotated[int, "step=1"]:
        """Uniquely identifies the modifier within the modifier stack that it is part of"""
        ...
    @property
    def geometry_mode(self) -> Literal['GENERATE', 'DISPLACE']:
        """Method of modifying geometry"""
        ...
    @geometry_mode.setter
    def geometry_mode(self, value: Literal['GENERATE', 'DISPLACE']):
        ...
    @property
    def size(self) -> Annotated[float, "subtype='UNSIGNED'", "step=1.0", "precision=-1"]:
        """Surface scale factor (does not affect the height of the waves)"""
        ...
    @size.setter
    def size(self, value: Annotated[float, "subtype='UNSIGNED'", "step=1.0", "precision=-1"]):
        ...
    @property
    def repeat_x(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Repetitions of the generated surface in X"""
        ...
    @repeat_x.setter
    def repeat_x(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def repeat_y(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Repetitions of the generated surface in Y"""
        ...
    @repeat_y.setter
    def repeat_y(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def use_normals(self) -> Annotated[bool, "is_animatable=False"]:
        """Output normals for bump mapping - disabling can speed up performance if it's not needed"""
        ...
    @use_normals.setter
    def use_normals(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_foam(self) -> Annotated[bool, "is_animatable=False"]:
        """Generate foam mask as a vertex color channel"""
        ...
    @use_foam.setter
    def use_foam(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_spray(self) -> Annotated[bool, "is_animatable=False"]:
        """Generate map of spray direction as a vertex color channel"""
        ...
    @use_spray.setter
    def use_spray(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def invert_spray(self) -> Annotated[bool, "is_animatable=False"]:
        """Invert the spray direction map"""
        ...
    @invert_spray.setter
    def invert_spray(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def spray_layer_name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the vertex color layer used for the spray direction map"""
        ...
    @spray_layer_name.setter
    def spray_layer_name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def resolution(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Resolution of the generated surface for rendering and baking"""
        ...
    @resolution.setter
    def resolution(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def viewport_resolution(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Viewport resolution of the generated surface"""
        ...
    @viewport_resolution.setter
    def viewport_resolution(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def spatial_size(self) -> Annotated[int, "step=2", "is_animatable=False"]:
        """Size of the simulation domain (in meters), and of the generated geometry (in BU)"""
        ...
    @spatial_size.setter
    def spatial_size(self, value: Annotated[int, "step=2", "is_animatable=False"]):
        ...
    @property
    def wind_velocity(self) -> Annotated[float, "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Wind speed"""
        ...
    @wind_velocity.setter
    def wind_velocity(self, value: Annotated[float, "subtype='VELOCITY'", "unit='VELOCITY'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def damping(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Damp reflected waves going in opposite direction to the wind"""
        ...
    @damping.setter
    def damping(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def wave_scale_min(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Shortest allowed wavelength"""
        ...
    @wave_scale_min.setter
    def wave_scale_min(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def wave_alignment(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3", "is_animatable=False"]:
        """How much the waves are aligned to each other"""
        ...
    @wave_alignment.setter
    def wave_alignment(self, value: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def wave_direction(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Main direction of the waves when they are (partially) aligned"""
        ...
    @wave_direction.setter
    def wave_direction(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def wave_scale(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]:
        """Scale of the displacement effect"""
        ...
    @wave_scale.setter
    def wave_scale(self, value: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3"]):
        ...
    @property
    def depth(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=-1", "is_animatable=False"]:
        """Depth of the solid ground below the water surface"""
        ...
    @depth.setter
    def depth(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=-1", "is_animatable=False"]):
        ...
    @property
    def foam_coverage(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of generated foam"""
        ...
    @foam_coverage.setter
    def foam_coverage(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def bake_foam_fade(self) -> Annotated[float, "subtype='UNSIGNED'", "step=1.0", "precision=-1", "is_animatable=False"]:
        """How much foam accumulates over time (baked ocean only)"""
        ...
    @bake_foam_fade.setter
    def bake_foam_fade(self, value: Annotated[float, "subtype='UNSIGNED'", "step=1.0", "precision=-1", "is_animatable=False"]):
        ...
    @property
    def foam_layer_name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the vertex color layer used for foam"""
        ...
    @foam_layer_name.setter
    def foam_layer_name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def choppiness(self) -> Annotated[float, "subtype='UNSIGNED'", "step=3.0", "precision=-1"]:
        """Choppiness of the wave's crest (adds some horizontal component to the displacement)"""
        ...
    @choppiness.setter
    def choppiness(self, value: Annotated[float, "subtype='UNSIGNED'", "step=3.0", "precision=-1"]):
        ...
    @property
    def time(self) -> Annotated[float, "subtype='UNSIGNED'", "step=1.0", "precision=-1"]:
        """Current time of the simulation"""
        ...
    @time.setter
    def time(self, value: Annotated[float, "subtype='UNSIGNED'", "step=1.0", "precision=-1"]):
        ...
    @property
    def spectrum(self) -> Annotated[Literal['PHILLIPS', 'PIERSON_MOSKOWITZ', 'JONSWAP', 'TEXEL_MARSEN_ARSLOE'], "is_animatable=False"]:
        """Spectrum to use"""
        ...
    @spectrum.setter
    def spectrum(self, value: Annotated[Literal['PHILLIPS', 'PIERSON_MOSKOWITZ', 'JONSWAP', 'TEXEL_MARSEN_ARSLOE'], "is_animatable=False"]):
        ...
    @property
    def fetch_jonswap(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3", "is_animatable=False"]:
        """This is the distance from a lee shore, called the fetch, or the distance over which the wind blows with constant velocity. Used by 'JONSWAP' and 'TMA' models."""
        ...
    @fetch_jonswap.setter
    def fetch_jonswap(self, value: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def sharpen_peak_jonswap(self) -> Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Peak sharpening for 'JONSWAP' and 'TMA' models"""
        ...
    @sharpen_peak_jonswap.setter
    def sharpen_peak_jonswap(self, value: Annotated[float, "subtype='UNSIGNED'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def random_seed(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Seed of the random generator"""
        ...
    @random_seed.setter
    def random_seed(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def frame_start(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """Start frame of the ocean baking"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]):
        ...
    @property
    def frame_end(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """End frame of the ocean baking"""
        ...
    @frame_end.setter
    def frame_end(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]):
        ...
    @property
    def is_cached(self) -> bool:
        """Whether the ocean is using cached data or simulating"""
        ...
    @property
    def filepath(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """Path to a folder to store external baked images"""
        ...
    @filepath.setter
    def filepath(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]):
        ...