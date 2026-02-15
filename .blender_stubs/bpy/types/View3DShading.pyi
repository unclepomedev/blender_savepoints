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
from .StudioLight import StudioLight
class View3DShading(bpy_struct):
    type: Literal['WIREFRAME', 'SOLID', 'MATERIAL', 'RENDERED']
    """Method to display/shade objects in the 3D View"""
    light: Literal['STUDIO', 'MATCAP', 'FLAT']
    """Lighting Method for Solid/Texture Viewport Shading"""
    show_object_outline: Annotated[bool, "is_animatable=False"]
    """Show Object Outline"""
    studio_light: Literal['DEFAULT']
    """Studio lighting setup"""
    use_world_space_lighting: Annotated[bool, "is_animatable=False"]
    """Make the lighting fixed and not follow the camera"""
    show_backface_culling: bool
    """Use back face culling to hide the back side of faces"""
    show_cavity: Annotated[bool, "is_animatable=False"]
    """Show Cavity"""
    cavity_type: Literal['WORLD', 'SCREEN', 'BOTH']
    """Way to display the cavity shading"""
    curvature_ridge_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Factor for the curvature ridges"""
    curvature_valley_factor: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Factor for the curvature valleys"""
    cavity_ridge_factor: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]
    """Factor for the cavity ridges"""
    cavity_valley_factor: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]
    """Factor for the cavity valleys"""
    @property
    def selected_studio_light(self) -> Annotated[Optional['StudioLight'], "is_animatable=False"]:
        """Selected StudioLight"""
        ...
    studiolight_rotate_z: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Rotation of the studiolight around the Z-Axis"""
    studiolight_intensity: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]
    """Strength of the studiolight"""
    studiolight_background_alpha: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]
    """Show the studiolight in the background"""
    studiolight_background_blur: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2", "is_animatable=False"]
    """Blur the studiolight in the background"""
    use_studiolight_view_rotation: Annotated[bool, "is_animatable=False"]
    """Make the HDR rotation fixed and not follow the camera"""
    color_type: Annotated[Literal['MATERIAL', 'OBJECT', 'RANDOM', 'VERTEX', 'TEXTURE', 'SINGLE'], "is_animatable=False"]
    """Color Type"""
    wireframe_color_type: Literal['THEME', 'OBJECT', 'RANDOM']
    """Wire Color Type"""
    single_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color for single color mode"""
    background_type: Literal['THEME', 'WORLD', 'VIEWPORT']
    """Way to display the background"""
    background_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color for custom background color"""
    show_shadows: Annotated[bool, "is_animatable=False"]
    """Show Shadow"""
    show_xray: Annotated[bool, "is_animatable=False"]
    """Show whole scene transparent"""
    show_xray_wireframe: Annotated[bool, "is_animatable=False"]
    """Show whole scene transparent"""
    xray_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Amount of opacity to use"""
    xray_alpha_wireframe: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]
    """Amount of opacity to use"""
    use_dof: Annotated[bool, "is_animatable=False"]
    """Use depth of field on viewport using the values from the active camera"""
    use_scene_lights: Annotated[bool, "is_animatable=False"]
    """Render lights and light probes of the scene"""
    use_scene_world: Annotated[bool, "is_animatable=False"]
    """Use scene world for lighting"""
    use_scene_lights_render: Annotated[bool, "is_animatable=False"]
    """Render lights and light probes of the scene"""
    use_scene_world_render: Annotated[bool, "is_animatable=False"]
    """Use scene world for lighting"""
    show_specular_highlight: Annotated[bool, "is_animatable=False"]
    """Render specular highlights"""
    object_outline_color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Color for object outline"""
    shadow_intensity: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]
    """Darkness of shadows"""
    render_pass: Literal['COMBINED', 'EMISSION', 'ENVIRONMENT', 'AO', 'SHADOW', 'TRANSPARENT', 'DIFFUSE_LIGHT', 'DIFFUSE_COLOR', 'SPECULAR_LIGHT', 'SPECULAR_COLOR', 'VOLUME_LIGHT', 'POSITION', 'NORMAL', 'MIST', 'CryptoObject', 'CryptoAsset', 'CryptoMaterial', 'AOV']
    """Render Pass to show in the viewport"""
    aov_name: Annotated[str, "is_animatable=False"]
    """Name of the active Shader AOV"""
    use_compositor: Annotated[Literal['DISABLED', 'CAMERA', 'ALWAYS'], "is_animatable=False"]
    """When to preview the compositor output inside the viewport"""
    @property
    def cycles(self) -> Annotated[Optional['CyclesView3DShadingSettings'], "is_animatable=False"]:
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...