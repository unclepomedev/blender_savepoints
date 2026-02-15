# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.TexMapping.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct

class TexMapping(bpy_struct):

    vector_type: Literal['POINT', 'TEXTURE', 'VECTOR', 'NORMAL']
    """Type of vector that the mapping transforms"""
    translation: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]

    rotation: Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=100.0", "precision=5"]

    scale: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]

    min: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Minimum value for clipping"""
    max: Annotated[list[float], "subtype='XYZ'", "step=10.0", "precision=3"]
    """Maximum value for clipping"""
    use_min: bool
    """Whether to use minimum clipping value"""
    use_max: bool
    """Whether to use maximum clipping value"""
    mapping_x: Literal['NONE', 'X', 'Y', 'Z']

    mapping_y: Literal['NONE', 'X', 'Y', 'Z']

    mapping_z: Literal['NONE', 'X', 'Y', 'Z']

    mapping: Literal['FLAT', 'CUBE', 'TUBE', 'SPHERE']
