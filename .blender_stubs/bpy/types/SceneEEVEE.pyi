# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .RaytraceEEVEE import RaytraceEEVEE
class SceneEEVEE(bpy_struct):
    gi_diffuse_bounces: int
    gi_cubemap_resolution: str
    gi_visibility_resolution: str
    gi_glossy_clamp: float
    gi_irradiance_pool_size: str
    taa_samples: int
    taa_render_samples: int
    use_taa_reprojection: bool
    ray_tracing_method: str
    use_shadow_jitter_viewport: bool
    clamp_surface_direct: float
    clamp_surface_indirect: float
    clamp_volume_direct: float
    clamp_volume_indirect: float
    volumetric_start: float
    volumetric_end: float
    volumetric_tile_size: str
    volumetric_samples: int
    volumetric_sample_distribution: float
    volumetric_ray_depth: int
    volumetric_light_clamp: float
    use_volumetric_shadows: bool
    volumetric_shadow_samples: int
    use_volume_custom_range: bool
    use_fast_gi: bool
    fast_gi_thickness_near: float
    fast_gi_thickness_far: float
    fast_gi_quality: float
    fast_gi_step_count: int
    fast_gi_ray_count: int
    fast_gi_method: str
    fast_gi_distance: float
    fast_gi_bias: float
    fast_gi_resolution: str
    bokeh_max_size: float
    bokeh_threshold: float
    bokeh_neighbor_max: float
    use_bokeh_jittered: bool
    bokeh_overblur: float
    motion_blur_depth_scale: float
    motion_blur_max: int
    motion_blur_steps: int
    use_shadows: bool
    shadow_pool_size: str
    shadow_ray_count: int
    shadow_step_count: int
    light_threshold: float
    use_overscan: bool
    overscan_size: float
    ray_tracing_options: 'RaytraceEEVEE'
    use_raytracing: bool
    shadow_resolution_scale: float