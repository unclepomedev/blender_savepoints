# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SceneEEVEE.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .RaytraceEEVEE import RaytraceEEVEE

class SceneEEVEE(bpy_struct):

    @property
    def gi_diffuse_bounces(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Number of times the light is reinjected inside light grids, 0 disable indirect diffuse light"""
        ...
    @gi_diffuse_bounces.setter
    def gi_diffuse_bounces(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def gi_cubemap_resolution(self) -> Annotated[Literal['128', '256', '512', '1024', '2048', '4096'], "is_animatable=False"]:
        """Size of every cubemaps"""
        ...
    @gi_cubemap_resolution.setter
    def gi_cubemap_resolution(self, value: Annotated[Literal['128', '256', '512', '1024', '2048', '4096'], "is_animatable=False"]):
        ...
    @property
    def gi_visibility_resolution(self) -> Annotated[Literal['8', '16', '32', '64'], "is_animatable=False"]:
        """Size of the shadow map applied to each irradiance sample"""
        ...
    @gi_visibility_resolution.setter
    def gi_visibility_resolution(self, value: Annotated[Literal['8', '16', '32', '64'], "is_animatable=False"]):
        ...
    @property
    def gi_glossy_clamp(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Clamp pixel intensity to reduce noise inside glossy reflections from reflection cubemaps (0 to disable)"""
        ...
    @gi_glossy_clamp.setter
    def gi_glossy_clamp(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def gi_irradiance_pool_size(self) -> Annotated[Literal['16', '32', '64', '128', '256', '512', '1024'], "is_animatable=False"]:
        """Size of the irradiance pool, a bigger pool size allows for more irradiance grid in the scene but might not fit into GPU memory and decrease performance"""
        ...
    @gi_irradiance_pool_size.setter
    def gi_irradiance_pool_size(self, value: Annotated[Literal['16', '32', '64', '128', '256', '512', '1024'], "is_animatable=False"]):
        ...
    @property
    def taa_samples(self) -> Annotated[int, "step=1"]:
        """Number of samples, unlimited if 0"""
        ...
    @taa_samples.setter
    def taa_samples(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def taa_render_samples(self) -> Annotated[int, "step=1"]:
        """Number of samples per pixel for rendering"""
        ...
    @taa_render_samples.setter
    def taa_render_samples(self, value: Annotated[int, "step=1"]):
        ...
    @property
    def use_taa_reprojection(self) -> bool:
        """Denoise image using temporal reprojection (can leave some ghosting)"""
        ...
    @use_taa_reprojection.setter
    def use_taa_reprojection(self, value: bool):
        ...
    @property
    def ray_tracing_method(self) -> Annotated[Literal['PROBE', 'SCREEN'], "is_animatable=False"]:
        """Select the tracing method used to find scene-ray intersections"""
        ...
    @ray_tracing_method.setter
    def ray_tracing_method(self, value: Annotated[Literal['PROBE', 'SCREEN'], "is_animatable=False"]):
        ...
    @property
    def use_shadow_jitter_viewport(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable jittered shadows on the viewport. (Jittered shadows are always enabled for final renders)."""
        ...
    @use_shadow_jitter_viewport.setter
    def use_shadow_jitter_viewport(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def clamp_surface_direct(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """If non-zero, the maximum value for lights contribution on a surface. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by light objects."""
        ...
    @clamp_surface_direct.setter
    def clamp_surface_direct(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def clamp_surface_indirect(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """If non-zero, the maximum value for indirect lighting on surface. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by ray-tracing and light-probes."""
        ...
    @clamp_surface_indirect.setter
    def clamp_surface_indirect(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def clamp_volume_direct(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """If non-zero, the maximum value for lights contribution in volumes. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by light objects."""
        ...
    @clamp_volume_direct.setter
    def clamp_volume_direct(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def clamp_volume_indirect(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """If non-zero, the maximum value for indirect lighting in volumes. Higher values will be scaled down to avoid too much noise and slow convergence at the cost of accuracy. Used by light-probes."""
        ...
    @clamp_volume_indirect.setter
    def clamp_volume_indirect(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def volumetric_start(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Start distance of the volumetric effect"""
        ...
    @volumetric_start.setter
    def volumetric_start(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def volumetric_end(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]:
        """End distance of the volumetric effect"""
        ...
    @volumetric_end.setter
    def volumetric_end(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def volumetric_tile_size(self) -> Annotated[Literal['1', '2', '4', '8', '16'], "is_animatable=False"]:
        """Control the quality of the volumetric effects. Higher resolution uses more memory."""
        ...
    @volumetric_tile_size.setter
    def volumetric_tile_size(self, value: Annotated[Literal['1', '2', '4', '8', '16'], "is_animatable=False"]):
        ...
    @property
    def volumetric_samples(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Number of steps to compute volumetric effects. Higher step count increase VRAM usage and quality."""
        ...
    @volumetric_samples.setter
    def volumetric_samples(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def volumetric_sample_distribution(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Distribute more samples closer to the camera"""
        ...
    @volumetric_sample_distribution.setter
    def volumetric_sample_distribution(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def volumetric_ray_depth(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Maximum surface intersection count used by the accurate volume intersection method. Will create artifact if it is exceeded. Higher count increases VRAM usage."""
        ...
    @volumetric_ray_depth.setter
    def volumetric_ray_depth(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def volumetric_light_clamp(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Maximum light contribution, reducing noise"""
        ...
    @volumetric_light_clamp.setter
    def volumetric_light_clamp(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def use_volumetric_shadows(self) -> Annotated[bool, "is_animatable=False"]:
        """Cast shadows from volumetric materials onto volumetric materials (Very expensive)"""
        ...
    @use_volumetric_shadows.setter
    def use_volumetric_shadows(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def volumetric_shadow_samples(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Number of samples to compute volumetric shadowing"""
        ...
    @volumetric_shadow_samples.setter
    def volumetric_shadow_samples(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def use_volume_custom_range(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable custom start and end clip distances for volume computation"""
        ...
    @use_volume_custom_range.setter
    def use_volume_custom_range(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_fast_gi(self) -> Annotated[bool, "is_animatable=False"]:
        """Use faster global illumination technique for high roughness surfaces"""
        ...
    @use_fast_gi.setter
    def use_fast_gi(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def fast_gi_thickness_near(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]:
        """Geometric thickness of the surfaces when computing fast GI and ambient occlusion. Reduces light leaking and missing contact occlusion."""
        ...
    @fast_gi_thickness_near.setter
    def fast_gi_thickness_near(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def fast_gi_thickness_far(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Angular thickness of the surfaces when computing fast GI and ambient occlusion. Reduces energy loss and missing occlusion of far geometry."""
        ...
    @fast_gi_thickness_far.setter
    def fast_gi_thickness_far(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def fast_gi_quality(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Precision of the fast GI ray marching"""
        ...
    @fast_gi_quality.setter
    def fast_gi_quality(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def fast_gi_step_count(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Amount of screen sample per GI ray"""
        ...
    @fast_gi_step_count.setter
    def fast_gi_step_count(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def fast_gi_ray_count(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Amount of GI ray to trace for each pixel"""
        ...
    @fast_gi_ray_count.setter
    def fast_gi_ray_count(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def fast_gi_method(self) -> Annotated[Literal['AMBIENT_OCCLUSION_ONLY', 'GLOBAL_ILLUMINATION'], "is_animatable=False"]:
        """Fast GI approximation method"""
        ...
    @fast_gi_method.setter
    def fast_gi_method(self, value: Annotated[Literal['AMBIENT_OCCLUSION_ONLY', 'GLOBAL_ILLUMINATION'], "is_animatable=False"]):
        ...
    @property
    def fast_gi_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]:
        """If non-zero, the maximum distance at which other surfaces will contribute to the fast GI approximation"""
        ...
    @fast_gi_distance.setter
    def fast_gi_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def fast_gi_bias(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2", "is_animatable=False"]:
        """Bias the shading normal to reduce self intersection artifacts"""
        ...
    @fast_gi_bias.setter
    def fast_gi_bias(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def fast_gi_resolution(self) -> Annotated[Literal['1', '2', '4', '8', '16'], "is_animatable=False"]:
        """Control the quality of the fast GI lighting. Higher resolution uses more memory."""
        ...
    @fast_gi_resolution.setter
    def fast_gi_resolution(self, value: Annotated[Literal['1', '2', '4', '8', '16'], "is_animatable=False"]):
        ...
    @property
    def bokeh_max_size(self) -> Annotated[float, "subtype='PIXEL'", "step=100.0", "precision=1", "is_animatable=False"]:
        """Max size of the bokeh shape for the depth of field (lower is faster)"""
        ...
    @bokeh_max_size.setter
    def bokeh_max_size(self, value: Annotated[float, "subtype='PIXEL'", "step=100.0", "precision=1", "is_animatable=False"]):
        ...
    @property
    def bokeh_threshold(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=2", "is_animatable=False"]:
        """Brightness threshold for using sprite base depth of field"""
        ...
    @bokeh_threshold.setter
    def bokeh_threshold(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def bokeh_neighbor_max(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=2", "is_animatable=False"]:
        """Maximum brightness to consider when rejecting bokeh sprites based on neighborhood (lower is faster)"""
        ...
    @bokeh_neighbor_max.setter
    def bokeh_neighbor_max(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def use_bokeh_jittered(self) -> Annotated[bool, "is_animatable=False"]:
        """Jitter camera position to create accurate blurring using render samples (only for final render)"""
        ...
    @use_bokeh_jittered.setter
    def use_bokeh_jittered(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def bokeh_overblur(self) -> Annotated[float, "subtype='PERCENTAGE'", "step=1.0", "precision=1", "is_animatable=False"]:
        """Apply blur to each jittered sample to reduce under-sampling artifacts"""
        ...
    @bokeh_overblur.setter
    def bokeh_overblur(self, value: Annotated[float, "subtype='PERCENTAGE'", "step=1.0", "precision=1", "is_animatable=False"]):
        ...
    @property
    def motion_blur_depth_scale(self) -> Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]:
        """Lower values will reduce background bleeding onto foreground elements"""
        ...
    @motion_blur_depth_scale.setter
    def motion_blur_depth_scale(self, value: Annotated[float, "step=1.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def motion_blur_max(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Maximum blur distance a pixel can spread over"""
        ...
    @motion_blur_max.setter
    def motion_blur_max(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]):
        ...
    @property
    def motion_blur_steps(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Controls accuracy of motion blur, more steps means longer render time"""
        ...
    @motion_blur_steps.setter
    def motion_blur_steps(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def use_shadows(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable shadow casting from lights"""
        ...
    @use_shadows.setter
    def use_shadows(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def shadow_pool_size(self) -> Annotated[Literal['16', '32', '64', '128', '256', '512', '1024'], "is_animatable=False"]:
        """Size of the shadow pool, a bigger pool size allows for more shadows in the scene but might not fit into GPU memory"""
        ...
    @shadow_pool_size.setter
    def shadow_pool_size(self, value: Annotated[Literal['16', '32', '64', '128', '256', '512', '1024'], "is_animatable=False"]):
        ...
    @property
    def shadow_ray_count(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Amount of shadow ray to trace for each light"""
        ...
    @shadow_ray_count.setter
    def shadow_ray_count(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def shadow_step_count(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]:
        """Amount of shadow map sample per shadow ray"""
        ...
    @shadow_step_count.setter
    def shadow_step_count(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]):
        ...
    @property
    def light_threshold(self) -> Annotated[float, "subtype='UNSIGNED'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]:
        """Minimum light intensity for a light to contribute to the lighting"""
        ...
    @light_threshold.setter
    def light_threshold(self, value: Annotated[float, "subtype='UNSIGNED'", "step=0.10000000149011612", "precision=3", "is_animatable=False"]):
        ...
    @property
    def use_overscan(self) -> Annotated[bool, "is_animatable=False"]:
        """Internally render past the image border to avoid screen-space effects disappearing"""
        ...
    @use_overscan.setter
    def use_overscan(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def overscan_size(self) -> Annotated[float, "subtype='PERCENTAGE'", "step=1.0", "precision=2", "is_animatable=False"]:
        """Percentage of render size to add as overscan to the internal render buffers"""
        ...
    @overscan_size.setter
    def overscan_size(self, value: Annotated[float, "subtype='PERCENTAGE'", "step=1.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def ray_tracing_options(self) -> Annotated[Optional['RaytraceEEVEE'], "is_animatable=False"]:
        """EEVEE settings for tracing reflections"""
        ...
    @property
    def use_raytracing(self) -> Annotated[bool, "is_animatable=False"]:
        """Enable the ray-tracing module"""
        ...
    @use_raytracing.setter
    def use_raytracing(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def shadow_resolution_scale(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Resolution percentage of shadow maps"""
        ...
    @shadow_resolution_scale.setter
    def shadow_resolution_scale(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...