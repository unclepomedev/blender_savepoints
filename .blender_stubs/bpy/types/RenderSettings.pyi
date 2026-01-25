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
from .BakeSettings import BakeSettings
from .CurveMapping import CurveMapping
from .FFmpegSettings import FFmpegSettings
from .ImageFormatSettings import ImageFormatSettings
from .SceneRenderView import SceneRenderView
class RenderSettings(bpy_struct):
    image_settings: 'ImageFormatSettings'
    resolution_x: int
    resolution_y: int
    resolution_percentage: int
    preview_pixel_size: str
    pixel_aspect_x: float
    pixel_aspect_y: float
    ppm_factor: float
    ppm_base: float
    ffmpeg: 'FFmpegSettings'
    fps: int
    fps_base: float
    frame_map_old: int
    frame_map_new: int
    dither_intensity: float
    filter_size: float
    film_transparent: bool
    use_freestyle: bool
    threads: int
    threads_mode: str
    use_motion_blur: bool
    motion_blur_shutter: float
    motion_blur_position: str
    motion_blur_shutter_curve: 'CurveMapping'
    hair_type: str
    hair_subdiv: int
    use_high_quality_normals: bool
    use_border: bool
    border_min_x: float
    border_min_y: float
    border_max_x: float
    border_max_y: float
    use_crop_to_border: bool
    use_placeholder: bool
    use_overwrite: bool
    use_compositing: bool
    use_sequencer: bool
    use_file_extension: bool
    file_extension: str
    is_movie_format: bool
    use_lock_interface: bool
    filepath: str
    use_render_cache: bool
    use_stamp_time: bool
    use_stamp_date: bool
    use_stamp_frame: bool
    use_stamp_frame_range: bool
    use_stamp_camera: bool
    use_stamp_lens: bool
    use_stamp_scene: bool
    use_stamp_note: bool
    use_stamp_marker: bool
    use_stamp_filename: bool
    use_stamp_sequencer_strip: bool
    use_stamp_render_time: bool
    stamp_note_text: str
    use_stamp: bool
    use_stamp_labels: bool
    metadata_input: str
    use_stamp_memory: bool
    use_stamp_hostname: bool
    stamp_font_size: int
    stamp_foreground: list[float]
    stamp_background: list[float]
    sequencer_gl_preview: str
    use_sequencer_override_scene_strip: bool
    use_single_layer: bool
    views: bpy_prop_collection['SceneRenderView']
    stereo_views: bpy_prop_collection['SceneRenderView']
    use_multiview: bool
    views_format: str
    engine: str
    has_multiple_engines: bool
    use_spherical_stereo: bool
    use_simplify: bool
    simplify_subdivision: int
    simplify_child_particles: float
    simplify_subdivision_render: int
    simplify_child_particles_render: float
    simplify_volumes: float
    use_simplify_normals: bool
    simplify_gpencil: bool
    simplify_gpencil_onplay: bool
    simplify_gpencil_antialiasing: bool
    simplify_gpencil_view_fill: bool
    simplify_gpencil_modifier: bool
    simplify_gpencil_shader_fx: bool
    simplify_gpencil_tint: bool
    use_persistent_data: bool
    line_thickness_mode: str
    line_thickness: float
    bake: 'BakeSettings'
    compositor_device: str
    compositor_precision: str
    compositor_denoise_device: str
    compositor_denoise_preview_quality: str
    compositor_denoise_final_quality: str
    def frame_path(self, *args, **kwargs) -> Any: ...