# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BoidSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .BoidRule import BoidRule
from .BoidState import BoidState
from .bpy_prop_collection import bpy_prop_collection

class BoidSettings(bpy_struct):

    @property
    def land_smooth(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """How smoothly the boids land"""
        ...
    @land_smooth.setter
    def land_smooth(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def bank(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of rotation around velocity vector on turns"""
        ...
    @bank.setter
    def bank(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def pitch(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Amount of rotation around side vector"""
        ...
    @pitch.setter
    def pitch(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def height(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Boid height relative to particle size"""
        ...
    @height.setter
    def height(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def states(self) -> Annotated[bpy_prop_collection['BoidState'], "is_animatable=False"]:

        ...
    @property
    def active_boid_state(self) -> Annotated[Optional['BoidRule'], "is_animatable=False"]:

        ...
    @property
    def active_boid_state_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:

        ...
    @active_boid_state_index.setter
    def active_boid_state_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]):
        ...
    @property
    def health(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Initial boid health when born"""
        ...
    @health.setter
    def health(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def strength(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum caused damage on attack per second"""
        ...
    @strength.setter
    def strength(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def aggression(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Boid will fight this times stronger enemy"""
        ...
    @aggression.setter
    def aggression(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def accuracy(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Accuracy of attack"""
        ...
    @accuracy.setter
    def accuracy(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def range(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum distance from which a boid can attack"""
        ...
    @range.setter
    def range(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def air_speed_min(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Minimum speed in air (relative to maximum speed)"""
        ...
    @air_speed_min.setter
    def air_speed_min(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def air_speed_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum speed in air"""
        ...
    @air_speed_max.setter
    def air_speed_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def air_acc_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum acceleration in air (relative to maximum speed)"""
        ...
    @air_acc_max.setter
    def air_acc_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def air_ave_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum angular velocity in air (relative to 180 degrees)"""
        ...
    @air_ave_max.setter
    def air_ave_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def air_personal_space(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Radius of boids personal space in air (% of particle size)"""
        ...
    @air_personal_space.setter
    def air_personal_space(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def land_jump_speed(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum speed for jumping"""
        ...
    @land_jump_speed.setter
    def land_jump_speed(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def land_speed_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum speed on land"""
        ...
    @land_speed_max.setter
    def land_speed_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def land_acc_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum acceleration on land (relative to maximum speed)"""
        ...
    @land_acc_max.setter
    def land_acc_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def land_ave_max(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum angular velocity on land (relative to 180 degrees)"""
        ...
    @land_ave_max.setter
    def land_ave_max(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def land_personal_space(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Radius of boids personal space on land (% of particle size)"""
        ...
    @land_personal_space.setter
    def land_personal_space(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def land_stick_force(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """How strong a force must be to start effecting a boid on land"""
        ...
    @land_stick_force.setter
    def land_stick_force(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def use_flight(self) -> bool:
        """Allow boids to move in air"""
        ...
    @use_flight.setter
    def use_flight(self, value: bool):
        ...
    @property
    def use_land(self) -> bool:
        """Allow boids to move on land"""
        ...
    @use_land.setter
    def use_land(self, value: bool):
        ...
    @property
    def use_climb(self) -> bool:
        """Allow boids to climb goal objects"""
        ...
    @use_climb.setter
    def use_climb(self, value: bool):
        ...