# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.EffectorWeights.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .Collection import Collection

class EffectorWeights(bpy_struct):

    @property
    def apply_to_hair_growing(self) -> bool:
        """Use force fields when growing hair"""
        ...
    @apply_to_hair_growing.setter
    def apply_to_hair_growing(self, value: bool) -> None:
        ...
    @property
    def collection(self) -> Annotated[Optional['Collection'], "is_animatable=False"]:
        """Limit effectors to this collection"""
        ...
    @collection.setter
    def collection(self, value: Annotated[Optional['Collection'], "is_animatable=False"]) -> None:
        ...
    @property
    def gravity(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Global gravity weight"""
        ...
    @gravity.setter
    def gravity(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def all(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """All effector's weight"""
        ...
    @all.setter
    def all(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def force(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Force effector weight"""
        ...
    @force.setter
    def force(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def vortex(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Vortex effector weight"""
        ...
    @vortex.setter
    def vortex(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def magnetic(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Magnetic effector weight"""
        ...
    @magnetic.setter
    def magnetic(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def wind(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Wind effector weight"""
        ...
    @wind.setter
    def wind(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def curve_guide(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Curve guide effector weight"""
        ...
    @curve_guide.setter
    def curve_guide(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def texture(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Texture effector weight"""
        ...
    @texture.setter
    def texture(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def harmonic(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Harmonic effector weight"""
        ...
    @harmonic.setter
    def harmonic(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def charge(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Charge effector weight"""
        ...
    @charge.setter
    def charge(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def lennardjones(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Lennard-Jones effector weight"""
        ...
    @lennardjones.setter
    def lennardjones(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def boid(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Boid effector weight"""
        ...
    @boid.setter
    def boid(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def turbulence(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Turbulence effector weight"""
        ...
    @turbulence.setter
    def turbulence(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def drag(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Drag effector weight"""
        ...
    @drag.setter
    def drag(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...
    @property
    def smokeflow(self) -> Annotated[float, "step=0.10000000149011612", "precision=3"]:
        """Fluid Flow effector weight"""
        ...
    @smokeflow.setter
    def smokeflow(self, value: Annotated[float, "step=0.10000000149011612", "precision=3"]) -> None:
        ...