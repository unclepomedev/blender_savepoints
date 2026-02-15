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
    base_pose_type: Annotated[Literal['SCENE_CAMERA', 'OBJECT', 'CUSTOM'], "is_animatable=False"]
    """Define where the location and rotation for the VR view come from, to which translation and rotation deltas from the VR headset will be applied to"""
    base_pose_object: Annotated[Optional['Object'], "is_animatable=False"]
    """Object to take the location and rotation to which translation and rotation deltas from the VR headset will be applied to"""
    base_pose_location: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5", "is_animatable=False"]
    """Coordinates to apply translation deltas from the VR headset to"""
    base_pose_angle: Annotated[float, "subtype='AXISANGLE'", "step=10.0", "precision=3", "is_animatable=False"]
    """Rotation angle around the Z-Axis to apply the rotation deltas from the VR headset to"""
    base_scale: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Uniform scale to apply to VR view"""
    show_floor: Annotated[bool, "is_animatable=False"]
    """Show the ground plane grid"""
    show_passthrough: Annotated[bool, "is_animatable=False"]
    """Show the passthrough view"""
    show_annotation: Annotated[bool, "is_animatable=False"]
    """Show annotations for this view"""
    show_selection: Annotated[bool, "is_animatable=False"]
    """Show selection outlines"""
    show_controllers: Annotated[bool, "is_animatable=False"]
    """Show VR controllers (requires VR actions for controller poses)"""
    show_custom_overlays: Annotated[bool, "is_animatable=False"]
    """Show custom VR overlays"""
    show_object_extras: Annotated[bool, "is_animatable=False"]
    """Show object extras, including empties, lights, and cameras"""
    controller_draw_style: Annotated[Literal['DARK', 'LIGHT', 'DARK_RAY', 'LIGHT_RAY'], "is_animatable=False"]
    """Style to use when drawing VR controllers"""
    clip_start: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]
    """VR viewport near clipping distance"""
    clip_end: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1000.0", "precision=3", "is_animatable=False"]
    """VR viewport far clipping distance"""
    fly_speed: Annotated[float, "step=50.0", "precision=3", "is_animatable=False"]
    """Fly speed in meters per second"""
    use_positional_tracking: Annotated[bool, "is_animatable=False"]
    """Allow VR headsets to affect the location in virtual space, in addition to the rotation"""
    use_absolute_tracking: Annotated[bool, "is_animatable=False"]
    """Allow the VR tracking origin to be defined independently of the headset location"""
    show_object_viewport_mesh: Annotated[bool, "is_animatable=False"]
    """Show mesh objects"""
    show_object_viewport_curve: Annotated[bool, "is_animatable=False"]
    """Show curves"""
    show_object_viewport_surf: Annotated[bool, "is_animatable=False"]
    """Show surfaces"""
    show_object_viewport_meta: Annotated[bool, "is_animatable=False"]
    """Show metaballs"""
    show_object_viewport_font: Annotated[bool, "is_animatable=False"]
    """Show text objects"""
    show_object_viewport_curves: Annotated[bool, "is_animatable=False"]
    """Show hair curves"""
    show_object_viewport_pointcloud: Annotated[bool, "is_animatable=False"]
    """Show point clouds"""
    show_object_viewport_volume: Annotated[bool, "is_animatable=False"]
    """Show volumes"""
    show_object_viewport_armature: Annotated[bool, "is_animatable=False"]
    """Show armatures"""
    show_object_viewport_lattice: Annotated[bool, "is_animatable=False"]
    """Show lattices"""
    show_object_viewport_empty: Annotated[bool, "is_animatable=False"]
    """Show empties"""
    show_object_viewport_grease_pencil: Annotated[bool, "is_animatable=False"]
    """Show Grease Pencil objects"""
    show_object_viewport_camera: Annotated[bool, "is_animatable=False"]
    """Show cameras"""
    show_object_viewport_light: Annotated[bool, "is_animatable=False"]
    """Show lights"""
    show_object_viewport_speaker: Annotated[bool, "is_animatable=False"]
    """Show speakers"""
    show_object_viewport_light_probe: Annotated[bool, "is_animatable=False"]
    """Show light probes"""
    show_object_select_mesh: Annotated[bool, "is_animatable=False"]
    """Allow selection of mesh objects"""
    show_object_select_curve: Annotated[bool, "is_animatable=False"]
    """Allow selection of curves"""
    show_object_select_surf: Annotated[bool, "is_animatable=False"]
    """Allow selection of surfaces"""
    show_object_select_meta: Annotated[bool, "is_animatable=False"]
    """Allow selection of metaballs"""
    show_object_select_font: Annotated[bool, "is_animatable=False"]
    """Allow selection of text objects"""
    show_object_select_curves: Annotated[bool, "is_animatable=False"]
    """Allow selection of hair curves"""
    show_object_select_pointcloud: Annotated[bool, "is_animatable=False"]
    """Allow selection of point clouds"""
    show_object_select_volume: Annotated[bool, "is_animatable=False"]
    """Allow selection of volumes"""
    show_object_select_armature: Annotated[bool, "is_animatable=False"]
    """Allow selection of armatures"""
    show_object_select_lattice: Annotated[bool, "is_animatable=False"]
    """Allow selection of lattices"""
    show_object_select_empty: Annotated[bool, "is_animatable=False"]
    """Allow selection of empties"""
    show_object_select_grease_pencil: Annotated[bool, "is_animatable=False"]
    """Allow selection of Grease Pencil objects"""
    show_object_select_camera: Annotated[bool, "is_animatable=False"]
    """Allow selection of cameras"""
    show_object_select_light: Annotated[bool, "is_animatable=False"]
    """Allow selection of lights"""
    show_object_select_speaker: Annotated[bool, "is_animatable=False"]
    """Allow selection of speakers"""
    show_object_select_light_probe: Annotated[bool, "is_animatable=False"]
    """Allow selection of light probes"""
    @property
    def icon_from_show_object_viewport(self) -> Annotated[int, "step=1", "is_animatable=False"]:

        ...