# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.DynamicPaintSurface.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Collection import Collection
from .EffectorWeights import EffectorWeights
from .PointCache import PointCache
from .Texture import Texture

class DynamicPaintSurface(bpy_struct):

    @property
    def surface_format(self) -> Annotated[Literal['VERTEX', 'IMAGE'], "is_animatable=False"]:
        """Surface Format"""
        ...
    @surface_format.setter
    def surface_format(self, value: Annotated[Literal['VERTEX', 'IMAGE'], "is_animatable=False"]) -> None:
        ...
    @property
    def surface_type(self) -> Annotated[Literal['PAINT'], "is_animatable=False"]:
        """Surface Type"""
        ...
    @surface_type.setter
    def surface_type(self, value: Annotated[Literal['PAINT'], "is_animatable=False"]) -> None:
        ...
    @property
    def is_active(self) -> bool:
        """Toggle whether surface is processed or ignored"""
        ...
    @is_active.setter
    def is_active(self, value: bool) -> None:
        ...
    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Surface name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def brush_collection(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Only use brush objects from this collection"""
        ...
    @brush_collection.setter
    def brush_collection(self, value: Annotated[Optional['Collection'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_dissolve(self) -> bool:
        """Enable to make surface changes disappear over time"""
        ...
    @use_dissolve.setter
    def use_dissolve(self, value: bool) -> None:
        ...
    @property
    def dissolve_speed(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=5"]:
        """Approximately in how many frames should dissolve happen"""
        ...
    @dissolve_speed.setter
    def dissolve_speed(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=5"]) -> None:
        ...
    @property
    def use_drying(self) -> bool:
        """Enable to make surface wetness dry over time"""
        ...
    @use_drying.setter
    def use_drying(self, value: bool) -> None:
        ...
    @property
    def dry_speed(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=5"]:
        """Approximately in how many frames should drying happen"""
        ...
    @dry_speed.setter
    def dry_speed(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=5"]) -> None:
        ...
    @property
    def image_resolution(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Output image resolution"""
        ...
    @image_resolution.setter
    def image_resolution(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def uv_layer(self) -> Annotated[str, "is_animatable=False"]:
        """UV map name"""
        ...
    @uv_layer.setter
    def uv_layer(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def frame_start(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Simulation start frame"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def frame_end(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Simulation end frame"""
        ...
    @frame_end.setter
    def frame_end(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def frame_substeps(self) -> Annotated[int, "step=1"]:
        """Do extra frames between scene frames to ensure smooth motion"""
        ...
    @frame_substeps.setter
    def frame_substeps(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_antialiasing(self) -> Annotated[bool, "is_animatable=False"]:
        """Use 5× multisampling to smooth paint edges"""
        ...
    @use_antialiasing.setter
    def use_antialiasing(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def brush_influence_scale(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]:
        """Adjust influence brush objects have on this surface"""
        ...
    @brush_influence_scale.setter
    def brush_influence_scale(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def brush_radius_scale(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]:
        """Adjust radius of proximity brushes or particles for this surface"""
        ...
    @brush_radius_scale.setter
    def brush_radius_scale(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def init_color_type(self) -> Annotated[Literal['NONE', 'COLOR', 'TEXTURE', 'VERTEX_COLOR'], "is_animatable=False"]:

        ...
    @init_color_type.setter
    def init_color_type(self, value: Annotated[Literal['NONE', 'COLOR', 'TEXTURE', 'VERTEX_COLOR'], "is_animatable=False"]) -> None:
        ...
    @property
    def init_color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Initial color of the surface"""
        ...
    @init_color.setter
    def init_color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def init_texture(self) -> Annotated[Optional['Texture'], "is_animatable=False"]:

        ...
    @init_texture.setter
    def init_texture(self, value: Annotated[Optional['Texture'], "is_animatable=False"]) -> None:
        ...
    @property
    def init_layername(self) -> Annotated[str, "is_animatable=False"]:

        ...
    @init_layername.setter
    def init_layername(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def effect_ui(self) -> Annotated[Literal['SPREAD', 'DRIP', 'SHRINK'], "is_animatable=False"]:

        ...
    @effect_ui.setter
    def effect_ui(self, value: Annotated[Literal['SPREAD', 'DRIP', 'SHRINK'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_dry_log(self) -> bool:
        """Use logarithmic drying (makes high values to dry faster than low values)"""
        ...
    @use_dry_log.setter
    def use_dry_log(self, value: bool) -> None:
        ...
    @property
    def use_dissolve_log(self) -> bool:
        """Use logarithmic dissolve (makes high values to fade faster than low values)"""
        ...
    @use_dissolve_log.setter
    def use_dissolve_log(self, value: bool) -> None:
        ...
    @property
    def use_spread(self) -> Annotated[bool, "is_animatable=False"]:
        """Process spread effect (spread wet paint around surface)"""
        ...
    @use_spread.setter
    def use_spread(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def spread_speed(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """How fast spread effect moves on the canvas surface"""
        ...
    @spread_speed.setter
    def spread_speed(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def color_dry_threshold(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]:
        """The wetness level when colors start to shift to the background"""
        ...
    @color_dry_threshold.setter
    def color_dry_threshold(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def color_spread_speed(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """How fast colors get mixed within wet paint"""
        ...
    @color_spread_speed.setter
    def color_spread_speed(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def use_drip(self) -> Annotated[bool, "is_animatable=False"]:
        """Process drip effect (drip wet paint to gravity direction)"""
        ...
    @use_drip.setter
    def use_drip(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_shrink(self) -> Annotated[bool, "is_animatable=False"]:
        """Process shrink effect (shrink paint areas)"""
        ...
    @use_shrink.setter
    def use_shrink(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def shrink_speed(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """How fast shrink effect moves on the canvas surface"""
        ...
    @shrink_speed.setter
    def shrink_speed(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def effector_weights(self) -> Annotated[Optional['EffectorWeights'], "is_animatable=False"]:

        ...
    @property
    def drip_velocity(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """How much surface velocity affects dripping"""
        ...
    @drip_velocity.setter
    def drip_velocity(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def drip_acceleration(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """How much surface acceleration affects dripping"""
        ...
    @drip_acceleration.setter
    def drip_acceleration(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def use_premultiply(self) -> Annotated[bool, "is_animatable=False"]:
        """Multiply color by alpha (recommended for Blender input)"""
        ...
    @use_premultiply.setter
    def use_premultiply(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def image_output_path(self) -> Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]:
        """Directory to save the textures"""
        ...
    @image_output_path.setter
    def image_output_path(self, value: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def output_name_a(self) -> Annotated[str, "is_animatable=False"]:
        """Name used to save output from this surface"""
        ...
    @output_name_a.setter
    def output_name_a(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def use_output_a(self) -> bool:
        """Save this output layer"""
        ...
    @use_output_a.setter
    def use_output_a(self, value: bool) -> None:
        ...
    @property
    def output_name_b(self) -> Annotated[str, "is_animatable=False"]:
        """Name used to save output from this surface"""
        ...
    @output_name_b.setter
    def output_name_b(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def use_output_b(self) -> bool:
        """Save this output layer"""
        ...
    @use_output_b.setter
    def use_output_b(self, value: bool) -> None:
        ...
    @property
    def depth_clamp(self) -> Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]:
        """Maximum level of depth intersection in object space (use 0.0 to disable)"""
        ...
    @depth_clamp.setter
    def depth_clamp(self, value: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]) -> None:
        ...
    @property
    def displace_factor(self) -> Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]:
        """Strength of displace when applied to the mesh"""
        ...
    @displace_factor.setter
    def displace_factor(self, value: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]) -> None:
        ...
    @property
    def image_fileformat(self) -> Annotated[Literal['PNG', 'OPENEXR'], "is_animatable=False"]:

        ...
    @image_fileformat.setter
    def image_fileformat(self, value: Annotated[Literal['PNG', 'OPENEXR'], "is_animatable=False"]) -> None:
        ...
    @property
    def displace_type(self) -> Annotated[Literal['DISPLACE', 'DEPTH'], "is_animatable=False"]:

        ...
    @displace_type.setter
    def displace_type(self, value: Annotated[Literal['DISPLACE', 'DEPTH'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_incremental_displace(self) -> Annotated[bool, "is_animatable=False"]:
        """New displace is added cumulatively on top of existing"""
        ...
    @use_incremental_displace.setter
    def use_incremental_displace(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def wave_damping(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Wave damping factor"""
        ...
    @wave_damping.setter
    def wave_damping(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def wave_speed(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Wave propagation speed"""
        ...
    @wave_speed.setter
    def wave_speed(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def wave_timescale(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Wave time scaling factor"""
        ...
    @wave_timescale.setter
    def wave_timescale(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def wave_spring(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Spring force that pulls water level back to zero"""
        ...
    @wave_spring.setter
    def wave_spring(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def wave_smoothness(self) -> Annotated[float, "step=1.0", "precision=2"]:
        """Limit maximum steepness of wave slope between simulation points (use higher values for smoother waves at expense of reduced detail)"""
        ...
    @wave_smoothness.setter
    def wave_smoothness(self, value: Annotated[float, "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def use_wave_open_border(self) -> bool:
        """Pass waves through mesh edges"""
        ...
    @use_wave_open_border.setter
    def use_wave_open_border(self, value: bool) -> None:
        ...
    @property
    def point_cache(self) -> Annotated['PointCache', "is_animatable=False"]:

        ...
    @property
    def is_cache_user(self) -> Annotated[bool, "is_animatable=False"]:

        ...
    def output_exists(self, *args, **kwargs) -> Any: ...