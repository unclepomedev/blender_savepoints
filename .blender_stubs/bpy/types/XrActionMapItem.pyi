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

    name: Annotated[str, "is_animatable=False"]
    """Name of the action map item"""
    type: Annotated[Literal['FLOAT', 'VECTOR2D', 'POSE', 'VIBRATION'], "is_animatable=False"]
    """Action type"""
    @property
    def user_paths(self) -> Annotated['XrUserPaths', "is_animatable=False"]:
        """OpenXR user paths"""
        ...
    op: Annotated[str, "is_animatable=False"]
    """Identifier of operator to call on action event"""
    @property
    def op_name(self) -> Annotated[str, "is_animatable=False"]:
        """Name of operator (translated) to call on action event"""
        ...
    @property
    def op_properties(self) -> Annotated[Optional['OperatorProperties'], "is_animatable=False"]:
        """Properties to set when the operator is called"""
        ...
    op_mode: Annotated[Literal['PRESS', 'RELEASE', 'MODAL'], "is_animatable=False"]
    """Operator execution mode"""
    bimanual: Annotated[bool, "is_animatable=False"]
    """The action depends on the states/poses of both user paths"""
    pose_is_controller_grip: Annotated[bool, "is_animatable=False"]
    """The action poses will be used for the VR controller grips"""
    pose_is_controller_aim: Annotated[bool, "is_animatable=False"]
    """The action poses will be used for the VR controller aims"""
    haptic_name: Annotated[str, "is_animatable=False"]
    """Name of the haptic action to apply when executing this action"""
    haptic_match_user_paths: Annotated[bool, "is_animatable=False"]
    """Apply haptics to the same user paths for the haptic action and this action"""
    haptic_duration: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Haptic duration in seconds. 0.0 is the minimum supported duration."""
    haptic_frequency: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Frequency of the haptic vibration in hertz. 0.0 specifies the OpenXR runtime's default frequency."""
    haptic_amplitude: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Intensity of the haptic vibration, ranging from 0.0 to 1.0"""
    haptic_mode: Annotated[Literal['PRESS', 'RELEASE', 'PRESS_RELEASE', 'REPEAT'], "is_animatable=False"]
    """Haptic application mode"""
    @property
    def bindings(self) -> Annotated['XrActionMapBindings', "is_animatable=False"]:
        """Bindings for the action map item, mapping the action to an XR input"""
        ...
    selected_binding: Annotated[int, "step=1", "is_animatable=False"]
    """Currently selected binding"""