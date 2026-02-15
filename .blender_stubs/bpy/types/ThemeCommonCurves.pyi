# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.ThemeCommonCurves.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class ThemeCommonCurves(bpy_struct):

    handle_free: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    handle_sel_free: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    handle_auto: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    handle_sel_auto: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    handle_vect: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    handle_sel_vect: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    handle_align: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    handle_sel_align: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    handle_auto_clamped: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    handle_sel_auto_clamped: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    handle_vertex: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    handle_vertex_select: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]

    handle_vertex_size: Annotated[int, "subtype='PIXEL'", "step=1"]
