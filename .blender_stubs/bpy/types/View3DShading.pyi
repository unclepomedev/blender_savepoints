# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.View3DShading.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .StudioLight import StudioLight

class View3DShading(bpy_struct):

    @property
    def type(self) -> Literal['WIREFRAME', 'SOLID', 'MATERIAL', 'RENDERED']:
        """Method to display/shade objects in the 3D View"""
        ...
    @type.setter
    def type(self, value: Literal['WIREFRAME', 'SOLID', 'MATERIAL', 'RENDERED']):
        ...
    @property
    def light(self) -> Literal['STUDIO', 'MATCAP', 'FLAT']:
        """Lighting Method for Solid/Texture Viewport Shading"""
        ...
    @light.setter
    def light(self, value: Literal['STUDIO', 'MATCAP', 'FLAT']):
        ...
    @property
    def show_object_outline(self) -> Annotated[bool, "is_animatable=False"]:
        """Show Object Outline"""
        ...
    @show_object_outline.setter
    def show_object_outline(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def studio_light(self) -> Literal['DEFAULT']:
        """Studio lighting setup"""
        ...
    @studio_light.setter
    def studio_light(self, value: Literal['DEFAULT']):
        ...
    @property
    def use_world_space_lighting(self) -> Annotated[bool, "is_animatable=False"]:
        """Make the lighting fixed and not follow the camera"""
        ...
    @use_world_space_lighting.setter
    def use_world_space_lighting(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_backface_culling(self) -> bool:
        """Use back face culling to hide the back side of faces"""
        ...
    @show_backface_culling.setter
    def show_backface_culling(self, value: bool):
        ...
    @property
    def show_cavity(self) -> Annotated[bool, "is_animatable=False"]:
        """Show Cavity"""
        ...
    @show_cavity.setter
    def show_cavity(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def cavity_type(self) -> Literal['WORLD', 'SCREEN', 'BOTH']:
        """Way to display the cavity shading"""
        ...
    @cavity_type.setter
    def cavity_type(self, value: Literal['WORLD', 'SCREEN', 'BOTH']):
        ...
    @property
    def curvature_ridge_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Factor for the curvature ridges"""
        ...
    @curvature_ridge_factor.setter
    def curvature_ridge_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def curvature_valley_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Factor for the curvature valleys"""
        ...
    @curvature_valley_factor.setter
    def curvature_valley_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def cavity_ridge_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]:
        """Factor for the cavity ridges"""
        ...
    @cavity_ridge_factor.setter
    def cavity_ridge_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def cavity_valley_factor(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]:
        """Factor for the cavity valleys"""
        ...
    @cavity_valley_factor.setter
    def cavity_valley_factor(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def selected_studio_light(self) -> Annotated[Optional['StudioLight'], "is_animatable=False"]:
        """Selected StudioLight"""
        ...
    @property
    def studiolight_rotate_z(self) -> Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Rotation of the studiolight around the Z-Axis"""
        ...
    @studiolight_rotate_z.setter
    def studiolight_rotate_z(self, value: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def studiolight_intensity(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]:
        """Strength of the studiolight"""
        ...
    @studiolight_intensity.setter
    def studiolight_intensity(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def studiolight_background_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]:
        """Show the studiolight in the background"""
        ...
    @studiolight_background_alpha.setter
    def studiolight_background_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def studiolight_background_blur(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2", "is_animatable=False"]:
        """Blur the studiolight in the background"""
        ...
    @studiolight_background_blur.setter
    def studiolight_background_blur(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2", "is_animatable=False"]):
        ...
    @property
    def use_studiolight_view_rotation(self) -> Annotated[bool, "is_animatable=False"]:
        """Make the HDR rotation fixed and not follow the camera"""
        ...
    @use_studiolight_view_rotation.setter
    def use_studiolight_view_rotation(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def color_type(self) -> Annotated[Literal['MATERIAL', 'OBJECT', 'RANDOM', 'VERTEX', 'TEXTURE', 'SINGLE'], "is_animatable=False"]:
        """Color Type"""
        ...
    @color_type.setter
    def color_type(self, value: Annotated[Literal['MATERIAL', 'OBJECT', 'RANDOM', 'VERTEX', 'TEXTURE', 'SINGLE'], "is_animatable=False"]):
        ...
    @property
    def wireframe_color_type(self) -> Literal['THEME', 'OBJECT', 'RANDOM']:
        """Wire Color Type"""
        ...
    @wireframe_color_type.setter
    def wireframe_color_type(self, value: Literal['THEME', 'OBJECT', 'RANDOM']):
        ...
    @property
    def single_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color for single color mode"""
        ...
    @single_color.setter
    def single_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def background_type(self) -> Literal['THEME', 'WORLD', 'VIEWPORT']:
        """Way to display the background"""
        ...
    @background_type.setter
    def background_type(self, value: Literal['THEME', 'WORLD', 'VIEWPORT']):
        ...
    @property
    def background_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color for custom background color"""
        ...
    @background_color.setter
    def background_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def show_shadows(self) -> Annotated[bool, "is_animatable=False"]:
        """Show Shadow"""
        ...
    @show_shadows.setter
    def show_shadows(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_xray(self) -> Annotated[bool, "is_animatable=False"]:
        """Show whole scene transparent"""
        ...
    @show_xray.setter
    def show_xray(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_xray_wireframe(self) -> Annotated[bool, "is_animatable=False"]:
        """Show whole scene transparent"""
        ...
    @show_xray_wireframe.setter
    def show_xray_wireframe(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def xray_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Amount of opacity to use"""
        ...
    @xray_alpha.setter
    def xray_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def xray_alpha_wireframe(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Amount of opacity to use"""
        ...
    @xray_alpha_wireframe.setter
    def xray_alpha_wireframe(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def use_dof(self) -> Annotated[bool, "is_animatable=False"]:
        """Use depth of field on viewport using the values from the active camera"""
        ...
    @use_dof.setter
    def use_dof(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_scene_lights(self) -> Annotated[bool, "is_animatable=False"]:
        """Render lights and light probes of the scene"""
        ...
    @use_scene_lights.setter
    def use_scene_lights(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_scene_world(self) -> Annotated[bool, "is_animatable=False"]:
        """Use scene world for lighting"""
        ...
    @use_scene_world.setter
    def use_scene_world(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_scene_lights_render(self) -> Annotated[bool, "is_animatable=False"]:
        """Render lights and light probes of the scene"""
        ...
    @use_scene_lights_render.setter
    def use_scene_lights_render(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_scene_world_render(self) -> Annotated[bool, "is_animatable=False"]:
        """Use scene world for lighting"""
        ...
    @use_scene_world_render.setter
    def use_scene_world_render(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_specular_highlight(self) -> Annotated[bool, "is_animatable=False"]:
        """Render specular highlights"""
        ...
    @show_specular_highlight.setter
    def show_specular_highlight(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def object_outline_color(self) -> Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]:
        """Color for object outline"""
        ...
    @object_outline_color.setter
    def object_outline_color(self, value: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]):
        ...
    @property
    def shadow_intensity(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]:
        """Darkness of shadows"""
        ...
    @shadow_intensity.setter
    def shadow_intensity(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def render_pass(self) -> Literal['COMBINED', 'EMISSION', 'ENVIRONMENT', 'AO', 'SHADOW', 'TRANSPARENT', 'DIFFUSE_LIGHT', 'DIFFUSE_COLOR', 'SPECULAR_LIGHT', 'SPECULAR_COLOR', 'VOLUME_LIGHT', 'POSITION', 'NORMAL', 'MIST', 'CryptoObject', 'CryptoAsset', 'CryptoMaterial', 'AOV']:
        """Render Pass to show in the viewport"""
        ...
    @render_pass.setter
    def render_pass(self, value: Literal['COMBINED', 'EMISSION', 'ENVIRONMENT', 'AO', 'SHADOW', 'TRANSPARENT', 'DIFFUSE_LIGHT', 'DIFFUSE_COLOR', 'SPECULAR_LIGHT', 'SPECULAR_COLOR', 'VOLUME_LIGHT', 'POSITION', 'NORMAL', 'MIST', 'CryptoObject', 'CryptoAsset', 'CryptoMaterial', 'AOV']):
        ...
    @property
    def aov_name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the active Shader AOV"""
        ...
    @aov_name.setter
    def aov_name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def use_compositor(self) -> Annotated[Literal['DISABLED', 'CAMERA', 'ALWAYS'], "is_animatable=False"]:
        """When to preview the compositor output inside the viewport"""
        ...
    @use_compositor.setter
    def use_compositor(self, value: Annotated[Literal['DISABLED', 'CAMERA', 'ALWAYS'], "is_animatable=False"]):
        ...
    @property
    def cycles(self) -> Annotated[Optional['CyclesView3DShadingSettings'], "is_animatable=False"]:

        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...