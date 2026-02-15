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
class FModifierEnvelopeControlPoint(bpy_struct):
    min: Annotated[float, "step=10.0", "precision=3"]
    """Lower bound of envelope at this control-point"""
    max: Annotated[float, "step=10.0", "precision=3"]
    """Upper bound of envelope at this control-point"""
    frame: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3"]
    """Frame this control-point occurs on"""