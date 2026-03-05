# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ParticleEdit.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Object import Object
from .ParticleBrush import ParticleBrush

class ParticleEdit(bpy_struct):

    @property
    def tool(self) -> Annotated[Literal['COMB', 'SMOOTH', 'ADD', 'LENGTH', 'PUFF', 'CUT', 'WEIGHT'], "is_animatable=False"]:

        ...
    @tool.setter
    def tool(self, value: Annotated[Literal['COMB', 'SMOOTH', 'ADD', 'LENGTH', 'PUFF', 'CUT', 'WEIGHT'], "is_animatable=False"]) -> None:
        ...
    @property
    def select_mode(self) -> Annotated[Literal['PATH', 'POINT', 'TIP'], "is_animatable=False"]:
        """Particle select and display mode"""
        ...
    @select_mode.setter
    def select_mode(self, value: Annotated[Literal['PATH', 'POINT', 'TIP'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_preserve_length(self) -> Annotated[bool, "is_animatable=False"]:
        """Keep path lengths constant"""
        ...
    @use_preserve_length.setter
    def use_preserve_length(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_preserve_root(self) -> Annotated[bool, "is_animatable=False"]:
        """Keep root keys unmodified"""
        ...
    @use_preserve_root.setter
    def use_preserve_root(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_emitter_deflect(self) -> Annotated[bool, "is_animatable=False"]:
        """Keep paths from intersecting the emitter"""
        ...
    @use_emitter_deflect.setter
    def use_emitter_deflect(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def emitter_distance(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Distance to keep particles away from the emitter"""
        ...
    @emitter_distance.setter
    def emitter_distance(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def use_fade_time(self) -> Annotated[bool, "is_animatable=False"]:
        """Fade paths and keys further away from current frame"""
        ...
    @use_fade_time.setter
    def use_fade_time(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_auto_velocity(self) -> Annotated[bool, "is_animatable=False"]:
        """Calculate point velocities automatically"""
        ...
    @use_auto_velocity.setter
    def use_auto_velocity(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def show_particles(self) -> Annotated[bool, "is_animatable=False"]:
        """Display actual particles"""
        ...
    @show_particles.setter
    def show_particles(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_default_interpolate(self) -> Annotated[bool, "is_animatable=False"]:
        """Interpolate new particles from the existing ones"""
        ...
    @use_default_interpolate.setter
    def use_default_interpolate(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def default_key_count(self) -> Annotated[int, "step=10", "is_animatable=False"]:
        """How many keys to make new particles with"""
        ...
    @default_key_count.setter
    def default_key_count(self, value: Annotated[int, "step=10", "is_animatable=False"]) -> None:
        ...
    @property
    def brush(self) -> Annotated[Optional['ParticleBrush'], "is_animatable=False"]:

        ...
    @property
    def display_step(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """How many steps to display the path with"""
        ...
    @display_step.setter
    def display_step(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def fade_frames(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """How many frames to fade"""
        ...
    @fade_frames.setter
    def fade_frames(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def type(self) -> Annotated[Literal['PARTICLES', 'SOFT_BODY', 'CLOTH'], "is_animatable=False"]:

        ...
    @type.setter
    def type(self, value: Annotated[Literal['PARTICLES', 'SOFT_BODY', 'CLOTH'], "is_animatable=False"]) -> None:
        ...
    @property
    def is_editable(self) -> Annotated[bool, "is_animatable=False"]:
        """A valid edit mode exists"""
        ...
    @property
    def is_hair(self) -> Annotated[bool, "is_animatable=False"]:
        """Editing hair"""
        ...
    @property
    def object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """The edited object"""
        ...
    @property
    def shape_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Outer shape to use for tools"""
        ...
    @shape_object.setter
    def shape_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...