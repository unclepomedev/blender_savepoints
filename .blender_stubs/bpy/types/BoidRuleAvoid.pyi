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
from .Object import Object
class BoidRuleAvoid(BoidRule):
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
    """Object to avoid"""
    use_predict: bool
    """Predict target movement"""
    fear_factor: Annotated[float, "step=10.0", "precision=3"]
    """Avoid object if danger from it is above this threshold"""