# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .BoidRule import BoidRule
from .BoidState import BoidState
class BoidSettings(bpy_struct):
    land_smooth: float
    bank: float
    pitch: float
    height: float
    states: bpy_prop_collection['BoidState']
    active_boid_state: 'BoidRule'
    active_boid_state_index: int
    health: float
    strength: float
    aggression: float
    accuracy: float
    range: float
    air_speed_min: float
    air_speed_max: float
    air_acc_max: float
    air_ave_max: float
    air_personal_space: float
    land_jump_speed: float
    land_speed_max: float
    land_acc_max: float
    land_ave_max: float
    land_personal_space: float
    land_stick_force: float
    use_flight: bool
    use_land: bool
    use_climb: bool