# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .BoidRule import BoidRule
class BoidRuleAverageSpeed(BoidRule):
    name: str
    type: str
    use_in_air: bool
    use_on_land: bool
    wander: float
    level: float
    speed: float