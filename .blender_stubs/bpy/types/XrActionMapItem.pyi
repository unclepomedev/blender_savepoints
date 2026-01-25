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
from .OperatorProperties import OperatorProperties
from .XrActionMapBinding import XrActionMapBinding
from .XrUserPath import XrUserPath
class XrActionMapItem(bpy_struct):
    name: str
    type: str
    user_paths: bpy_prop_collection['XrUserPath']
    op: str
    op_name: str
    op_properties: 'OperatorProperties'
    op_mode: str
    bimanual: bool
    pose_is_controller_grip: bool
    pose_is_controller_aim: bool
    haptic_name: str
    haptic_match_user_paths: bool
    haptic_duration: float
    haptic_frequency: float
    haptic_amplitude: float
    haptic_mode: str
    bindings: bpy_prop_collection['XrActionMapBinding']
    selected_binding: int