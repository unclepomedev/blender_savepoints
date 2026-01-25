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
class SPHFluidSettings(bpy_struct):
    solver: str
    spring_force: float
    fluid_radius: float
    rest_length: float
    use_viscoelastic_springs: bool
    use_initial_rest_length: bool
    plasticity: float
    yield_ratio: float
    spring_frames: int
    linear_viscosity: float
    stiff_viscosity: float
    stiffness: float
    repulsion: float
    rest_density: float
    buoyancy: float
    use_factor_repulsion: bool
    use_factor_density: bool
    use_factor_radius: bool
    use_factor_stiff_viscosity: bool
    use_factor_rest_length: bool