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

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Boid state name"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def ruleset_type(self) -> Literal['FUZZY', 'RANDOM', 'AVERAGE']:
        """How the rules in the list are evaluated"""
        ...
    @ruleset_type.setter
    def ruleset_type(self, value: Literal['FUZZY', 'RANDOM', 'AVERAGE']) -> None:
        ...
    @property
    def rules(self) -> Annotated[bpy_prop_collection['BoidRule'], "is_animatable=False"]:

        ...
    @property
    def active_boid_rule(self) -> Annotated[Optional['BoidRule'], "is_animatable=False"]:

        ...
    @property
    def active_boid_rule_index(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:

        ...
    @active_boid_rule_index.setter
    def active_boid_rule_index(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def rule_fuzzy(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @rule_fuzzy.setter
    def rule_fuzzy(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def volume(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @volume.setter
    def volume(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def falloff(self) -> Annotated[float, "step=10.0", "precision=3"]:

        ...
    @falloff.setter
    def falloff(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...