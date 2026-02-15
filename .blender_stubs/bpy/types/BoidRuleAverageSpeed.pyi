# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .BoidRule import BoidRule
class BoidRuleAverageSpeed(BoidRule):
    name: Annotated[str, "is_animatable=False"]
    """Boid rule name"""
    @property
    def type(self) -> Literal['GOAL', 'AVOID', 'AVOID_COLLISION', 'SEPARATE', 'FLOCK', 'FOLLOW_LEADER', 'AVERAGE_SPEED', 'FIGHT']:
        ...
    use_in_air: bool
    """Use rule when boid is flying"""
    use_on_land: bool
    """Use rule when boid is on land"""
    wander: Annotated[float, "step=10.0", "precision=3"]
    """How fast velocity's direction is randomized"""
    level: Annotated[float, "step=10.0", "precision=3"]
    """How much velocity's z-component is kept constant"""
    speed: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Percentage of maximum speed"""