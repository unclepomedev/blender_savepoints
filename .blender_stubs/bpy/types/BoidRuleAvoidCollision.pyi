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

    name: Annotated[str, "is_animatable=False"]
    """Boid rule name"""
    @property
    def type(self) -> Literal['GOAL', 'AVOID', 'AVOID_COLLISION', 'SEPARATE', 'FLOCK', 'FOLLOW_LEADER', 'AVERAGE_SPEED', 'FIGHT']:

        ...
    use_in_air: bool
    """Use rule when boid is flying"""
    use_on_land: bool
    """Use rule when boid is on land"""
    use_avoid: bool
    """Avoid collision with other boids"""
    use_avoid_collision: bool
    """Avoid collision with deflector objects"""
    look_ahead: Annotated[float, "step=10.0", "precision=3"]
    """Time to look ahead in seconds"""