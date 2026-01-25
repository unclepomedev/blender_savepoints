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
from .Object import Object
from .View3DShading import View3DShading
class XrSessionSettings(bpy_struct):
    shading: 'View3DShading'
    base_pose_type: str
    base_pose_object: 'Object'
    base_pose_location: float
    base_pose_angle: float
    base_scale: float
    show_floor: bool
    show_passthrough: bool
    show_annotation: bool
    show_selection: bool
    show_controllers: bool
    show_custom_overlays: bool
    show_object_extras: bool
    controller_draw_style: str
    clip_start: float
    clip_end: float
    fly_speed: float
    use_positional_tracking: bool
    use_absolute_tracking: bool
    show_object_viewport_mesh: bool
    show_object_viewport_curve: bool
    show_object_viewport_surf: bool
    show_object_viewport_meta: bool
    show_object_viewport_font: bool
    show_object_viewport_curves: bool
    show_object_viewport_pointcloud: bool
    show_object_viewport_volume: bool
    show_object_viewport_armature: bool
    show_object_viewport_lattice: bool
    show_object_viewport_empty: bool
    show_object_viewport_grease_pencil: bool
    show_object_viewport_camera: bool
    show_object_viewport_light: bool
    show_object_viewport_speaker: bool
    show_object_viewport_light_probe: bool
    show_object_select_mesh: bool
    show_object_select_curve: bool
    show_object_select_surf: bool
    show_object_select_meta: bool
    show_object_select_font: bool
    show_object_select_curves: bool
    show_object_select_pointcloud: bool
    show_object_select_volume: bool
    show_object_select_armature: bool
    show_object_select_lattice: bool
    show_object_select_empty: bool
    show_object_select_grease_pencil: bool
    show_object_select_camera: bool
    show_object_select_light: bool
    show_object_select_speaker: bool
    show_object_select_light_probe: bool
    icon_from_show_object_viewport: int