# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.XrActionMapItem.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .OperatorProperties import OperatorProperties
from .XrActionMapBinding import XrActionMapBinding
from .XrActionMapBindings import XrActionMapBindings
from .XrUserPath import XrUserPath
from .XrUserPaths import XrUserPaths
from .bpy_prop_collection import bpy_prop_collection

class XrActionMapItem(bpy_struct):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the action map item"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Annotated[Literal['FLOAT', 'VECTOR2D', 'POSE', 'VIBRATION'], "is_animatable=False"]:
        """Action type"""
        ...
    @type.setter
    def type(self, value: Annotated[Literal['FLOAT', 'VECTOR2D', 'POSE', 'VIBRATION'], "is_animatable=False"]):
        ...
    @property
    def user_paths(self) -> Annotated['XrUserPaths', "is_animatable=False"]:
        """OpenXR user paths"""
        ...
    @property
    def op(self) -> Annotated[str, "is_animatable=False"]:
        """Identifier of operator to call on action event"""
        ...
    @op.setter
    def op(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def op_name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of operator (translated) to call on action event"""
        ...
    @property
    def op_properties(self) -> Annotated[Optional['OperatorProperties'], "is_animatable=False"]:
        """Properties to set when the operator is called"""
        ...
    @property
    def op_mode(self) -> Annotated[Literal['PRESS', 'RELEASE', 'MODAL'], "is_animatable=False"]:
        """Operator execution mode"""
        ...
    @op_mode.setter
    def op_mode(self, value: Annotated[Literal['PRESS', 'RELEASE', 'MODAL'], "is_animatable=False"]):
        ...
    @property
    def bimanual(self) -> Annotated[bool, "is_animatable=False"]:
        """The action depends on the states/poses of both user paths"""
        ...
    @bimanual.setter
    def bimanual(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def pose_is_controller_grip(self) -> Annotated[bool, "is_animatable=False"]:
        """The action poses will be used for the VR controller grips"""
        ...
    @pose_is_controller_grip.setter
    def pose_is_controller_grip(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def pose_is_controller_aim(self) -> Annotated[bool, "is_animatable=False"]:
        """The action poses will be used for the VR controller aims"""
        ...
    @pose_is_controller_aim.setter
    def pose_is_controller_aim(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def haptic_name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of the haptic action to apply when executing this action"""
        ...
    @haptic_name.setter
    def haptic_name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def haptic_match_user_paths(self) -> Annotated[bool, "is_animatable=False"]:
        """Apply haptics to the same user paths for the haptic action and this action"""
        ...
    @haptic_match_user_paths.setter
    def haptic_match_user_paths(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def haptic_duration(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Haptic duration in seconds. 0.0 is the minimum supported duration."""
        ...
    @haptic_duration.setter
    def haptic_duration(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def haptic_frequency(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Frequency of the haptic vibration in hertz. 0.0 specifies the OpenXR runtime's default frequency."""
        ...
    @haptic_frequency.setter
    def haptic_frequency(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def haptic_amplitude(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Intensity of the haptic vibration, ranging from 0.0 to 1.0"""
        ...
    @haptic_amplitude.setter
    def haptic_amplitude(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def haptic_mode(self) -> Annotated[Literal['PRESS', 'RELEASE', 'PRESS_RELEASE', 'REPEAT'], "is_animatable=False"]:
        """Haptic application mode"""
        ...
    @haptic_mode.setter
    def haptic_mode(self, value: Annotated[Literal['PRESS', 'RELEASE', 'PRESS_RELEASE', 'REPEAT'], "is_animatable=False"]):
        ...
    @property
    def bindings(self) -> Annotated['XrActionMapBindings', "is_animatable=False"]:
        """Bindings for the action map item, mapping the action to an XR input"""
        ...
    @property
    def selected_binding(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Currently selected binding"""
        ...
    @selected_binding.setter
    def selected_binding(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...