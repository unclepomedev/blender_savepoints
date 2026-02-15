# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BoidRuleFollowLeader.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .BoidRule import BoidRule
from .Object import Object

class BoidRuleFollowLeader(BoidRule):

    name: Annotated[str, "is_animatable=False"]
    """Boid rule name"""
    @property
    def type(self) -> Literal['GOAL', 'AVOID', 'AVOID_COLLISION', 'SEPARATE', 'FLOCK', 'FOLLOW_LEADER', 'AVERAGE_SPEED', 'FIGHT']:

        ...
    use_in_air: bool
    """Use rule when boid is flying"""
    use_on_land: bool
    """Use rule when boid is on land"""
    object: Annotated[Optional['Object'], "is_animatable=False"]
    """Follow this object instead of a boid"""
    distance: Annotated[float, "step=10.0", "precision=3"]
    """Distance behind leader to follow"""
    queue_count: Annotated[int, "step=1"]
    """How many boids in a line"""
    use_line: bool
    """Follow leader in a line"""