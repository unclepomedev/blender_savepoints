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
class MovieTrackingDopesheet(bpy_struct):
    sort_method: Literal['NAME', 'LONGEST', 'TOTAL', 'AVERAGE_ERROR', 'START', 'END']
    """Method to be used to sort channels in dopesheet view"""
    use_invert_sort: bool
    """Invert sort order of dopesheet channels"""
    show_only_selected: bool
    """Only include channels relating to selected objects and data"""
    show_hidden: bool
    """Include channels from objects/bone that are not visible"""