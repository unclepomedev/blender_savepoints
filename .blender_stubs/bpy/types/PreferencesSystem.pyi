# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.PreferencesSystem.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .UserSolidLight import UserSolidLight
from .bpy_prop_collection import bpy_prop_collection

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
    @property
    def memory_cache_limit(self) -> Annotated[int, "step=1"]:
        """Memory cache limit (in megabytes)"""
        ...
    @memory_cache_limit.setter
    def memory_cache_limit(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def sequencer_proxy_setup(self) -> Literal['MANUAL', 'AUTOMATIC']:
        """When and how proxies are created"""
        ...
    @sequencer_proxy_setup.setter
    def sequencer_proxy_setup(self, value: Literal['MANUAL', 'AUTOMATIC']) -> None:
        ...
    @property
    def scrollback(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Maximum number of lines to store for the console buffer"""
        ...
    @scrollback.setter
    def scrollback(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def use_overlay_smooth_wire(self) -> bool:
        """Enable overlay smooth wires, reducing aliasing"""
        ...
    @use_overlay_smooth_wire.setter
    def use_overlay_smooth_wire(self, value: bool) -> None:
        ...
    @property
    def use_edit_mode_smooth_wire(self) -> bool:
        """Enable edit mode edge smoothing, reducing aliasing (requires restart)"""
        ...
    @use_edit_mode_smooth_wire.setter
    def use_edit_mode_smooth_wire(self, value: bool) -> None:
        ...
    @property
    def use_region_overlap(self) -> bool:
        """Display tool/property regions over the main region"""
        ...
    @use_region_overlap.setter
    def use_region_overlap(self, value: bool) -> None:
        ...
    @property
    def viewport_aa(self) -> Annotated[Literal['OFF', 'FXAA', '5', '8', '11', '16', '32'], "is_animatable=False"]:
        """Method of anti-aliasing in 3d viewport"""
        ...
    @viewport_aa.setter
    def viewport_aa(self, value: Annotated[Literal['OFF', 'FXAA', '5', '8', '11', '16', '32'], "is_animatable=False"]) -> None:
        ...
    @property
    def solid_lights(self) -> Annotated[bpy_prop_collection['UserSolidLight'], "is_animatable=False"]:
        """Lights used to display objects in solid shading mode"""
        ...
    @property
    def light_ambient(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color of the ambient light that uniformly lit the scene"""
        ...
    @light_ambient.setter
    def light_ambient(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_studio_light_edit(self) -> bool:
        """View the result of the studio light editor in the viewport"""
        ...
    @use_studio_light_edit.setter
    def use_studio_light_edit(self, value: bool) -> None:
        ...
    @property
    def gl_clip_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Clip alpha below this threshold in the 3D textured view"""
        ...
    @gl_clip_alpha.setter
    def gl_clip_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def image_draw_method(self) -> Literal['AUTO', '2DTEXTURE', 'GLSL']:
        """Method used for displaying images on the screen"""
        ...
    @image_draw_method.setter
    def image_draw_method(self, value: Literal['AUTO', '2DTEXTURE', 'GLSL']) -> None:
        ...
    @property
    def anisotropic_filter(self) -> Literal['FILTER_0', 'FILTER_2', 'FILTER_4', 'FILTER_8', 'FILTER_16']:
        """Quality of anisotropic filtering"""
        ...
    @anisotropic_filter.setter
    def anisotropic_filter(self, value: Literal['FILTER_0', 'FILTER_2', 'FILTER_4', 'FILTER_8', 'FILTER_16']) -> None:
        ...
    @property
    def gl_texture_limit(self) -> Literal['CLAMP_OFF', 'CLAMP_8192', 'CLAMP_4096', 'CLAMP_2048', 'CLAMP_1024', 'CLAMP_512', 'CLAMP_256', 'CLAMP_128']:
        """Limit the texture size to save graphics memory"""
        ...
    @gl_texture_limit.setter
    def gl_texture_limit(self, value: Literal['CLAMP_OFF', 'CLAMP_8192', 'CLAMP_4096', 'CLAMP_2048', 'CLAMP_1024', 'CLAMP_512', 'CLAMP_256', 'CLAMP_128']) -> None:
        ...
    @property
    def texture_time_out(self) -> Annotated[int, "step=1"]:
        """Time since last access of a GL texture in seconds after which it is freed (set to 0 to keep textures allocated)"""
        ...
    @texture_time_out.setter
    def texture_time_out(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def texture_collection_rate(self) -> Annotated[int, "step=1"]:
        """Number of seconds between each run of the GL texture garbage collector"""
        ...
    @texture_collection_rate.setter
    def texture_collection_rate(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def vbo_time_out(self) -> Annotated[int, "step=1"]:
        """Time since last access of a GL vertex buffer object in seconds after which it is freed (set to 0 to keep VBO allocated)"""
        ...
    @vbo_time_out.setter
    def vbo_time_out(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def vbo_collection_rate(self) -> Annotated[int, "step=1"]:
        """Number of seconds between each run of the GL vertex buffer object garbage collector"""
        ...
    @vbo_collection_rate.setter
    def vbo_collection_rate(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_gpu_subdivision(self) -> bool:
        """Enable GPU acceleration for evaluating the last subdivision surface modifiers in the stack"""
        ...
    @use_gpu_subdivision.setter
    def use_gpu_subdivision(self, value: bool) -> None:
        ...
    @property
    def gpu_backend(self) -> Literal['OPENGL', 'METAL', 'VULKAN']:
        """GPU backend to use (requires restarting Blender for changes to take effect)"""
        ...
    @gpu_backend.setter
    def gpu_backend(self, value: Literal['OPENGL', 'METAL', 'VULKAN']) -> None:
        ...
    @property
    def gpu_preferred_device(self) -> Literal['AUTO']:
        """Preferred device to select during detection (requires restarting Blender for changes to take effect)"""
        ...
    @gpu_preferred_device.setter
    def gpu_preferred_device(self, value: Literal['AUTO']) -> None:
        ...
    @property
    def gpu_shader_workers(self) -> Annotated[int, "step=1"]:
        """Number of shader compilation threads or subprocesses, clamped at the max threads supported by the CPU (requires restarting Blender for changes to take effect). A higher number increases the RAM usage while reducing compilation time. A value of 0 will use automatic configuration. (OpenGL only)"""
        ...
    @gpu_shader_workers.setter
    def gpu_shader_workers(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def shader_compilation_method(self) -> Literal['THREAD', 'SUBPROCESS']:
        """Compilation method used for compiling shaders in parallel. Subprocess requires a lot more RAM for each worker but might compile shaders faster on some systems. Requires restarting Blender for changes to take effect. (OpenGL only)"""
        ...
    @shader_compilation_method.setter
    def shader_compilation_method(self, value: Literal['THREAD', 'SUBPROCESS']) -> None:
        ...
    @property
    def use_online_access(self) -> bool:
        """Allow Blender to access the internet. Add-ons that follow this setting will only connect to the internet if enabled. However, Blender cannot prevent third-party add-ons from violating this rule."""
        ...
    @use_online_access.setter
    def use_online_access(self, value: bool) -> None:
        ...
    @property
    def network_timeout(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """The time in seconds to wait for online operations before a connection may fail with a time-out error. Zero uses the systems default."""
        ...
    @network_timeout.setter
    def network_timeout(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def network_connection_limit(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Limit the number of simultaneous internet connections online operations may make at once. Zero disables the limit."""
        ...
    @network_connection_limit.setter
    def network_connection_limit(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def audio_mixing_buffer(self) -> Literal['SAMPLES_256', 'SAMPLES_512', 'SAMPLES_1024', 'SAMPLES_2048', 'SAMPLES_4096', 'SAMPLES_8192', 'SAMPLES_16384', 'SAMPLES_32768']:
        """Number of samples used by the audio mixing buffer"""
        ...
    @audio_mixing_buffer.setter
    def audio_mixing_buffer(self, value: Literal['SAMPLES_256', 'SAMPLES_512', 'SAMPLES_1024', 'SAMPLES_2048', 'SAMPLES_4096', 'SAMPLES_8192', 'SAMPLES_16384', 'SAMPLES_32768']) -> None:
        ...
    @property
    def audio_device(self) -> Literal['None']:
        """Audio output device"""
        ...
    @audio_device.setter
    def audio_device(self, value: Literal['None']) -> None:
        ...
    @property
    def audio_sample_rate(self) -> Literal['RATE_44100', 'RATE_48000', 'RATE_96000', 'RATE_192000']:
        """Audio sample rate"""
        ...
    @audio_sample_rate.setter
    def audio_sample_rate(self, value: Literal['RATE_44100', 'RATE_48000', 'RATE_96000', 'RATE_192000']) -> None:
        ...
    @property
    def audio_sample_format(self) -> Literal['U8', 'S16', 'S24', 'S32', 'FLOAT', 'DOUBLE']:
        """Audio sample format"""
        ...
    @audio_sample_format.setter
    def audio_sample_format(self, value: Literal['U8', 'S16', 'S24', 'S32', 'FLOAT', 'DOUBLE']) -> None:
        ...
    @property
    def audio_channels(self) -> Literal['MONO', 'STEREO', 'SURROUND4', 'SURROUND51', 'SURROUND71']:
        """Audio channel count"""
        ...
    @audio_channels.setter
    def audio_channels(self, value: Literal['MONO', 'STEREO', 'SURROUND4', 'SURROUND51', 'SURROUND71']) -> None:
        ...
    @property
    def legacy_compute_device_type(self) -> Annotated[int, "step=1"]:
        """For backwards compatibility only"""
        ...
    @property
    def register_all_users(self) -> bool:
        """Make this Blender version open blend files for all users. Requires elevated privileges."""
        ...
    @register_all_users.setter
    def register_all_users(self, value: bool) -> None:
        ...
    @property
    def is_microsoft_store_install(self) -> bool:
        """Whether this blender installation is a sandboxed Microsoft Store version"""
        ...