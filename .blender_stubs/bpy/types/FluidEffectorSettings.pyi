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
class FluidEffectorSettings(bpy_struct):
    effector_type: Literal['COLLISION', 'GUIDE']
    """Change type of effector in the simulation"""
    surface_distance: Annotated[float, "step=0.05000000074505806", "precision=5"]
    """Additional distance around mesh surface to consider as effector"""
    use_plane_init: bool
    """Treat this object as a planar, unclosed mesh"""
    velocity_factor: Annotated[float, "step=10.0", "precision=3"]
    """Multiplier of obstacle velocity"""
    guide_mode: Literal['MAXIMUM', 'MINIMUM', 'OVERRIDE', 'AVERAGED']
    """How to create guiding velocities"""
    use_effector: bool
    """Control when to apply the effector"""
    subframes: Annotated[int, "step=1"]
    """Number of additional samples to take between frames to improve quality of fast moving effector objects"""