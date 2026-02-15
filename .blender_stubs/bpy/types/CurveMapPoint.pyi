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
class CurveMapPoint(bpy_struct):
    location: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """X/Y coordinates of the curve point"""
    handle_type: Literal['AUTO', 'AUTO_CLAMPED', 'VECTOR']
    """Curve interpolation at this point: Bézier or vector"""
    select: bool
    """Selection state of the curve point"""