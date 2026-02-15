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

    land_smooth: Annotated[float, "step=10.0", "precision=3"]
    """How smoothly the boids land"""
    bank: Annotated[float, "step=10.0", "precision=3"]
    """Amount of rotation around velocity vector on turns"""
    pitch: Annotated[float, "step=10.0", "precision=3"]
    """Amount of rotation around side vector"""
    height: Annotated[float, "step=10.0", "precision=3"]
    """Boid height relative to particle size"""
    @property
    def states(self) -> Annotated[bpy_prop_collection['BoidState'], "is_animatable=False"]:

        ...
    @property
    def active_boid_state(self) -> Annotated[Optional['BoidRule'], "is_animatable=False"]:

        ...
    active_boid_state_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]

    health: Annotated[float, "step=10.0", "precision=3"]
    """Initial boid health when born"""
    strength: Annotated[float, "step=10.0", "precision=3"]
    """Maximum caused damage on attack per second"""
    aggression: Annotated[float, "step=10.0", "precision=3"]
    """Boid will fight this times stronger enemy"""
    accuracy: Annotated[float, "step=10.0", "precision=3"]
    """Accuracy of attack"""
    range: Annotated[float, "step=10.0", "precision=3"]
    """Maximum distance from which a boid can attack"""
    air_speed_min: Annotated[float, "step=10.0", "precision=3"]
    """Minimum speed in air (relative to maximum speed)"""
    air_speed_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum speed in air"""
    air_acc_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum acceleration in air (relative to maximum speed)"""
    air_ave_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum angular velocity in air (relative to 180 degrees)"""
    air_personal_space: Annotated[float, "step=10.0", "precision=3"]
    """Radius of boids personal space in air (% of particle size)"""
    land_jump_speed: Annotated[float, "step=10.0", "precision=3"]
    """Maximum speed for jumping"""
    land_speed_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum speed on land"""
    land_acc_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum acceleration on land (relative to maximum speed)"""
    land_ave_max: Annotated[float, "step=10.0", "precision=3"]
    """Maximum angular velocity on land (relative to 180 degrees)"""
    land_personal_space: Annotated[float, "step=10.0", "precision=3"]
    """Radius of boids personal space on land (% of particle size)"""
    land_stick_force: Annotated[float, "step=10.0", "precision=3"]
    """How strong a force must be to start effecting a boid on land"""
    use_flight: bool
    """Allow boids to move in air"""
    use_land: bool
    """Allow boids to move on land"""
    use_climb: bool
    """Allow boids to climb goal objects"""