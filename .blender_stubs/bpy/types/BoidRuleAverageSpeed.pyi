# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BoidRuleAverageSpeed.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .BoidRule import BoidRule

class BoidRuleAverageSpeed(BoidRule):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Boid rule name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def type(self) -> Literal['GOAL', 'AVOID', 'AVOID_COLLISION', 'SEPARATE', 'FLOCK', 'FOLLOW_LEADER', 'AVERAGE_SPEED', 'FIGHT']:

        ...
    @property
    def use_in_air(self) -> bool:
        """Use rule when boid is flying"""
        ...
    @use_in_air.setter
    def use_in_air(self, value: bool) -> None:
        ...
    @property
    def use_on_land(self) -> bool:
        """Use rule when boid is on land"""
        ...
    @use_on_land.setter
    def use_on_land(self, value: bool) -> None:
        ...
    @property
    def wander(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """How fast velocity's direction is randomized"""
        ...
    @wander.setter
    def wander(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def level(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """How much velocity's z-component is kept constant"""
        ...
    @level.setter
    def level(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def speed(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Percentage of maximum speed"""
        ...
    @speed.setter
    def speed(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...