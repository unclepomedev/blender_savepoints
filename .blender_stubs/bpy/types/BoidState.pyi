# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.BoidState.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .BoidRule import BoidRule
from .bpy_prop_collection import bpy_prop_collection

class BoidState(bpy_struct):

    name: Annotated[str, "is_animatable=False"]
    """Boid state name"""
    ruleset_type: Literal['FUZZY', 'RANDOM', 'AVERAGE']
    """How the rules in the list are evaluated"""
    @property
    def rules(self) -> Annotated[bpy_prop_collection['BoidRule'], "is_animatable=False"]:

        ...
    @property
    def active_boid_rule(self) -> Annotated[Optional['BoidRule'], "is_animatable=False"]:

        ...
    active_boid_rule_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]

    rule_fuzzy: Annotated[float, "step=10.0", "precision=3"]

    volume: Annotated[float, "step=10.0", "precision=3"]

    falloff: Annotated[float, "step=10.0", "precision=3"]
