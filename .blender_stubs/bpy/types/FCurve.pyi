# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FCurve.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .ActionGroup import ActionGroup
from .Driver import Driver
from .FCurveKeyframePoints import FCurveKeyframePoints
from .FCurveModifiers import FCurveModifiers
from .FCurveSample import FCurveSample
from .FModifier import FModifier
from .Keyframe import Keyframe
from .bpy_prop_collection import bpy_prop_collection

class FCurve(bpy_struct):

    @property
    def extrapolation(self) -> Literal['CONSTANT', 'LINEAR']:
        """Method used for evaluating value of F-Curve outside first and last keyframes"""
        ...
    @extrapolation.setter
    def extrapolation(self, value: Literal['CONSTANT', 'LINEAR']) -> None:
        ...
    @property
    def driver(self) -> Annotated[Optional['Driver'], "is_animatable=False"]:
        """Channel Driver (only set for Driver F-Curves)"""
        ...
    @property
    def group(self) -> Annotated[Optional['ActionGroup'], "is_animatable=False"]:
        """Action Group that this F-Curve belongs to"""
        ...
    @group.setter
    def group(self, value: Annotated[Optional['ActionGroup'], "is_animatable=False"]) -> None:
        ...
    @property
    def data_path(self) -> Annotated[str, "is_animatable=False"]:
        """RNA Path to property affected by F-Curve"""
        ...
    @data_path.setter
    def data_path(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def array_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Index to the specific property affected by F-Curve if applicable"""
        ...
    @array_index.setter
    def array_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def color_mode(self) -> Literal['AUTO_RAINBOW', 'AUTO_RGB', 'AUTO_YRGB', 'CUSTOM']:
        """Method used to determine color of F-Curve in Graph Editor"""
        ...
    @color_mode.setter
    def color_mode(self, value: Literal['AUTO_RAINBOW', 'AUTO_RGB', 'AUTO_YRGB', 'CUSTOM']) -> None:
        ...
    @property
    def color(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color of the F-Curve in the Graph Editor"""
        ...
    @color.setter
    def color(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def select(self) -> bool:
        """F-Curve is selected for editing"""
        ...
    @select.setter
    def select(self, value: bool) -> None:
        ...
    @property
    def lock(self) -> bool:
        """F-Curve's settings cannot be edited"""
        ...
    @lock.setter
    def lock(self, value: bool) -> None:
        ...
    @property
    def mute(self) -> bool:
        """Disable F-Curve evaluation"""
        ...
    @mute.setter
    def mute(self, value: bool) -> None:
        ...
    @property
    def hide(self) -> bool:
        """F-Curve and its keyframes are hidden in the Graph Editor graphs"""
        ...
    @hide.setter
    def hide(self, value: bool) -> None:
        ...
    @property
    def auto_smoothing(self) -> Literal['NONE', 'CONT_ACCEL']:
        """Algorithm used to compute automatic handles"""
        ...
    @auto_smoothing.setter
    def auto_smoothing(self, value: Literal['NONE', 'CONT_ACCEL']) -> None:
        ...
    @property
    def is_valid(self) -> bool:
        """False when F-Curve could not be evaluated in past, so should be skipped when evaluating"""
        ...
    @is_valid.setter
    def is_valid(self, value: bool) -> None:
        ...
    @property
    def is_empty(self) -> bool:
        """True if the curve contributes no animation due to lack of keyframes or useful modifiers, and should be deleted"""
        ...
    @property
    def sampled_points(self) -> Annotated[bpy_prop_collection['FCurveSample'], "is_animatable=False"]:
        """Sampled animation data"""
        ...
    @property
    def keyframe_points(self) -> Annotated['FCurveKeyframePoints', "is_animatable=False"]:
        """User-editable keyframes"""
        ...
    @property
    def modifiers(self) -> Annotated['FCurveModifiers', "is_animatable=False"]:
        """Modifiers affecting the shape of the F-Curve"""
        ...
    def evaluate(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def range(self, *args, **kwargs) -> Any: ...
    def update_autoflags(self, *args, **kwargs) -> Any: ...
    def convert_to_samples(self, *args, **kwargs) -> Any: ...
    def convert_to_keyframes(self, *args, **kwargs) -> Any: ...
    def bake(self, *args, **kwargs) -> Any: ...