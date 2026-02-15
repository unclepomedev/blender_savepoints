# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.OperatorOptions.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class OperatorOptions(bpy_struct):

    @property
    def is_grab_cursor(self) -> bool:
        """True when the cursor is grabbed"""
        ...
    @property
    def is_invoke(self) -> bool:
        """True when invoked (even if only the execute callbacks available)"""
        ...
    @property
    def is_repeat(self) -> bool:
        """True when run from the 'Adjust Last Operation' panel"""
        ...
    @property
    def is_repeat_last(self) -> bool:
        """True when run from the operator 'Repeat Last'"""
        ...
    use_cursor_region: bool
    """Enable to use the region under the cursor for modal execution"""