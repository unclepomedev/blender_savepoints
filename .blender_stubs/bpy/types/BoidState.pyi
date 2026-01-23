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
class BoidState(bpy_struct):
    name: str
    ruleset_type: str
    rules: bpy_prop_collection['BoidRule']
    active_boid_rule: 'BoidRule'
    active_boid_rule_index: int
    rule_fuzzy: float
    volume: float
    falloff: float