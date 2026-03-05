# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BoidRuleAvoidCollision.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .BoidRule import BoidRule

class BoidRuleAvoidCollision(BoidRule):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Boid rule name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def type(self) -> Literal['GOAL', 'AVOID', 'AVOID_COLLISION', 'SEPARATE', 'FLOCK', 'FOLLOW_LEADER', 'AVERAGE_SPEED', 'FIGHT']:

        ...
    @property
    def use_in_air(self) -> bool:
        """Use rule when boid is flying"""
        ...
    @use_in_air.setter
    def use_in_air(self, value: bool):
        ...
    @property
    def use_on_land(self) -> bool:
        """Use rule when boid is on land"""
        ...
    @use_on_land.setter
    def use_on_land(self, value: bool):
        ...
    @property
    def use_avoid(self) -> bool:
        """Avoid collision with other boids"""
        ...
    @use_avoid.setter
    def use_avoid(self, value: bool):
        ...
    @property
    def use_avoid_collision(self) -> bool:
        """Avoid collision with deflector objects"""
        ...
    @use_avoid_collision.setter
    def use_avoid_collision(self, value: bool):
        ...
    @property
    def look_ahead(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Time to look ahead in seconds"""
        ...
    @look_ahead.setter
    def look_ahead(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...