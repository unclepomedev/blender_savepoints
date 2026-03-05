# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FModifierCycles.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .FModifier import FModifier

class FModifierCycles(FModifier):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """F-Curve Modifier name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def type(self) -> Literal['NULL', 'GENERATOR', 'FNGENERATOR', 'ENVELOPE', 'CYCLES', 'NOISE', 'LIMITS', 'STEPPED']:
        """F-Curve Modifier Type"""
        ...
    @property
    def show_expanded(self) -> bool:
        """F-Curve Modifier's panel is expanded in UI"""
        ...
    @show_expanded.setter
    def show_expanded(self, value: bool) -> None:
        ...
    @property
    def mute(self) -> bool:
        """Enable F-Curve modifier evaluation"""
        ...
    @mute.setter
    def mute(self, value: bool) -> None:
        ...
    @property
    def is_valid(self) -> bool:
        """F-Curve Modifier has invalid settings and will not be evaluated"""
        ...
    @property
    def active(self) -> bool:
        """F-Curve modifier will show settings in the editor"""
        ...
    @active.setter
    def active(self, value: bool) -> None:
        ...
    @property
    def use_restricted_range(self) -> bool:
        """F-Curve Modifier is only applied for the specified frame range to help mask off effects in order to chain them"""
        ...
    @use_restricted_range.setter
    def use_restricted_range(self, value: bool) -> None:
        ...
    @property
    def frame_start(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Frame that modifier's influence starts (if Restrict Frame Range is in use)"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def frame_end(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Frame that modifier's influence ends (if Restrict Frame Range is in use)"""
        ...
    @frame_end.setter
    def frame_end(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def blend_in(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Number of frames from start frame for influence to take effect"""
        ...
    @blend_in.setter
    def blend_in(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def blend_out(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Number of frames from end frame for influence to fade out"""
        ...
    @blend_out.setter
    def blend_out(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_influence(self) -> bool:
        """F-Curve Modifier's effects will be tempered by a default factor"""
        ...
    @use_influence.setter
    def use_influence(self, value: bool) -> None:
        ...
    @property
    def influence(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Amount of influence F-Curve Modifier will have when not fading in/out"""
        ...
    @influence.setter
    def influence(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def mode_before(self) -> Literal['NONE', 'REPEAT', 'REPEAT_OFFSET', 'MIRROR']:
        """Cycling mode to use before first keyframe"""
        ...
    @mode_before.setter
    def mode_before(self, value: Literal['NONE', 'REPEAT', 'REPEAT_OFFSET', 'MIRROR']) -> None:
        ...
    @property
    def cycles_before(self) -> Annotated[int, "step=1"]:
        """Maximum number of cycles to allow before first keyframe (0 = infinite)"""
        ...
    @cycles_before.setter
    def cycles_before(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def mode_after(self) -> Literal['NONE', 'REPEAT', 'REPEAT_OFFSET', 'MIRROR']:
        """Cycling mode to use after last keyframe"""
        ...
    @mode_after.setter
    def mode_after(self, value: Literal['NONE', 'REPEAT', 'REPEAT_OFFSET', 'MIRROR']) -> None:
        ...
    @property
    def cycles_after(self) -> Annotated[int, "step=1"]:
        """Maximum number of cycles to allow after last keyframe (0 = infinite)"""
        ...
    @cycles_after.setter
    def cycles_after(self, value: Annotated[int, "step=1"]) -> None:
        ...