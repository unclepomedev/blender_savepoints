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
from .Object import Object
class BoidRuleAvoid(BoidRule):
    name: str
    type: str
    use_in_air: bool
    use_on_land: bool
    object: 'Object'
    use_predict: bool
    fear_factor: float