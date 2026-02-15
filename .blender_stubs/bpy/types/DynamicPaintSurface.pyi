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
from .Collection import Collection
from .EffectorWeights import EffectorWeights
from .PointCache import PointCache
from .Texture import Texture
class DynamicPaintSurface(bpy_struct):
    surface_format: Annotated[Literal['VERTEX', 'IMAGE'], "is_animatable=False"]
    """Surface Format"""
    surface_type: Annotated[Literal['PAINT'], "is_animatable=False"]
    """Surface Type"""
    is_active: bool
    """Toggle whether surface is processed or ignored"""
    name: Annotated[str, "is_animatable=False"]
    """Surface name"""
    brush_collection: Annotated[Optional['Collection'], "is_animatable=False"]
    """Only use brush objects from this collection"""
    use_dissolve: bool
    """Enable to make surface changes disappear over time"""
    dissolve_speed: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=5"]
    """Approximately in how many frames should dissolve happen"""
    use_drying: bool
    """Enable to make surface wetness dry over time"""
    dry_speed: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=5"]
    """Approximately in how many frames should drying happen"""
    image_resolution: Annotated[int, "step=1", "is_animatable=False"]
    """Output image resolution"""
    uv_layer: Annotated[str, "is_animatable=False"]
    """UV map name"""
    frame_start: Annotated[int, "step=1", "is_animatable=False"]
    """Simulation start frame"""
    frame_end: Annotated[int, "step=1", "is_animatable=False"]
    """Simulation end frame"""
    frame_substeps: Annotated[int, "step=1"]
    """Do extra frames between scene frames to ensure smooth motion"""
    use_antialiasing: Annotated[bool, "is_animatable=False"]
    """Use 5× multisampling to smooth paint edges"""
    brush_influence_scale: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]
    """Adjust influence brush objects have on this surface"""
    brush_radius_scale: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]
    """Adjust radius of proximity brushes or particles for this surface"""
    init_color_type: Annotated[Literal['NONE', 'COLOR', 'TEXTURE', 'VERTEX_COLOR'], "is_animatable=False"]
    init_color: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3", "is_animatable=False"]
    """Initial color of the surface"""
    init_texture: Annotated[Optional['Texture'], "is_animatable=False"]
    init_layername: Annotated[str, "is_animatable=False"]
    effect_ui: Annotated[Literal['SPREAD', 'DRIP', 'SHRINK'], "is_animatable=False"]
    use_dry_log: bool
    """Use logarithmic drying (makes high values to dry faster than low values)"""
    use_dissolve_log: bool
    """Use logarithmic dissolve (makes high values to fade faster than low values)"""
    use_spread: Annotated[bool, "is_animatable=False"]
    """Process spread effect (spread wet paint around surface)"""
    spread_speed: Annotated[float, "step=1.0", "precision=2"]
    """How fast spread effect moves on the canvas surface"""
    color_dry_threshold: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]
    """The wetness level when colors start to shift to the background"""
    color_spread_speed: Annotated[float, "step=1.0", "precision=2"]
    """How fast colors get mixed within wet paint"""
    use_drip: Annotated[bool, "is_animatable=False"]
    """Process drip effect (drip wet paint to gravity direction)"""
    use_shrink: Annotated[bool, "is_animatable=False"]
    """Process shrink effect (shrink paint areas)"""
    shrink_speed: Annotated[float, "step=1.0", "precision=2"]
    """How fast shrink effect moves on the canvas surface"""
    @property
    def effector_weights(self) -> Annotated[Optional['EffectorWeights'], "is_animatable=False"]:
        ...
    drip_velocity: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """How much surface velocity affects dripping"""
    drip_acceleration: Annotated[float, "step=0.10000000149011612", "precision=3"]
    """How much surface acceleration affects dripping"""
    use_premultiply: Annotated[bool, "is_animatable=False"]
    """Multiply color by alpha (recommended for Blender input)"""
    image_output_path: Annotated[str, "subtype='DIR_PATH'", "is_animatable=False"]
    """Directory to save the textures"""
    output_name_a: Annotated[str, "is_animatable=False"]
    """Name used to save output from this surface"""
    use_output_a: bool
    """Save this output layer"""
    output_name_b: Annotated[str, "is_animatable=False"]
    """Name used to save output from this surface"""
    use_output_b: bool
    """Save this output layer"""
    depth_clamp: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]
    """Maximum level of depth intersection in object space (use 0.0 to disable)"""
    displace_factor: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]
    """Strength of displace when applied to the mesh"""
    image_fileformat: Annotated[Literal['PNG', 'OPENEXR'], "is_animatable=False"]
    displace_type: Annotated[Literal['DISPLACE', 'DEPTH'], "is_animatable=False"]
    use_incremental_displace: Annotated[bool, "is_animatable=False"]
    """New displace is added cumulatively on top of existing"""
    wave_damping: Annotated[float, "step=1.0", "precision=2"]
    """Wave damping factor"""
    wave_speed: Annotated[float, "step=1.0", "precision=2"]
    """Wave propagation speed"""
    wave_timescale: Annotated[float, "step=1.0", "precision=2"]
    """Wave time scaling factor"""
    wave_spring: Annotated[float, "step=1.0", "precision=2"]
    """Spring force that pulls water level back to zero"""
    wave_smoothness: Annotated[float, "step=1.0", "precision=2"]
    """Limit maximum steepness of wave slope between simulation points (use higher values for smoother waves at expense of reduced detail)"""
    use_wave_open_border: bool
    """Pass waves through mesh edges"""
    @property
    def point_cache(self) -> Annotated['PointCache', "is_animatable=False"]:
        ...
    @property
    def is_cache_user(self) -> Annotated[bool, "is_animatable=False"]:
        ...
    def output_exists(self, *args, **kwargs) -> Any: ...