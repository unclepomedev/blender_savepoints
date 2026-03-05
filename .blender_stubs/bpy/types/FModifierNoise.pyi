# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.FModifierNoise.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .FModifier import FModifier

class FModifierNoise(FModifier):

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
    def blend_type(self) -> Literal['REPLACE', 'ADD', 'SUBTRACT', 'MULTIPLY']:
        """Method of modifying the existing F-Curve"""
        ...
    @blend_type.setter
    def blend_type(self, value: Literal['REPLACE', 'ADD', 'SUBTRACT', 'MULTIPLY']) -> None:
        ...
    @property
    def scale(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Scaling (in time) of the noise"""
        ...
    @scale.setter
    def scale(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def strength(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amplitude of the noise - the amount that it modifies the underlying curve"""
        ...
    @strength.setter
    def strength(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def phase(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """A random seed for the noise effect"""
        ...
    @phase.setter
    def phase(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def offset(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Time offset for the noise effect"""
        ...
    @offset.setter
    def offset(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def lacunarity(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Gap between successive frequencies. Depth needs to be greater than 0 for this to have an effect"""
        ...
    @lacunarity.setter
    def lacunarity(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def roughness(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of high frequency detail. Depth needs to be greater than 0 for this to have an effect"""
        ...
    @roughness.setter
    def roughness(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def depth(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Amount of fine level detail present in the noise"""
        ...
    @depth.setter
    def depth(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def use_legacy_noise(self) -> bool:
        """Use the legacy way of generating noise. Has the issue that it can produce values outside of -1/1"""
        ...
    @use_legacy_noise.setter
    def use_legacy_noise(self, value: bool) -> None:
        ...