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
from .RaytraceEEVEE import RaytraceEEVEE
class SceneEEVEE(bpy_struct):
    gi_diffuse_bounces: Annotated[int, "step=1", "is_animatable=False"]
    """Number of times the light is reinjected inside light grids, 0 disable indirect diffuse light"""
    gi_cubemap_resolution: Annotated[Literal['128', '256', '512', '1024', '2048', '4096'], "is_animatable=False"]
    """Size of every cubemaps"""
    gi_visibility_resolution: Annotated[Literal['8', '16', '32', '64'], "is_animatable=False"]
    """Size of the shadow map applied to each irradiance sample"""
    gi_glossy_clamp: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Clamp pixel intensity to reduce noise inside glossy reflections from reflection cubemaps (0 to disable)"""
    gi_irradiance_pool_size: Annotated[Literal['16', '32', '64', '128', '256', '512', '1024'], "is_animatable=False"]
    """Size of the irradiance pool, a bigger pool size allows for more irradiance grid in the scene but might not fit into GPU memory and decrease performance"""
    taa_samples: Annotated[int, "step=1"]
    """Number of samples, unlimited if 0"""
    taa_render_samples: Annotated[int, "step=1"]
    """Number of samples per pixel for rendering"""
    use_taa_reprojection: bool
    """Denoise image using temporal reprojection (can leave some ghosting)"""
    ray_tracing_method: Annotated[Literal['PROBE', 'SCREEN'], "is_animatable=False"]
    """Select the tracing method used to find scene-ray intersections"""
    use_shadow_jitter_viewport: Annotated[bool, "is_animatable=False"]
    """Enable jittered shadows on the viewport. (Jittered shadows are always enabled for final renders)."""
    clamp_surface_direct: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """If non-zero, the maximum value for lights contribution on a surface. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by light objects."""
    clamp_surface_indirect: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """If non-zero, the maximum value for indirect lighting on surface. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by ray-tracing and light-probes."""
    clamp_volume_direct: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """If non-zero, the maximum value for lights contribution in volumes. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by light objects."""
    clamp_volume_indirect: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """If non-zero, the maximum value for indirect lighting in volumes. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by light-probes."""
    volumetric_start: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]
    """Start distance of the volumetric effect"""
    volumetric_end: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]
    """End distance of the volumetric effect"""
    volumetric_tile_size: Annotated[Literal['1', '2', '4', '8', '16'], "is_animatable=False"]
    """Control the quality of the volumetric effects. Higher resolution uses more memory."""
    volumetric_samples: Annotated[int, "step=1", "is_animatable=False"]
    """Number of steps to compute volumetric effects. Higher step count increase VRAM usage and quality."""
    volumetric_sample_distribution: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Distribute more samples closer to the camera"""
    volumetric_ray_depth: Annotated[int, "step=1", "is_animatable=False"]
    """Maximum surface intersection count used by the accurate volume intersection method. Will create artifact if it is exceeded. Higher count increases VRAM usage."""
    volumetric_light_clamp: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Maximum light contribution, reducing noise"""
    use_volumetric_shadows: Annotated[bool, "is_animatable=False"]
    """Cast shadows from volumetric materials onto volumetric materials (Very expensive)"""
    volumetric_shadow_samples: Annotated[int, "step=1", "is_animatable=False"]
    """Number of samples to compute volumetric shadowing"""
    use_volume_custom_range: Annotated[bool, "is_animatable=False"]
    """Enable custom start and end clip distances for volume computation"""
    use_fast_gi: Annotated[bool, "is_animatable=False"]
    """Use faster global illumination technique for high roughness surfaces"""
    fast_gi_thickness_near: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]
    """Geometric thickness of the surfaces when computing fast GI and ambient occlusion. Reduces light leaking and missing contact occlusion."""
    fast_gi_thickness_far: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Angular thickness of the surfaces when computing fast GI and ambient occlusion. Reduces energy loss and missing occlusion of far geometry."""
    fast_gi_quality: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Precision of the fast GI ray marching"""
    fast_gi_step_count: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Amount of screen sample per GI ray"""
    fast_gi_ray_count: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Amount of GI ray to trace for each pixel"""
    fast_gi_method: Annotated[Literal['AMBIENT_OCCLUSION_ONLY', 'GLOBAL_ILLUMINATION'], "is_animatable=False"]
    """Fast GI approximation method"""
    fast_gi_distance: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]
    """If non-zero, the maximum distance at which other surfaces will contribute to the fast GI approximation"""
    fast_gi_bias: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2", "is_animatable=False"]
    """Bias the shading normal to reduce self intersection artifacts"""
    fast_gi_resolution: Annotated[Literal['1', '2', '4', '8', '16'], "is_animatable=False"]
    """Control the quality of the fast GI lighting. Higher resolution uses more memory."""
    bokeh_max_size: Annotated[float, "subtype='PIXEL'", "step=100.0", "precision=1", "is_animatable=False"]
    """Max size of the bokeh shape for the depth of field (lower is faster)"""
    bokeh_threshold: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=2", "is_animatable=False"]
    """Brightness threshold for using sprite base depth of field"""
    bokeh_neighbor_max: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=2", "is_animatable=False"]
    """Maximum brightness to consider when rejecting bokeh sprites based on neighborhood (lower is faster)"""
    use_bokeh_jittered: Annotated[bool, "is_animatable=False"]
    """Jitter camera position to create accurate blurring using render samples (only for final render)"""
    bokeh_overblur: Annotated[float, "subtype='PERCENTAGE'", "step=1.0", "precision=1", "is_animatable=False"]
    """Apply blur to each jittered sample to reduce under-sampling artifacts"""
    motion_blur_depth_scale: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]
    """Lower values will reduce background bleeding onto foreground elements"""
    motion_blur_max: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Maximum blur distance a pixel can spread over"""
    motion_blur_steps: Annotated[int, "step=1", "is_animatable=False"]
    """Controls accuracy of motion blur, more steps means longer render time"""
    use_shadows: Annotated[bool, "is_animatable=False"]
    """Enable shadow casting from lights"""
    shadow_pool_size: Annotated[Literal['16', '32', '64', '128', '256', '512', '1024'], "is_animatable=False"]
    """Size of the shadow pool, a bigger pool size allows for more shadows in the scene but might not fit into GPU memory"""
    shadow_ray_count: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Amount of shadow ray to trace for each light"""
    shadow_step_count: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Amount of shadow map sample per shadow ray"""
    light_threshold: Annotated[float, "subtype='UNSIGNED'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]
    """Minimum light intensity for a light to contribute to the lighting"""
    use_overscan: Annotated[bool, "is_animatable=False"]
    """Internally render past the image border to avoid screen-space effects disappearing"""
    overscan_size: Annotated[float, "subtype='PERCENTAGE'", "step=1.0", "precision=2", "is_animatable=False"]
    """Percentage of render size to add as overscan to the internal render buffers"""
    @property
    def ray_tracing_options(self) -> Annotated[Optional['RaytraceEEVEE'], "is_animatable=False"]:
        """EEVEE settings for tracing reflections"""
        ...
    use_raytracing: Annotated[bool, "is_animatable=False"]
    """Enable the ray-tracing module"""
    shadow_resolution_scale: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Resolution percentage of shadow maps"""