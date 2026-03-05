# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BoidRuleAvoid.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .BoidRule import BoidRule
from .Object import Object

class BoidRuleAvoid(BoidRule):

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
    def object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Object to avoid"""
        ...
    @object.setter
    def object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_predict(self) -> bool:
        """Predict target movement"""
        ...
    @use_predict.setter
    def use_predict(self, value: bool) -> None:
        ...
    @property
    def fear_factor(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Avoid object if danger from it is above this threshold"""
        ...
    @fear_factor.setter
    def fear_factor(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...