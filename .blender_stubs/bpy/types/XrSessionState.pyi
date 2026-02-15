# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.XrSessionState.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .XrActionMap import XrActionMap
from .XrActionMaps import XrActionMaps
from .bpy_prop_collection import bpy_prop_collection

class XrSessionState(bpy_struct):

    @property
    def viewer_pose_location(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Last known location of the viewer pose (center between the eyes) in world space"""
        ...
    @property
    def viewer_pose_rotation(self) -> Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Last known rotation of the viewer pose (center between the eyes) in world space"""
        ...
    navigation_location: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]
    """Location offset to apply to base pose when determining viewer location"""
    navigation_rotation: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3", "is_animatable=False"]
    """Rotation offset to apply to base pose when determining viewer rotation"""
    navigation_scale: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Additional scale multiplier to apply to base scale when determining viewer scale"""
    @property
    def actionmaps(self) -> Annotated['XrActionMaps', "is_animatable=False"]:

        ...
    active_actionmap: Annotated[int, "step=1", "is_animatable=False"]

    selected_actionmap: Annotated[int, "step=1", "is_animatable=False"]

    def is_running(self, *args, **kwargs) -> Any: ...
    def reset_to_base_pose(self, *args, **kwargs) -> Any: ...
    def action_set_create(self, *args, **kwargs) -> Any: ...
    def action_create(self, *args, **kwargs) -> Any: ...
    def action_binding_create(self, *args, **kwargs) -> Any: ...
    def active_action_set_set(self, *args, **kwargs) -> Any: ...
    def controller_pose_actions_set(self, *args, **kwargs) -> Any: ...
    def action_state_get(self, *args, **kwargs) -> Any: ...
    def haptic_action_apply(self, *args, **kwargs) -> Any: ...
    def haptic_action_stop(self, *args, **kwargs) -> Any: ...
    def controller_grip_location_get(self, *args, **kwargs) -> Any: ...
    def controller_grip_rotation_get(self, *args, **kwargs) -> Any: ...
    def controller_aim_location_get(self, *args, **kwargs) -> Any: ...
    def controller_aim_rotation_get(self, *args, **kwargs) -> Any: ...