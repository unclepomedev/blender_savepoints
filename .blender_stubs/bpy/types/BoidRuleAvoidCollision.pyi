# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .BoidRule import BoidRule
class BoidRuleAvoidCollision(BoidRule):
    name: str
    type: str
    use_in_air: bool
    use_on_land: bool
    use_avoid: bool
    use_avoid_collision: bool
    look_ahead: float