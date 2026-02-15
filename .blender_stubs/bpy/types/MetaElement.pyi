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
class MetaElement(bpy_struct):
    type: Literal['BALL', 'CAPSULE', 'PLANE', 'ELLIPSOID', 'CUBE']
    """Metaball type"""
    co: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=10.0", "precision=3"]
    rotation: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]
    """Normalized quaternion rotation"""
    radius: Annotated[float, "subtype=''", "unit='LENGTH'", "step=10.0", "precision=3"]
    size_x: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Size of element, use of components depends on element type"""
    size_y: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Size of element, use of components depends on element type"""
    size_z: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """Size of element, use of components depends on element type"""
    stiffness: Annotated[float, "step=10.0", "precision=3"]
    """Stiffness defines how much of the element to fill"""
    use_negative: bool
    """Set metaball as negative one"""
    use_scale_stiffness: bool
    """Scale stiffness instead of radius"""
    select: bool
    """Select element"""
    hide: bool
    """Hide element"""