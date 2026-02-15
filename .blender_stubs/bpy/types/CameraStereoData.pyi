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
class CameraStereoData(bpy_struct):
    convergence_mode: Literal['OFFAXIS', 'PARALLEL', 'TOE']
    pivot: Literal['LEFT', 'RIGHT', 'CENTER']
    interocular_distance: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]
    """Set the distance between the eyes - the stereo plane distance / 30 should be fine"""
    convergence_distance: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=3"]
    """The converge point for the stereo cameras (often the distance between a projector and the projection screen)"""
    use_spherical_stereo: bool
    """Render every pixel rotating the camera around the middle of the interocular distance"""
    use_pole_merge: bool
    """Fade interocular distance to 0 after the given cutoff angle"""
    pole_merge_angle_from: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Angle at which interocular distance starts to fade to 0"""
    pole_merge_angle_to: Annotated[float, "subtype='ANGLE'", "unit='ROTATION'", "step=10.0", "precision=3"]
    """Angle at which interocular distance is 0"""