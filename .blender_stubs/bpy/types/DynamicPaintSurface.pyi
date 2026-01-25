# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .Collection import Collection
from .EffectorWeights import EffectorWeights
from .PointCache import PointCache
from .Texture import Texture
class DynamicPaintSurface(bpy_struct):
    surface_format: str
    surface_type: str
    is_active: bool
    name: str
    brush_collection: 'Collection'
    use_dissolve: bool
    dissolve_speed: int
    use_drying: bool
    dry_speed: int
    image_resolution: int
    uv_layer: str
    frame_start: int
    frame_end: int
    frame_substeps: int
    use_antialiasing: bool
    brush_influence_scale: float
    brush_radius_scale: float
    init_color_type: str
    init_color: float
    init_texture: 'Texture'
    init_layername: str
    effect_ui: str
    use_dry_log: bool
    use_dissolve_log: bool
    use_spread: bool
    spread_speed: float
    color_dry_threshold: float
    color_spread_speed: float
    use_drip: bool
    use_shrink: bool
    shrink_speed: float
    effector_weights: 'EffectorWeights'
    drip_velocity: float
    drip_acceleration: float
    use_premultiply: bool
    image_output_path: str
    output_name_a: str
    use_output_a: bool
    output_name_b: str
    use_output_b: bool
    depth_clamp: float
    displace_factor: float
    image_fileformat: str
    displace_type: str
    use_incremental_displace: bool
    wave_damping: float
    wave_speed: float
    wave_timescale: float
    wave_spring: float
    wave_smoothness: float
    use_wave_open_border: bool
    point_cache: 'PointCache'
    is_cache_user: bool
    def output_exists(self, *args, **kwargs) -> Any: ...