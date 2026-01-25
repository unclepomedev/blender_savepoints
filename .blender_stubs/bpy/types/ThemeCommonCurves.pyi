# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
class ThemeCommonCurves(bpy_struct):
    handle_free: list[float]
    handle_sel_free: list[float]
    handle_auto: list[float]
    handle_sel_auto: list[float]
    handle_vect: list[float]
    handle_sel_vect: list[float]
    handle_align: list[float]
    handle_sel_align: list[float]
    handle_auto_clamped: list[float]
    handle_sel_auto_clamped: list[float]
    handle_vertex: list[float]
    handle_vertex_select: list[float]
    handle_vertex_size: int