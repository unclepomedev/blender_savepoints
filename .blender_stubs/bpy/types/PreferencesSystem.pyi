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
from .UserSolidLight import UserSolidLight
class PreferencesSystem(bpy_struct):
    @property
    def ui_scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Size multiplier to use when displaying custom user interface elements, so that they are scaled correctly on screens with different DPI. This value is based on operating system DPI settings and Blender display scale."""
        ...
    @property
    def ui_line_width(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Suggested line thickness and point size in pixels, for add-ons displaying custom user interface elements, based on operating system settings and Blender UI scale"""
        ...
    @property
    def dpi(self) -> Annotated[int, "step=1"]:
        ...
    @property
    def pixel_size(self) -> Annotated[float, "step=10.0", "precision=3"]:
        ...
    memory_cache_limit: Annotated[int, "step=1"]
    """Memory cache limit (in megabytes)"""
    sequencer_proxy_setup: Literal['MANUAL', 'AUTOMATIC']
    """When and how proxies are created"""
    scrollback: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Maximum number of lines to store for the console buffer"""
    use_overlay_smooth_wire: bool
    """Enable overlay smooth wires, reducing aliasing"""
    use_edit_mode_smooth_wire: bool
    """Enable edit mode edge smoothing, reducing aliasing (requires restart)"""
    use_region_overlap: bool
    """Display tool/property regions over the main region"""
    viewport_aa: Annotated[Literal['OFF', 'FXAA', '5', '8', '11', '16', '32'], "is_animatable=False"]
    """Method of anti-aliasing in 3d viewport"""
    @property
    def solid_lights(self) -> Annotated[bpy_prop_collection['UserSolidLight'], "is_animatable=False"]:
        """Lights used to display objects in solid shading mode"""
        ...
    light_ambient: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color of the ambient light that uniformly lit the scene"""
    use_studio_light_edit: bool
    """View the result of the studio light editor in the viewport"""
    gl_clip_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Clip alpha below this threshold in the 3D textured view"""
    image_draw_method: Literal['AUTO', '2DTEXTURE', 'GLSL']
    """Method used for displaying images on the screen"""
    anisotropic_filter: Literal['FILTER_0', 'FILTER_2', 'FILTER_4', 'FILTER_8', 'FILTER_16']
    """Quality of anisotropic filtering"""
    gl_texture_limit: Literal['CLAMP_OFF', 'CLAMP_8192', 'CLAMP_4096', 'CLAMP_2048', 'CLAMP_1024', 'CLAMP_512', 'CLAMP_256', 'CLAMP_128']
    """Limit the texture size to save graphics memory"""
    texture_time_out: Annotated[int, "step=1"]
    """Time since last access of a GL texture in seconds after which it is freed (set to 0 to keep textures allocated)"""
    texture_collection_rate: Annotated[int, "step=1"]
    """Number of seconds between each run of the GL texture garbage collector"""
    vbo_time_out: Annotated[int, "step=1"]
    """Time since last access of a GL vertex buffer object in seconds after which it is freed (set to 0 to keep VBO allocated)"""
    vbo_collection_rate: Annotated[int, "step=1"]
    """Number of seconds between each run of the GL vertex buffer object garbage collector"""
    use_gpu_subdivision: bool
    """Enable GPU acceleration for evaluating the last subdivision surface modifiers in the stack"""
    gpu_backend: Literal['OPENGL', 'METAL', 'VULKAN']
    """GPU backend to use (requires restarting Blender for changes to take effect)"""
    gpu_preferred_device: Literal['AUTO']
    """Preferred device to select during detection (requires restarting Blender for changes to take effect)"""
    gpu_shader_workers: Annotated[int, "step=1"]
    """Number of shader compilation threads or subprocesses, clamped at the max threads supported by the CPU (requires restarting Blender for changes to take effect). A higher number increases the RAM usage while reducing compilation time. A value of 0 will use automatic configuration. (OpenGL only)"""
    shader_compilation_method: Literal['THREAD', 'SUBPROCESS']
    """Compilation method used for compiling shaders in parallel. Subprocess requires a lot more RAM for each worker but might compile shaders faster on some systems. Requires restarting Blender for changes to take effect. (OpenGL only)"""
    use_online_access: bool
    """Allow Blender to access the internet. Add-ons that follow this setting will only connect to the internet if enabled. However, Blender cannot prevent third-party add-ons from violating this rule."""
    network_timeout: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """The time in seconds to wait for online operations before a connection may fail with a time-out error. Zero uses the systems default."""
    network_connection_limit: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Limit the number of simultaneous internet connections online operations may make at once. Zero disables the limit."""
    audio_mixing_buffer: Literal['SAMPLES_256', 'SAMPLES_512', 'SAMPLES_1024', 'SAMPLES_2048', 'SAMPLES_4096', 'SAMPLES_8192', 'SAMPLES_16384', 'SAMPLES_32768']
    """Number of samples used by the audio mixing buffer"""
    audio_device: Literal['None']
    """Audio output device"""
    audio_sample_rate: Literal['RATE_44100', 'RATE_48000', 'RATE_96000', 'RATE_192000']
    """Audio sample rate"""
    audio_sample_format: Literal['U8', 'S16', 'S24', 'S32', 'FLOAT', 'DOUBLE']
    """Audio sample format"""
    audio_channels: Literal['MONO', 'STEREO', 'SURROUND4', 'SURROUND51', 'SURROUND71']
    """Audio channel count"""
    @property
    def legacy_compute_device_type(self) -> Annotated[int, "step=1"]:
        """For backwards compatibility only"""
        ...
    register_all_users: bool
    """Make this Blender version open blend files for all users. Requires elevated privileges."""
    @property
    def is_microsoft_store_install(self) -> bool:
        """Whether this blender installation is a sandboxed Microsoft Store version"""
        ...