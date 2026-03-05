# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.XrSessionSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Object import Object
from .View3DShading import View3DShading

class XrSessionSettings(bpy_struct):

    @property
    def shading(self) -> Annotated['View3DShading', "is_animatable=False"]:

        ...
    @property
    def base_pose_type(self) -> Annotated[Literal['SCENE_CAMERA', 'OBJECT', 'CUSTOM'], "is_animatable=False"]:
        """Define where the location and rotation for the VR view come from, to which translation and rotation deltas from the VR headset will be applied to"""
        ...
    @base_pose_type.setter
    def base_pose_type(self, value: Annotated[Literal['SCENE_CAMERA', 'OBJECT', 'CUSTOM'], "is_animatable=False"]) -> None:
        ...
    @property
    def base_pose_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to take the location and rotation to which translation and rotation deltas from the VR headset will be applied to"""
        ...
    @base_pose_object.setter
    def base_pose_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def base_pose_location(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5", "is_animatable=False"]:
        """Coordinates to apply translation deltas from the VR headset to"""
        ...
    @base_pose_location.setter
    def base_pose_location(self, value: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5", "is_animatable=False"]) -> None:
        ...
    @property
    def base_pose_angle(self) -> Annotated[float, "subtype='AXISANGLE'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Rotation angle around the Z-Axis to apply the rotation deltas from the VR headset to"""
        ...
    @base_pose_angle.setter
    def base_pose_angle(self, value: Annotated[float, "subtype='AXISANGLE'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def base_scale(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Uniform scale to apply to VR view"""
        ...
    @base_scale.setter
    def base_scale(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def show_floor(self) -> Annotated[bool, "is_animatable=False"]:
        """Show the ground plane grid"""
        ...
    @show_floor.setter
    def show_floor(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_passthrough(self) -> Annotated[bool, "is_animatable=False"]:
        """Show the passthrough view"""
        ...
    @show_passthrough.setter
    def show_passthrough(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_annotation(self) -> Annotated[bool, "is_animatable=False"]:
        """Show annotations for this view"""
        ...
    @show_annotation.setter
    def show_annotation(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_selection(self) -> Annotated[bool, "is_animatable=False"]:
        """Show selection outlines"""
        ...
    @show_selection.setter
    def show_selection(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_controllers(self) -> Annotated[bool, "is_animatable=False"]:
        """Show VR controllers (requires VR actions for controller poses)"""
        ...
    @show_controllers.setter
    def show_controllers(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_custom_overlays(self) -> Annotated[bool, "is_animatable=False"]:
        """Show custom VR overlays"""
        ...
    @show_custom_overlays.setter
    def show_custom_overlays(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_extras(self) -> Annotated[bool, "is_animatable=False"]:
        """Show object extras, including empties, lights, and cameras"""
        ...
    @show_object_extras.setter
    def show_object_extras(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def controller_draw_style(self) -> Annotated[Literal['DARK', 'LIGHT', 'DARK_RAY', 'LIGHT_RAY'], "is_animatable=False"]:
        """Style to use when drawing VR controllers"""
        ...
    @controller_draw_style.setter
    def controller_draw_style(self, value: Annotated[Literal['DARK', 'LIGHT', 'DARK_RAY', 'LIGHT_RAY'], "is_animatable=False"]) -> None:
        ...
    @property
    def clip_start(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]:
        """VR viewport near clipping distance"""
        ...
    @clip_start.setter
    def clip_start(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def clip_end(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1000.0", "precision=3", "is_animatable=False"]:
        """VR viewport far clipping distance"""
        ...
    @clip_end.setter
    def clip_end(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1000.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def fly_speed(self) -> Annotated[float, "step=50.0", "precision=3", "is_animatable=False"]:
        """Fly speed in meters per second"""
        ...
    @fly_speed.setter
    def fly_speed(self, value: Annotated[float, "step=50.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def use_positional_tracking(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow VR headsets to affect the location in virtual space, in addition to the rotation"""
        ...
    @use_positional_tracking.setter
    def use_positional_tracking(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_absolute_tracking(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow the VR tracking origin to be defined independently of the headset location"""
        ...
    @use_absolute_tracking.setter
    def use_absolute_tracking(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_mesh(self) -> Annotated[bool, "is_animatable=False"]:
        """Show mesh objects"""
        ...
    @show_object_viewport_mesh.setter
    def show_object_viewport_mesh(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_curve(self) -> Annotated[bool, "is_animatable=False"]:
        """Show curves"""
        ...
    @show_object_viewport_curve.setter
    def show_object_viewport_curve(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_surf(self) -> Annotated[bool, "is_animatable=False"]:
        """Show surfaces"""
        ...
    @show_object_viewport_surf.setter
    def show_object_viewport_surf(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_meta(self) -> Annotated[bool, "is_animatable=False"]:
        """Show metaballs"""
        ...
    @show_object_viewport_meta.setter
    def show_object_viewport_meta(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_font(self) -> Annotated[bool, "is_animatable=False"]:
        """Show text objects"""
        ...
    @show_object_viewport_font.setter
    def show_object_viewport_font(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_curves(self) -> Annotated[bool, "is_animatable=False"]:
        """Show hair curves"""
        ...
    @show_object_viewport_curves.setter
    def show_object_viewport_curves(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_pointcloud(self) -> Annotated[bool, "is_animatable=False"]:
        """Show point clouds"""
        ...
    @show_object_viewport_pointcloud.setter
    def show_object_viewport_pointcloud(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_volume(self) -> Annotated[bool, "is_animatable=False"]:
        """Show volumes"""
        ...
    @show_object_viewport_volume.setter
    def show_object_viewport_volume(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_armature(self) -> Annotated[bool, "is_animatable=False"]:
        """Show armatures"""
        ...
    @show_object_viewport_armature.setter
    def show_object_viewport_armature(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_lattice(self) -> Annotated[bool, "is_animatable=False"]:
        """Show lattices"""
        ...
    @show_object_viewport_lattice.setter
    def show_object_viewport_lattice(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_empty(self) -> Annotated[bool, "is_animatable=False"]:
        """Show empties"""
        ...
    @show_object_viewport_empty.setter
    def show_object_viewport_empty(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_grease_pencil(self) -> Annotated[bool, "is_animatable=False"]:
        """Show Grease Pencil objects"""
        ...
    @show_object_viewport_grease_pencil.setter
    def show_object_viewport_grease_pencil(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_camera(self) -> Annotated[bool, "is_animatable=False"]:
        """Show cameras"""
        ...
    @show_object_viewport_camera.setter
    def show_object_viewport_camera(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_light(self) -> Annotated[bool, "is_animatable=False"]:
        """Show lights"""
        ...
    @show_object_viewport_light.setter
    def show_object_viewport_light(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_speaker(self) -> Annotated[bool, "is_animatable=False"]:
        """Show speakers"""
        ...
    @show_object_viewport_speaker.setter
    def show_object_viewport_speaker(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_viewport_light_probe(self) -> Annotated[bool, "is_animatable=False"]:
        """Show light probes"""
        ...
    @show_object_viewport_light_probe.setter
    def show_object_viewport_light_probe(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_mesh(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of mesh objects"""
        ...
    @show_object_select_mesh.setter
    def show_object_select_mesh(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_curve(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of curves"""
        ...
    @show_object_select_curve.setter
    def show_object_select_curve(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_surf(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of surfaces"""
        ...
    @show_object_select_surf.setter
    def show_object_select_surf(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_meta(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of metaballs"""
        ...
    @show_object_select_meta.setter
    def show_object_select_meta(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_font(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of text objects"""
        ...
    @show_object_select_font.setter
    def show_object_select_font(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_curves(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of hair curves"""
        ...
    @show_object_select_curves.setter
    def show_object_select_curves(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_pointcloud(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of point clouds"""
        ...
    @show_object_select_pointcloud.setter
    def show_object_select_pointcloud(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_volume(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of volumes"""
        ...
    @show_object_select_volume.setter
    def show_object_select_volume(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_armature(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of armatures"""
        ...
    @show_object_select_armature.setter
    def show_object_select_armature(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_lattice(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of lattices"""
        ...
    @show_object_select_lattice.setter
    def show_object_select_lattice(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_empty(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of empties"""
        ...
    @show_object_select_empty.setter
    def show_object_select_empty(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_grease_pencil(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of Grease Pencil objects"""
        ...
    @show_object_select_grease_pencil.setter
    def show_object_select_grease_pencil(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_camera(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of cameras"""
        ...
    @show_object_select_camera.setter
    def show_object_select_camera(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_light(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of lights"""
        ...
    @show_object_select_light.setter
    def show_object_select_light(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_speaker(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of speakers"""
        ...
    @show_object_select_speaker.setter
    def show_object_select_speaker(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_object_select_light_probe(self) -> Annotated[bool, "is_animatable=False"]:
        """Allow selection of light probes"""
        ...
    @show_object_select_light_probe.setter
    def show_object_select_light_probe(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def icon_from_show_object_viewport(self) -> Annotated[int, "step=1", "is_animatable=False"]:

        ...