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
class XrEventData(bpy_struct):
    @property
    def action_set(self) -> Annotated[str, "is_animatable=False"]:
        """XR action set name"""
        ...
    @property
    def action(self) -> Annotated[str, "is_animatable=False"]:
        """XR action name"""
        ...
    @property
    def user_path(self) -> Annotated[str, "is_animatable=False"]:
        """User path of the action. E.g. "/user/hand/left" """
        ...
    @property
    def user_path_other(self) -> Annotated[str, "is_animatable=False"]:
        """Other user path, for bimanual actions. E.g. "/user/hand/right" """
        ...
    @property
    def type(self) -> Annotated[Literal['FLOAT', 'VECTOR2D', 'POSE', 'VIBRATION'], "is_animatable=False"]:
        """XR action type"""
        ...
    @property
    def state(self) -> Annotated[list[float], "step=10.0", "precision=3", "is_animatable=False"]:
        """XR action values corresponding to type"""
        ...
    @property
    def state_other(self) -> Annotated[list[float], "step=10.0", "precision=3", "is_animatable=False"]:
        """State of the other user path for bimanual actions"""
        ...
    @property
    def float_threshold(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Input threshold for float/2D vector actions"""
        ...
    @property
    def controller_location(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Location of the action's corresponding controller aim in world space"""
        ...
    @property
    def controller_rotation(self) -> Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Rotation of the action's corresponding controller aim in world space"""
        ...
    @property
    def controller_location_other(self) -> Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Controller aim location of the other user path for bimanual actions"""
        ...
    @property
    def controller_rotation_other(self) -> Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Controller aim rotation of the other user path for bimanual actions"""
        ...
    @property
    def bimanual(self) -> Annotated[bool, "is_animatable=False"]:
        """Whether bimanual interaction is occurring"""
        ...