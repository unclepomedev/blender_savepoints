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
class ClothSolverResult(bpy_struct):
    @property
    def status(self) -> set[str]:
        """Status of the solver iteration"""
        ...
    @property
    def max_error(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum error during substeps"""
        ...
    @property
    def min_error(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Minimum error during substeps"""
        ...
    @property
    def avg_error(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Average error during substeps"""
        ...
    @property
    def max_iterations(self) -> Annotated[int, "step=1"]:
        """Maximum iterations during substeps"""
        ...
    @property
    def min_iterations(self) -> Annotated[int, "step=1"]:
        """Minimum iterations during substeps"""
        ...
    @property
    def avg_iterations(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Average iterations during substeps"""
        ...