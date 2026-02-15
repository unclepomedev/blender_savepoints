# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .ID import ID
class IDOverrideLibraryPropertyOperation(bpy_struct):
    @property
    def operation(self) -> Literal['NOOP', 'REPLACE', 'DIFF_ADD', 'DIFF_SUB', 'FACT_MULTIPLY', 'INSERT_AFTER', 'INSERT_BEFORE']:
        """What override operation is performed"""
        ...
    @property
    def flag(self) -> set[str]:
        """Status flags"""
        ...
    @property
    def subitem_reference_name(self) -> Annotated[str, "is_animatable=False"]:
        """Used to handle changes into collection"""
        ...
    @property
    def subitem_local_name(self) -> Annotated[str, "is_animatable=False"]:
        """Used to handle changes into collection"""
        ...
    @property
    def subitem_reference_id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """Collection of IDs only, used to disambiguate between potential IDs with same name from different libraries"""
        ...
    @property
    def subitem_local_id(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """Collection of IDs only, used to disambiguate between potential IDs with same name from different libraries"""
        ...
    @property
    def subitem_reference_index(self) -> Annotated[int, "step=1"]:
        """Used to handle changes into collection"""
        ...
    @property
    def subitem_local_index(self) -> Annotated[int, "step=1"]:
        """Used to handle changes into collection"""
        ...