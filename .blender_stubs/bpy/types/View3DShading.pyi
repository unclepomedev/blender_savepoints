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
from .StudioLight import StudioLight
class View3DShading(bpy_struct):
    type: str
    light: str
    show_object_outline: bool
    studio_light: str
    use_world_space_lighting: bool
    show_backface_culling: bool
    show_cavity: bool
    cavity_type: str
    curvature_ridge_factor: float
    curvature_valley_factor: float
    cavity_ridge_factor: float
    cavity_valley_factor: float
    selected_studio_light: 'StudioLight'
    studiolight_rotate_z: float
    studiolight_intensity: float
    studiolight_background_alpha: float
    studiolight_background_blur: float
    use_studiolight_view_rotation: bool
    color_type: str
    wireframe_color_type: str
    single_color: float
    background_type: str
    background_color: float
    show_shadows: bool
    show_xray: bool
    show_xray_wireframe: bool
    xray_alpha: float
    xray_alpha_wireframe: float
    use_dof: bool
    use_scene_lights: bool
    use_scene_world: bool
    use_scene_lights_render: bool
    use_scene_world_render: bool
    show_specular_highlight: bool
    object_outline_color: float
    shadow_intensity: float
    render_pass: str
    aov_name: str
    use_compositor: str
    cycles: 'CyclesView3DShadingSettings'
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...