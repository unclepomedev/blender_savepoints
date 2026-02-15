# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BoidRule.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class BoidRule(bpy_struct):

    name: Annotated[str, "is_animatable=False"]
    """Boid rule name"""
    @property
    def type(self) -> Literal['GOAL', 'AVOID', 'AVOID_COLLISION', 'SEPARATE', 'FLOCK', 'FOLLOW_LEADER', 'AVERAGE_SPEED', 'FIGHT']:

        ...
    use_in_air: bool
    """Use rule when boid is flying"""
    use_on_land: bool
    """Use rule when boid is on land"""