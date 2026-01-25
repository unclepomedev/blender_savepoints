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
from .UserSolidLight import UserSolidLight
class PreferencesSystem(bpy_struct):
    ui_scale: float
    ui_line_width: float
    dpi: int
    pixel_size: float
    memory_cache_limit: int
    sequencer_proxy_setup: str
    scrollback: int
    use_overlay_smooth_wire: bool
    use_edit_mode_smooth_wire: bool
    use_region_overlap: bool
    viewport_aa: str
    solid_lights: bpy_prop_collection['UserSolidLight']
    light_ambient: float
    use_studio_light_edit: bool
    gl_clip_alpha: float
    image_draw_method: str
    anisotropic_filter: str
    gl_texture_limit: str
    texture_time_out: int
    texture_collection_rate: int
    vbo_time_out: int
    vbo_collection_rate: int
    use_gpu_subdivision: bool
    gpu_backend: str
    gpu_preferred_device: str
    gpu_shader_workers: int
    shader_compilation_method: str
    use_online_access: bool
    network_timeout: int
    network_connection_limit: int
    audio_mixing_buffer: str
    audio_device: str
    audio_sample_rate: str
    audio_sample_format: str
    audio_channels: str
    legacy_compute_device_type: int
    register_all_users: bool
    is_microsoft_store_install: bool